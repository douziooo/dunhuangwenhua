<template>
  <div class="mogao-page">
    <NavBar />
    <div class="page-header">
      <h1 class="page-title">崖壁佛国</h1>
      <p class="page-subtitle">探索莫高窟的千年奇迹，感受洞窟艺术的震撼</p>
    </div>
    <div class="container">
      <div class="stats-section">
        <el-row :gutter="30">
          <el-col :xs="24" :sm="8" v-for="stat in stats" :key="stat.label">
            <el-card class="stat-card">
              <div class="stat-icon">{{ stat.icon }}</div>
              <div class="stat-value">{{ stat.value }}</div>
              <div class="stat-label">{{ stat.label }}</div>
            </el-card>
          </el-col>
        </el-row>
      </div>
      
      <!-- 开篇定调：大漠藏瑰宝，千年一窟间 -->
      <div class="intro-section">
        <div class="intro-content-wrapper">
          <div class="intro-image-container" @mouseenter="showVideoControls = true" @mouseleave="showVideoControls = false">
            <video 
              ref="introVideoRef"
              class="intro-video"
              loop
              playsinline
              :poster="assetUrl('/images/mogao/mg01.jpg')"
              @loadedmetadata="onVideoLoaded"
              @timeupdate="onTimeUpdate"
              @play="isPlaying = true"
              @pause="isPlaying = false"
              @click="togglePlay"
            >
              <source :src="assetUrl('/video/mg01.mp4')" type="video/mp4">
              您的浏览器不支持视频播放。
            </video>
            <div class="video-controls" :class="{ 'show': showVideoControls || !isPlaying }">
              <!-- 进度条 -->
              <div class="video-progress-container" @click="seekVideo">
                <div class="video-progress-bar">
                  <div class="video-progress-filled" :style="{ width: progressPercentage + '%' }"></div>
                  <div class="video-progress-thumb" :style="{ left: progressPercentage + '%' }"></div>
                </div>
              </div>
              <!-- 控制按钮 -->
              <div class="video-controls-buttons">
                <button class="video-control-btn" @click.stop="togglePlay">
                  <span v-if="isPlaying">⏸</span>
                  <span v-else>▶</span>
                </button>
                <button class="video-control-btn" @click.stop="toggleMute">
                  <span v-if="isMuted">🔇</span>
                  <span v-else>🔊</span>
                </button>
                <button class="video-control-btn video-fullscreen-btn" @click.stop="toggleFullscreen" title="全屏">
                  <span v-if="isFullscreen" class="fullscreen-icon exit">⊟</span>
                  <span v-else class="fullscreen-icon">⊞</span>
                </button>
                <span class="video-time">{{ formatTime(currentTime) }} / {{ formatTime(duration) }}</span>
              </div>
            </div>
          </div>
          <div class="intro-text-container">
            <h2 class="intro-title">大漠藏瑰宝，千年一窟间</h2>
            <p class="intro-description">
              在茫茫大漠之中，莫高窟如一颗璀璨的明珠，静静地诉说着千年的历史。从公元366年乐尊和尚开凿第一个洞窟开始，这座艺术宝库见证了十六国、北朝、隋、唐、五代、西夏、元等历代王朝的兴衰更迭。
            </p>
            <p class="intro-description">
              735个洞窟，4.5万平方米壁画，2415尊彩塑，这些数字背后是无数艺术家的心血与智慧。每一笔一划，每一尊塑像，都承载着厚重的历史文化底蕴，展现了中华文明的博大精深。
            </p>
          </div>
        </div>
      </div>
      
      <!-- 壁上丹青——壁画艺术 -->
      <div class="mural-art-section">
        <h2 class="section-title">壁上丹青——壁画艺术</h2>
        <p class="section-subtitle">Mural Art</p>
        <div class="mural-carousel-container">
          <button class="mural-carousel-btn mural-carousel-btn-left" @click="prevMuralCard">
            <span>‹</span>
          </button>
          <div class="mural-carousel-wrapper">
            <div 
              class="mural-carousel-track"
              :style="{ 
                transform: `translateX(-${currentMuralIndex * (320 + 30)}px)`,
                transition: 'transform 0.5s ease'
              }"
            >
              <div 
                class="mural-card" 
                v-for="(item, index) in muralArtItems" 
                :key="index"
              >
                <div class="mural-card-image-container">
                  <img
                    v-if="item.image"
                    class="mural-card-image"
                    :src="item.image"
                    :alt="item.title"
                  />
                  <div v-else class="mural-card-image-placeholder">图片预留区域</div>
                </div>
                <div class="mural-card-content">
                  <h3 class="mural-card-title">{{ item.title }}</h3>
                  <p class="mural-card-description">{{ item.description }}</p>
                </div>
              </div>
            </div>
          </div>
          <button class="mural-carousel-btn mural-carousel-btn-right" @click="nextMuralCard">
            <span>›</span>
          </button>
        </div>
      </div>
      
      <!-- 艺术价值的至高性 -->
      <div class="art-value-section">
        <h2 class="section-title">艺术价值的至高性</h2>
        <p class="section-subtitle">The Supreme Value of Art</p>
        <div class="art-value-cards">
          <div 
            class="art-value-card" 
            v-for="(item, index) in artValueItems" 
            :key="index"
          >
            <div class="art-value-image-container">
              <img
                v-if="item.image"
                class="art-value-image"
                :src="item.image"
                :alt="item.title"
              />
              <div v-else class="art-value-image-placeholder">图片预留区域</div>
            </div>
            <div class="art-value-content">
              <h3 class="art-value-title">{{ item.title }}</h3>
              <p class="art-value-description">{{ item.description }}</p>
            </div>
          </div>
        </div>
      </div>
      
      <div class="cave-experience-section">
        <h2 class="section-title">数字洞窟体验</h2>
        <p class="section-subtitle">360°全景探索第45窟</p>
        <div class="panorama-container">
          <div class="panorama-carousel">
            <!-- 左侧切换按钮 -->
            <button class="carousel-btn carousel-btn-left" @click="prevImage">
              <span>‹</span>
            </button>
            
            <!-- 轮播图内容 -->
            <div class="panorama-slide-wrapper">
              <div 
                class="panorama-slides-container"
                :style="{ 
                  transform: `translateX(-${currentImageIndex * 100}%)`,
                  transition: isTransitioning ? 'transform 0.6s cubic-bezier(0.25, 0.46, 0.45, 0.94)' : 'none'
                }"
                @transitionend="handleTransitionEnd"
              >
                <div 
                  class="panorama-slide" 
                  v-for="(item, index) in slidesWithClones" 
                  :key="`slide-${index}`"
                >
                  <div class="panorama-placeholder">
                    <div class="panorama-image-container">
                      <img 
                        v-if="item.src" 
                        :src="item.src" 
                        :alt="item.alt" 
                        class="panorama-image"
                      />
                      <div v-else class="panorama-image-placeholder">
                        <span>图片预留区域 {{ index + 1 }}</span>
                      </div>
                    </div>
                    <div class="panorama-content">
                      <p class="panorama-text">360°全景视图</p>
                      <p class="panorama-desc">拖拽鼠标环视洞窟内部</p>
                      <div class="panorama-controls">
                        <el-button type="primary" @click="item.buttonAction">查看洞窟信息</el-button>
                      </div>
                    </div>
                    <div class="panorama-bg"></div>
                  </div>
                </div>
              </div>
            </div>
            
            <!-- 右侧切换按钮 -->
            <button class="carousel-btn carousel-btn-right" @click="nextImage">
              <span>›</span>
            </button>
          </div>
          
          <!-- 轮播图指示器 -->
          <div class="carousel-indicators">
            <span 
              v-for="(item, index) in panoramaImages" 
              :key="index"
              class="indicator"
              :class="{ active: currentImageIndex === index + 1 }"
              @click="goToImage(index)"
            ></span>
          </div>
        </div>
      </div>
      
      <div class="cave-info-section">
        <el-row :gutter="30">
          <el-col :xs="24" :md="12" v-for="info in caveInfos" :key="info.title">
            <el-card class="info-card">
              <div class="info-header">
                <h3 class="info-title">{{ info.title }}</h3>
                <span class="info-period">{{ info.period }}</span>
              </div>
              <p class="info-description">{{ info.description }}</p>
              <div class="info-features">
                <el-tag v-for="feature in info.features" :key="feature" size="small">{{ feature }}</el-tag>
              </div>
            </el-card>
          </el-col>
        </el-row>
      </div>

      <h2 class="section-title">旅游指南打卡点</h2>
      <p class="section-subtitle">Travel Guide Checkpoints</p>

      <div class="mogao-bottom-split">
        <div class="mogao-bottom-left">
          <div class="heritage-list">
            <div
              v-for="(item, index) in heritageListItems"
              :key="item.title"
              class="heritage-item"
              :class="{ 'heritage-item-last': index === heritageListItems.length - 1 }"
            >
              <div class="heritage-item-inner">
                <div class="heritage-image">
                  <div class="heritage-image-placeholder">
                    <img
                      v-if="item.image"
                      class="heritage-image-img"
                      :src="item.image"
                      :alt="item.title"
                    />
                    <span v-else>图片预留区域</span>
                  </div>
                </div>
                <div class="heritage-info">
                  <div class="heritage-title">{{ item.title }}</div>
                  <div class="heritage-lines">
                    <div class="heritage-line"><span class="heritage-label">门票：</span>{{ item.ticket }}</div>
                    <div class="heritage-line"><span class="heritage-label">开放时间：</span>{{ item.hours }}</div>
                    <div class="heritage-line"><span class="heritage-label">建议游玩：</span>{{ item.suggested }}</div>
                    <div class="heritage-quote">{{ item.quote }}</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="mogao-bottom-right">
          <div class="heritage-list">
            <div
              v-for="(item, index) in heritageListItemsRight"
              :key="item.title"
              class="heritage-item"
              :class="{ 'heritage-item-last': index === heritageListItemsRight.length - 1 }"
            >
              <div class="heritage-item-inner">
                <div class="heritage-image">
                  <div class="heritage-image-placeholder">
                    <img
                      v-if="item.image"
                      class="heritage-image-img"
                      :src="item.image"
                      :alt="item.title"
                    />
                    <span v-else>图片预留区域</span>
                  </div>
                </div>
                <div class="heritage-info">
                  <div class="heritage-title">{{ item.title }}</div>
                  <div class="heritage-lines">
                    <div class="heritage-line"><span class="heritage-label">门票：</span>{{ item.ticket }}</div>
                    <div class="heritage-line"><span class="heritage-label">开放时间：</span>{{ item.hours }}</div>
                    <div class="heritage-line"><span class="heritage-label">建议游玩：</span>{{ item.suggested }}</div>
                    <div class="heritage-quote">{{ item.quote }}</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    
    <!-- 洞窟信息对话框 -->
    <el-dialog
      v-model="caveInfoVisible"
      title="第45窟 - 盛唐代表洞窟"
      width="800px"
    >
      <div class="cave-detail">
        <el-image
          src="https://images.unsplash.com/photo-1519681393784-d120267933ba?w=800&h=600&fit=crop"
          fit="cover"
          class="cave-detail-image"
        />
        <div class="cave-detail-text">
          <h4>洞窟简介</h4>
          <p>第45窟是莫高窟盛唐时期的代表洞窟之一，以其精美的彩塑和壁画而闻名。洞窟内保存有七身彩塑，包括一佛、二弟子、二菩萨、二天王，是莫高窟彩塑艺术的杰作。</p>
          <h4>艺术特色</h4>
          <ul>
            <li>彩塑造型优美，神态生动，体现了盛唐艺术的成熟</li>
            <li>壁画内容丰富，包括经变画、供养人像等</li>
            <li>色彩运用丰富，以石青、石绿、朱砂、金箔为主</li>
            <li>整体布局严谨，体现了唐代佛教艺术的巅峰水平</li>
          </ul>
        </div>
      </div>
    </el-dialog>
  </div>
</template>

<script setup>
import { ref, computed, nextTick, onMounted, onUnmounted } from 'vue'
import NavBar from '../components/NavBar.vue'

const baseURL = import.meta.env.BASE_URL || '/'
const assetUrl = (path) => path.startsWith('/') ? baseURL + path.slice(1) : path

// 视频控制
const introVideoRef = ref(null)
const isPlaying = ref(false)
const isMuted = ref(true)
const showVideoControls = ref(false)
const currentTime = ref(0)
const duration = ref(0)
const progressPercentage = ref(0)
const isFullscreen = ref(false)

// 格式化时间显示
const formatTime = (seconds) => {
  if (!seconds || isNaN(seconds)) return '00:00'
  const mins = Math.floor(seconds / 60)
  const secs = Math.floor(seconds % 60)
  return `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`
}

// 视频加载完成
const onVideoLoaded = () => {
  if (introVideoRef.value) {
    duration.value = introVideoRef.value.duration
    // 自动播放
    introVideoRef.value.play().then(() => {
      isPlaying.value = true
    }).catch(() => {
      isPlaying.value = false
    })
  }
}

// 时间更新
const onTimeUpdate = () => {
  if (introVideoRef.value) {
    currentTime.value = introVideoRef.value.currentTime
    if (duration.value > 0) {
      progressPercentage.value = (currentTime.value / duration.value) * 100
    }
  }
}

// 切换播放/暂停
const togglePlay = () => {
  if (introVideoRef.value) {
    if (isPlaying.value) {
      introVideoRef.value.pause()
      isPlaying.value = false
    } else {
      introVideoRef.value.play().then(() => {
        isPlaying.value = true
      })
    }
  }
}

// 切换静音
const toggleMute = () => {
  if (introVideoRef.value) {
    introVideoRef.value.muted = !isMuted.value
    isMuted.value = !isMuted.value
  }
}

// 跳转到指定时间
const seekVideo = (event) => {
  if (introVideoRef.value && duration.value > 0) {
    const progressContainer = event.currentTarget
    const rect = progressContainer.getBoundingClientRect()
    const clickX = event.clientX - rect.left
    const percentage = clickX / rect.width
    const newTime = percentage * duration.value
    introVideoRef.value.currentTime = newTime
    currentTime.value = newTime
  }
}

// 切换全屏
const toggleFullscreen = () => {
  const videoContainer = introVideoRef.value?.parentElement
  if (!videoContainer) return

  if (!isFullscreen.value) {
    // 进入全屏
    if (videoContainer.requestFullscreen) {
      videoContainer.requestFullscreen()
    } else if (videoContainer.webkitRequestFullscreen) {
      // Safari
      videoContainer.webkitRequestFullscreen()
    } else if (videoContainer.mozRequestFullScreen) {
      // Firefox
      videoContainer.mozRequestFullScreen()
    } else if (videoContainer.msRequestFullscreen) {
      // IE/Edge
      videoContainer.msRequestFullscreen()
    }
  } else {
    // 退出全屏
    if (document.exitFullscreen) {
      document.exitFullscreen()
    } else if (document.webkitExitFullscreen) {
      // Safari
      document.webkitExitFullscreen()
    } else if (document.mozCancelFullScreen) {
      // Firefox
      document.mozCancelFullScreen()
    } else if (document.msExitFullscreen) {
      // IE/Edge
      document.msExitFullscreen()
    }
  }
}

// 检查是否处于全屏状态
const checkFullscreen = () => {
  const fullscreenElement = 
    document.fullscreenElement ||
    document.webkitFullscreenElement ||
    document.mozFullScreenElement ||
    document.msFullscreenElement
  
  isFullscreen.value = !!fullscreenElement
}

onMounted(() => {
  // 确保视频元素已加载
  nextTick(() => {
    if (introVideoRef.value) {
      introVideoRef.value.muted = true
    }
  })

  // 监听全屏状态变化
  document.addEventListener('fullscreenchange', checkFullscreen)
  document.addEventListener('webkitfullscreenchange', checkFullscreen)
  document.addEventListener('mozfullscreenchange', checkFullscreen)
  document.addEventListener('MSFullscreenChange', checkFullscreen)
})

onUnmounted(() => {
  // 移除全屏状态监听
  document.removeEventListener('fullscreenchange', checkFullscreen)
  document.removeEventListener('webkitfullscreenchange', checkFullscreen)
  document.removeEventListener('mozfullscreenchange', checkFullscreen)
  document.removeEventListener('MSFullscreenChange', checkFullscreen)
})

const caveInfoVisible = ref(false)
const currentImageIndex = ref(1) // 从1开始，因为0是克隆的最后一张
const isTransitioning = ref(true)

// 轮播图数据（3张图片，预留位置）
const panoramaImages = ref([
  { 
    src: assetUrl('/images/mogao/mg01.jpg'), 
    alt: '全景图1',
    buttonAction: () => {
      window.open('https://vr.justeasy.cn/view/17h24244fh27l591-1722443200.html', '_blank')
    }
  },
  { 
    src: assetUrl('/images/mogao/mg02.jpg'), 
    alt: '全景图2',
    buttonAction: () => {
      window.open('https://vr.justeasy.cn/view/h91744715v3038e6-1744713036.html', '_blank')
    }
  },
  { 
    src: assetUrl('/images/mogao/mg03.jpg'), 
    alt: '全景图3',
    buttonAction: () => {
      window.open('https://vr.justeasy.cn/view/1750f7ja2333q911-1750733911.html', '_blank')
    }
  }
])

// 创建包含克隆项的完整数组（最后一张 + 原数组 + 第一张）
const slidesWithClones = computed(() => {
  const lastItem = panoramaImages.value[panoramaImages.value.length - 1]
  const firstItem = panoramaImages.value[0]
  return [lastItem, ...panoramaImages.value, firstItem]
})

// 切换到上一张图片
const prevImage = () => {
  currentImageIndex.value--
}

// 切换到下一张图片
const nextImage = () => {
  currentImageIndex.value++
}

// 跳转到指定图片
const goToImage = (index) => {
  currentImageIndex.value = index + 1 // +1 因为第一个是克隆项
}

// 处理过渡结束事件
const handleTransitionEnd = () => {
  if (currentImageIndex.value === 0) {
    // 到达克隆的最后一张，跳转到真正的最后一张
    isTransitioning.value = false
    requestAnimationFrame(() => {
      currentImageIndex.value = panoramaImages.value.length
      requestAnimationFrame(() => {
        isTransitioning.value = true
      })
    })
  } else if (currentImageIndex.value === slidesWithClones.value.length - 1) {
    // 到达克隆的第一张，跳转到真正的第一张
    isTransitioning.value = false
    requestAnimationFrame(() => {
      currentImageIndex.value = 1
      requestAnimationFrame(() => {
        isTransitioning.value = true
      })
    })
  }
}

const stats = ref([
  {
    icon: '🏛️',
    value: '735',
    label: '洞窟数量'
  },
  {
    icon: '🎨',
    value: '4.5万',
    label: '平方米壁画'
  },
  {
    icon: '🗿',
    value: '2415',
    label: '彩塑数量'
  }
])

const caveInfos = ref([
  {
    title: '第45窟',
    period: '盛唐',
    description: '第45窟是莫高窟盛唐时期的代表洞窟，以其精美的彩塑和壁画而闻名。洞窟内保存有七身彩塑，造型优美，神态生动，体现了盛唐艺术的成熟。',
    features: ['彩塑', '经变画', '盛唐艺术']
  },
  {
    title: '第220窟',
    period: '初唐',
    description: '第220窟是初唐时期的代表洞窟，以其精美的西方净土变而闻名。画面色彩绚丽，层次丰富，展现了西方极乐世界的庄严景象。',
    features: ['经变画', '净土变', '初唐艺术']
  },
  {
    title: '第428窟',
    period: '北周',
    description: '第428窟是北周时期的代表洞窟，是莫高窟最大的中心塔柱式洞窟。洞窟内保存有大量的千佛图和本生故事画，体现了北周艺术的特色。',
    features: ['中心塔柱', '千佛图', '本生故事']
  },
  {
    title: '第96窟',
    period: '初唐',
    description: '第96窟是莫高窟的标志性洞窟，内有高达35.5米的弥勒大佛，是莫高窟最大的佛像。洞窟外建有九层楼，是莫高窟的标志性建筑。',
    features: ['大佛', '九层楼', '标志性建筑']
  }
])

// 壁画艺术横向滚动卡片数据
const muralArtItems = ref([
  {
    title: '经变画',
    description: '经变画是莫高窟壁画的重要组成部分，通过图像的方式展现佛教经典内容，画面内容丰富，色彩绚丽，展现了古代绘画艺术的精湛技艺。',
    image: assetUrl('/images/mogao/mg12.jpg'),
    price: '200元'
  },
  {
    title: '本生故事画',
    description: '本生故事画描绘了释迦牟尼前世的故事，画面叙事性强，人物形象生动，体现了古代画师对故事情节的理解和表现能力。',
    image: assetUrl('/images/mogao/mg13.jpg'),
    price: '300元'
  },
  {
    title: '尊像画',
    description: '尊像画主要描绘佛、菩萨、弟子等形象，造型庄严，神态安详，展现了佛教艺术的崇高境界和审美追求。',
    image: assetUrl('/images/mogao/mg14.jpg'),
    price: '250元'
  },
  {
    title: '供养人像',
    description: '供养人像是出资开凿洞窟的功德主形象，真实反映了不同历史时期的人物服饰、社会风貌，具有重要的历史研究价值。',
    image: assetUrl('/images/mogao/mg15.jpg'),
    price: '180元'
  }
])

const currentMuralIndex = ref(0)

const prevMuralCard = () => {
  if (currentMuralIndex.value > 0) {
    currentMuralIndex.value--
  }
}

const nextMuralCard = () => {
  // 根据屏幕宽度计算可见卡片数量
  const cardWidth = 320
  const gap = 30
  const visibleCards = window.innerWidth <= 768 ? 1 : 3
  const maxIndex = Math.max(0, muralArtItems.value.length - visibleCards)
  if (currentMuralIndex.value < maxIndex) {
    currentMuralIndex.value++
  }
}

// 艺术价值的至高性卡片数据
const artValueItems = ref([
  {
    title: '历史价值',
    description: '莫高窟见证了丝绸之路的繁荣，记录了东西方文化交流的历史，是研究中国古代历史、宗教、艺术、民俗等的重要资料库。',
    image: assetUrl('/images/mogao/mg09.jpg')
  },
  {
    title: '艺术价值',
    description: '莫高窟的壁画和彩塑代表了中国古代绘画和雕塑艺术的最高成就，其独特的风格和精湛的技艺对后世艺术产生了深远影响。',
    image: assetUrl('/images/mogao/mg10.jpg')
  },
  {
    title: '文化价值',
    description: '莫高窟融合了多种文化元素，展现了中华文明的包容性和创造性，是中华优秀传统文化的重要载体和世界文化遗产的瑰宝。',
    image: assetUrl('/images/mogao/mg11.jpg')
  }
])

const heritageListItems = ref([
  {
    title: '阳关遗址',
    ticket: '50',
    hours: '8:00-21:00',
    suggested: '1-2h',
    quote: '丝绸之路上的重镇，“劝君更尽一杯酒，西出阳关无故人”',
    image: assetUrl('/images/mogao/mg16.jpg')
  },
  {
    title: '玉门关遗址',
    ticket: '40',
    hours: '7:00-20:00',
    suggested: '1-2h',
    quote: '曾随丝绸之路三通三绝而屡次兴废，“春风不度玉门关”',
    image: assetUrl('/images/mogao/mg17.jpg')
  },
  {
    title: '敦煌博物馆',
    ticket: '免费（需预约）',
    hours: '9:00-18:00',
    suggested: '1.5-2h',
    quote: '聚焦丝路与敦煌文化的展陈，系统了解莫高艺术的时代脉络',
    image: assetUrl('/images/mogao/mg18.jpg')
  }
])

const heritageListItemsRight = ref([
  {
    title: '敦煌丝路遗产城',
    ticket: '60',
    hours: '7:00-23:00',
    suggested: '1-2h',
    quote: '拍照爱好者可去，人造景，有大明宫、太和殿、帕特农神庙等',
    image: assetUrl('/images/mogao/mg19.jpg')
  },
  {
    title: '敦煌古城',
    ticket: '40',
    hours: '8:30-17:00',
    suggested: '1-2h',
    quote: '仿宋朝沙洲古城的影视城，《封神演义》《新龙门客栈》取景地',
    image: assetUrl('/images/mogao/mg20.jpg')
  },
  {
    title: '月牙泉小镇',
    ticket: '免费',
    hours: '全天',
    suggested: '1-2h',
    quote: '古汉式建筑，有客栈和各类餐饮，充满地域特色',
    image: assetUrl('/images/mogao/mg21.jpg')
  }
])

</script>

<style scoped>
.mogao-page {
  min-height: 100vh;
  background: var(--dunhuang-cream-white);
  padding-top: 55px;
}

.page-header {
  text-align: center;
  padding: 80px 40px 60px;
  background: linear-gradient(180deg, rgba(212, 175, 55, 0.15) 0%, rgba(139, 111, 71, 0.08) 50%, transparent 100%);
  background-image: url('/images/mogao/mg06.jpg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  position: relative;
}

.page-header::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.4);
  pointer-events: none;
  z-index: 0;
}

.page-header::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(180deg, rgba(212, 175, 55, 0.15) 0%, rgba(139, 111, 71, 0.08) 50%, transparent 100%);
  background-image: url('data:image/svg+xml,<svg width="100" height="100" xmlns="http://www.w3.org/2000/svg"><rect width="100" height="100" fill="none"/><path d="M20,20 L80,20 L80,80 L20,80 Z" stroke="rgba(139,111,71,0.1)" stroke-width="1" fill="none"/></svg>');
  opacity: 0.3;
  pointer-events: none;
  z-index: 0;
}

.page-title {
  font-family: var(--font-title);
  font-size: 56px;
  color: var(--dunhuang-wall-brown);
  margin-bottom: 20px;
  letter-spacing: 4px;
  position: relative;
  z-index: 1;
}

.page-subtitle {
  font-size: 18px;
  color: var(--dunhuang-medium-gray);
  max-width: 600px;
  margin: 0 auto;
  position: relative;
  z-index: 1;
}

.container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 40px;
}

.stats-section {
  margin-bottom: 80px;
}

.stat-card {
  text-align: center;
  padding: 40px 20px;
  transition: var(--transition-base);
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.9), rgba(245, 241, 232, 0.9));
}

.stat-card:hover {
  transform: translateY(-8px);
  background: linear-gradient(135deg, rgba(212, 175, 55, 0.1), rgba(139, 111, 71, 0.1));
}

.stat-icon {
  font-size: 48px;
  margin-bottom: 20px;
}

.stat-value {
  font-family: var(--font-title);
  font-size: 42px;
  font-weight: 700;
  color: var(--dunhuang-wall-brown);
  margin-bottom: 10px;
}

.stat-label {
  font-size: 16px;
  color: var(--dunhuang-medium-gray);
}

/* 开篇定调部分 */
.intro-section {
  margin: 80px 0;
}

.intro-content-wrapper {
  display: flex;
  gap: 60px;
  align-items: center;
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 40px;
}

.intro-image-container {
  flex: 1;
  min-width: 500px;
  height: 400px;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.1);
  position: relative;
  background: #000;
  cursor: pointer;
}

.intro-video {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.video-controls {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background: linear-gradient(to top, rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0));
  padding: 20px;
  opacity: 0;
  transition: opacity 0.3s ease;
  pointer-events: none;
}

.video-controls.show {
  opacity: 1;
  pointer-events: auto;
}

.video-progress-container {
  width: 100%;
  margin-bottom: 15px;
  cursor: pointer;
}

.video-progress-bar {
  width: 100%;
  height: 4px;
  background: rgba(255, 255, 255, 0.3);
  border-radius: 2px;
  position: relative;
  cursor: pointer;
}

.video-progress-filled {
  height: 100%;
  background: var(--dunhuang-sand-gold);
  border-radius: 2px;
  transition: width 0.1s linear;
}

.video-progress-thumb {
  position: absolute;
  top: 50%;
  transform: translate(-50%, -50%);
  width: 12px;
  height: 12px;
  background: var(--dunhuang-sand-gold);
  border-radius: 50%;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
  opacity: 0;
  transition: opacity 0.2s ease;
}

.video-progress-container:hover .video-progress-thumb {
  opacity: 1;
}

.video-controls-buttons {
  display: flex;
  align-items: center;
  gap: 15px;
}

.video-control-btn {
  width: 40px;
  height: 40px;
  border: none;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 50%;
  color: white;
  font-size: 18px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
  backdrop-filter: blur(10px);
}

.video-control-btn:hover {
  background: rgba(255, 255, 255, 0.3);
  transform: scale(1.1);
}

.fullscreen-icon {
  display: inline-block;
  font-size: 18px;
  line-height: 1;
  font-weight: bold;
}

.video-time {
  color: white;
  font-size: 14px;
  margin-left: auto;
  font-family: monospace;
}

.intro-text-container {
  flex: 1;
  padding: 20px;
}

.intro-title {
  font-family: var(--font-title);
  font-size: 42px;
  color: var(--dunhuang-wall-brown);
  margin-bottom: 30px;
  line-height: 1.3;
}

.intro-description {
  font-size: 16px;
  line-height: 1.8;
  color: var(--dunhuang-dark-gray);
  margin-bottom: 20px;
}

/* 壁画艺术横向滚动部分 */
.mural-art-section {
  margin: 80px 0;
}

.mural-carousel-container {
  position: relative;
  max-width: 1400px;
  margin: 40px auto 0;
  padding: 0 40px;
}

.mural-carousel-wrapper {
  overflow: hidden;
  margin: 0 60px;
}

.mural-carousel-track {
  display: flex;
  gap: 30px;
  will-change: transform;
  padding: 10px 0;
}

.mural-card {
  flex: 0 0 320px;
  background: rgba(255, 255, 255, 0.9);
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.mural-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.15);
}

.mural-card-image-container {
  width: 100%;
  height: 240px;
  background: linear-gradient(135deg, rgba(139, 111, 71, 0.1), rgba(212, 175, 55, 0.1));
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.mural-card-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.mural-card-image-placeholder {
  color: var(--dunhuang-medium-gray);
  font-size: 14px;
  text-align: center;
}

.mural-card-content {
  padding: 24px;
}

.mural-card-title {
  font-family: var(--font-title);
  font-size: 24px;
  color: var(--dunhuang-wall-brown);
  margin-bottom: 12px;
}

.mural-card-description {
  font-size: 14px;
  line-height: 1.6;
  color: var(--dunhuang-dark-gray);
  margin-bottom: 16px;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.mural-card-price {
  font-size: 16px;
  color: var(--dunhuang-sand-gold);
  font-weight: 600;
}

.mural-carousel-btn {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: 50px;
  height: 50px;
  background: rgba(255, 255, 255, 0.9);
  border: none;
  border-radius: 50%;
  cursor: pointer;
  z-index: 10;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 32px;
  color: var(--dunhuang-wall-brown);
  transition: all 0.3s ease;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
}

.mural-carousel-btn:hover {
  background: rgba(255, 255, 255, 1);
  transform: translateY(-50%) scale(1.1);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
}

.mural-carousel-btn-left {
  left: 0;
}

.mural-carousel-btn-right {
  right: 0;
}

.mural-carousel-btn span {
  line-height: 1;
  font-weight: bold;
}

/* 艺术价值的至高性部分 */
.art-value-section {
  margin: 80px 0;
}

.art-value-cards {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 40px;
  max-width: 1400px;
  margin: 40px auto 0;
  padding: 0 40px;
}

.art-value-card {
  background: rgba(255, 255, 255, 0.9);
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.art-value-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.15);
}

.art-value-image-container {
  width: 100%;
  height: 300px;
  background: linear-gradient(135deg, rgba(139, 111, 71, 0.1), rgba(212, 175, 55, 0.1));
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.art-value-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.art-value-image-placeholder {
  color: var(--dunhuang-medium-gray);
  font-size: 16px;
  text-align: center;
}

.art-value-content {
  padding: 32px;
}

.art-value-title {
  font-family: var(--font-title);
  font-size: 28px;
  color: var(--dunhuang-wall-brown);
  margin-bottom: 20px;
}

.art-value-description {
  font-size: 16px;
  line-height: 1.8;
  color: var(--dunhuang-dark-gray);
}

.cave-experience-section {
  margin-bottom: 80px;
}

.section-title {
  font-family: var(--font-title);
  font-size: 36px;
  color: var(--dunhuang-wall-brown);
  text-align: center;
  margin-bottom: 10px;
}

.section-subtitle {
  text-align: center;
  color: var(--dunhuang-medium-gray);
  margin-bottom: 40px;
  font-size: 16px;
}

.panorama-container {
  position: relative;
  width: 100%;
  height: 600px;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 8px 40px rgba(0, 0, 0, 0.15);
  border: 5px solid #C0C0C0;
}

.panorama-carousel {
  position: relative;
  width: 100%;
  height: 100%;
}

.panorama-slide-wrapper {
  position: relative;
  width: 100%;
  height: 100%;
  overflow: hidden;
}

.panorama-slides-container {
  display: flex;
  width: 100%;
  height: 100%;
  will-change: transform;
}

.panorama-slide {
  flex: 0 0 100%;
  width: 100%;
  height: 100%;
  position: relative;
}

.panorama-placeholder {
  position: relative;
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, var(--dunhuang-wall-brown), var(--dunhuang-dark-gray));
  display: flex;
  align-items: center;
  justify-content: center;
}

.panorama-image-container {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 1;
}

.panorama-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.panorama-image-placeholder {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(0, 0, 0, 0.3);
  color: rgba(255, 255, 255, 0.6);
  font-size: 18px;
}

.panorama-bg {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image: 
    radial-gradient(circle at 20% 30%, rgba(212, 175, 55, 0.2) 0%, transparent 50%),
    radial-gradient(circle at 80% 70%, rgba(74, 144, 164, 0.2) 0%, transparent 50%);
  opacity: 0.5;
}

.panorama-content {
  position: relative;
  z-index: 10;
  text-align: center;
  color: white;
}

.panorama-icon {
  font-size: 80px;
  margin-bottom: 20px;
  opacity: 0.9;
}

.panorama-text {
  font-family: var(--font-title);
  font-size: 60px;
  font-weight: bold;
  margin-bottom: 10px;
}

.panorama-desc {
  font-size: 36px;
  font-weight: bold;
  opacity: 0.8;
  margin-bottom: 30px;
}

.panorama-controls {
  margin-top: 20px;
}

.panorama-controls .el-button {
  font-size: 20px;
  padding: 16px 32px;
  height: auto;
}

/* 轮播图切换按钮 */
.carousel-btn {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: 50px;
  height: 50px;
  background: rgba(255, 255, 255, 0.9);
  border: none;
  border-radius: 50%;
  cursor: pointer;
  z-index: 10;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 32px;
  color: var(--dunhuang-wall-brown);
  transition: all 0.3s ease;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
}

.carousel-btn:hover {
  background: rgba(255, 255, 255, 1);
  transform: translateY(-50%) scale(1.1);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
}

.carousel-btn:active {
  transform: translateY(-50%) scale(0.95);
}

.carousel-btn-left {
  left: 20px;
}

.carousel-btn-right {
  right: 20px;
}

.carousel-btn span {
  line-height: 1;
  font-weight: bold;
}

/* 轮播图指示器 */
.carousel-indicators {
  position: absolute;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 10px;
  z-index: 10;
}

.indicator {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.5);
  cursor: pointer;
  transition: all 0.3s ease;
}

.indicator:hover {
  background: rgba(255, 255, 255, 0.8);
  transform: scale(1.2);
}

.indicator.active {
  background: rgba(255, 255, 255, 1);
  width: 24px;
  border-radius: 6px;
}

.cave-info-section {
  margin-top: 80px;
}

.mogao-bottom-split {
  max-width: 1400px;
  margin: 80px auto 0;
  padding: 0 40px;
  display: flex;
  gap: 40px;
  align-items: flex-start;
}

.mogao-bottom-left {
  flex: 0 0 50%;
  min-width: 0;
}

.mogao-bottom-right {
  flex: 0 0 50%;
  min-width: 0;
}

.heritage-list {
  background: transparent;
}

.heritage-item {
  padding: 24px 0;
  border-bottom: 2px dashed rgba(165, 90, 90, 0.85);
}

.heritage-item.heritage-item-last {
  border-bottom: none;
}

.heritage-item-inner {
  display: grid;
  grid-template-columns: 52% 48%;
  gap: 24px;
  align-items: start;
}

.heritage-image {
  width: 100%;
}

.heritage-image-placeholder {
  width: 100%;
  aspect-ratio: 4 / 3;
  background: linear-gradient(135deg, rgba(139, 111, 71, 0.14), rgba(212, 175, 55, 0.12));
  border: 2px solid rgba(139, 111, 71, 0.35);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--dunhuang-medium-gray);
  font-size: 16px;
  overflow: hidden;
}

.heritage-image-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.heritage-info {
  padding-top: 4px;
}

.heritage-title {
  display: inline-block;
  padding: 10px 18px;
  background: rgba(212, 175, 55, 0.35);
  color: rgba(139, 111, 71, 1);
  font-family: var(--font-title);
  font-size: 30px;
  letter-spacing: 2px;
  margin-bottom: 14px;
}

.heritage-lines {
  color: var(--dunhuang-dark-gray);
  font-size: 18px;
  line-height: 1.8;
  font-family: 'SimSun', '宋体', serif;
}

.heritage-line {
  margin-bottom: 6px;
}

.heritage-label {
  font-weight: 700;
  color: rgba(0, 0, 0, 0.75);
  margin-right: 6px;
}

.heritage-quote {
  margin-top: 10px;
  padding-top: 10px;
  border-top: 1px solid rgba(165, 90, 90, 0.45);
  color: rgba(0, 0, 0, 0.75);
}

@media (max-width: 1200px) {
  .mogao-bottom-split {
    flex-direction: column;
    gap: 30px;
    padding: 0 20px;
  }

  .mogao-bottom-left {
    flex: 1;
    width: 100%;
  }

  .mogao-bottom-right {
    flex: 1;
    width: 100%;
  }
}

.info-card {
  margin-bottom: 30px;
  transition: var(--transition-base);
}

.info-card:hover {
  border-color: var(--dunhuang-sand-gold);
}

.info-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 15px;
}

.info-title {
  font-family: var(--font-title);
  font-size: 24px;
  color: var(--dunhuang-wall-brown);
}

.info-period {
  font-size: 14px;
  color: var(--dunhuang-medium-gray);
  background: rgba(139, 111, 71, 0.1);
  padding: 4px 12px;
  border-radius: 12px;
}

.info-description {
  font-size: 16px;
  line-height: 1.8;
  color: var(--dunhuang-dark-gray);
  margin-bottom: 15px;
}

.info-features {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}

.cave-detail {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.cave-detail-image {
  width: 100%;
  height: 300px;
  border-radius: 12px;
}

.cave-detail-text h4 {
  font-family: var(--font-title);
  font-size: 20px;
  color: var(--dunhuang-wall-brown);
  margin-bottom: 10px;
  margin-top: 20px;
}

.cave-detail-text h4:first-child {
  margin-top: 0;
}

.cave-detail-text p {
  font-size: 16px;
  line-height: 1.8;
  color: var(--dunhuang-dark-gray);
}

.cave-detail-text ul {
  padding-left: 20px;
  color: var(--dunhuang-dark-gray);
}

.cave-detail-text li {
  margin-bottom: 8px;
  line-height: 1.8;
}

@media (max-width: 768px) {
  .panorama-container {
    height: 400px;
  }
  
  .stat-value {
    font-size: 32px;
  }
  
  .intro-content-wrapper {
    flex-direction: column;
    padding: 0 20px;
  }
  
  .intro-image-container {
    min-width: 100%;
    height: 300px;
  }
  
  .intro-title {
    font-size: 32px;
  }
  
  .mural-carousel-container {
    padding: 0 20px;
  }
  
  .mural-carousel-wrapper {
    margin: 0 50px;
  }
  
  .mural-card {
    flex: 0 0 280px;
  }
  
  .art-value-cards {
    grid-template-columns: 1fr;
    gap: 30px;
    padding: 0 20px;
  }
}
</style>

