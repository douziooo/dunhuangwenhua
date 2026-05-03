<template>
  <div class="home-page">
    <NavBar />
    <div class="top-image-section">
      <video class="top-image" autoplay muted loop playsinline preload="auto">
        <source :src="baseURL + 'video/sy1.mp4'" type="video/mp4" />
      </video>
      <div class="image-title">
        <h1 class="dunhuang-title">敦煌文化</h1>
      </div>
    </div>
    
    <!-- 关于敦煌区域 -->
    <div class="about-dunhuang-section">
      <div class="about-header">
        <div class="header-line"></div>
        <h2 class="about-title">关于敦煌</h2>
        <div class="header-line"></div>
        <div class="header-decoration-left">敦煌</div>
        <div class="header-decoration-right">敦煌</div>
      </div>
      
      <div class="about-content">
        <div class="about-text-box">
          <h3 class="about-subtitle">敦煌简介</h3>
          <div class="about-text">
            <p>敦煌是一座融合了历史、艺术、宗教、文化等多种元素的千年古城，位于古代丝绸之路的重要节点。自汉代设郡以来，敦煌见证了东西方文明的交流与融合。</p>
            <p>敦煌莫高窟被誉为"东方艺术宝库"，保存了从4世纪到14世纪长达千年的佛教艺术珍品。这里不仅有精美的壁画、彩塑，还保存了大量珍贵的文献资料。</p>
            <p>敦煌艺术以其独特的风格和深厚的文化内涵，展现了中华文明的博大精深，是研究中国古代艺术、宗教、历史的重要窗口，也是世界文化遗产的璀璨明珠。</p>
          </div>
        </div>
        
        <div class="about-image-box">
          <div class="cube-scene" aria-label="敦煌图片立方体">
            <div class="cube" aria-hidden="true">
              <div class="cube-face cube-front"><img :src="baseURL + 'images/home/s1.jpg'" alt="敦煌" /></div>
              <div class="cube-face cube-back"><img :src="baseURL + 'images/home/s2.jpg'" alt="敦煌" /></div>
              <div class="cube-face cube-right"><img :src="baseURL + 'images/home/s3.jpg'" alt="敦煌" /></div>
              <div class="cube-face cube-left"><img :src="baseURL + 'images/home/s4.jpg'" alt="敦煌" /></div>
              <div class="cube-face cube-top"><img :src="baseURL + 'images/home/s5.jpg'" alt="敦煌" /></div>
              <div class="cube-face cube-bottom"><img :src="baseURL + 'images/home/s6.jpg'" alt="敦煌" /></div>
            </div>
          </div>
        </div>
      </div>
      
      <div class="about-buttons">
        <button class="about-btn">探索敦煌</button>
        <button class="about-btn" type="button" @click="openDunhuangMore">了解更多</button>
        <button class="about-btn">文化传承</button>
      </div>
    </div>
    
    <!-- 探索敦煌区域 -->
    <div class="explore-dunhuang-section">
      <div class="explore-header">
        <div class="explore-decorative-left"></div>
        <h2 class="explore-title">探索敦煌</h2>
        <div class="explore-decorative-right"></div>
      </div>
      <p class="explore-subtitle">探索敦煌的独特魅力，感受千年文明的完美传承。</p>
      
      <div class="explore-gallery">
        <button class="gallery-nav-btn gallery-nav-left" @click="scrollGallery('left')">
          <span>&lt;</span>
        </button>
        
        <div class="gallery-container" ref="galleryContainer">
          <div 
            v-for="(position, positionIndex) in 5" 
            :key="positionIndex"
            class="gallery-card"
            :class="{
              'card-center': positionIndex === 2,
              'card-adjacent': positionIndex === 1 || positionIndex === 3,
              'card-outer': positionIndex === 0 || positionIndex === 4
            }"
            @click="handleCardClick(getItemAtPosition(positionIndex).route)"
          >
            <div class="card-image-wrapper">
              <img 
                :key="`${positionIndex}-${currentCenterIndex}`"
                :src="getItemAtPosition(positionIndex).image" 
                :alt="getItemAtPosition(positionIndex).title" 
                class="card-image"
                :class="{
                  'image-center': positionIndex === 2,
                  'image-adjacent': positionIndex === 1 || positionIndex === 3,
                  'image-outer': positionIndex === 0 || positionIndex === 4
                }"
              />
              <div class="card-glow"></div>
            </div>
            <div class="card-content">
              <h3 
                :key="`title-${positionIndex}-${currentCenterIndex}`"
                class="card-title"
              >{{ getItemAtPosition(positionIndex).title }}</h3>
              <button class="card-enter-btn">点击进入</button>
            </div>
          </div>
        </div>
        
        <button class="gallery-nav-btn gallery-nav-right" @click="scrollGallery('right')">
          <span>&gt;</span>
        </button>
      </div>
    </div>

    <div class="dunhuang-guardians-section">
      <div class="guardians-header">
        <div class="guardians-line"></div>
        <h2 class="guardians-title">传承有人</h2>
        <div class="guardians-line"></div>
      </div>
      <p class="guardians-subtitle">他们用一生守护莫高窟与敦煌文献，让千年文明在今天依然可见、可读、可感。</p>

      <div class="guardians-grid">
        <div class="guardian-card" v-for="person in guardians" :key="person.name">
          <div class="guardian-avatar">
            <img :src="person.image" :alt="person.name" />
          </div>
          <div class="guardian-body">
            <div class="guardian-name">{{ person.name }}</div>
            <div class="guardian-role">{{ person.role }}</div>
            <div class="guardian-desc">{{ person.desc }}</div>
            <div class="guardian-actions">
              <button class="guardian-more-btn" type="button" @click="openGuardianMore(person)">了解更多</button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="dunhuang-history-section">
      <div class="history-header">
        <div class="history-line"></div>
        <h2 class="history-title">敦煌历史</h2>
        <div class="history-line"></div>
      </div>

      <div class="history-list">
        <div
          class="history-item"
          v-for="(item, idx) in historyStages"
          :key="item.era"
          :class="{ 'is-right': idx % 2 === 1 }"
        >
          <div class="history-range" :class="item.rangeSide === 'right' ? 'range-right' : 'range-left'">{{ item.range }}</div>
          <div class="history-card">
            <div class="history-avatar">
              <img :src="item.image" :alt="item.era" />
            </div>
            <div class="history-body">
              <div class="history-era">{{ item.era }}</div>
              <div class="history-desc">{{ item.desc }}</div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="dunhuang-location-section">
      <div class="location-header">
        <div class="location-line"></div>
        <h2 class="location-title">地理位置</h2>
        <div class="location-line"></div>
      </div>

      <div class="location-content">
        <div class="location-left">
          <div class="location-map">
            <div class="china-map-wrapper" :style="dunhuangCssVars">
              <svg
                v-if="chinaMapReady"
                class="china-map-svg"
                viewBox="0 0 1000 780"
                preserveAspectRatio="xMidYMid meet"
                role="img"
                aria-label="中国省界地图"
              >
                <g class="china-provinces" aria-hidden="true">
                  <path
                    v-for="p in chinaProvincePaths"
                    :key="p.adcode"
                    class="china-province-path"
                    :d="p.d"
                  />
                </g>
                <g class="china-labels" aria-hidden="true">
                  <text
                    v-for="l in chinaProvinceLabels"
                    :key="l.adcode"
                    class="china-label"
                    :x="l.x"
                    :y="l.y"
                  >{{ l.text }}</text>
                </g>
              </svg>

              <img
                v-else
                class="china-map-img"
                :src="baseURL + 'images/maps/cn-admin1.svg'"
                alt="中国地图"
                loading="lazy"
                referrerpolicy="no-referrer"
              />

              <div class="china-map-hint" aria-live="polite">
                <template v-if="chinaMapReady">省界已加载（{{ chinaGeoSource }}）</template>
                <template v-else-if="chinaGeoLoading">省界加载中…</template>
                <template v-else-if="chinaGeoError">省界加载失败，已回退占位图</template>
                <template v-else>省界未就绪，已回退占位图</template>
              </div>

              <div v-if="chinaMapReady" class="dunhuang-marker" aria-label="敦煌位置标记">
                <span class="marker-pulse" aria-hidden="true"></span>
                <span class="marker-dot" aria-hidden="true"></span>
                <span class="marker-label">敦煌</span>
              </div>
            </div>
          </div>

          <div class="location-climate-card">
            <div class="location-climate-title">敦煌地理气候</div>
            <div class="location-climate-text">敦煌属典型温带大陆性干旱气候，日照充足、昼夜温差大。年降水量少而蒸发量大，空气干燥、云量偏少。春季多大风与风沙天气，沙尘活动频繁；夏季炎热干燥，午后易出现短时阵风；秋季晴朗少雨、气温回落快，是一年中较为舒适的时段；冬季寒冷干燥，受冷空气影响降温明显。敦煌位于绿洲与荒漠交错地带，水资源主要依赖疏勒河水系与地下水补给，形成独特的绿洲景观，也使得防风固沙与节水利用尤为重要。</div>
          </div>
        </div>

        <div class="location-side">
          <div class="location-notes">
            <div class="location-note-title">敦煌坐标</div>
            <div class="location-note-text">敦煌位于甘肃省西端，地处河西走廊与塔克拉玛干沙漠边缘，是丝绸之路的关键节点。</div>
            <div class="location-legend">
              <div class="legend-item">
                <span class="legend-swatch is-dunhuang"></span>
                <span class="legend-text">敦煌位置</span>
              </div>
              <div class="legend-item">
                <span class="legend-swatch is-china"></span>
                <span class="legend-text">中国轮廓</span>
              </div>
            </div>
          </div>

          <div class="location-flip-card" :style="{ aspectRatio: locationSideAspectRatio }">
            <div class="location-flip-inner" :style="{ transform: `rotateY(${locationSideRotateY}deg)` }">
              <div class="location-flip-face is-front">
                <img
                  :src="baseURL + 'images/home/sy20.jpg'"
                  alt="敦煌"
                  loading="lazy"
                  @load="onLocationSideFrontLoad"
                />
              </div>
              <div class="location-flip-face is-back">
                <img :src="baseURL + 'images/home/sy21.jpg'" alt="敦煌" loading="lazy" />
              </div>
            </div>
            <button
              class="location-flip-btn is-left"
              type="button"
              aria-label="向左旋转"
              @click.stop="rotateLocationSideLeft"
            >
              <span aria-hidden="true">‹</span>
            </button>
            <button
              class="location-flip-btn is-right"
              type="button"
              aria-label="向右旋转"
              @click.stop="rotateLocationSideRight"
            >
              <span aria-hidden="true">›</span>
            </button>
          </div>
        </div>
      </div>
    </div>
    
    <!-- 主题区块区域 -->
    <div class="themes-section">
      <div 
        v-for="(theme, index) in themes" 
        :key="index"
        class="theme-block"
        :class="{ 'theme-block-reverse': index % 2 === 1 }"
      >
        <div class="theme-content">
          <div class="theme-number">{{ String(index + 1).padStart(2, '0') }}</div>
          <div class="theme-header">
            <span class="theme-label">{{ theme.label }}</span>
            <div class="theme-line"></div>
          </div>
          <h2 class="theme-title">{{ theme.title }}</h2>
          <div class="theme-description">
            <p v-for="(para, pIndex) in theme.description" :key="pIndex">{{ para }}</p>
          </div>
          <router-link :to="theme.route" class="theme-link">了解更多</router-link>
        </div>
        <div class="theme-illustration">
          <div class="illustration-glow"></div>
          <div class="illustration-content">
            <div 
              class="illustration-pattern"
            >
              <div class="illustration-photo" :style="{ backgroundImage: `url(${theme.image})` }"></div>
              <div class="illustration-dim" aria-hidden="true"></div>
              <div class="illustration-hover" aria-hidden="true">
                <div class="illustration-hover-sub">{{ theme.label }}</div>
                <div class="illustration-hover-title">{{ theme.title }}</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div id="home-contact" class="contact-section">
      <div class="contact-header">
        <h2 class="contact-main-title">联系我们</h2>
        <p class="contact-subtitle">如有任何问题或建议，请随时与我们联系</p>
      </div>

      <div class="contact-content">
        <div class="contact-left">
          <h3 class="contact-left-title">联系方式</h3>

          <div class="contact-list">
            <div class="contact-item">
              <div class="contact-icon-wrap" aria-hidden="true">
                <svg class="contact-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M12 21s7-4.4 7-11a7 7 0 1 0-14 0c0 6.6 7 11 7 11Z" stroke="currentColor" stroke-width="1.8" />
                  <path d="M12 12.2a2.2 2.2 0 1 0 0-4.4 2.2 2.2 0 0 0 0 4.4Z" fill="currentColor" />
                </svg>
              </div>
              <div class="contact-item-body">
                <div class="contact-item-title">地址</div>
                <div class="contact-item-text">甘肃省敦煌市鸣沙山月牙泉附近</div>
              </div>
            </div>

            <div class="contact-item">
              <div class="contact-icon-wrap" aria-hidden="true">
                <svg class="contact-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M7 6.5c3.2 6.6 6.9 10.3 13.5 13.5l2-2.5c.4-.5.3-1.2-.2-1.6l-3-2.3c-.4-.3-1-.3-1.4 0l-1.7 1.3c-1.4-.8-3.6-3-4.4-4.4l1.3-1.7c.3-.4.3-1 0-1.4L10.6 3c-.4-.5-1.1-.6-1.6-.2L6.5 4.5l.5 2Z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" />
                </svg>
              </div>
              <div class="contact-item-body">
                <div class="contact-item-title">电话</div>
                <div class="contact-item-text">0595-12345678</div>
              </div>
            </div>

            <div class="contact-item">
              <div class="contact-icon-wrap" aria-hidden="true">
                <svg class="contact-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M4 7.5A2.5 2.5 0 0 1 6.5 5h11A2.5 2.5 0 0 1 20 7.5v9A2.5 2.5 0 0 1 17.5 19h-11A2.5 2.5 0 0 1 4 16.5v-9Z" stroke="currentColor" stroke-width="1.8" />
                  <path d="m6 8 6 5 6-5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" />
                </svg>
              </div>
              <div class="contact-item-body">
                <div class="contact-item-title">邮箱</div>
                <div class="contact-item-text">contact@dunhuang.com</div>
              </div>
            </div>

            <div class="contact-item">
              <div class="contact-icon-wrap" aria-hidden="true">
                <svg class="contact-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M12 22a10 10 0 1 0 0-20 10 10 0 0 0 0 20Z" stroke="currentColor" stroke-width="1.8" />
                  <path d="M12 6v6l4 2" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" />
                </svg>
              </div>
              <div class="contact-item-body">
                <div class="contact-item-title">工作时间</div>
                <div class="contact-item-text">周一至周五：9:00 - 22:00</div>
                <div class="contact-item-text">周六：11:00 - 20:00</div>
              </div>
            </div>
          </div>
        </div>

        <div class="contact-right">
          <div class="contact-form">
            <div class="contact-field">
              <div class="contact-label">姓名</div>
              <input class="contact-input" type="text" v-model.trim="contactName" placeholder="请输入您的姓名" />
            </div>
            <div class="contact-field">
              <div class="contact-label">邮箱</div>
              <input class="contact-input" type="email" v-model.trim="contactEmail" placeholder="请输入您的邮箱" />
            </div>
            <div class="contact-field">
              <div class="contact-label">主题</div>
              <input class="contact-input" type="text" v-model.trim="contactSubject" placeholder="请输入主题" />
            </div>
            <div class="contact-field">
              <div class="contact-label">留言</div>
              <textarea class="contact-textarea" v-model.trim="contactMessage" rows="6" placeholder="请输入您的留言内容"></textarea>
            </div>
            <div class="contact-submit-row">
              <button class="contact-submit-btn" type="button" @click="submitContact">发送留言</button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <footer class="site-footer">
      <div class="site-footer-inner">
        <div class="site-footer-columns">
          <div class="footer-col">
            <div class="footer-brand">敦煌文化·数字展馆</div>
            <div class="footer-desc">以莫高窟、壁画、飞天与丝路文明为线索，呈现敦煌艺术的历史脉络与审美精神。欢迎在这里漫游千年风华。</div>
            <div class="footer-social">
              <a class="footer-social-btn" href="#" aria-label="站点" title="站点">
                <span class="footer-social-dot"></span>
              </a>
              <a class="footer-social-btn" href="#" aria-label="相册" title="相册">
                <span class="footer-social-dot"></span>
              </a>
              <a class="footer-social-btn" href="#" aria-label="音乐" title="音乐">
                <span class="footer-social-dot"></span>
              </a>
              <a class="footer-social-btn" href="#" aria-label="联系" title="联系">
                <span class="footer-social-dot"></span>
              </a>
            </div>
          </div>

          <div class="footer-col">
            <div class="footer-title">快速链接</div>
            <div class="footer-links">
              <router-link class="footer-link" to="/mogao">莫高窟</router-link>
              <router-link class="footer-link" to="/mural">敦煌壁画</router-link>
              <router-link class="footer-link" to="/feitian">飞天艺术</router-link>
              <router-link class="footer-link" to="/history">敦煌历史</router-link>
            </div>
          </div>

          <div class="footer-col">
            <div class="footer-title">联系方式</div>
            <div class="footer-contact">
              <div class="footer-contact-item">
                <span class="footer-contact-icon" aria-hidden="true">📍</span>
                <span class="footer-contact-text">甘肃省敦煌市</span>
              </div>
              <div class="footer-contact-item">
                <span class="footer-contact-icon" aria-hidden="true">📞</span>
                <span class="footer-contact-text">0595-12345678</span>
              </div>
              <div class="footer-contact-item">
                <span class="footer-contact-icon" aria-hidden="true">✉️</span>
                <span class="footer-contact-text">contact@dunhuang.com</span>
              </div>
            </div>

            <div class="footer-title footer-title-spaced">团队名字：</div>
            <div class="footer-team">葱明伶俐小组</div>
          </div>
        </div>

        <div class="footer-bottom">
          <div class="footer-divider" aria-hidden="true"></div>
          <div class="footer-copy">© {{ currentYear }} 敦煌文化·数字展馆</div>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import NavBar from '../components/NavBar.vue'

const router = useRouter()
const baseURL = import.meta.env.BASE_URL || '/'

const assetUrl = (path) => {
  if (path.startsWith('/')) {
    return baseURL + path.slice(1)
  }
  return path
}

const contactName = ref('')
const contactEmail = ref('')
const contactSubject = ref('')
const contactMessage = ref('')

const currentYear = new Date().getFullYear()

const submitContact = () => {
  contactName.value = ''
  contactEmail.value = ''
  contactSubject.value = ''
  contactMessage.value = ''
}

const openDunhuangMore = () => {
  window.open(
    'https://baike.baidu.com/item/%E6%95%A6%E7%85%8C%E5%B8%82/3725231',
    '_blank',
    'noopener,noreferrer'
  )
}

const openGuardianMore = (person) => {
  const name = (person && person.name) ? String(person.name).trim() : ''
  if (!name) return
  if (name === '常书鸿') {
    window.open(
      'https://baike.baidu.com/item/%E5%B8%B8%E4%B9%A6%E9%B8%BF/1829577',
      '_blank',
      'noopener,noreferrer'
    )
    return
  }
  if (name === '樊锦诗') {
    window.open(
      'https://baike.baidu.com/item/%E6%A8%8A%E9%94%A6%E8%AF%97/1260898',
      '_blank',
      'noopener,noreferrer'
    )
    return
  }
  if (name === '段文杰') {
    window.open(
      'https://baike.baidu.com/item/%E6%AE%B5%E6%96%87%E6%9D%B0/26456',
      '_blank',
      'noopener,noreferrer'
    )
    return
  }
  if (name === '赵声良') {
    window.open(
      'https://baike.baidu.com/item/%E8%B5%B5%E5%A3%B0%E8%89%AF?fromModule=lemma_search-box',
      '_blank',
      'noopener,noreferrer'
    )
    return
  }
  const url = `https://baike.baidu.com/search/word?word=${encodeURIComponent(name)}`
  window.open(url, '_blank', 'noopener,noreferrer')
}

const locationSideRotateY = ref(0)
const locationSideAspectRatio = ref('16 / 9')

const rotateLocationSideLeft = () => {
  locationSideRotateY.value -= 180
}

const rotateLocationSideRight = () => {
  locationSideRotateY.value += 180
}

const onLocationSideFrontLoad = (e) => {
  const img = e && e.target
  if (!img || !img.naturalWidth || !img.naturalHeight) return
  locationSideAspectRatio.value = `${img.naturalWidth} / ${img.naturalHeight}`
}

const exploreItems = ref([
  {
    title: '敦煌风光',
    image: assetUrl('/images/home/sy10.jpg'),
    route: '/mogao'
  },
  {
    title: '壁画纹样',
    image: assetUrl('/images/home/sy11.jpg'),
    route: '/mural'
  },
  {
    title: '石窟建筑',
    image: assetUrl('/images/home/sy12.jpg'),
    route: '/mogao'
  },
  {
    title: '飞天神韵',
    image: assetUrl('/images/home/sy13.jpg'),
    route: '/feitian'
  },
  {
    title: '丝路印记',
    image: assetUrl('/images/home/sy14.jpg'),
    route: '/history'
  }
])

const chinaGeoJson = ref(null)
const chinaGeoLoading = ref(true)
const chinaGeoError = ref(false)
const chinaGeoSource = ref('')

onMounted(async () => {
  try {
    const tryFetch = async (url) => {
      const r = await fetch(url)
      if (!r.ok) throw new Error(String(r.status))
      const data = await r.json()
      if (!data || !Array.isArray(data.features) || data.features.length === 0) {
        throw new Error('invalid-geojson')
      }
      return data
    }

    try {
      const base = (import.meta && import.meta.env && import.meta.env.BASE_URL) || '/'
      const localUrl = `${base}data/china-100000_full.json`
      chinaGeoJson.value = await tryFetch(localUrl)
      chinaGeoSource.value = '本地'
    } catch (e) {
      chinaGeoJson.value = await tryFetch('https://geo.datav.aliyun.com/areas_v3/bound/100000_full.json')
      chinaGeoSource.value = '线上'
    }
  } catch (e) {
    chinaGeoError.value = true
    chinaGeoSource.value = ''
  } finally {
    chinaGeoLoading.value = false
  }
})

const merc = (latDeg) => {
  const safe = Math.max(-85, Math.min(85, latDeg))
  const rad = (safe * Math.PI) / 180
  return Math.log(Math.tan(Math.PI / 4 + rad / 2))
}

const lonRad = (lonDeg) => {
  return (lonDeg * Math.PI) / 180
}

const chinaProjection = computed(() => {
  const gj = chinaGeoJson.value
  if (!gj || !gj.features || !gj.features.length) return null

  const ignoreFeature = (f) => {
    const name = f && f.properties && f.properties.name
    return name === '南海诸岛'
  }

  let minLon = Infinity
  let maxLon = -Infinity
  let minM = Infinity
  let maxM = -Infinity

  const visit = (coords) => {
    if (typeof coords[0] === 'number') {
      const lon = lonRad(coords[0])
      const lat = coords[1]
      const m = merc(lat)
      if (lon < minLon) minLon = lon
      if (lon > maxLon) maxLon = lon
      if (m < minM) minM = m
      if (m > maxM) maxM = m
      return
    }
    for (const c of coords) visit(c)
  }

  for (const f of gj.features) {
    if (ignoreFeature(f)) continue
    if (!f.geometry || !f.geometry.coordinates) continue
    visit(f.geometry.coordinates)
  }

  const viewW = 1000
  const viewH = 780
  const pad = 24
  const dLon = Math.max(1e-9, maxLon - minLon)
  const dM = Math.max(1e-9, maxM - minM)
  const scale = Math.min((viewW - pad * 2) / dLon, (viewH - pad * 2) / dM)
  const usedW = dLon * scale
  const usedH = dM * scale
  const left = (viewW - usedW) / 2
  const top = (viewH - usedH) / 2

  const project = (lon, lat) => {
    const x = (lonRad(lon) - minLon) * scale + left
    const y = (maxM - merc(lat)) * scale + top
    return { x, y }
  }

  return { project, viewW, viewH }
})

const geoToPath = (geometry) => {
  const proj = chinaProjection.value
  if (!proj || !geometry) return ''

  const ringToPath = (ring) => {
    const step = ring.length > 1600 ? Math.ceil(ring.length / 900) : 1
    let d = ''
    for (let i = 0; i < ring.length; i += step) {
      const pt = ring[i]
      const { x, y } = proj.project(pt[0], pt[1])
      d += `${i === 0 ? 'M' : 'L'}${x.toFixed(1)},${y.toFixed(1)}`
    }
    if (step > 1 && ring.length > 0) {
      const pt = ring[0]
      const { x, y } = proj.project(pt[0], pt[1])
      d += `L${x.toFixed(1)},${y.toFixed(1)}`
    }
    return `${d}Z`
  }

  if (geometry.type === 'Polygon') {
    return geometry.coordinates.map((ring) => ringToPath(ring)).join('')
  }
  if (geometry.type === 'MultiPolygon') {
    return geometry.coordinates
      .map((poly) => poly.map((ring) => ringToPath(ring)).join(''))
      .join('')
  }
  return ''
}

const chinaProvincePaths = computed(() => {
  const gj = chinaGeoJson.value
  const proj = chinaProjection.value
  if (!gj || !proj || !gj.features) return []

  return gj.features
    .filter((f) => f && f.properties && f.properties.adcode && f.geometry && f.properties.name !== '南海诸岛')
    .map((f) => ({
      adcode: String(f.properties.adcode),
      name: String(f.properties.name || ''),
      d: geoToPath(f.geometry)
    }))
    .filter((p) => p.d)
})

const shortProvinceName = (name) => {
  return String(name)
    .replace(/特别行政区/g, '')
    .replace(/维吾尔自治区/g, '')
    .replace(/壮族自治区/g, '')
    .replace(/回族自治区/g, '')
    .replace(/自治区/g, '')
    .replace(/省/g, '')
    .replace(/市/g, '')
}

const chinaProvinceLabels = computed(() => {
  const gj = chinaGeoJson.value
  const proj = chinaProjection.value
  if (!gj || !proj || !gj.features) return []

  return gj.features
    .filter((f) => f && f.properties && f.properties.adcode && f.properties.name !== '南海诸岛')
    .map((f) => {
      const pt = f.properties.centroid || f.properties.center
      if (!pt || pt.length < 2) return null
      const { x, y } = proj.project(pt[0], pt[1])
      return {
        adcode: String(f.properties.adcode),
        text: shortProvinceName(f.properties.name || ''),
        x: Number(x.toFixed(1)),
        y: Number(y.toFixed(1))
      }
    })
    .filter(Boolean)
})

const chinaMapReady = computed(() => {
  return !!chinaProjection.value && chinaProvincePaths.value.length > 0
})

const dunhuangCssVars = computed(() => {
  const proj = chinaProjection.value
  if (!proj) return {}
  const dunhuang = { lat: 40.142, lon: 94.662 }
  const { x, y } = proj.project(dunhuang.lon, dunhuang.lat)
  const xPct = (x / proj.viewW) * 100
  const yPct = (y / proj.viewH) * 100
  return {
    '--dunhuang-x': `${xPct.toFixed(2)}%`,
    '--dunhuang-y': `${yPct.toFixed(2)}%`
  }
})

const historyStages = ref([
  {
    era: '汉朝',
    range: '公元前111年—220年',
    rangeSide: 'right',
    desc: '在汉武帝时期，敦煌成为河西走廊的重要关隘与丝路枢纽。郡县设立与交通畅通，使商旅往来与文化交流在此汇聚。',
    image: assetUrl('/images/home/sy15.jpg')
  },
  {
    era: '魏晋',
    range: '220年—581年',
    rangeSide: 'left',
    desc: '魏晋南北朝时期，佛教东传加速，敦煌开始出现早期洞窟与壁画传统。多元信仰与艺术样式在这里逐步沉淀成形。',
    image: assetUrl('/images/home/sy16.jpg')
  },
  {
    era: '隋唐',
    range: '581年—907年',
    rangeSide: 'right',
    desc: '隋唐之际，丝路贸易繁盛，莫高窟迎来兴建高峰。壁画题材与绘制技法日趋成熟，形成兼容并蓄、气象宏阔的艺术面貌。',
    image: assetUrl('/images/home/sy17.jpg')
  },
  {
    era: '宋元',
    range: '960年—1368年',
    rangeSide: 'left',
    desc: '宋元时期，敦煌在边塞格局与民族往来中持续发展。洞窟营建延续不断，艺术风格呈现出更鲜明的地域与时代特征。',
    image: assetUrl('/images/home/sy18.jpg')
  },
  {
    era: '明清',
    range: '1368年—1912年',
    rangeSide: 'right',
    desc: '明清以后，敦煌逐渐淡出交通要冲，但洞窟与文献仍被守护留存。近现代的发现与研究，让敦煌重新进入世界文化视野。',
    image: assetUrl('/images/home/sy19.jpg')
  }
])

const currentCenterIndex = ref(2)
const galleryContainer = ref(null)

// 根据位置索引获取对应的item
const getItemAtPosition = (positionIndex) => {
  // positionIndex: 0, 1, 2, 3, 4 (固定5个位置)
  // currentCenterIndex: 当前中心显示的item索引
  // 计算每个位置应该显示哪个item
  const offset = positionIndex - 2 // -2, -1, 0, 1, 2
  const itemIndex = (currentCenterIndex.value + offset + exploreItems.value.length) % exploreItems.value.length
  return exploreItems.value[itemIndex]
}

const scrollGallery = (direction) => {
  if (direction === 'left') {
    currentCenterIndex.value = (currentCenterIndex.value - 1 + exploreItems.value.length) % exploreItems.value.length
  } else {
    currentCenterIndex.value = (currentCenterIndex.value + 1) % exploreItems.value.length
  }
}

const handleCardClick = (route) => {
  router.push(route)
}

const guardians = ref([
  {
    name: '常书鸿',
    role: '“敦煌守护神” · 莫高窟保护开拓者',
    desc: '1944年出任国立敦煌艺术研究所所长，组织洞窟调查与壁画临摹，奠定了近现代敦煌保护与研究的基础。',
    image: assetUrl('/images/home/syrw1.jpg')
  },
  {
    name: '樊锦诗',
    role: '敦煌研究院名誉院长 · 数字敦煌推动者',
    desc: '长期扎根大漠，推动文物保护与开放利用平衡发展，推进"数字敦煌"建设，让敦煌艺术以更安全的方式走向世界。',
    image: assetUrl('/images/home/syrw2.jpg')
  },
  {
    name: '段文杰',
    role: '敦煌研究院原院长 · 壁画学体系建设者',
    desc: '主持洞窟测绘、分期与内容研究，系统推进壁画图像学与艺术史研究，促进敦煌学学科建设与国际交流。',
    image: assetUrl('/images/home/syrw3.jpg')
  },
  {
    name: '赵声良',
    role: '敦煌研究院研究员 · 图像与传播研究者',
    desc: '围绕敦煌图像、题材与传播路径开展研究，推动公众传播与学术普及，让敦煌故事以更易懂的方式被看见。',
    image: assetUrl('/images/home/syrw4.jpg')
  }
])

const themes = ref([
  {
    label: '千年丝路明珠，飞天壁影间',
    title: '敦煌历史',
    description: [
      '敦煌历史悠久，是古代丝绸之路的重要节点。自汉代设郡以来，敦煌见证了东西方文明的交流与融合。',
      '这里保存了丰富的历史文化遗产，从汉代的边塞文化到唐代的繁荣盛世，每一段历史都留下了深刻的印记。'
    ],
    route: '/history',
    image: assetUrl('/images/home/sy06.jpg')
  },
  {
    label: '千窟十朝佛光，笔笔都往时间深处飞',
    title: '敦煌壁画',
    description: [
      '敦煌壁画是莫高窟艺术的精华，以其精湛的技艺和丰富的题材闻名于世。这些壁画描绘了佛教故事、历史事件和世俗生活。',
      '从北凉到元代，不同时期的壁画风格各异，展现了千年来艺术风格的演变，是研究中国古代绘画史的珍贵资料。'
    ],
    route: '/mural',
    image: assetUrl('/images/home/sy07.jpg')
  },
  {
    label: '日色与千年的佛光，色彩与信仰的梦',
    title: '莫高窟',
    description: [
      '莫高窟，俗称千佛洞，是世界上现存规模最大、内容最丰富的佛教艺术圣地。开凿于公元366年，历经十六国、北朝、隋、唐、五代、西夏、元等朝代的兴建。',
      '现存洞窟735个，壁画4.5万平方米，泥质彩塑2415尊，是世界上规模最大的佛教石窟群，被誉为"东方艺术宝库"。'
    ],
    route: '/mogao',
    image: assetUrl('/images/home/sy08.jpg')
  },
  {
    label: '敦煌飞天散花回望，千年壁画上飘行',
    title: '飞天艺术',
    description: [
      '飞天是敦煌艺术的标志性形象，以其优美的姿态和飘逸的动感而闻名。飞天形象源于印度佛教艺术，在敦煌得到了独特的中国化发展。',
      '从早期的粗犷风格到唐代的优雅飘逸，飞天形象经历了千年的演变，体现了不同时期艺术风格的特色，是敦煌艺术中最具代表性的形象之一。'
    ],
    route: '/feitian',
    image: assetUrl('/images/home/sy09.jpg')
  }
])

onMounted(() => {
  if (typeof window === 'undefined') return
  if (window.location.hash !== '#home-contact') return
  requestAnimationFrame(() => {
    const el = document.getElementById('home-contact')
    if (!el) return
    el.scrollIntoView({ behavior: 'smooth', block: 'start' })
  })
})
</script>

<style scoped>
.home-page {
  min-height: 100vh;
  overflow-x: hidden;
}

.top-image-section {
  width: 100%;
  height: calc(100vh - 55px);
  min-height: 600px;
  overflow: hidden;
  position: relative;
  margin-top: 55px;
}

.top-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
  display: block;
  animation: imageZoomIn 3s ease-in-out;
  transform-origin: center center;
}

@keyframes imageZoomIn {
  0% {
    transform: scale(1.2);
  }
  100% {
    transform: scale(1);
  }
}

.image-title {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 10;
  text-align: center;
  pointer-events: none;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.dunhuang-guardians-section {
  width: 100%;
  min-height: 100vh;
  background-color: #f3d9b4;
  background-image: url('/images/home/sy24.jpg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  padding: 80px 50px 100px;
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.dunhuang-guardians-section::before {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, rgba(243, 217, 180, 0.78), rgba(242, 209, 166, 0.58));
  pointer-events: none;
  z-index: 0;
}

.dunhuang-guardians-section > * {
  position: relative;
  z-index: 1;
}

.guardians-header {
  width: 100%;
  max-width: 1400px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 18px;
}

.guardians-line {
  width: 120px;
  height: 2px;
  background: linear-gradient(90deg, transparent, rgba(139, 111, 71, 0.9), transparent);
}

.guardians-title {
  font-family: var(--font-calligraphy);
  font-size: 54px;
  font-weight: normal;
  color: #5c3e2a;
  letter-spacing: 10px;
  margin: 0 34px;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.08);
}

.guardians-subtitle {
  max-width: 1100px;
  text-align: center;
  font-size: 18px;
  color: #6b4e3d;
  letter-spacing: 2px;
  margin-bottom: 48px;
}

.guardians-grid {
  width: 100%;
  max-width: 1400px;
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 28px;
}

.guardian-card {
  display: flex;
  gap: 18px;
  align-items: center;
  background: rgba(255, 248, 240, 0.85);
  border: 1px solid rgba(139, 111, 71, 0.28);
  border-radius: 16px;
  padding: 22px 20px;
  box-shadow: 0 10px 26px rgba(0, 0, 0, 0.16);
  transition: transform 0.32s ease, box-shadow 0.32s ease, border-color 0.32s ease, background 0.32s ease;
}

.guardian-avatar {
  width: 106px;
  height: 106px;
  border-radius: 50%;
  overflow: hidden;
  flex-shrink: 0;
  border: 4px solid rgba(139, 111, 71, 0.35);
  box-shadow: 0 8px 18px rgba(0, 0, 0, 0.18);
  background: rgba(255, 255, 255, 0.8);
}

.guardian-avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transform: scale(1);
  transition: transform 0.45s ease;
}

.guardian-body {
  flex: 1;
}

.guardian-actions {
  display: flex;
  justify-content: flex-end;
  margin-top: 12px;
}

.guardian-more-btn {
  padding: 8px 18px;
  border-radius: 999px;
  border: 1px solid rgba(139, 111, 71, 0.55);
  background: rgba(139, 111, 71, 0.14);
  color: #5c3e2a;
  font-size: 13px;
  letter-spacing: 1px;
  cursor: pointer;
  transition: transform 0.22s ease, box-shadow 0.22s ease, background 0.22s ease;
}

@media (hover: hover) and (pointer: fine) {
  .guardian-more-btn:hover {
    transform: translateY(-2px);
    background: rgba(139, 111, 71, 0.22);
    box-shadow: 0 10px 22px rgba(0, 0, 0, 0.12);
  }
}

.guardian-name {
  font-size: 20px;
  font-weight: 700;
  color: #5c3e2a;
  letter-spacing: 2px;
  margin-bottom: 6px;
  position: relative;
  padding-left: 14px;
}

.guardian-name::before {
  content: '';
  position: absolute;
  left: 0;
  top: 50%;
  transform: translateY(-50%);
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: rgba(139, 111, 71, 0.9);
}

.guardian-role {
  font-size: 14px;
  color: rgba(92, 62, 42, 0.85);
  letter-spacing: 1px;
  margin-bottom: 10px;
}

.guardian-desc {
  font-size: 15px;
  line-height: 1.9;
  color: rgba(92, 62, 42, 0.82);
  text-align: justify;
}

@media (hover: hover) and (pointer: fine) {
  .guardian-card:hover {
    transform: translate3d(0, -6px, 0);
    box-shadow: 0 16px 34px rgba(0, 0, 0, 0.18);
    border-color: rgba(212, 175, 55, 0.55);
    background: rgba(255, 252, 248, 0.92);
  }

  .guardian-card:hover .guardian-avatar img {
    transform: scale(1.06);
  }
}

@media (prefers-reduced-motion: reduce) {
  .guardian-card,
  .guardian-avatar img {
    transition: none;
  }

  .guardian-card:hover {
    transform: none;
  }
}

.dunhuang-history-section {
  width: 100%;
  min-height: auto;
  background-color: #e5bf8c;
  background-image: url('/images/home/sy25.jpg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  padding: 64px 50px 72px;
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.dunhuang-history-section::before {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, rgba(229, 191, 140, 0.78), rgba(225, 178, 122, 0.56));
  pointer-events: none;
  z-index: 0;
}

.dunhuang-history-section > * {
  position: relative;
  z-index: 1;
}

.history-header {
  width: 100%;
  max-width: 1400px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 14px;
}

.history-line {
  width: 140px;
  height: 2px;
  background: linear-gradient(90deg, transparent, rgba(92, 62, 42, 0.85), transparent);
  opacity: 0.9;
}

.history-title {
  font-family: var(--font-calligraphy);
  font-size: 54px;
  font-weight: normal;
  color: #5c3e2a;
  letter-spacing: 10px;
  margin: 0 34px;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.08);
}

.history-list {
  width: 100%;
  max-width: 1400px;
  display: flex;
  flex-direction: column;
  gap: 14px;
  margin-top: 8px;
  position: relative;
}

.history-list::before {
  content: '';
  position: absolute;
  top: 0;
  bottom: 0;
  left: 50%;
  width: 2px;
  transform: translateX(-50%);
  background: linear-gradient(
    180deg,
    transparent 0%,
    rgba(92, 62, 42, 0.16) 18%,
    rgba(92, 62, 42, 0.14) 50%,
    rgba(92, 62, 42, 0.16) 82%,
    transparent 100%
  );
  filter: blur(0.2px);
  pointer-events: none;
  opacity: 0.85;
}

.history-item {
  width: 100%;
  display: flex;
  justify-content: flex-start;
  padding-right: 34px;
  position: relative;
  box-sizing: border-box;
}

.history-item.is-right {
  justify-content: flex-end;
  padding-right: 0;
  padding-left: 34px;
}

.history-range {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  font-family: var(--font-calligraphy);
  font-size: 28px;
  font-weight: 800;
  color: rgba(92, 62, 42, 0.75);
  letter-spacing: 2px;
  text-shadow: 2px 2px 3px rgba(0, 0, 0, 0.08);
  pointer-events: none;
  user-select: none;
  z-index: 2;
}

.history-range::after {
  content: '';
  position: absolute;
  left: 2px;
  right: 2px;
  bottom: -6px;
  height: 2px;
  border-radius: 2px;
  background: rgba(92, 62, 42, 0.55);
  box-shadow: 0 1px 0 rgba(255, 244, 232, 0.35);
}

.history-range.range-right {
  left: 50%;
  right: auto;
  transform: translate(6px, -50%);
}

.history-range.range-left {
  left: 50%;
  right: auto;
  transform: translate(calc(-100% - 6px), -50%);
}

.history-card {
  width: min(640px, calc(50% - 34px));
  display: flex;
  align-items: flex-start;
  gap: 18px;
  padding: 16px 18px;
  background: rgba(255, 244, 232, 0.78);
  border: 1px solid rgba(92, 62, 42, 0.22);
  border-radius: 16px;
  box-shadow: 0 10px 24px rgba(0, 0, 0, 0.18);
  transition: transform 0.28s ease;
}

@media (hover: hover) and (pointer: fine) {
  .history-card:hover {
    transform: translate3d(0, 2px, 0);
  }
}

@media (prefers-reduced-motion: reduce) {
  .history-card {
    transition: none;
  }

  .history-card:hover {
    transform: none;
  }
}

.history-item.is-right .history-card {
  flex-direction: row-reverse;
  text-align: right;
}

.history-avatar {
  width: 78px;
  height: 78px;
  border-radius: 50%;
  overflow: hidden;
  flex-shrink: 0;
  border: 4px solid rgba(92, 62, 42, 0.28);
  box-shadow: 0 8px 18px rgba(0, 0, 0, 0.18);
  background: rgba(255, 255, 255, 0.7);
}

.history-avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.history-body {
  flex: 1;
}

.history-era {
  font-size: 17px;
  font-weight: 700;
  color: #5c3e2a;
  letter-spacing: 2px;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 8px;
}

.history-era::before {
  content: '•';
  font-size: 18px;
  line-height: 1;
  color: rgba(92, 62, 42, 0.9);
}

.history-item.is-right .history-era {
  justify-content: flex-end;
}

.history-item.is-right .history-era::before {
  content: '';
  display: none;
}

.history-item.is-right .history-era::after {
  content: '•';
  font-size: 18px;
  line-height: 1;
  color: rgba(92, 62, 42, 0.9);
  margin-left: 8px;
}

.dunhuang-history-section .history-desc {
  font-size: 15px;
  line-height: 1.9;
  color: rgba(92, 62, 42, 0.82);
  text-align: justify;
}

.history-item.is-right .history-desc {
  text-align: justify;
}

.dunhuang-location-section {
  width: 100%;
  background: linear-gradient(180deg, #f0d9b8 0%, #f2d1a6 55%, #f0d9b8 100%);
  padding: 64px 50px 72px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.location-header {
  width: 100%;
  max-width: 1400px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 14px;
}

.location-line {
  width: 140px;
  height: 2px;
  background: linear-gradient(90deg, transparent, rgba(92, 62, 42, 0.85), transparent);
  opacity: 0.9;
}

.location-title {
  font-family: var(--font-calligraphy);
  font-size: 54px;
  font-weight: normal;
  color: #5c3e2a;
  letter-spacing: 10px;
  margin: 0 34px;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.08);
}

.location-content {
  width: 100%;
  max-width: 1400px;
  display: flex;
  gap: 24px;
  align-items: stretch;
  margin-top: 8px;
}

.location-left {
  flex: 1.2 1 0;
  display: flex;
  flex-direction: column;
  gap: 14px;
  min-width: 0;
}

.location-map {
  width: 100%;
  border-radius: 18px;
  background: rgba(255, 244, 232, 0.72);
  border: 1px solid rgba(92, 62, 42, 0.22);
  box-shadow: 0 10px 24px rgba(0, 0, 0, 0.18);
  padding: 18px;
  flex: 0 0 auto;
}

.location-side {
  flex: 0.8 1 0;
  display: flex;
  flex-direction: column;
  gap: 14px;
  min-width: 0;
}

.location-climate-card {
  width: 100%;
  border-radius: 18px;
  background: rgba(255, 236, 210, 0.78);
  border: 1px solid rgba(92, 62, 42, 0.14);
  box-shadow: 0 10px 26px rgba(0, 0, 0, 0.12);
  padding: 26px 34px;
  flex: 1 1 auto;
}

.location-climate-title {
  font-size: 22px;
  font-weight: 800;
  color: #5c3e2a;
  letter-spacing: 2px;
  margin-bottom: 14px;
}

.location-climate-text {
  font-size: 16px;
  line-height: 2;
  color: rgba(92, 62, 42, 0.82);
  text-align: justify;
}

.china-map-wrapper {
  position: relative;
  width: 100%;
  border-radius: 14px;
  overflow: hidden;
  background: rgba(255, 252, 248, 0.75);
}

.china-map-img {
  width: 100%;
  height: auto;
  display: block;
  opacity: 0.96;
  filter: contrast(1.18) brightness(1.02);
}

.china-map-svg {
  width: 100%;
  height: auto;
  display: block;
}

.china-map-hint {
  position: absolute;
  right: 10px;
  bottom: 10px;
  z-index: 3;
  padding: 6px 10px;
  border-radius: 12px;
  font-size: 12px;
  font-weight: 700;
  color: rgba(92, 62, 42, 0.92);
  background: rgba(255, 244, 232, 0.9);
  border: 1px solid rgba(92, 62, 42, 0.22);
  box-shadow: 0 10px 22px rgba(0, 0, 0, 0.14);
  pointer-events: none;
}

.china-province-path {
  fill: rgba(255, 252, 248, 0.72);
  stroke: rgba(92, 62, 42, 0.42);
  stroke-width: 1.1;
  vector-effect: non-scaling-stroke;
}

.china-label {
  font-size: 18px;
  font-weight: 700;
  fill: rgba(92, 62, 42, 0.82);
  text-anchor: middle;
  dominant-baseline: central;
  paint-order: stroke;
  stroke: rgba(255, 244, 232, 0.85);
  stroke-width: 3px;
  vector-effect: non-scaling-stroke;
}

.dunhuang-marker {
  position: absolute;
  left: var(--dunhuang-x);
  top: var(--dunhuang-y);
  transform: translate(-50%, -50%);
  z-index: 2;
  pointer-events: none;
}

.marker-pulse {
  position: absolute;
  left: 50%;
  top: 50%;
  width: 44px;
  height: 44px;
  transform: translate(-50%, -50%);
  border-radius: 50%;
  background: rgba(205, 65, 47, 0.16);
  border: 2px solid rgba(205, 65, 47, 0.35);
  animation: dunhuangPulse 1.8s ease-in-out infinite;
}

.marker-dot {
  position: absolute;
  left: 50%;
  top: 50%;
  width: 12px;
  height: 12px;
  transform: translate(-50%, -50%);
  border-radius: 50%;
  background: rgba(205, 65, 47, 0.95);
  border: 2px solid rgba(92, 62, 42, 0.7);
  box-shadow: 0 8px 18px rgba(0, 0, 0, 0.18);
}

.marker-label {
  position: absolute;
  left: 16px;
  top: -16px;
  font-family: var(--font-calligraphy);
  font-size: 28px;
  font-weight: 800;
  color: rgba(92, 62, 42, 0.92);
  text-shadow: 0 0 0 rgba(255, 244, 232, 0.85), 2px 2px 3px rgba(0, 0, 0, 0.08);
  white-space: nowrap;
}

@keyframes dunhuangPulse {
  0% {
    transform: translate(-50%, -50%) scale(0.9);
    opacity: 0.65;
  }
  50% {
    transform: translate(-50%, -50%) scale(1.2);
    opacity: 0.35;
  }
  100% {
    transform: translate(-50%, -50%) scale(0.9);
    opacity: 0.65;
  }
}

.location-notes {
  width: 100%;
  border-radius: 18px;
  background: rgba(255, 244, 232, 0.7);
  border: 1px solid rgba(92, 62, 42, 0.18);
  box-shadow: 0 10px 24px rgba(0, 0, 0, 0.16);
  padding: 18px 18px;
  align-self: start;
}

.location-flip-card {
  width: 100%;
  border-radius: 18px;
  border: 1px solid rgba(92, 62, 42, 0.18);
  box-shadow: 0 10px 24px rgba(0, 0, 0, 0.16);
  overflow: hidden;
  position: relative;
  background: rgba(255, 252, 248, 0.85);
  perspective: 1100px;
}

.location-flip-inner {
  position: absolute;
  inset: 0;
  transform-style: preserve-3d;
  transition: transform 650ms cubic-bezier(0.2, 0.8, 0.2, 1);
}

.location-flip-face {
  position: absolute;
  inset: 0;
  backface-visibility: hidden;
}

.location-flip-face.is-back {
  transform: rotateY(180deg);
}

.location-flip-face img {
  width: 100%;
  height: 100%;
  display: block;
  object-fit: cover;
}

.location-flip-btn {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: 40px;
  height: 40px;
  border-radius: 50%;
  border: 1px solid rgba(255, 255, 255, 0.45);
  background: rgba(0, 0, 0, 0.3);
  color: rgba(255, 255, 255, 0.95);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 3;
  transition: background 200ms ease, transform 200ms ease;
}

.location-flip-btn span {
  font-size: 24px;
  line-height: 1;
}

.location-flip-btn.is-left {
  left: 10px;
}

.location-flip-btn.is-right {
  right: 10px;
}

.location-flip-btn:hover {
  background: rgba(0, 0, 0, 0.45);
  transform: translateY(-50%) scale(1.05);
}

.location-note-title {
  font-size: 18px;
  font-weight: 800;
  color: #5c3e2a;
  letter-spacing: 2px;
  margin-bottom: 10px;
}

.location-note-text {
  font-size: 15px;
  line-height: 1.9;
  color: rgba(92, 62, 42, 0.82);
  text-align: justify;
  margin-bottom: 14px;
}

.location-legend {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.legend-item {
  display: flex;
  align-items: center;
  gap: 10px;
}

.legend-swatch {
  width: 14px;
  height: 14px;
  border-radius: 50%;
  flex-shrink: 0;
}

.legend-swatch.is-dunhuang {
  background: rgba(205, 65, 47, 0.95);
  box-shadow: 0 0 0 3px rgba(205, 65, 47, 0.18);
}

.legend-swatch.is-china {
  background: rgba(255, 252, 248, 0.9);
  border: 2px solid rgba(92, 62, 42, 0.65);
}

.legend-text {
  font-size: 14px;
  color: rgba(92, 62, 42, 0.8);
  letter-spacing: 1px;
}

.image-title > * {
  pointer-events: auto;
}

.dunhuang-title {
  font-family: var(--font-calligraphy);
  font-size: 196px;
  font-weight: normal;
  color: rgba(255, 255, 255, 0.95);
  text-shadow: 
    8px 8px 16px rgba(0, 0, 0, 0.6),
    12px 12px 24px rgba(0, 0, 0, 0.4),
    0 0 30px rgba(212, 175, 55, 0.4),
    0 0 60px rgba(212, 175, 55, 0.2);
  letter-spacing: 12px;
  line-height: 1.2;
  margin: 0;
  animation: titleFadeIn 2s ease-out;
  white-space: nowrap;
  position: relative;
  display: inline-block;
  will-change: letter-spacing, text-shadow;
  transition: letter-spacing 420ms ease, text-shadow 420ms ease, transform 420ms ease, filter 420ms ease, color 420ms ease;
}

.dunhuang-title:hover,
.dunhuang-title:focus-visible {
  letter-spacing: 36px;
  transform: translate3d(0, -6px, 0);
  filter: brightness(2) saturate(1.1);
  color: rgba(255, 255, 255, 1);
  text-shadow:
    8px 8px 16px rgba(0, 0, 0, 0.6),
    12px 12px 24px rgba(0, 0, 0, 0.4),
    0 0 30px rgba(212, 175, 55, 0.4),
    0 0 60px rgba(212, 175, 55, 0.2);
}

@keyframes titleFadeIn {
  0% {
    opacity: 0;
    transform: translateY(30px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}

/* 关于敦煌区域样式 */
.about-dunhuang-section {
  width: 100%;
  min-height: 100vh;
  background-color: #f4d5b8;
  background-image: url('/images/home/sy22.jpg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  padding: 80px 50px 100px;
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.about-dunhuang-section::before {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, rgba(244, 213, 184, 0.86), rgba(244, 213, 184, 0.62));
  pointer-events: none;
}

.about-dunhuang-section > * {
  position: relative;
  z-index: 1;
}

.about-header {
  width: 100%;
  max-width: 1200px;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  margin-bottom: 60px;
}

.header-line {
  width: 80px;
  height: 2px;
  background: #8b6f47;
  margin: 0 20px;
}

.about-title {
  font-family: var(--font-calligraphy);
  font-size: 48px;
  font-weight: normal;
  color: #5c3e2a;
  letter-spacing: 8px;
  margin: 0;
}

.header-decoration-left,
.header-decoration-right {
  position: absolute;
  font-family: var(--font-calligraphy);
  font-size: 24px;
  color: rgba(92, 62, 42, 0.3);
  writing-mode: vertical-rl;
  letter-spacing: 4px;
  top: 50%;
  transform: translateY(-50%);
}

.header-decoration-left {
  left: 0;
}

.header-decoration-right {
  right: 0;
}

.about-content {
  width: 100%;
  max-width: 1200px;
  display: flex;
  gap: 60px;
  align-items: flex-start;
  margin-bottom: 60px;
}

.about-text-box {
  flex: 1;
  background: rgba(255, 248, 240, 0.9);
  padding: 40px;
  border-radius: 8px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
}

.about-subtitle {
  font-family: var(--font-calligraphy);
  font-size: 28px;
  font-weight: normal;
  color: #5c3e2a;
  margin: 0 0 30px 0;
  letter-spacing: 4px;
}

.about-text {
  color: #5c3e2a;
  line-height: 2;
  font-size: 16px;
}

.about-text p {
  margin-bottom: 20px;
  text-align: justify;
}

.about-image-box {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: flex-start;
}

.image-frame {
  position: relative;
  width: 100%;
  max-width: 500px;
  padding: 15px;
  background: rgba(255, 248, 240, 0.6);
  border: 2px solid rgba(139, 111, 71, 0.3);
  border-radius: 4px;
}

.corner-decoration {
  position: absolute;
  width: 40px;
  height: 40px;
  border: 2px solid rgba(139, 111, 71, 0.4);
  z-index: 1;
}

.corner-decoration.top-right {
  top: 0;
  right: 0;
  border-left: none;
  border-bottom: none;
  border-top-right-radius: 4px;
}

.corner-decoration.bottom-left {
  bottom: 0;
  left: 0;
  border-right: none;
  border-top: none;
  border-bottom-left-radius: 4px;
}

.about-image {
  width: 100%;
  height: auto;
  display: block;
  border-radius: 2px;
}

.cube-scene {
  width: 420px;
  height: 420px;
  display: flex;
  align-items: center;
  justify-content: center;
  perspective: 900px;
  perspective-origin: 50% 40%;
  margin-top: 6px;
}

.cube {
  position: relative;
  width: 320px;
  height: 320px;
  transform-style: preserve-3d;
  --cube-gap: 0px;
  animation: cubeSpin 12s linear infinite;
}

.cube-face {
  position: absolute;
  inset: var(--cube-gap);
  border-radius: 18px;
  overflow: hidden;
  backface-visibility: hidden;
  box-shadow: 0 14px 28px rgba(0, 0, 0, 0.22);
}

.cube-face img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.cube-front {
  transform: rotateY(0deg) translateZ(160px);
}

.cube-back {
  transform: rotateY(180deg) translateZ(160px);
}

.cube-right {
  transform: rotateY(90deg) translateZ(160px);
}

.cube-left {
  transform: rotateY(-90deg) translateZ(160px);
}

.cube-top {
  transform: rotateX(90deg) translateZ(160px);
}

.cube-bottom {
  transform: rotateX(-90deg) translateZ(160px);
}

@keyframes cubeSpin {
  0% {
    transform: rotateX(-18deg) rotateY(0deg);
  }
  100% {
    transform: rotateX(-18deg) rotateY(360deg);
  }
}

.about-buttons {
  display: flex;
  gap: 30px;
  justify-content: center;
  flex-wrap: wrap;
}

.about-btn {
  padding: 12px 40px;
  background: rgba(139, 111, 71, 0.8);
  border: 2px solid #8b6f47;
  border-radius: 25px;
  color: #fff;
  font-size: 16px;
  font-weight: 500;
  letter-spacing: 2px;
  cursor: pointer;
  transition: all 0.3s ease;
  font-family: var(--font-calligraphy);
}

.about-btn:hover {
  background: #8b6f47;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(139, 111, 71, 0.4);
}

/* 探索敦煌区域样式 */
.explore-dunhuang-section {
  width: 100%;
  min-height: 100vh;
  background-color: #f5e6d3;
  background-image: url('/images/home/sy23.jpg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  padding: 80px 50px 100px;
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.explore-dunhuang-section::before {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, rgba(245, 230, 211, 0.78), rgba(240, 221, 208, 0.58));
  pointer-events: none;
  z-index: 0;
}

.explore-dunhuang-section > * {
  position: relative;
  z-index: 1;
}

.explore-header {
  width: 100%;
  max-width: 1400px;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  margin-bottom: 30px;
}

.explore-decorative-left,
.explore-decorative-right {
  width: 120px;
  height: 60px;
  background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 120 60'%3E%3Cpath d='M10,30 Q30,10 50,30 Q70,50 90,30 Q110,10 120,30' stroke='%238b6f47' stroke-width='2' fill='none'/%3E%3Cpath d='M10,30 Q30,50 50,30 Q70,10 90,30 Q110,50 120,30' stroke='%238b6f47' stroke-width='2' fill='none'/%3E%3C/svg%3E") no-repeat center;
  background-size: contain;
  opacity: 0.6;
}

.explore-title {
  font-family: var(--font-calligraphy);
  font-size: 64px;
  font-weight: normal;
  color: #5c3e2a;
  letter-spacing: 12px;
  margin: 0 40px;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
}

.explore-subtitle {
  font-size: 18px;
  color: #6b4e3d;
  text-align: center;
  margin-bottom: 60px;
  letter-spacing: 2px;
}

.explore-gallery {
  width: 100%;
  max-width: 1400px;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0 80px;
}

.gallery-container {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  width: 100%;
  overflow: visible;
  perspective: 1200px;
}

.gallery-card {
  flex: 0 0 200px;
  height: 300px;
  background: transparent;
  border-radius: 12px;
  overflow: hidden;
  cursor: pointer;
  position: relative;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
  transform: scale(0.65) translateZ(0);
  opacity: 0.6;
  z-index: 1;
  /* 固定大小，不变化 */
  transition: none;
}

.gallery-card.card-adjacent {
  flex: 0 0 240px;
  height: 360px;
  transform: scale(0.8) translateZ(0);
  opacity: 0.75;
  z-index: 5;
  /* 固定大小，不变化 */
  transition: none;
}

.gallery-card.card-center {
  flex: 0 0 320px;
  height: 480px;
  transform: scale(1) translateZ(0);
  opacity: 1;
  z-index: 10;
  box-shadow: 0 16px 48px rgba(0, 0, 0, 0.25);
  /* 固定大小，不变化 */
  transition: none;
}

.gallery-card.card-outer {
  transform: scale(0.65) translateZ(0);
  opacity: 0.6;
  z-index: 1;
  /* 固定大小，不变化 */
  transition: none;
}

.gallery-card:hover {
  box-shadow: 0 12px 36px rgba(0, 0, 0, 0.2);
}

.gallery-card.card-adjacent:hover {
  box-shadow: 0 12px 36px rgba(0, 0, 0, 0.2);
}

.gallery-card.card-center:hover {
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
}

.card-image-wrapper {
  width: 100%;
  height: 100%;
  position: relative;
  overflow: hidden;
  background: transparent;
}

.gallery-card.card-adjacent .card-image-wrapper {
  height: 100%;
}

.gallery-card.card-center .card-image-wrapper {
  height: 100%;
}

.card-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  opacity: 1;
  display: block;
  filter: none;
  transition: none;
}

.card-image-wrapper {
  position: relative;
  overflow: hidden;
}

/* 中心图片：先放大再回弹 */
.card-image.image-center {
  animation: none;
  transform: none;
}

@keyframes centerImageZoom {
  0% {
    transform: scale(0.95);
  }
  50% {
    transform: scale(1.15);
  }
  100% {
    transform: scale(1.1);
  }
}

/* 相邻图片：中等缩放 */
.card-image.image-adjacent {
  animation: none;
  transform: none;
}

@keyframes adjacentImageZoom {
  0% {
    transform: scale(0.9);
  }
  50% {
    transform: scale(1.08);
  }
  100% {
    transform: scale(1.05);
  }
}

/* 外侧图片：小缩放 */
.card-image.image-outer {
  animation: none;
  transform: none;
}

@keyframes outerImageZoom {
  0% {
    transform: scale(0.88);
  }
  50% {
    transform: scale(1.05);
  }
  100% {
    transform: scale(1.02);
  }
}

.gallery-card:hover .card-image {
  opacity: 1;
}

.gallery-card.card-center:hover .card-image {
  transform: none;
}

.gallery-card.card-adjacent:hover .card-image {
  transform: none;
}

.gallery-card.card-outer:hover .card-image {
  transform: none;
}

.card-glow {
  display: none;
}

.card-content {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 16px;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 0;
  background: transparent;
  pointer-events: none;
}

.card-title {
  display: none;
}

.card-enter-btn {
  pointer-events: auto;
  padding: 10px 26px;
  background: rgba(0, 0, 0, 0.45);
  border: 1px solid rgba(255, 255, 255, 0.55);
  color: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(6px);
  -webkit-backdrop-filter: blur(6px);
}

.gallery-card.card-adjacent .card-content {
  bottom: 14px;
}

.gallery-card.card-center .card-content {
  bottom: 18px;
}

.card-enter-btn:hover {
  background: rgba(0, 0, 0, 0.55);
}

.gallery-nav-btn {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.8);
  border: 2px solid rgba(139, 111, 71, 0.3);
  color: #8b6f47;
  font-size: 28px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
  z-index: 20;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.gallery-nav-btn:hover {
  background: rgba(255, 255, 255, 1);
  border-color: #8b6f47;
  transform: translateY(-50%) scale(1.1);
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.15);
}

.gallery-nav-left {
  left: 0;
}

.gallery-nav-right {
  right: 0;
}

.gallery-nav-btn span {
  line-height: 1;
  font-weight: bold;
}

/* 主题区块样式 */
.themes-section {
  width: 100%;
  background: linear-gradient(
    180deg,
    #1a1815 0%,
    #2a2520 30%,
    #1f1c18 70%,
    #1a1815 100%
  );
  padding: 100px 0;
  position: relative;
}

.themes-section::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: 
    radial-gradient(circle at 20% 30%, rgba(139, 111, 71, 0.08) 0%, transparent 50%),
    radial-gradient(circle at 80% 70%, rgba(212, 175, 55, 0.06) 0%, transparent 50%);
  pointer-events: none;
  z-index: 0;
}

.themes-section > * {
  position: relative;
  z-index: 1;
}

.theme-block {
  display: flex;
  align-items: center;
  justify-content: space-between;
  max-width: 1400px;
  margin: 0 auto;
  padding: 80px 50px;
  min-height: 500px;
  position: relative;
  border-top: 1px solid rgba(212, 175, 55, 0.08);
  border-bottom: 1px solid rgba(212, 175, 55, 0.08);
  transition: background 0.3s ease;
}

.theme-block::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(
    90deg,
    transparent 0%,
    rgba(212, 175, 55, 0.02) 50%,
    transparent 100%
  );
  opacity: 0;
  transition: opacity 0.3s ease;
}

.theme-block:hover::before {
  opacity: 1;
}

.theme-block-reverse {
  flex-direction: row-reverse;
}

.theme-content {
  flex: 1;
  max-width: 600px;
  padding-right: 30px;
  position: relative;
}

.theme-block-reverse .theme-content {
  padding-right: 0;
  padding-left: 30px;
}

.theme-number {
  font-size: 120px;
  font-weight: 300;
  color: rgba(255, 255, 255, 0.15);
  line-height: 1;
  margin-bottom: 20px;
  font-family: 'Arial', sans-serif;
  letter-spacing: -4px;
}

.theme-header {
  display: flex;
  align-items: center;
  gap: 20px;
  margin-bottom: 30px;
  position: relative;
}

.theme-label {
  font-family: var(--font-calligraphy);
  font-size: 18px;
  color: rgba(255, 255, 255, 0.3);
  letter-spacing: 8px;
  position: absolute;
  top: -10px;
  left: 140px;
}

.theme-line {
  width: 200px;
  height: 1px;
  background: rgba(255, 255, 255, 0.2);
  margin-top: 10px;
}

.theme-title {
  font-family: var(--font-calligraphy);
  font-size: 56px;
  font-weight: normal;
  color: rgba(255, 255, 255, 0.9);
  margin: 0 0 40px 0;
  letter-spacing: 4px;
}

.theme-description {
  margin-bottom: 40px;
}

.theme-description p {
  font-size: 16px;
  line-height: 1.8;
  color: rgba(255, 255, 255, 0.7);
  margin-bottom: 20px;
  text-align: justify;
}

.theme-link {
  display: inline-block;
  font-size: 14px;
  color: rgba(255, 255, 255, 0.6);
  text-decoration: none;
  letter-spacing: 2px;
  transition: color 0.3s ease;
  position: relative;
  padding-bottom: 5px;
}

.theme-link::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0;
  height: 1px;
  background: rgba(212, 175, 55, 0.8);
  transition: width 0.3s ease;
}

.theme-link:hover {
  color: rgba(212, 175, 55, 0.9);
}

.theme-link:hover::after {
  width: 100%;
}

.theme-illustration {
  flex: 1;
  max-width: 500px;
  height: 500px;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.illustration-glow {
  position: absolute;
  width: 400px;
  height: 400px;
  border-radius: 50%;
  background: radial-gradient(
    circle,
    rgba(255, 200, 100, 0.4) 0%,
    rgba(255, 180, 80, 0.2) 30%,
    transparent 70%
  );
  filter: blur(40px);
  animation: glowPulse 4s ease-in-out infinite;
}

@keyframes glowPulse {
  0%, 100% {
    transform: scale(1);
    opacity: 0.6;
  }
  50% {
    transform: scale(1.1);
    opacity: 0.8;
  }
}

.illustration-content {
  position: relative;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1;
}

.illustration-pattern {
  width: 350px;
  height: 450px;
  border-radius: 20px;
  position: relative;
  overflow: hidden;
  box-shadow: 
    0 0 0 2px rgba(212, 175, 55, 0.9),
    0 8px 32px rgba(0, 0, 0, 0.4),
    inset 0 0 40px rgba(212, 175, 55, 0.1);
}

.illustration-photo {
  position: absolute;
  inset: 0;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  transform: scale(1);
  transition: transform 0.6s ease;
  z-index: 0;
}

.illustration-dim {
  position: absolute;
  inset: 0;
  background: rgba(0, 0, 0, 0.5);
  opacity: 0;
  transition: opacity 0.35s ease;
  z-index: 3;
}

.illustration-hover {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  opacity: 0;
  transform: translate3d(0, 8px, 0);
  transition: opacity 0.35s ease, transform 0.35s ease;
  z-index: 4;
  pointer-events: none;
}

.illustration-hover-sub {
  font-size: 16px;
  color: rgba(255, 255, 255, 0.88);
  letter-spacing: 2px;
  margin-bottom: 12px;
}

.illustration-hover-title {
  font-size: 34px;
  font-weight: 800;
  color: rgba(255, 255, 255, 0.95);
  letter-spacing: 6px;
  text-shadow: 0 8px 24px rgba(0, 0, 0, 0.45);
}

.illustration-pattern::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(
    135deg,
    rgba(212, 175, 55, 0.05) 0%,
    rgba(139, 111, 71, 0.1) 50%,
    rgba(212, 175, 55, 0.05) 100%
  );
  border-radius: 20px;
  z-index: 1;
}

.illustration-pattern::after {
  content: '';
  position: absolute;
  top: -50%;
  right: -20%;
  width: 200px;
  height: 200px;
  background: radial-gradient(
    circle,
    rgba(255, 220, 150, 0.2) 0%,
    transparent 70%
  );
  border-radius: 50%;
  filter: blur(30px);
  z-index: 2;
}

@media (hover: hover) and (pointer: fine) {
  .illustration-pattern:hover .illustration-photo {
    transform: scale(1.16);
  }

  .illustration-pattern:hover .illustration-dim {
    opacity: 1;
  }

  .illustration-pattern:hover .illustration-hover {
    opacity: 1;
    transform: translate3d(0, 0, 0);
  }
}

@media (prefers-reduced-motion: reduce) {
  .illustration-photo,
  .illustration-dim,
  .illustration-hover {
    transition: none;
  }

  .illustration-pattern:hover .illustration-photo {
    transform: none;
  }
}

.contact-section {
  width: 100%;
  background: #ffffff;
  padding: 86px 50px 100px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.contact-header {
  text-align: center;
  margin-bottom: 58px;
}

.contact-main-title {
  font-family: var(--font-calligraphy);
  font-size: 54px;
  font-weight: normal;
  color: #2b2b2b;
  letter-spacing: 8px;
  margin: 0 0 14px 0;
}

.contact-subtitle {
  font-size: 16px;
  color: rgba(43, 43, 43, 0.7);
  margin: 0;
}

.contact-content {
  width: 100%;
  max-width: 1200px;
  display: grid;
  grid-template-columns: 1fr 1.1fr;
  gap: 80px;
  align-items: start;
}

.contact-left-title {
  font-size: 26px;
  font-weight: 700;
  color: #1f1f1f;
  margin: 0 0 24px 0;
  letter-spacing: 2px;
}

.contact-list {
  display: flex;
  flex-direction: column;
  gap: 22px;
}

.contact-item {
  display: flex;
  gap: 16px;
  align-items: flex-start;
}

.contact-icon-wrap {
  width: 46px;
  height: 46px;
  border-radius: 50%;
  background: #215cf2;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  box-shadow: 0 10px 22px rgba(33, 92, 242, 0.28);
}

.contact-icon {
  width: 22px;
  height: 22px;
  color: #ffffff;
}

.contact-item-title {
  font-size: 16px;
  font-weight: 700;
  color: #1f1f1f;
  margin-bottom: 6px;
}

.contact-item-text {
  font-size: 14px;
  color: rgba(43, 43, 43, 0.72);
  line-height: 1.6;
}

.contact-form {
  width: 100%;
}

.contact-field {
  margin-bottom: 18px;
}

.contact-label {
  font-size: 13px;
  font-weight: 700;
  color: rgba(43, 43, 43, 0.85);
  margin-bottom: 8px;
}

.contact-input,
.contact-textarea {
  width: 100%;
  border: 1px solid rgba(0, 0, 0, 0.08);
  border-radius: 4px;
  padding: 12px 14px;
  font-size: 14px;
  outline: none;
  background: rgba(0, 0, 0, 0.02);
  transition: border-color 0.2s ease, background 0.2s ease;
}

.contact-textarea {
  resize: vertical;
  min-height: 140px;
}

.contact-input:focus,
.contact-textarea:focus {
  border-color: rgba(33, 92, 242, 0.55);
  background: rgba(0, 0, 0, 0.01);
}

.contact-submit-row {
  display: flex;
  justify-content: center;
  margin-top: 24px;
}

.contact-submit-btn {
  padding: 12px 36px;
  border: none;
  border-radius: 6px;
  background: #215cf2;
  color: #ffffff;
  font-size: 14px;
  font-weight: 700;
  letter-spacing: 2px;
  cursor: pointer;
  transition: transform 0.22s ease, box-shadow 0.22s ease, background 0.22s ease;
  box-shadow: 0 14px 32px rgba(33, 92, 242, 0.25);
}

@media (hover: hover) and (pointer: fine) {
  .contact-submit-btn:hover {
    transform: translateY(-2px);
    background: #1d52db;
    box-shadow: 0 18px 40px rgba(33, 92, 242, 0.3);
  }
}

.site-footer {
  width: 100%;
  background: #3a3a3a;
  color: rgba(255, 255, 255, 0.88);
}

.site-footer-inner {
  max-width: 1200px;
  margin: 0 auto;
  padding: 54px 50px 24px;
}

.site-footer-columns {
  display: grid;
  grid-template-columns: 1.2fr 0.8fr 1fr;
  gap: 80px;
}

.footer-brand {
  font-size: 20px;
  font-weight: 800;
  letter-spacing: 1px;
  color: rgba(255, 255, 255, 0.94);
  margin-bottom: 14px;
}

.footer-desc {
  font-size: 13px;
  line-height: 1.9;
  color: rgba(255, 255, 255, 0.7);
}

.footer-social {
  display: flex;
  gap: 10px;
  margin-top: 18px;
}

.footer-social-btn {
  width: 34px;
  height: 34px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.08);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  text-decoration: none;
  transition: transform 0.22s ease, background 0.22s ease;
}

.footer-social-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: rgba(212, 175, 55, 0.9);
  box-shadow: 0 10px 22px rgba(212, 175, 55, 0.18);
}

@media (hover: hover) and (pointer: fine) {
  .footer-social-btn:hover {
    transform: translateY(-2px);
    background: rgba(255, 255, 255, 0.14);
  }
}

.footer-title {
  font-size: 16px;
  font-weight: 800;
  color: rgba(255, 255, 255, 0.92);
  margin-bottom: 16px;
  letter-spacing: 1px;
}

.footer-title-spaced {
  margin-top: 18px;
}

.footer-links {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.footer-link {
  color: rgba(255, 255, 255, 0.72);
  text-decoration: none;
  font-size: 13px;
  transition: color 0.22s ease;
}

@media (hover: hover) and (pointer: fine) {
  .footer-link:hover {
    color: rgba(212, 175, 55, 0.95);
  }
}

.footer-contact {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.footer-contact-item {
  display: flex;
  align-items: center;
  gap: 10px;
}

.footer-contact-icon {
  width: 20px;
  text-align: center;
  opacity: 0.9;
}

.footer-contact-text {
  font-size: 13px;
  color: rgba(255, 255, 255, 0.72);
}

.footer-team {
  font-size: 13px;
  color: rgba(255, 255, 255, 0.78);
}

.footer-bottom {
  margin-top: 34px;
}

.footer-divider {
  height: 1px;
  background: rgba(255, 255, 255, 0.08);
  margin-bottom: 16px;
}

.footer-copy {
  font-size: 12px;
  color: rgba(255, 255, 255, 0.45);
  text-align: center;
}

@media (max-width: 768px) {
  .dunhuang-title {
    font-size: 48px;
    letter-spacing: 6px;
  }

  .dunhuang-title:hover,
  .dunhuang-title:focus-visible {
    letter-spacing: 16px;
    transform: translate3d(0, -2px, 0);
  }
  
  .about-dunhuang-section {
    padding: 60px 20px 80px;
  }
  
  .about-header {
    margin-bottom: 40px;
  }
  
  .header-line {
    width: 40px;
    margin: 0 10px;
  }
  
  .about-title {
    font-size: 32px;
    letter-spacing: 4px;
  }
  
  .header-decoration-left,
  .header-decoration-right {
    font-size: 18px;
    display: none;
  }
  
  .about-content {
    flex-direction: column;
    gap: 40px;
  }

  .cube-scene {
    width: 320px;
    height: 320px;
  }

  .cube {
    width: 240px;
    height: 240px;
    --cube-gap: 0px;
  }

  .cube-front,
  .cube-back,
  .cube-right,
  .cube-left,
  .cube-top,
  .cube-bottom {
    transform: none;
  }

  .cube-front {
    transform: rotateY(0deg) translateZ(120px);
  }

  .cube-back {
    transform: rotateY(180deg) translateZ(120px);
  }

  .cube-right {
    transform: rotateY(90deg) translateZ(120px);
  }

  .cube-left {
    transform: rotateY(-90deg) translateZ(120px);
  }

  .cube-top {
    transform: rotateX(90deg) translateZ(120px);
  }

  .cube-bottom {
    transform: rotateX(-90deg) translateZ(120px);
  }
  
  .about-text-box {
    padding: 30px 20px;
  }
  
  .about-subtitle {
    font-size: 24px;
  }
  
  .about-text {
    font-size: 14px;
  }
  
  .about-buttons {
    gap: 20px;
  }
  
  .about-btn {
    padding: 10px 30px;
    font-size: 14px;
  }
  
  .explore-dunhuang-section {
    padding: 60px 20px 80px;
  }
  
  .explore-title {
    font-size: 36px;
    letter-spacing: 6px;
    margin: 0 20px;
  }
  
  .explore-decorative-left,
  .explore-decorative-right {
    width: 60px;
    height: 30px;
  }
  
  .explore-subtitle {
    font-size: 16px;
    padding: 0 20px;
  }
  
  .explore-gallery {
    padding: 0 60px;
  }

  .dunhuang-guardians-section {
    padding: 60px 20px 80px;
  }

  .guardians-title {
    font-size: 34px;
    letter-spacing: 6px;
    margin: 0 18px;
  }

  .guardians-line {
    width: 50px;
  }

  .guardians-subtitle {
    font-size: 16px;
    padding: 0 10px;
  }

  .guardians-grid {
    grid-template-columns: 1fr;
    gap: 18px;
  }

  .guardian-card {
    padding: 18px 16px;
  }

  .guardian-avatar {
    width: 88px;
    height: 88px;
  }

  .guardian-name {
    font-size: 18px;
  }

  .guardian-desc {
    font-size: 14px;
  }

  .dunhuang-history-section {
    padding: 60px 20px 80px;
  }

  .dunhuang-location-section {
    padding: 60px 20px 80px;
  }

  .location-title {
    font-size: 34px;
    letter-spacing: 6px;
    margin: 0 18px;
  }

  .location-line {
    width: 60px;
  }

  .location-content {
    flex-direction: column;
    gap: 18px;
    margin-top: 8px;
  }

  .location-map,
  .location-notes {
    padding: 16px;
  }

  .location-side {
    gap: 12px;
  }

  .location-climate-card {
    padding: 20px 20px;
    border-radius: 16px;
  }

  .location-climate-title {
    font-size: 18px;
    margin-bottom: 10px;
  }

  .location-climate-text {
    font-size: 14px;
    line-height: 1.9;
  }

  .location-side {
    gap: 12px;
  }

  .location-flip-btn {
    width: 36px;
    height: 36px;
  }

  .marker-pulse {
    width: 38px;
    height: 38px;
  }

  .marker-dot {
    width: 10px;
    height: 10px;
  }

  .marker-label {
    font-size: 22px;
    left: 14px;
    top: -14px;
  }

  .china-label {
    font-size: 14px;
    stroke-width: 2.5px;
  }

  .history-title {
    font-size: 34px;
    letter-spacing: 6px;
    margin: 0 18px;
  }

  .history-line {
    width: 60px;
  }

  .history-list {
    gap: 16px;
  }

  .history-list::before {
    display: none;
  }

  .history-item,
  .history-item.is-right {
    justify-content: center;
    padding-left: 0;
    padding-right: 0;
    flex-direction: column;
    align-items: center;
  }

  .history-range {
    position: static;
    transform: none;
    width: 100%;
    text-align: center;
    margin-bottom: 10px;
    font-family: var(--font-calligraphy);
    font-size: 22px;
    font-weight: 800;
    letter-spacing: 2px;
  }

  .history-card {
    width: 100%;
    padding: 18px 16px;
  }

  .history-avatar {
    width: 72px;
    height: 72px;
  }

  .history-era {
    font-size: 16px;
  }

  .dunhuang-history-section .history-desc {
    font-size: 14px;
  }
  
  .gallery-container {
    gap: 8px;
  }
  
  .gallery-card {
    flex: 0 0 150px;
    height: 240px;
    transform: scale(0.6) translateZ(0);
  }
  
  .gallery-card.card-adjacent {
    flex: 0 0 180px;
    height: 280px;
    transform: scale(0.75) translateZ(0);
  }
  
  .gallery-card.card-center {
    flex: 0 0 220px;
    height: 340px;
    transform: scale(1) translateZ(0);
  }
  
  .card-image-wrapper {
    height: 150px;
  }
  
  .gallery-card.card-adjacent .card-image-wrapper {
    height: 180px;
  }
  
  .gallery-card.card-center .card-image-wrapper {
    height: 220px;
  }
  
  .card-title {
    font-size: 14px;
  }
  
  .gallery-card.card-adjacent .card-title {
    font-size: 16px;
  }
  
  .gallery-card.card-center .card-title {
    font-size: 20px;
  }
  
  .card-enter-btn {
    padding: 6px 20px;
    font-size: 11px;
  }
  
  .gallery-card.card-adjacent .card-enter-btn {
    padding: 7px 22px;
    font-size: 12px;
  }
  
  .gallery-card.card-center .card-enter-btn {
    padding: 8px 25px;
    font-size: 12px;
  }
  
  .gallery-nav-btn {
    width: 40px;
    height: 40px;
    font-size: 24px;
  }
  
  .gallery-nav-left {
    left: 10px;
  }
  
  .gallery-nav-right {
    right: 10px;
  }
  
  .themes-section {
    padding: 50px 0;
  }
  
  .theme-block {
    flex-direction: column;
    padding: 40px 20px;
    min-height: auto;
  }
  
  .theme-block-reverse {
    flex-direction: column;
  }
  
  .theme-content {
    max-width: 100%;
    padding-right: 0;
    padding-left: 0;
    margin-bottom: 40px;
  }
  
  .theme-number {
    font-size: 80px;
  }
  
  .theme-label {
    font-size: 14px;
    left: 100px;
  }
  
  .theme-title {
    font-size: 36px;
  }
  
  .theme-description p {
    font-size: 14px;
  }
  
  .theme-illustration {
    max-width: 100%;
    height: 300px;
  }
  
  .illustration-glow {
    width: 250px;
    height: 250px;
  }
  
  .illustration-pattern {
    width: 200px;
    height: 250px;
  }

  .contact-section {
    padding: 60px 20px 80px;
  }

  .contact-main-title {
    font-size: 36px;
    letter-spacing: 6px;
  }

  .contact-header {
    margin-bottom: 34px;
  }

  .contact-content {
    grid-template-columns: 1fr;
    gap: 34px;
  }

  .site-footer-inner {
    padding: 44px 20px 20px;
  }

  .site-footer-columns {
    grid-template-columns: 1fr;
    gap: 28px;
  }
}
</style>

