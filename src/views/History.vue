<template>
  <div class="history-page">
    <NavBar />
    <!-- 全屏背景图 - 双层实现滑动效果 -->
    <div class="background-container">
      <div 
        class="background-image background-current" 
        :class="{ 
          'slide-out': isTransitioning && prevBackgroundIndex !== -1,
          'no-transition': !isTransitioning
        }"
        :style="{ backgroundImage: `url(${displayBackground || currentBackground})` }"
      ></div>
      <div 
        v-if="isTransitioning && nextBackground"
        class="background-image background-next"
        :style="{ backgroundImage: `url(${nextBackground})` }"
      ></div>
    </div>
    
    <div class="content-wrapper">
      <!-- 左侧：时间线和简介 -->
      <div class="left-panel">
        <div class="timeline-container">
          <div 
            v-for="(period, index) in historyPeriods" 
            :key="index"
            class="timeline-node-wrapper"
            :class="{ active: currentIndex === index }"
            @click="selectPeriod(index)"
          >
            <div class="timeline-node"></div>
            <div v-if="index < historyPeriods.length - 1" class="timeline-line"></div>
          </div>
        </div>
        
        <div class="text-content">
          <h1 class="period-title">
            <span class="title-chinese">{{ currentPeriod.title }}</span>
            <span class="title-english">{{ currentPeriod.titleEn }}</span>
          </h1>
          <p class="period-description">{{ currentPeriod.description }}</p>
          <button class="period-button">历史</button>
        </div>
      </div>
      
      <!-- 右侧：图片轮播 -->
      <div class="right-panel">
        <div class="carousel-container" :class="{ 'transitioning': isTransitioning }">
          <div 
            v-for="(period, index) in historyPeriods" 
            :key="index"
            class="carousel-item"
            :class="{ 
              'active': currentIndex === index,
              'prev': currentIndex === index + 1 || (currentIndex === 0 && index === historyPeriods.length - 1),
              'next': currentIndex === index - 1 || (currentIndex === historyPeriods.length - 1 && index === 0)
            }"
            @click="selectPeriod(index)"
          >
            <div class="carousel-image" :style="{ backgroundImage: `url(${period.image})` }">
            </div>
            <div class="carousel-label">
              <div class="label-title">{{ period.title }}</div>
              <div class="label-subtitle">{{ period.subtitle }}</div>
            </div>
          </div>
        </div>
        
        <!-- 导航箭头 -->
        <div class="carousel-nav">
          <button class="nav-arrow nav-prev" @click="prevPeriod">‹</button>
          <button class="nav-arrow nav-next" @click="nextPeriod">›</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import NavBar from '../components/NavBar.vue'

const currentIndex = ref(0)
const isTransitioning = ref(false)
const prevBackgroundIndex = ref(-1)
const displayBackground = ref('')

const historyPeriods = ref([
  {
    time: '公元前111年',
    title: '两汉时期',
    titleEn: 'HAN DYNASTY',
    subtitle: '丝绸之路起点',
    description: '汉武帝设立敦煌郡，敦煌成为丝绸之路的重要节点。这一时期，敦煌开始成为东西方文化交流的枢纽，佛教文化开始传入。作为古代丝绸之路的咽喉要道，敦煌见证了东西方文明的首次大规模交流与融合。',
    image: '/images/history/ls06.jpg',
    background: '/images/history/ls01.jpg'
  },
  {
    time: '220-589年',
    title: '魏晋南北朝',
    titleEn: 'WEI JIN PERIOD',
    subtitle: '莫高窟开凿',
    description: '敦煌进入佛教艺术发展的黄金时期。莫高窟开始开凿，大量精美的壁画和彩塑被创作出来，形成了独特的敦煌艺术风格。这一时期，佛教艺术与中原文化深度融合，创造了举世闻名的敦煌艺术瑰宝。',
    image: '/images/history/ls07.jpg',
    background: '/images/history/ls02.jpg'
  },
  {
    time: '581-907年',
    title: '隋唐时期',
    titleEn: 'SUI TANG PERIOD',
    subtitle: '艺术巅峰',
    description: '敦煌达到历史上的鼎盛时期。莫高窟规模不断扩大，艺术水平达到巅峰。丝绸之路贸易繁荣，敦煌成为国际性大都市。这一时期，敦煌艺术达到了前所未有的高度，成为世界艺术史上的璀璨明珠。',
    image: '/images/history/ls08.jpg',
    background: '/images/history/ls03.jpg'
  },
  {
    time: '960-1368年',
    title: '宋元时期',
    titleEn: 'SONG YUAN PERIOD',
    subtitle: '多民族融合',
    description: '虽然丝绸之路逐渐衰落，但敦煌艺术仍在继续发展。西夏和元朝时期，莫高窟仍有新的洞窟开凿，艺术风格融合了多民族特色。这一时期展现了中华文化的包容性和多元性，艺术风格更加丰富多样。',
    image: '/images/history/ls09.jpg',
    background: '/images/history/ls04.jpg'
  },
  {
    time: '1900年至今',
    title: '近现代',
    titleEn: 'MODERN ERA',
    subtitle: '数字保护',
    description: '1900年，王道士发现藏经洞，震惊世界。敦煌学兴起，成为国际显学。如今，敦煌文化遗产得到保护和研究，数字敦煌项目让千年艺术得以永续传承。现代科技为古老艺术注入了新的生命力。',
    image: '/images/history/ls10.jpg',
    background: '/images/history/ls05.jpg'
  }
])

const currentPeriod = computed(() => historyPeriods.value[currentIndex.value])
const currentBackground = computed(() => currentPeriod.value.background)
const nextBackground = computed(() => {
  if (!isTransitioning.value) return null
  return historyPeriods.value[currentIndex.value].background
})

onMounted(() => {
  displayBackground.value = currentBackground.value
})

const selectPeriod = (index) => {
  if (isTransitioning.value || index === currentIndex.value) return
  prevBackgroundIndex.value = currentIndex.value
  isTransitioning.value = true
  currentIndex.value = index
  setTimeout(() => {
    // 先更新背景图片（此时 background-current 还在 slide-out 状态）
    displayBackground.value = currentBackground.value
    // 等待一个动画帧，确保背景已更新
    requestAnimationFrame(() => {
      // 先结束过渡（添加 no-transition 类），这样移除 slide-out 时不会有过渡动画
      isTransitioning.value = false
      // 再等待一个动画帧，确保 no-transition 类已生效
      requestAnimationFrame(() => {
        // 移除 slide-out 类，此时位置会立即重置（无过渡）
        prevBackgroundIndex.value = -1
      })
    })
  }, 800)
}

const nextPeriod = () => {
  if (isTransitioning.value) return
  prevBackgroundIndex.value = currentIndex.value
  isTransitioning.value = true
  currentIndex.value = (currentIndex.value + 1) % historyPeriods.value.length
  setTimeout(() => {
    displayBackground.value = currentBackground.value
    requestAnimationFrame(() => {
      isTransitioning.value = false
      requestAnimationFrame(() => {
        prevBackgroundIndex.value = -1
      })
    })
  }, 800)
}

const prevPeriod = () => {
  if (isTransitioning.value) return
  prevBackgroundIndex.value = currentIndex.value
  isTransitioning.value = true
  currentIndex.value = (currentIndex.value - 1 + historyPeriods.value.length) % historyPeriods.value.length
  setTimeout(() => {
    displayBackground.value = currentBackground.value
    requestAnimationFrame(() => {
      isTransitioning.value = false
      requestAnimationFrame(() => {
        prevBackgroundIndex.value = -1
      })
    })
  }, 800)
}
</script>

<style scoped>
.history-page {
  min-height: 100vh;
  position: relative;
  padding-top: 55px;
  overflow: hidden;
}

.background-container {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100vh;
  z-index: 0;
  overflow: hidden;
  background: #000;
}

.background-image {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-size: 100% 100%;
  background-position: center;
  background-repeat: no-repeat;
  filter: blur(4px) brightness(1.15);
  transform: scale(1.1);
  will-change: transform;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
  background-color: #000;
}

.background-current {
  z-index: 1;
  transform: scale(1.1) translateY(0);
  transition: transform 0.8s cubic-bezier(0.4, 0, 0.2, 1);
}

.background-current.slide-out {
  transform: scale(1.1) translateY(-100%);
}

.background-current.no-transition {
  transition: none !important;
}

.background-next {
  z-index: 2;
  transform: scale(1.1) translateY(100%);
  animation: slideInUp 0.8s cubic-bezier(0.4, 0, 0.2, 1) forwards;
}

@keyframes slideInUp {
  from {
    transform: scale(1.1) translateY(100%);
  }
  to {
    transform: scale(1.1) translateY(0);
  }
}

.background-image::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.45);
  z-index: 1;
}

.content-wrapper {
  position: relative;
  z-index: 2;
  display: flex;
  height: calc(100vh - 55px);
  min-height: calc(100vh - 55px);
  padding: 80px 60px;
  gap: 80px;
  max-width: 1600px;
  margin: 0 auto;
  align-items: center;
  justify-content: center;
}

/* 左侧面板 */
.left-panel {
  flex: 0 0 500px;
  display: flex;
  gap: 40px;
  align-items: center;
}

.timeline-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0;
  padding-top: 20px;
}

.timeline-node-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  cursor: pointer;
  position: relative;
}

.timeline-node {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.4);
  transition: all 0.3s ease;
  z-index: 2;
}

.timeline-node-wrapper.active .timeline-node {
  width: 20px;
  height: 20px;
  background: rgba(255, 255, 255, 1);
  box-shadow: 0 0 20px rgba(255, 255, 255, 0.6);
}

.timeline-line {
  width: 2px;
  height: 120px;
  background: rgba(255, 255, 255, 0.3);
  margin: 10px 0;
}

.text-content {
  flex: 1;
  color: white;
}

.period-title {
  margin: 0 0 30px 0;
  line-height: 1.2;
}

.title-chinese {
  display: block;
  font-size: 56px;
  font-weight: 700;
  margin-bottom: 8px;
  letter-spacing: 2px;
}

.title-english {
  display: block;
  font-size: 22px;
  font-weight: 300;
  letter-spacing: 4px;
  opacity: 0.9;
}

.period-description {
  font-size: 18px;
  line-height: 1.8;
  color: rgba(255, 255, 255, 0.9);
  margin-bottom: 40px;
  max-width: 450px;
}

.period-button {
  padding: 12px 32px;
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-radius: 6px;
  color: white;
  font-size: 16px;
  cursor: pointer;
  transition: all 0.3s ease;
  backdrop-filter: blur(10px);
}

.period-button:hover {
  background: rgba(255, 255, 255, 0.2);
  border-color: rgba(255, 255, 255, 0.5);
}

/* 右侧面板 */
.right-panel {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  position: relative;
  transform: translateY(80px);
}

.carousel-container {
  position: relative;
  width: 100%;
  max-width: 800px;
  height: 600px;
  perspective: 1500px;
}

.carousel-container.transitioning .carousel-item {
  pointer-events: none;
}

.carousel-item {
  position: absolute;
  width: 400px;
  height: 500px;
  cursor: pointer;
  transition: all 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94);
  transform-style: preserve-3d;
  will-change: transform, opacity, left;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
}

.carousel-item.active {
  left: 50%;
  transform: translateX(-50%) translateZ(0) scale(1);
  z-index: 3;
  opacity: 1;
  visibility: visible;
  pointer-events: auto;
}

.carousel-item.prev {
  left: 10%;
  transform: translateX(-50%) translateZ(-250px) scale(0.7);
  z-index: 1;
  opacity: 0.5;
  visibility: visible;
  pointer-events: auto;
}

.carousel-item.next {
  left: 90%;
  transform: translateX(-50%) translateZ(-250px) scale(0.7);
  z-index: 1;
  opacity: 0.5;
  visibility: visible;
  pointer-events: auto;
}

.carousel-item:not(.active):not(.prev):not(.next) {
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transform: translateX(-50%) translateZ(-300px) scale(0.6);
}

.carousel-image {
  width: 100%;
  height: 400px;
  background-size: cover;
  background-position: center;
  border-radius: 12px;
  position: relative;
  overflow: hidden;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
  margin-bottom: 30px;
  will-change: transform;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
  transform: translateZ(0);
}

.carousel-image::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.2);
}

.carousel-label {
  margin-top: 30px;
  text-align: center;
  color: white;
  padding: 0 20px;
}

.label-title {
  font-size: 24px;
  font-weight: 600;
  margin-bottom: 6px;
}

.label-subtitle {
  font-size: 14px;
  opacity: 0.8;
}

.carousel-nav {
  display: flex;
  gap: 20px;
  margin-top: 40px;
  transform: translateY(-100px);
}

.nav-arrow {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.3);
  color: white;
  font-size: 32px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
  backdrop-filter: blur(10px);
}

.nav-arrow:hover {
  background: rgba(255, 255, 255, 0.2);
  border-color: rgba(255, 255, 255, 0.5);
  transform: scale(1.1);
}

@media (max-width: 1200px) {
  .content-wrapper {
    flex-direction: column;
    gap: 60px;
    padding: 60px 40px;
  }
  
  .left-panel {
    flex: none;
    width: 100%;
  }
  
  .carousel-container {
    max-width: 100%;
  }
  
  .carousel-item {
    width: 350px;
    height: 450px;
  }
  
  .carousel-image {
    height: 350px;
  }
}

@media (max-width: 768px) {
  .content-wrapper {
    padding: 40px 20px;
  }
  
  .title-chinese {
    font-size: 36px;
  }
  
  .carousel-item {
    width: 280px;
    height: 380px;
  }
  
  .carousel-image {
    height: 280px;
  }
  
  .carousel-item.prev {
    left: 10%;
  }
  
  .carousel-item.next {
    left: 90%;
  }
}
</style>
