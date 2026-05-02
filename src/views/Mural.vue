<template>
  <div class="mural-page">
    <NavBar />
    <div class="top-banner">
      <img 
        src="/images/mural/bh01.jpg" 
        alt="壁画" 
        class="banner-image"
        :style="{ filter: `brightness(${1 - darkenOpacity * 0.85})` }"
      />
      <div class="banner-title">
        <h1
          class="main-title"
          :style="{ 
            transform: `translateY(${-300 * scrollProgress}px) scale(${titleScale})`,
            filter: `brightness(${titleBrightness})`
          }"
        >
          敦煌壁画
        </h1>
      </div>
    </div>
    
    <!-- 尊像画内容区域 -->
    <div class="content-section">
      <h2 class="section-title">尊像画：信仰的主体</h2>
      <div class="content-wrapper">
        <!-- 左侧图片区域 -->
        <div class="image-section" ref="imageSectionRef">
          <div class="image-container">
            <img src="/images/mural/bh02.jpg" alt="尊像画" class="content-image" />
          </div>
        </div>
        
        <!-- 右侧文本区域 -->
        <div class="text-section" ref="textSectionRef">
          <div class="text-box">
            <h1 class="text-title">尊像画</h1>
            <p class="text-subtitle">尊像画是敦煌壁画中的重要题材，主要描绘各种佛教尊像。</p>
            <div class="text-body">
              <p>
                尊像画是敦煌壁画中最为重要的题材之一，主要描绘各种佛教尊像，包括释迦牟尼佛、阿弥陀佛、药师佛等诸佛，以及观音菩萨、文殊菩萨、普贤菩萨等诸菩萨，还有罗汉、弟子、天王、力士等形象。
              </p>
              <p>
                这些尊像画不仅具有极高的艺术价值，更承载着深厚的宗教文化内涵。画师们通过精湛的技艺，将佛教经典中的形象生动地呈现在壁画之上，展现了古代艺术家对佛教文化的深刻理解和卓越的艺术表现力。
              </p>
              <p>
                尊像画的构图严谨，色彩丰富，线条流畅，体现了不同历史时期的艺术风格和审美特点。从早期的粗犷豪放，到唐代的精致华美，再到后期的程式化表现，每一时期的尊像画都反映了当时的社会文化背景和艺术发展水平。
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
    
    <!-- 佛教故事画内容区域 -->
    <div class="story-section">
      <div class="story-wrapper">
        <!-- 左侧文本区域 -->
        <div class="story-text-section" ref="storyTextSectionRef">
          <div class="story-text-box">
            <h1 class="story-title">佛传故事:乘象入胎 夜半逾城</h1>
            <div class="story-body">
              <div class="story-paragraph">
                <h2 class="story-subtitle">乘象入胎</h2>
                <p>
                  释迦牟尼在成佛之前，是住在兜率天的菩萨。他为了度化众生，决定降生到人间，并选择了净饭王和摩耶夫人作为他的父母。摩耶夫人在梦中见到一只白象从她的右胁进入，这预示着将要怀孕一个神圣的儿子，净饭王和摩耶夫人因此非常高兴。
                </p>
              </div>
              <div class="story-paragraph">
                <h2 class="story-subtitle">夜半逾城</h2>
                <p>
                  悉达多太子在看到生老病死的痛苦后，决定在29岁时舍弃王子的身份，出家修行。在一个夜晚，太子在诸天的帮助下，骑着马越过王宫城墙，开始了漫长的苦行之路。虽然故事本身可能看似简单，但在艺术表现中（如敦煌壁画），这一题材的描绘却异常复杂，线条流畅，色彩富丽堂皇。太子头戴宝冠，骑着白马，手持缰绳，四位天神托起马的四蹄，白马腾空而起，有力士护持，天女奏乐散花在周围。
                </p>
              </div>
            </div>
          </div>
        </div>
        
        <!-- 右侧图片区域（预留） -->
        <div class="story-image-section" ref="storyImageSectionRef">
          <div class="story-image-container mural-hover-frame">
            <img src="/images/mural/bh03.jpg" alt="佛教故事画" class="story-content-image" />
            <div class="mural-hover-dim" aria-hidden="true"></div>
            <div class="mural-hover-caption" aria-hidden="true">
              <div class="mural-hover-title">佛传故事</div>
              <div class="mural-hover-desc">乘象入胎 · 夜半逾城</div>
            </div>
          </div>
        </div>
      </div>
      
      <!-- 装饰图案画内容区域 -->
      <div class="decoration-wrapper">
        <!-- 左侧图片区域（预留） -->
        <div class="decoration-image-section" ref="decorationImageSectionRef">
          <div class="decoration-image-container mural-hover-frame">
            <img src="/images/mural/bh04.jpg" alt="装饰图案画" class="decoration-content-image" />
            <div class="mural-hover-dim" aria-hidden="true"></div>
            <div class="mural-hover-caption" aria-hidden="true">
              <div class="mural-hover-title">装饰图案画</div>
              <div class="mural-hover-desc">纹样秩序 · 色彩之美</div>
            </div>
          </div>
        </div>
        
        <!-- 右侧文本区域 -->
        <div class="decoration-text-section" ref="decorationTextSectionRef">
          <div class="decoration-text-box">
            <h1 class="decoration-title">装饰图案画</h1>
            <p class="decoration-subtitle">装饰图案画是敦煌壁画中的重要组成部分，具有独特的艺术价值。</p>
            <div class="decoration-body">
              <p>
                装饰图案画是敦煌壁画中不可或缺的装饰元素，主要用于美化洞窟空间，营造庄严神圣的氛围。这些图案包括各种花卉、云纹、几何纹样等，形式多样，变化丰富。
              </p>
              <p>
                装饰图案画的绘制技法精湛，色彩丰富，线条流畅，体现了古代画师高超的技艺和对美的追求。不同时期的装饰图案呈现出不同的风格特点，从早期的简洁粗犷，到唐代的繁复华丽，再到后期的程式化表现。
              </p>
              <p>
                这些装饰图案不仅具有装饰功能，更承载着深厚的文化内涵。它们往往与佛教思想相结合，通过图案的象征意义传达宗教理念，是敦煌艺术中重要的文化载体。
              </p>
            </div>
          </div>
        </div>
      </div>
      
      <!-- 固定背景图片区域 -->
      <div class="fixed-image-section">
        <div class="fixed-image-viewport"></div>
      </div>
      
      <!-- 经变画内容区域 -->
      <div class="sutra-wrapper">
        <h2 class="sutra-main-title">经变画：唐代壁画的主体与巅峰</h2>
        <div class="sutra-content-wrapper">
          <!-- 左侧：经变画介绍 -->
          <div class="sutra-column sutra-column-left">
            <div class="sutra-text-box">
              <h3 class="sutra-column-title">经变画介绍</h3>
              <div class="sutra-body">
                <p>
                  经变画，又称"变相"或"变"，是指将佛教经典中的内容以图像的形式表现出来。经变画是唐代敦煌壁画的主体，代表了敦煌艺术的最高成就。这些壁画以宏大的规模、精湛的技艺、丰富的内涵，展现了佛教教义的深刻内涵和唐代艺术的辉煌成就。
                </p>
                <!-- 图片区域 -->
                <div class="sutra-left-image-area">
                  <img src="/images/mural/bh09.jpg" alt="经变画介绍" class="sutra-content-image" />
                </div>
                <p>
                  经变画的内容主要包括《法华经变》《维摩诘经变》《弥勒经变》《阿弥陀经变》《药师经变》等，每一幅经变画都是对相应经典的生动诠释。画师们通过巧妙的构图、丰富的色彩、细腻的笔触，将抽象的佛教教义转化为直观的视觉形象，使得深奥的佛法变得通俗易懂。
                </p>
              </div>
            </div>
          </div>
          
          <!-- 中间分隔线 -->
          <div class="sutra-divider"></div>
          
          <!-- 中间：经变画特点介绍 -->
          <div class="sutra-column sutra-column-middle">
            <div class="sutra-text-box">
              <!-- 图片区域 -->
              <div class="sutra-image-area">
                <img src="/images/mural/bh08.jpg" alt="经变画特点" class="sutra-content-image" />
              </div>
              <h3 class="sutra-column-title">经变画特点</h3>
              <div class="sutra-body">
                <p>
                  唐代经变画的艺术风格以富丽堂皇、气势恢宏著称。画面构图严谨，人物形象生动，色彩丰富而和谐，线条流畅而有力。这些壁画不仅具有极高的艺术价值，更是研究唐代社会、文化、宗教的重要资料。
                </p>
                <p>
                  经变画在技法上采用了多种绘画技巧，包括细腻的晕染、丰富的层次、生动的表情刻画等。画面中的人物、建筑、山水、花鸟等元素都经过精心设计，形成了独特的艺术风格和视觉效果。
                </p>
              </div>
              <!-- 图片区域 -->
              <div class="sutra-middle-bottom-image-area">
                <img src="/images/mural/bh06.jpg" alt="经变画特点" class="sutra-content-image" />
              </div>
            </div>
          </div>
          
          <!-- 右侧分隔线 -->
          <div class="sutra-divider"></div>
          
          <!-- 右边：经变画历史演变介绍 -->
          <div class="sutra-column sutra-column-right">
            <div class="sutra-text-box">
              <h3 class="sutra-column-title">历史演变</h3>
              <div class="sutra-body">
                <p>
                  经变画的发展经历了从早期到唐代的演变过程。早期的经变画相对简单，主要表现经典的文字内容。到了唐代，经变画达到了艺术高峰，不仅内容丰富，而且技法精湛，形成了独特的艺术风格。
                </p>
                <p>
                  随着时间的推移，经变画在不同时期呈现出不同的特点。从初唐的雄浑大气，到盛唐的富丽堂皇，再到晚唐的细腻精致，经变画的发展历程反映了唐代艺术的发展轨迹，是中华文明和世界艺术的珍贵遗产。
                </p>
              </div>
              <!-- 图片区域 -->
              <div class="sutra-image-area sutra-right-image-area">
                <img src="/images/mural/bh07.jpg" alt="历史演变" class="sutra-content-image" />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="mural-showcase-section">
      <div class="mural-showcase-header">
        <div class="mural-showcase-title">敦煌壁画赏析</div>
      </div>

      <div class="mural-showcase-body">
        <div class="mural-showcase-left">
          <div class="mural-showcase-media">
            <video
              class="mural-showcase-video"
              src="/video/bh.mp4"
              autoplay
              muted
              loop
              playsinline
              preload="metadata"
              controls
            ></video>
          </div>

          <div class="mural-showcase-text">
            <div class="mural-showcase-text-title">千年壁画的艺术与守护</div>
            <div class="mural-showcase-text-body">
              敦煌壁画以宏阔的叙事与精妙的线描、设色闻名，内容涵盖佛教故事、供养人像、飞天乐舞与世俗生活等，集中展现了多元文化在丝路交汇处的融合与创造。如今，数字化采集与科学修复技术让这些跨越千年的色彩与笔触得以更长久地被看见与研究。
            </div>
          </div>
        </div>

        <div class="mural-showcase-right">
          <div class="mural-showcase-image">
            <div
              class="mural-showcase-image-placeholder mural-showcase-image-placeholder-filled"
              style="background-image: url('/images/mural/bh10.jpg')"
              aria-label="敦煌壁画赏析图片1"
            ></div>
          </div>
          <div class="mural-showcase-image">
            <div
              class="mural-showcase-image-placeholder mural-showcase-image-placeholder-filled"
              style="background-image: url('/images/mural/bh11.jpg')"
              aria-label="敦煌壁画赏析图片2"
            ></div>
          </div>
          <div class="mural-showcase-image">
            <div
              class="mural-showcase-image-placeholder mural-showcase-image-placeholder-filled"
              style="background-image: url('/images/mural/bh12.jpg')"
              aria-label="敦煌壁画赏析图片3"
            ></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onBeforeUnmount, nextTick } from 'vue'
import NavBar from '../components/NavBar.vue'

// 滚动暗化效果
const scrollProgress = ref(0)
const darkenOpacity = computed(() => {
  // 根据滚动进度计算暗度，最大暗度为0.95
  return Math.min(scrollProgress.value * 0.95, 0.95)
})

// 标题缩放，最大约 1.3 倍
const titleScale = computed(() => {
  return 1 + Math.min(scrollProgress.value, 1) * 0.3
})

// 标题亮度，随滚动逐渐变亮
const titleBrightness = computed(() => {
  // 从1.0逐渐增加到1.5倍亮度
  return 1 + Math.min(scrollProgress.value, 1) * 0.5
})

const handleScroll = () => {
  const viewportHeight = window.innerHeight || 1
  // 计算滚动进度，当滚动一个视口高度时达到最大值
  const progress = Math.min(Math.max(window.scrollY / viewportHeight, 0), 1)
  scrollProgress.value = progress
}

// 图片和文本区域的引用
const imageSectionRef = ref(null)
const textSectionRef = ref(null)
const storyTextSectionRef = ref(null)
const storyImageSectionRef = ref(null)
const decorationTextSectionRef = ref(null)
const decorationImageSectionRef = ref(null)

// 匹配图片区域和文本区域的高度
const matchHeights = () => {
  nextTick(() => {
    if (imageSectionRef.value && textSectionRef.value) {
      const textBox = textSectionRef.value.querySelector('.text-box')
      const imageContainer = imageSectionRef.value.querySelector('.image-container')
      
      if (textBox && imageContainer) {
        const textHeight = textBox.offsetHeight
        imageContainer.style.height = `${textHeight}px`
      }
    }
    
    // 匹配佛教故事画区域的高度
    if (storyTextSectionRef.value && storyImageSectionRef.value) {
      const storyTextBox = storyTextSectionRef.value.querySelector('.story-text-box')
      const storyImageContainer = storyImageSectionRef.value.querySelector('.story-image-container')
      
      if (storyTextBox && storyImageContainer) {
        const storyTextHeight = storyTextBox.offsetHeight
        storyImageContainer.style.height = `${storyTextHeight}px`
      }
    }
    
    // 匹配装饰图案画区域的高度
    if (decorationTextSectionRef.value && decorationImageSectionRef.value) {
      const decorationTextBox = decorationTextSectionRef.value.querySelector('.decoration-text-box')
      const decorationImageContainer = decorationImageSectionRef.value.querySelector('.decoration-image-container')
      
      if (decorationTextBox && decorationImageContainer) {
        const decorationTextHeight = decorationTextBox.offsetHeight
        decorationImageContainer.style.height = `${decorationTextHeight}px`
      }
    }
  })
}

onMounted(() => {
  handleScroll()
  window.addEventListener('scroll', handleScroll, { passive: true })
  
  // 匹配高度
  matchHeights()
  
  // 监听窗口大小变化
  window.addEventListener('resize', matchHeights)
  
  // 使用 ResizeObserver 监听文本区域高度变化
  if (textSectionRef.value) {
    const textBox = textSectionRef.value.querySelector('.text-box')
    if (textBox && window.ResizeObserver) {
      const resizeObserver = new ResizeObserver(() => {
        matchHeights()
      })
      resizeObserver.observe(textBox)
      
      onBeforeUnmount(() => {
        resizeObserver.disconnect()
      })
    }
  }
  
  // 监听佛教故事画文本区域高度变化
  if (storyTextSectionRef.value) {
    const storyTextBox = storyTextSectionRef.value.querySelector('.story-text-box')
    if (storyTextBox && window.ResizeObserver) {
      const storyResizeObserver = new ResizeObserver(() => {
        matchHeights()
      })
      storyResizeObserver.observe(storyTextBox)
      
      onBeforeUnmount(() => {
        storyResizeObserver.disconnect()
      })
    }
  }
  
  // 监听装饰图案画文本区域高度变化
  if (decorationTextSectionRef.value) {
    const decorationTextBox = decorationTextSectionRef.value.querySelector('.decoration-text-box')
    if (decorationTextBox && window.ResizeObserver) {
      const decorationResizeObserver = new ResizeObserver(() => {
        matchHeights()
      })
      decorationResizeObserver.observe(decorationTextBox)
      
      onBeforeUnmount(() => {
        decorationResizeObserver.disconnect()
      })
    }
  }
})

onBeforeUnmount(() => {
  window.removeEventListener('scroll', handleScroll)
  window.removeEventListener('resize', matchHeights)
})
</script>

<style scoped>
.mural-page {
  min-height: 100vh;
  background: var(--dunhuang-cream-white);
  padding-top: 0;
  padding-bottom: 0;
}

.top-banner {
  width: 100%;
  height: 100vh;
  position: fixed;
  top: 0;
  left: 0;
  z-index: 1;
  overflow: hidden;
  margin-top: 0;
}

.banner-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
  display: block;
  transform-origin: center;
  animation: bannerZoom 14s ease-in-out infinite alternate;
  will-change: transform;
  transition: filter 0.1s linear;
}

.banner-title {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 10;
  text-align: center;
  pointer-events: none;
  animation: titleFadeIn 2s ease-out;
}

.main-title {
  font-family: 'STXingkai', '华文行楷', 'STKaiti', 'KaiTi', serif;
  font-size: 180px;
  font-weight: normal;
  color: rgba(255, 255, 255, 0.95);
  -webkit-text-stroke: 3px #D4AF37;
  text-stroke: 3px #D4AF37;
  text-shadow: 
    4px 4px 12px rgba(0, 0, 0, 0.8),
    8px 8px 24px rgba(0, 0, 0, 0.6),
    0 0 40px rgba(255, 255, 255, 0.3),
    0 0 80px rgba(255, 255, 255, 0.2),
    0 0 20px rgba(212, 175, 55, 0.6),
    0 0 40px rgba(212, 175, 55, 0.4);
  letter-spacing: 30px;
  line-height: 1.2;
  margin: 0;
  white-space: nowrap;
  display: inline-block;
  transform-origin: center;
  transition: transform 0.2s ease-out, filter 0.2s ease-out;
}

@keyframes titleFadeIn {
  0% {
    opacity: 0;
    transform: translate(-50%, calc(-50% + 30px));
  }
  100% {
    opacity: 1;
    transform: translate(-50%, -50%);
  }
}

@keyframes bannerZoom {
  0% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.12);
  }
  100% {
    transform: scale(1.06);
  }
}

/* 尊像画内容区域 */
.content-section {
  position: relative;
  z-index: 10;
  margin-top: 100vh;
  background: #0d1117;
  min-height: 100vh;
  padding: 120px 80px;
  overflow: hidden;
}

.content-section::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image: 
    radial-gradient(ellipse at 25% 25%, rgba(79, 172, 254, 0.12) 0%, transparent 60%),
    radial-gradient(ellipse at 75% 75%, rgba(56, 189, 248, 0.08) 0%, transparent 60%),
    radial-gradient(ellipse at 50% 50%, rgba(30, 64, 175, 0.06) 0%, transparent 80%);
  pointer-events: none;
  opacity: 0.6;
}

.section-title {
  position: absolute;
  top: 50px;
  left: 80px;
  font-family: 'STXingkai', '华文行楷', 'STKaiti', 'KaiTi', serif;
  font-size: 42px;
  color: #D4AF37;
  font-weight: normal;
  letter-spacing: 4px;
  z-index: 20;
  padding-bottom: 4px;
  border-bottom: 2px solid #D4AF37;
}

.content-wrapper {
  max-width: 1400px;
  margin: 0 auto;
  display: flex;
  gap: 80px;
  align-items: flex-start;
  position: relative;
  z-index: 1;
  margin-top: 50px;
}

/* 左侧图片区域 */
.image-section {
  flex: 0 0 auto;
  width: calc(45% - 100px);
  position: relative;
  transform: translateX(100px);
  z-index: 2;
  display: flex;
  align-items: flex-start;
}

.image-container {
  position: relative;
  padding: 8px;
  border-radius: 4px;
  background: linear-gradient(135deg, #D4AF37 0%, #FFD700 25%, #FFA500 50%, #D4AF37 75%, #B8860B 100%);
  box-shadow: 0 12px 48px rgba(0, 0, 0, 0.4), 0 4px 16px rgba(0, 0, 0, 0.3);
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.content-image {
  width: 100%;
  height: 100%;
  display: block;
  object-fit: cover;
  border-radius: 2px;
  background: #fff;
}

/* 右侧文本区域 */
.text-section {
  flex: 0 0 55%;
  transform: translateX(-100px) translateY(75px);
  position: relative;
  z-index: 1;
}

.text-box {
  background: #ffffff;
  padding: 60px 50px 60px 150px;
  border-radius: 4px;
  box-shadow: 0 12px 48px rgba(0, 0, 0, 0.4), 0 4px 16px rgba(0, 0, 0, 0.3);
}

.text-title {
  font-family: 'STXingkai', '华文行楷', 'STKaiti', 'KaiTi', serif;
  font-size: 52px;
  color: #ff6b35;
  margin: 0 0 20px 0;
  font-weight: normal;
  line-height: 1.3;
  letter-spacing: 4px;
}

.text-subtitle {
  font-size: 18px;
  color: #ff6b35;
  margin: 0 0 35px 0;
  line-height: 1.8;
  font-weight: 500;
  font-family: 'STKaiti', 'KaiTi', serif;
}

.text-body {
  font-size: 16px;
  color: #222;
  line-height: 2;
  font-family: 'SimSun', '宋体', serif;
}

.text-body p {
  margin: 0 0 24px 0;
  text-align: justify;
  text-indent: 2em;
}

.text-body p:last-child {
  margin-bottom: 0;
}

/* 响应式设计 */
@media (max-width: 1400px) {
  .content-section {
    padding: 100px 60px;
  }
  
  .section-title {
    top: 30px;
    left: 60px;
    font-size: 38px;
  }
  
  .content-wrapper {
    gap: 60px;
  }
}

@media (max-width: 1200px) {
  .content-wrapper {
    flex-direction: column;
    gap: 50px;
  }
  
  .image-section {
    flex: 1;
    width: 100%;
    max-width: 600px;
  }
  
  .text-section {
    flex: 1;
    width: 100%;
  }
  
  .text-box {
    padding: 50px 40px;
  }
}

@media (max-width: 768px) {
  .content-section {
    padding: 80px 30px;
  }
  
  .section-title {
    top: 10px;
    left: 30px;
    font-size: 32px;
    letter-spacing: 2px;
    padding-bottom: 4px;
  }
  
  .content-wrapper {
    gap: 40px;
  }
  
  .text-box {
    padding: 40px 30px;
  }
  
  .text-title {
    font-size: 40px;
    letter-spacing: 2px;
  }
  
  .text-subtitle {
    font-size: 16px;
  }
  
  .text-body {
    font-size: 15px;
    line-height: 1.8;
  }
}

/* 佛教故事画内容区域 */
.story-section {
  position: relative;
  z-index: 10;
  background: #1a3a3f;
  min-height: auto;
  padding: 120px 80px;
  padding-bottom: 80px;
  overflow: visible;
}

.story-section::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image: 
    radial-gradient(ellipse at 20% 30%, rgba(79, 172, 254, 0.1) 0%, transparent 60%),
    radial-gradient(ellipse at 80% 70%, rgba(56, 189, 248, 0.08) 0%, transparent 60%);
  pointer-events: none;
  opacity: 0.5;
  z-index: 0;
}

.story-wrapper {
  max-width: 1400px;
  margin: 0 auto;
  display: flex;
  gap: 0px;
  align-items: center;
  position: relative;
  z-index: 1;
}

/* 左侧文本区域 */
.story-text-section {
  flex: 0 0 auto;
  width: calc(55% - 150px);
  position: relative;
  z-index: 1;
  margin: 0 auto;
}

.story-text-box {
  color: #fff;
}

.story-title {
  font-family: 'STXingkai', '华文行楷', 'STKaiti', 'KaiTi', serif;
  font-size: 42px;
  color: #D4AF37;
  margin: 0 0 25px 0;
  padding-bottom: 15px;
  border-bottom: 1px solid #fff;
  font-weight: normal;
  letter-spacing: 4px;
  line-height: 1.5;
}

.story-body {
  font-size: 18px;
  color: #fff;
  line-height: 1.6;
  font-family: 'SimSun', '宋体', serif;
}

.story-paragraph {
  margin-bottom: 20px;
}

.story-paragraph:last-child {
  margin-bottom: 0;
}

.story-subtitle {
  font-family: 'STXingkai', '华文行楷', 'STKaiti', 'KaiTi', serif;
  font-size: 28px;
  color: #A55A5A;
  margin: 0 0 12px 0;
  font-weight: normal;
  letter-spacing: 2px;
}

.story-body p {
  margin: 0 0 16px 0;
  text-align: justify;
  text-indent: 2em;
  line-height: 1.6;
}

.story-body p:last-child {
  margin-bottom: 0;
}

/* 右侧图片区域 */
.story-image-section {
  flex: 0 0 45%;
  position: relative;
  z-index: 2;
  display: flex;
  align-items: flex-start;
  justify-content: center;
  margin-left: -50px;
}

.story-image-container {
  position: relative;
  width: fit-content;
  border: dimgrey solid 5px;
  border-radius: 4px;
  background: #fff;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto;
  box-shadow: 11px 10px 10px rgba(0, 0, 0, 0.5);
}

.story-content-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.story-image-placeholder {
  width: 400px;
  height: 100%;
  background: linear-gradient(135deg, #f5f5f5 0%, #e0e0e0 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  color: #999;
  font-size: 16px;
}

/* 佛教故事画响应式设计 */
@media (max-width: 1400px) {
  .story-section {
    padding: 100px 60px;
  }
  
  .story-wrapper {
    gap: 10px;
  }
}

@media (max-width: 1200px) {
  .story-wrapper {
    flex-direction: column;
    gap: 50px;
  }
  
  .story-text-section {
    flex: 1;
    width: 100%;
  }
  
  .story-image-section {
    flex: 1;
    width: 100%;
  }
  
  .story-image-container {
    min-height: 400px;
    width: calc(100% - 150px);
  }
}

@media (max-width: 768px) {
  .story-section {
    padding: 80px 30px;
  }
  
  .story-wrapper {
    gap: 20px;
  }
  
  .story-title {
    font-size: 32px;
    letter-spacing: 2px;
    margin-bottom: 30px;
  }
  
  .story-subtitle {
    font-size: 24px;
  }
  
  .story-body {
    font-size: 16px;
    line-height: 1.8;
  }
  
  .story-image-container {
    min-height: 300px;
    width: calc(100% - 100px);
  }
}

/* 装饰图案画内容区域 */
.decoration-wrapper {
  max-width: 1400px;
  margin: 100px auto 0;
  display: flex;
  gap: 0px;
  align-items: center;
  position: relative;
  z-index: 1;
}

/* 左侧图片区域 */
.decoration-image-section {
  flex: 0 0 45%;
  position: relative;
  z-index: 2;
  display: flex;
  align-items: flex-start;
  justify-content: center;
}

.decoration-image-container {
  position: relative;
  width: fit-content;
  border: dimgrey solid 5px;
  border-radius: 4px;
  background: #fff;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto;
  box-shadow: -11px 10px 10px rgba(0, 0, 0, 0.5);
}

.decoration-content-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.mural-hover-frame {
  overflow: hidden;
}

.mural-hover-dim {
  position: absolute;
  inset: 0;
  background: rgba(0, 0, 0, 0.55);
  opacity: 0;
  transition: opacity 0.35s ease;
  z-index: 3;
  pointer-events: none;
}

.mural-hover-caption {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  padding: 22px 18px 20px;
  background: rgba(0, 0, 0, 0.82);
  opacity: 0;
  transform: translate3d(0, 100%, 0);
  transition: transform 0.38s ease, opacity 0.38s ease;
  z-index: 4;
  pointer-events: none;
  text-align: center;
}

.mural-hover-title {
  font-size: 44px;
  font-weight: 800;
  letter-spacing: 6px;
  color: rgba(255, 255, 255, 0.96);
  line-height: 1.2;
  margin-bottom: 10px;
}

.mural-hover-desc {
  font-size: 20px;
  letter-spacing: 2px;
  color: rgba(255, 255, 255, 0.88);
}

@media (hover: hover) and (pointer: fine) {
  .mural-hover-frame .story-content-image,
  .mural-hover-frame .decoration-content-image {
    transition: transform 0.6s ease;
    transform: translate3d(0, 0, 0);
    will-change: transform;
  }

  .mural-hover-frame:hover .story-content-image,
  .mural-hover-frame:hover .decoration-content-image {
    transform: translate3d(0, -18px, 0) scale(1.04);
  }

  .mural-hover-frame:hover .mural-hover-caption {
    opacity: 1;
    transform: translate3d(0, 0, 0);
  }
}

@media (prefers-reduced-motion: reduce) {
  .mural-hover-dim,
  .mural-hover-caption,
  .mural-hover-frame .story-content-image,
  .mural-hover-frame .decoration-content-image {
    transition: none;
  }

  .mural-hover-frame:hover .story-content-image,
  .mural-hover-frame:hover .decoration-content-image {
    transform: none;
  }
}

.decoration-image-placeholder {
  width: 400px;
  height: 100%;
  background: linear-gradient(135deg, #f5f5f5 0%, #e0e0e0 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  color: #999;
  font-size: 16px;
}

/* 右侧文本区域 */
.decoration-text-section {
  flex: 0 0 auto;
  width: calc(55% - 150px);
  position: relative;
  z-index: 1;
  transform: translateX(50px);
}

.decoration-text-box {
  color: #fff;
}

.decoration-title {
  font-family: 'STXingkai', '华文行楷', 'STKaiti', 'KaiTi', serif;
  font-size: 42px;
  color: #D4AF37;
  margin: 0 0 25px 0;
  padding-bottom: 15px;
  border-bottom: 1px solid #fff;
  font-weight: normal;
  letter-spacing: 4px;
  line-height: 1.5;
}

.decoration-subtitle {
  font-size: 18px;
  color: #fff;
  margin: 0 0 20px 0;
  line-height: 1.8;
  font-weight: 500;
  font-family: 'STKaiti', 'KaiTi', serif;
}

.decoration-body {
  font-size: 18px;
  color: #fff;
  line-height: 1.6;
  font-family: 'SimSun', '宋体', serif;
}

.decoration-body p {
  margin: 0 0 16px 0;
  text-align: justify;
  text-indent: 2em;
  line-height: 1.6;
}

.decoration-body p:last-child {
  margin-bottom: 0;
}

/* 装饰图案画响应式设计 */
@media (max-width: 1400px) {
  .decoration-wrapper {
    gap: 10px;
    margin-top: 80px;
  }
}

@media (max-width: 1200px) {
  .decoration-wrapper {
    flex-direction: column;
    gap: 50px;
    margin-top: 60px;
  }
  
  .decoration-text-section {
    flex: 1;
    width: 100%;
    margin-left: 0;
  }
  
  .decoration-image-section {
    flex: 1;
    width: 100%;
  }
  
  .decoration-image-container {
    min-height: 400px;
    width: calc(100% - 150px);
  }
}

@media (max-width: 768px) {
  .decoration-wrapper {
    gap: 20px;
    margin-top: 50px;
  }
  
  .decoration-title {
    font-size: 32px;
    letter-spacing: 2px;
    margin-bottom: 30px;
  }
  
  .decoration-subtitle {
    font-size: 16px;
  }
  
  .decoration-body {
    font-size: 16px;
    line-height: 1.8;
  }
  
  .decoration-image-container {
    min-height: 300px;
    width: calc(100% - 100px);
  }
}

/* 经变画内容区域 */
.sutra-wrapper {
  max-width: 1400px;
  margin: 80px auto 0;
  position: relative;
  z-index: 20;
  padding: 40px 40px;
  background: transparent;
}

.sutra-main-title {
  font-family: 'STXingkai', '华文行楷', 'STKaiti', 'KaiTi', serif;
  font-size: 48px;
  color: #D4AF37;
  text-align: center;
  margin: 0 0 40px 0;
  font-weight: normal;
  letter-spacing: 6px;
  line-height: 1.5;
  position: relative;
  z-index: 21;
  padding-bottom: 15px;
  border-bottom: 2px solid rgba(255, 255, 255, 0.5);
}

.sutra-content-wrapper {
  display: flex;
  align-items: stretch;
  position: relative;
  gap: 0;
  min-height: 260px;
  width: 100%;
}

.sutra-column {
  position: relative;
  padding: 0 40px;
  min-width: 0;
}

.sutra-column-left {
  padding-left: 0;
  flex: 0 0 calc(33.333% - 150px);
}

.sutra-column-middle {
  flex: 1;
  padding-left: 70px;
  padding-right: 70px;
}

.sutra-column-right {
  padding-right: 0;
  padding-left: 50px;
  flex: 1;
}

.sutra-divider {
  width: 2px;
  background: rgba(255, 255, 255, 0.3);
  align-self: stretch;
  flex-shrink: 0;
  min-height: 100%;
  position: relative;
}

.sutra-divider::after {
  content: '';
  position: absolute;
  bottom: -150px;
  left: 0;
  width: 2px;
  height: 150px;
  background: rgba(255, 255, 255, 0.3);
}

.sutra-text-box {
  color: #fff;
  position: relative;
  z-index: 21;
}

.sutra-column-title {
  font-family: 'STXingkai', '华文行楷', 'STKaiti', 'KaiTi', serif;
  font-size: 32px;
  color: #A55A5A;
  margin: 0 0 25px 0;
  padding-bottom: 15px;
  border-bottom: 2px solid rgba(255, 255, 255, 0.5);
  font-weight: normal;
  letter-spacing: 3px;
  line-height: 1.5;
}

.sutra-body {
  font-size: 17px;
  color: #fff;
  line-height: 1.8;
  font-family: 'SimSun', '宋体', serif;
}

.sutra-body p {
  margin: 0 0 20px 0;
  text-align: justify;
  text-indent: 2em;
  line-height: 1.8;
}

.sutra-body p:last-child {
  margin-bottom: 0;
}

/* 左边列第一个段落添加下划线 */
.sutra-column-left .sutra-body p:first-child {
  padding-bottom: 20px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.5);
  margin-bottom: 20px;
}

/* 左边列图片区域 */
.sutra-left-image-area {
  width: 100%;
  margin-top: 20px;
  margin-bottom: 20px;
  padding-bottom: 20px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.5);
}

/* 中间列的文本下划线 */
.sutra-column-middle .sutra-body {
  padding-bottom: 20px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.5);
}

/* 右侧列的文本下划线 */
.sutra-column-right .sutra-body {
  padding-bottom: 20px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.5);
}

/* 右侧列的图片区域 */
.sutra-right-image-area {
  margin-top: 30px;
  margin-bottom: 0;
  transform: translateY(20px);
}

.sutra-right-image-area .sutra-content-image {
  height: 520px;
}

/* 中间列的图片区域 */
.sutra-image-area {
  margin-top: 0;
  margin-bottom: 25px;
  width: 100%;
}

/* 中间列底部图片区域 */
.sutra-middle-bottom-image-area {
  margin-top: 20px;
  margin-bottom: 0;
  width: 100%;
}

.sutra-image-placeholder {
  width: 100%;
  height: 300px;
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.1) 0%, rgba(255, 255, 255, 0.05) 100%);
  border: 2px solid rgba(255, 255, 255, 0.2);
  border-radius: 4px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: rgba(255, 255, 255, 0.5);
  font-size: 16px;
  font-family: 'SimSun', '宋体', serif;
}

.sutra-image-placeholder::before {
  content: '图片预留区域';
}

/* 经变画图片样式 */
.sutra-content-image {
  width: 100%;
  height: 260px;
  object-fit: cover;
  border-radius: 4px;
  display: block;
}

/* 经变画响应式设计 */
@media (max-width: 1400px) {
  .sutra-wrapper {
    padding: 0 30px;
  }
  
  .sutra-main-title {
    font-size: 42px;
    margin-bottom: 50px;
  }
  
  .sutra-column {
    padding: 0 30px;
  }
}

@media (max-width: 1200px) {
  .sutra-content-wrapper {
    flex-direction: column;
    gap: 0;
  }
  
  .sutra-column {
    flex: 1;
    width: 100%;
    padding: 40px 0;
  }
  
  .sutra-column-left,
  .sutra-column-right {
    padding-left: 0;
    padding-right: 0;
  }
  
  .sutra-divider {
    width: 100%;
    height: 1px;
    margin: 20px 0;
  }
}

@media (max-width: 768px) {
  .sutra-wrapper {
    margin-top: 80px;
    padding: 0 20px;
  }
  
  .sutra-main-title {
    font-size: 32px;
    letter-spacing: 3px;
    margin-bottom: 40px;
  }
  
  .sutra-column-title {
    font-size: 26px;
    letter-spacing: 2px;
    margin-bottom: 20px;
  }
  
  .sutra-body {
    font-size: 15px;
    line-height: 1.8;
  }
  
  .sutra-body p {
    margin-bottom: 18px;
  }
}

/* 固定背景图片区域 */
.fixed-image-section {
  position: relative;
  width: 100%;
  height: 400px;
  margin-top: 100px;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: visible;
  z-index: 15;
}

.fixed-image-viewport {
  width: 1200px;
  height: 400px;
  position: relative;
  background-color: rgba(255, 255, 255, 0.1);
  background-image: url('/images/mural/bh05.jpg');
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
  background-repeat: no-repeat;
  border-radius: 4px;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
  border: 2px solid rgba(255, 255, 255, 0.3);
}

.mural-showcase-section {
  position: relative;
  z-index: 20;
  padding: 80px 80px 60px;
  background: linear-gradient(135deg, #2a1d14 0%, #3a281a 40%, #2b1f16 100%);
  overflow: hidden;
}

.mural-showcase-section::before,
.mural-showcase-section::after {
  content: '';
  position: absolute;
  inset: -25%;
  pointer-events: none;
  z-index: 0;
  filter: blur(48px);
  opacity: 0.55;
  transform: translate3d(0, 0, 0);
}

.mural-showcase-section::before {
  background:
    radial-gradient(60% 60% at 20% 35%, rgba(255, 196, 120, 0.55) 0%, rgba(255, 196, 120, 0) 60%),
    radial-gradient(55% 55% at 80% 30%, rgba(189, 118, 60, 0.55) 0%, rgba(189, 118, 60, 0) 62%),
    radial-gradient(60% 60% at 45% 85%, rgba(120, 70, 35, 0.65) 0%, rgba(120, 70, 35, 0) 65%);
  mix-blend-mode: screen;
  animation: muralAuroraDrift 16s ease-in-out infinite alternate;
}

.mural-showcase-section::after {
  background:
    radial-gradient(65% 65% at 30% 60%, rgba(255, 220, 170, 0.35) 0%, rgba(255, 220, 170, 0) 62%),
    radial-gradient(55% 55% at 70% 70%, rgba(150, 85, 35, 0.55) 0%, rgba(150, 85, 35, 0) 64%),
    linear-gradient(120deg, rgba(255, 190, 120, 0.18) 0%, rgba(120, 70, 35, 0.0) 55%, rgba(200, 120, 60, 0.16) 100%);
  mix-blend-mode: overlay;
  opacity: 0.45;
  animation: muralAuroraDrift2 22s ease-in-out infinite;
}

@keyframes muralAuroraDrift {
  0% {
    transform: translate3d(-3%, -2%, 0) rotate(0deg) scale(1);
  }
  100% {
    transform: translate3d(4%, 3%, 0) rotate(12deg) scale(1.05);
  }
}

@keyframes muralAuroraDrift2 {
  0% {
    transform: translate3d(3%, 2%, 0) rotate(-6deg) scale(1);
  }
  50% {
    transform: translate3d(-2%, 0%, 0) rotate(6deg) scale(1.03);
  }
  100% {
    transform: translate3d(2%, -2%, 0) rotate(-10deg) scale(1.02);
  }
}

.mural-showcase-header {
  max-width: 1400px;
  margin: 0 auto 30px;
  display: flex;
  justify-content: center;
}

.mural-showcase-title {
  padding: 10px 30px;
  background: rgba(0, 0, 0, 0.25);
  color: #D4AF37;
  font-size: 26px;
  font-weight: 700;
  letter-spacing: 2px;
  border-radius: 4px;
  border: 1px solid rgba(212, 175, 55, 0.55);
  box-shadow: 0 10px 26px rgba(0, 0, 0, 0.25);
}

.mural-showcase-body {
  max-width: 1400px;
  margin: 0 auto;
  display: flex;
  gap: 36px;
  align-items: stretch;
  position: relative;
  z-index: 1;
}

@media (prefers-reduced-motion: reduce) {
  .mural-showcase-section::before,
  .mural-showcase-section::after {
    animation: none;
  }
}

.mural-showcase-left {
  flex: 0 0 52%;
  display: flex;
  flex-direction: column;
  gap: 22px;
}

.mural-showcase-right {
  flex: 1;
  display: grid;
  grid-template-rows: repeat(3, 1fr);
  gap: 18px;
}

.mural-showcase-media {
  border: 6px solid #1a4f6b;
  background: rgba(0, 0, 0, 0.4);
  padding: 10px;
}

.mural-showcase-video-placeholder {
  width: 100%;
  aspect-ratio: 16 / 9;
  background: linear-gradient(135deg, rgba(0, 0, 0, 0.7) 0%, rgba(0, 0, 0, 0.25) 100%);
  border: 2px solid rgba(255, 255, 255, 0.25);
  display: flex;
  align-items: center;
  justify-content: center;
  color: rgba(255, 255, 255, 0.85);
  font-size: 16px;
  letter-spacing: 1px;
}

.mural-showcase-video {
  width: 100%;
  aspect-ratio: 16 / 9;
  display: block;
  object-fit: cover;
  background: #000;
  border: 2px solid rgba(255, 255, 255, 0.25);
}

.mural-showcase-text {
  border: 6px solid #1a4f6b;
  background: rgba(26, 79, 107, 0.12);
  padding: 18px 18px 20px;
}

.mural-showcase-text-title {
  color: #fff;
  text-align: center;
  font-size: 18px;
  font-weight: 700;
  padding: 10px 12px;
  background: #1a4f6b;
  border-radius: 3px;
  margin-bottom: 14px;
}

.mural-showcase-text-body {
  color: rgba(255, 255, 255, 0.92);
  font-size: 14px;
  line-height: 1.9;
  text-align: justify;
}

.mural-showcase-image {
  border: 6px solid #1a4f6b;
  background: rgba(26, 79, 107, 0.12);
  padding: 10px;
}

.mural-showcase-img {
  width: 100%;
  height: 100%;
  min-height: 160px;
  display: block;
  object-fit: cover;
  background: #fff;
  border: 2px solid rgba(26, 79, 107, 0.35);
}

.mural-showcase-image-placeholder {
  width: 100%;
  height: 100%;
  min-height: 160px;
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.55) 0%, rgba(255, 255, 255, 0.15) 100%);
  border: 2px solid rgba(26, 79, 107, 0.35);
  display: flex;
  align-items: center;
  justify-content: center;
  color: rgba(26, 79, 107, 0.85);
  font-size: 15px;
  letter-spacing: 1px;
}

.mural-showcase-image-placeholder-filled {
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  color: transparent;
}

@media (max-width: 1200px) {
  .mural-showcase-section {
    padding: 70px 60px 50px;
  }

  .mural-showcase-body {
    gap: 28px;
  }
}

@media (max-width: 900px) {
  .mural-showcase-section {
    padding: 60px 30px 40px;
  }

  .mural-showcase-body {
    flex-direction: column;
  }

  .mural-showcase-left {
    flex: 1;
  }

  .mural-showcase-right {
    grid-template-rows: none;
    grid-template-columns: 1fr;
  }
}

</style>

