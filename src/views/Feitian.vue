<template>
  <div class="feitian-page">
    <NavBar />
    
    <!-- 首页区块 -->
    <section ref="heroSectionEl" class="content-section hero-section">
      <!-- 全屏背景图 -->
      <div class="hero-background">
        <img :src="assetUrl('/images/feitian/ft21.jpg')" alt="飞天" class="background-image" />
        <div class="hero-overlay-wrap" :style="heroOverlayWrapStyle" aria-hidden="true">
          <div class="hero-overlay-float">
            <img :src="assetUrl('/images/feitian/ft1.png')" alt="" class="hero-overlay-image" />
            <div class="hero-overlay-watermark-cover"></div>
          </div>
        </div>
      </div>

      <!-- 主要内容区域 - 左上角 -->
      <div class="main-content">
        <div class="location-tag">敦煌艺术</div>
        <h1 class="main-title">飞天</h1>
        <p class="main-description">
          飞天是敦煌艺术的标志性形象，以其优美的姿态和飘逸的动感而闻名。从早期的粗犷风格到唐代的优雅飘逸，飞天形象经历了千年的演变，体现了不同时期艺术风格的特色。
        </p>
        <button class="discover-btn" @click="scrollToNextSection">
          <span>探索飞天</span>
        </button>
      </div>
      
      <!-- 卡片轮播 - 右下角 -->
      <div class="cards-carousel">
        <div class="cards-container" @transitionend="handleTransitionEnd">
          <div 
            class="carousel-card" 
            v-for="(item, index) in cardsWithClones" 
            :key="`card-${index}`"
            :data-index="index"
            :style="{ 
              transform: `translateX(${(currentCardIndex - index) * 280}px)`,
              zIndex: cardsWithClones.length - Math.abs(index - currentCardIndex),
              opacity: isCardVisible(index) ? 1 : 0,
              visibility: isCardVisible(index) ? 'visible' : 'hidden',
              transition: isTransitioning ? 'transform 0.6s cubic-bezier(0.25, 0.46, 0.45, 0.94), opacity 0.3s ease' : 'none'
            }"
          >
            <div class="card-image">
              <img 
                :src="item.image" 
                :alt="item.title" 
                class="card-image-img"
                @error="handleImageError"
              />
            </div>
            <div class="card-content">
              <div class="card-location">{{ item.location }}</div>
              <div class="card-title">{{ item.title }}</div>
            </div>
          </div>
        </div>

        <!-- 轮播控制 -->
        <div class="carousel-controls">
          <button class="carousel-nav-btn" @click="prevCard">‹</button>
          <button class="carousel-nav-btn" @click="nextCard">›</button>
          <span class="carousel-page">{{ String(displayIndex).padStart(2, '0') }} / 05</span>
        </div>
      </div>

    </section>
    
    <!-- 内容区块 - 拼接式布局 -->
    <!-- 飞天简介 -->
    <section id="feitian-intro" class="content-section section-intro">
      <h2 class="section-title">飞天简介</h2>
      <div class="intro-content">
        <div class="intro-image">
          <div class="intro-image-swap">
            <img :src="assetUrl('/images/feitian/ft07.jpg')" alt="飞天" class="intro-image-img intro-image-img-base" />
            <img :src="assetUrl('/images/feitian/cxy.jpg')" alt="" class="intro-image-img intro-image-img-hover" aria-hidden="true" />
          </div>
            </div>
        <div class="intro-text">
          <p>飞天是敦煌艺术的标志性形象，以其优美的姿态和飘逸的动感而闻名于世。从早期的粗犷风格到唐代的优雅飘逸，飞天形象经历了千年的演变，体现了不同时期艺术风格的特色。</p>
          <p>飞天形象最早出现在北凉时期，经过北魏、隋代的发展，在唐代达到艺术巅峰。不同时期的飞天在造型、色彩、姿态上都有显著差异，反映了当时的社会文化背景和艺术审美取向。</p>
          <p>飞天不仅是佛教艺术的重要元素，更是中华文化的瑰宝。她们以曼妙的舞姿、飘逸的衣带、生动的表情，展现了古代艺术家对美的追求和对生命的赞美，成为敦煌艺术中最具代表性的形象之一。</p>

          <!-- 飞天音乐播放器 -->
          <div class="feitian-player">
            <div class="player-card">
              <!-- 左侧“唱片卡片” -->
              <div class="player-cover-card">
                <div class="player-cover-square">
                  <div class="player-cover-circle" :class="{ 'is-rotating': isPlaying }">
                    <img
                      :src="currentTrack.cover"
                      alt="飞天音乐封面"
                      class="player-cover-img"
                    />
                    <div class="player-cover-inner"></div>
                  </div>
                </div>
              </div>

              <!-- 右侧信息 + 进度条 -->
              <div class="player-main-panel">
                <div class="player-text-block">
                  <div class="player-title">{{ currentTrack.title }}</div>
                  <div class="player-sub">{{ currentTrack.subtitle }}</div>
                </div>
                <div class="player-progress-row">
                  <div class="player-progress-track">
                    <div class="player-progress-fill" :style="{ width: progressPercent + '%' }"></div>
                  </div>
                  <div class="player-time-row">
                    <span>{{ formattedCurrentTime }}</span>
                    <span>{{ formattedDuration }}</span>
                  </div>
                </div>
                <!-- 进度条下方控制按钮 -->
                <div class="player-bottom-bar">
                  <div class="player-bottom-inner">
                    <button class="player-small-btn" type="button" @click="prevTrack">
                      <span class="player-icon-double-left"></span>
                    </button>
                    <button class="player-pause-block" type="button" @click="togglePlay">
                      <template v-if="isPlaying">
                        <span class="player-pause-bar"></span>
                        <span class="player-pause-bar"></span>
                      </template>
                      <template v-else>
                        <span class="player-play-mini"></span>
                      </template>
                    </button>
                    <div class="player-volume">
                      <span class="player-volume-icon">🔊</span>
                      <input
                        class="player-volume-slider"
                        type="range"
                        min="0"
                        max="1"
                        step="0.01"
                        v-model.number="volume"
                        @input="onVolumeChange"
                      />
                    </div>
                    <button class="player-small-btn" type="button" @click="nextTrack">
                      <span class="player-icon-double-right"></span>
                    </button>
                  </div>
                </div>
              </div>

            </div>

            <!-- 隐藏音频元素 -->
            <audio
              ref="feitianAudio"
              :src="currentTrack.src"
              @timeupdate="onAudioTimeUpdate"
              @loadedmetadata="onAudioLoaded"
              @ended="onAudioEnded"
            ></audio>
          </div>
        </div>
              </div>
    </section>

    <section class="content-section section-roles">
      <div class="roles-panel">
        <div class="roles-header">
          <h2 class="roles-title">主要形象</h2>
          <div class="roles-divider"></div>
        </div>
        <div class="roles-grid">
          <div class="role-card">
            <div class="role-media">
              <img :src="assetUrl('/images/feitian/ft02.jpg')" alt="伎乐飞天" class="role-img" />
            </div>
            <div class="role-body">
              <div class="role-name">伎乐飞天</div>
              <div class="role-sub">形象关键词：乐舞、律动、飘带</div>
              <div class="role-desc">以演奏乐器、起舞腾空为特征。衣袂与飘带形成流动的线条节奏，强化了“空中乐舞”的空间感，是敦煌壁画中最具动势的飞天类型之一。</div>
              <div class="role-meta">
                <div class="role-badge">代表：乐舞场景</div>
                <div class="role-badge">风格：动感强</div>
                <div class="role-stars">★★★★★</div>
              </div>
            </div>
          </div>

          <div class="role-card reverse">
            <div class="role-media">
              <img :src="assetUrl('/images/feitian/ft03.jpg')" alt="散花飞天" class="role-img" />
            </div>
            <div class="role-body">
              <div class="role-name">散花飞天</div>
              <div class="role-sub">形象关键词：花雨、祝愿、祥瑞</div>
              <div class="role-desc">多以手持花篮或散花姿态出现，象征吉祥与礼赞。花瓣与云气相互交织，使画面更具层次与氛围，常见于庄严宏大的礼佛题材中。</div>
              <div class="role-meta">
                <div class="role-badge">代表：散花礼赞</div>
                <div class="role-badge">风格：轻盈雅致</div>
                <div class="role-stars">★★★★★</div>
              </div>
            </div>
          </div>

          <div class="role-card">
            <div class="role-media">
              <img :src="assetUrl('/images/feitian/ft04.jpg')" alt="供养飞天" class="role-img" />
            </div>
            <div class="role-body">
              <div class="role-name">供养飞天</div>
              <div class="role-sub">形象关键词：供品、恭敬、仪式</div>
              <div class="role-desc">常见于供养与礼拜场景，手捧香炉、宝盖或供品，姿态端庄含蓄。线条更趋稳定，强调礼仪的秩序感与神圣氛围。</div>
              <div class="role-meta">
                <div class="role-badge">代表：供养仪式</div>
                <div class="role-badge">风格：庄重含蓄</div>
                <div class="role-stars">★★★★☆</div>
              </div>
            </div>
          </div>

          <div class="role-card reverse">
            <div class="role-media">
              <img :src="assetUrl('/images/feitian/ft05.jpg')" alt="持莲飞天" class="role-img" />
            </div>
            <div class="role-body">
              <div class="role-name">持莲飞天</div>
              <div class="role-sub">形象关键词：莲华、清净、典雅</div>
              <div class="role-desc">以莲花为核心符号，寓意清净与觉悟。构图多采用舒展的弧线与对称的节奏，在“静”中呈现“动”，体现盛唐时期的成熟审美。</div>
              <div class="role-meta">
                <div class="role-badge">代表：莲华意象</div>
                <div class="role-badge">风格：典雅舒展</div>
                <div class="role-stars">★★★★★</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 飞天信息 -->
    <section class="content-section section-info">
      <h2 class="section-title">飞天信息</h2>
      <div class="info-cards">
        <div class="info-card">
          <div class="info-icon">📊</div>
          <div class="info-label">主要时期</div>
          <div class="info-value">5个时期</div>
        </div>
        <div class="info-card">
          <div class="info-icon">🎨</div>
          <div class="info-label">艺术风格</div>
          <div class="info-value">佛教艺术</div>
        </div>
        <div class="info-card">
          <div class="info-icon">📅</div>
          <div class="info-label">出现时间</div>
          <div class="info-value">公元4-10世纪</div>
        </div>
        <div class="info-card">
          <div class="info-icon">🏛️</div>
          <div class="info-label">主要位置</div>
          <div class="info-value">莫高窟</div>
        </div>
        <div class="info-card">
          <div class="info-icon">👥</div>
          <div class="info-label">艺术特点</div>
          <div class="info-value">飘逸动感</div>
        </div>
        <div class="info-card">
          <div class="info-icon">🌟</div>
          <div class="info-label">文化价值</div>
          <div class="info-value">世界遗产</div>
        </div>
      </div>
    </section>

    <section class="content-section section-culture">
      <h2 class="section-title">文化内涵与象征意义</h2>
      <div class="culture-list">
        <div class="culture-item">
          <div class="culture-card">
            <div class="culture-media">
              <div class="ft-hover-frame">
                <img :src="assetUrl('/images/feitian/ft14.jpg')" alt="宗教角色" class="culture-img" />
                <div class="ft-hover-caption" aria-hidden="true">
                  <div class="ft-hover-title">宗教角色</div>
                  <div class="ft-hover-desc">礼赞与供养的天人之舞</div>
                </div>
              </div>
            </div>
            <div class="culture-text">
              <h3 class="culture-title">宗教角色</h3>
              <p class="culture-desc">飞天源于佛教天人（乾闼婆、紧那罗等）的艺术转译，常出现在供养、礼赞与说法场景中。她们以乐舞与散花营造庄严氛围，象征对佛法的赞颂与对净土的向往。</p>
            </div>
          </div>
        </div>

        <div class="culture-item">
          <div class="culture-card reverse">
            <div class="culture-media">
              <div class="ft-hover-frame">
                <img :src="assetUrl('/images/feitian/ft15.jpg')" alt="哲学寓意" class="culture-img" />
                <div class="ft-hover-caption" aria-hidden="true">
                  <div class="ft-hover-title">哲学寓意</div>
                  <div class="ft-hover-desc">空灵与自由的象征表达</div>
                </div>
              </div>
            </div>
            <div class="culture-text">
              <h3 class="culture-title">哲学寓意</h3>
              <p class="culture-desc">飘带与云气的流动，暗合“无常”“空灵”的东方审美与哲思；轻盈腾跃的姿态在动静之间呈现生命的张力。飞天既是美的形象，也是对自由、超越与心灵澄明的象征表达。</p>
            </div>
          </div>
        </div>

        <div class="culture-item">
          <div class="culture-card">
            <div class="culture-media">
              <div class="ft-hover-frame">
                <img :src="assetUrl('/images/feitian/ft16.jpg')" alt="丝路见证" class="culture-img" />
                <div class="ft-hover-caption" aria-hidden="true">
                  <div class="ft-hover-title">丝路见证</div>
                  <div class="ft-hover-desc">多元文明的交汇印记</div>
                </div>
              </div>
            </div>
            <div class="culture-text">
              <h3 class="culture-title">丝路见证</h3>
              <p class="culture-desc">敦煌位于丝绸之路要冲，飞天形象吸收了中亚、印度与中原艺术语言，在千年演变中形成多元融合的视觉体系。她们见证了文明交流与审美互鉴，成为丝路文化传播的鲜明符号。</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 飞天人物/风采 -->
    <section class="content-section section-feitian-inheritors">
      <div class="inheritors-panel">
        <div class="inheritors-header">
          <div class="inheritors-line"></div>
          <h2 class="inheritors-title">艺术特色</h2>
          <div class="inheritors-line"></div>
        </div>

        <div class="inheritors-grid">
          <div class="inheritor-card">
            <div class="inheritor-avatar">
              <img :src="assetUrl('/images/feitian/ft17.jpg')" alt="形态之美" />
            </div>
            <div class="inheritor-body">
              <div class="inheritor-name">形态之美</div>
              <div class="inheritor-tag">优雅身姿，灵动飘逸</div>
              <div class="inheritor-desc">
                飞天形象体态修长，身姿曼妙，或持乐器、或散花、或供养，姿态各异。
                身体曲线流畅自然，衣袂飘动，营造出轻盈飘逸的视觉效果，展现古代艺术家对人物形态的精准把握。
              </div>
            </div>
          </div>

          <div class="inheritor-card">
            <div class="inheritor-avatar">
              <img :src="assetUrl('/images/feitian/ft18.jpg')" alt="线条之美" />
            </div>
            <div class="inheritor-body">
              <div class="inheritor-name">线条之美</div>
              <div class="inheritor-tag">流畅笔触，韵律节奏</div>
              <div class="inheritor-desc">
                飞天艺术以流畅的线条勾勒轮廓，衣带、飘带形成优美的曲线韵律。
                线条疏密有致，刚柔并济，既有力度又显柔美，体现了中国传统绘画"以线造型"的精髓。
              </div>
            </div>
          </div>

          <div class="inheritor-card">
            <div class="inheritor-avatar">
              <img :src="assetUrl('/images/feitian/ft19.jpg')" alt="色彩之美" />
            </div>
            <div class="inheritor-body">
              <div class="inheritor-name">色彩之美</div>
              <div class="inheritor-tag">丰富层次，和谐统一</div>
              <div class="inheritor-desc">
                飞天壁画色彩丰富，以石青、石绿、朱砂、金粉等矿物颜料绘制，历经千年仍鲜艳如初。
                色彩搭配和谐统一，既有对比又相互呼应，营造出庄重典雅、富丽堂皇的视觉效果。
              </div>
            </div>
          </div>

          <div class="inheritor-card">
            <div class="inheritor-avatar">
              <img :src="assetUrl('/images/feitian/ft20.jpg')" alt="意境之美" />
            </div>
            <div class="inheritor-body">
              <div class="inheritor-name">意境之美</div>
              <div class="inheritor-tag">空灵超脱，神韵悠远</div>
              <div class="inheritor-desc">
                飞天艺术追求"空灵"与"超脱"的意境，通过云气、花雨等元素营造出仙境般的氛围。
                画面虚实结合，动静相宜，传达出超越凡尘的精神追求，体现了佛教艺术的深邃内涵。
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 飞天海报 -->
    <section class="content-section section-posters">
      <h2 class="section-title">飞天海报</h2>
      <div class="posters-grid">
        <div class="poster-item">
          <div
            class="poster-image"
            @mouseenter="handlePosterMouseEnter"
            @mouseleave="handlePosterMouseLeave"
          >
            <video
              class="poster-video"
              :src="assetUrl('/video/ft1.mp4')"
              data-start="2"
              loop
              muted
              playsinline
            ></video>
          </div>
          <div class="poster-desc">
            飞天伎乐主题海报，以流动的线条与光影捕捉飞天在乐舞中的瞬间神采。
          </div>
          <button class="poster-fav-btn" type="button" @click="handleCollect">
            收藏
          </button>
        </div>
        <div class="poster-item">
          <div
            class="poster-image"
            @mouseenter="handlePosterMouseEnter"
            @mouseleave="handlePosterMouseLeave"
          >
            <video
              class="poster-video"
              :src="assetUrl('/video/ft2.mp4')"
              data-start="1"
              loop
              muted
              playsinline
            ></video>
          </div>
          <div class="poster-desc">
            壁画局部动态呈现，展现飞天与供养人同处一域的庄严而灵动的画面。
          </div>
          <button class="poster-fav-btn" type="button" @click="handleCollect">
            收藏
          </button>
        </div>
        <div class="poster-item">
          <div
            class="poster-image"
            @mouseenter="handlePosterMouseEnter"
            @mouseleave="handlePosterMouseLeave"
          >
            <video
              class="poster-video"
              :src="assetUrl('/video/ft3.mp4')"
              loop
              muted
              playsinline
            ></video>
          </div>
          <div class="poster-desc">
            飞天剪影与空间光晕交织，象征丝绸之路上多元文明交汇的辉煌记忆。
          </div>
          <button class="poster-fav-btn" type="button" @click="handleCollect">
            收藏
          </button>
        </div>
      </div>
    </section>

    <section class="content-section section-community">
      <div class="community-panel">
        <div class="community-header">
          <h2 class="community-title">超话交流社区</h2>
          <div class="community-divider"></div>
        </div>

        <div class="community-grid">
          <div class="community-left">
            <div class="community-subtitle">发表评论</div>
            <div class="community-form">
              <label class="community-label">用户名</label>
              <input class="community-input" type="text" v-model.trim="commentName" placeholder="请输入您的用户名" />

              <label class="community-label">评论内容</label>
              <textarea class="community-textarea" v-model.trim="commentContent" placeholder="请分享您的观点..." rows="6"></textarea>

              <div v-if="commentError" class="community-error">{{ commentError }}</div>

              <button class="community-submit" type="button" @click="submitComment">发表评论</button>
            </div>
          </div>

          <div class="community-right">
            <div class="community-subtitle">最新评论</div>
            <div class="community-list" ref="latestListEl">
              <div class="comment-item" :class="{ 'comment-item-fire': item.isFire }" v-for="item in comments" :key="item.id">
                <div class="comment-head">
                  <div class="comment-user">
                    <div class="comment-avatar">飞</div>
                    <div class="comment-userinfo">
                      <div class="comment-name">{{ item.name }}</div>
                      <div class="comment-time">{{ item.time }}</div>
                    </div>
                  </div>
                </div>
                <div class="comment-content">{{ item.content }}</div>
                <div class="comment-actions">
                  <button class="comment-action" :class="{ 'comment-action-fire': item.isFire }" type="button" @click="likeComment(item.id)">
                    <span class="comment-action-icon" v-if="!item.isFire">👍</span>
                    <span class="comment-action-icon-fire" v-if="item.isFire">🔥</span>
                    <span>点赞({{ item.likes }})</span>
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="contact-section">
      <div class="contact-inner">
        <router-link class="contact-title" :to="{ path: '/', hash: '#home-contact' }">联系我们</router-link>
        <div class="contact-actions">
          <a class="contact-icon-btn" href="#" aria-label="邮箱">
            <svg viewBox="0 0 24 24" class="contact-icon" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M4 7.5C4 6.67157 4.67157 6 5.5 6H18.5C19.3284 6 20 6.67157 20 7.5V16.5C20 17.3284 19.3284 18 18.5 18H5.5C4.67157 18 4 17.3284 4 16.5V7.5Z" stroke="currentColor" stroke-width="1.6" />
              <path d="M5.5 7.5L12 12.2L18.5 7.5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" />
            </svg>
          </a>
          <a class="contact-icon-btn" href="#" aria-label="微博">
            <svg viewBox="0 0 24 24" class="contact-icon" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M12 20c4.418 0 8-3.358 8-7.5S16.418 5 12 5 4 8.358 4 12.5 7.582 20 12 20Z" stroke="currentColor" stroke-width="1.6" />
              <path d="M9.2 13.2c.6 1.5 2.9 2.2 4.9 1.4 1.9-.8 2.8-2.8 2-4.2" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" />
            </svg>
          </a>
          <a class="contact-icon-btn" href="#" aria-label="抖音">
            <svg viewBox="0 0 24 24" class="contact-icon" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M13 4v9.2a3.8 3.8 0 1 1-2.6-3.6" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" />
              <path d="M13 6.2c1.1 2 2.9 3.1 5 3.2" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" />
            </svg>
          </a>
          <a class="contact-icon-btn" href="#" aria-label="站内留言">
            <svg viewBox="0 0 24 24" class="contact-icon" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M20 12c0 3.866-3.582 7-8 7a9.5 9.5 0 0 1-2.6-.36L6 20l.98-3.1C5.06 15.65 4 13.92 4 12c0-3.866 3.582-7 8-7s8 3.134 8 7Z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round" />
              <path d="M8 12h8" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" />
            </svg>
          </a>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted, nextTick } from 'vue'
import { ElNotification } from 'element-plus'
import NavBar from '../components/NavBar.vue'

const baseURL = import.meta.env.BASE_URL || '/'
const assetUrl = (path) => path.startsWith('/') ? baseURL + path.slice(1) : path

const currentCardIndex = ref(1) // 从1开始，因为0是克隆的最后一张
const isTransitioning = ref(true)

const heroSectionEl = ref(null)
const heroOverlayScrollProgress = ref(0)
let heroOverlayRaf = 0
let reduceMotionQuery = null
let reduceMotionChangeHandler = null
const heroOverlayReduceMotion = ref(false)

const heroOverlayWrapStyle = computed(() => {
  const p = heroOverlayScrollProgress.value
  const baseX = -100
  const baseY = 30
  const translateX = baseX - 320 * p
  const translateY = baseY + 260 * p
  const scale = 1 + 0.18 * p
  return {
    transform: `translate3d(${translateX}px, ${translateY}px, 0) scale(${scale})`
  }
})

// 飞天音乐播放器 - 音频控制
const feitianAudio = ref(null)
const isPlaying = ref(false)
const currentTime = ref(0)
const duration = ref(0)
const volume = ref(0.8)

const tracks = ref([
  {
    src: assetUrl('/video/千年的祈祷.mp3'),
    cover: assetUrl('/images/feitian/ft08.jpg'),
    title: '飞天 · 乐舞主题',
    subtitle: 'Dunhuang Feitian · Ethereal Soundscape'
  },
  {
    src: assetUrl('/video/yh.mp3'),
    cover: assetUrl('/images/feitian/ft22.jpg'),
    title: '飞天 · 乐舞主题',
    subtitle: '雨后的风景'
  }
])

const currentTrackIndex = ref(0)

const currentTrack = computed(() => {
  return tracks.value[currentTrackIndex.value] || tracks.value[0]
})

const commentName = ref('')
const commentContent = ref('')
const commentError = ref('')
const latestListEl = ref(null)

const COMMENTS_STORAGE_KEY = 'feitian_latest_comments'

const formatDateTime = (d) => {
  const pad = (n) => String(n).padStart(2, '0')
  const yyyy = d.getFullYear()
  const mm = pad(d.getMonth() + 1)
  const dd = pad(d.getDate())
  const hh = pad(d.getHours())
  const mi = pad(d.getMinutes())
  return `${yyyy}-${mm}-${dd} ${hh}:${mi}`
}

const comments = ref([
  {
    id: 'seed-fire',
    name: '蒸蛋',
    content: '制作不易，请给\'葱\'明伶俐小组投一票',
    time: '2026-01-15 10:00',
    likes: 9999,
    isFire: true
  },
  {
    id: 'seed-1',
    name: '飞天旅人',
    content: '飘带的线条太美了，像风在壁画里流动，越看越有层次。',
    time: '2026-01-14 21:10',
    likes: 128
  },
  {
    id: 'seed-2',
    name: '敦煌拾光',
    content: '散花飞天的意象很有仪式感，既庄严又轻盈，太喜欢这种"动静相宜"。',
    time: '2026-01-14 21:26',
    likes: 96
  },
  {
    id: 'seed-3',
    name: '丝路观者',
    content: '从北魏到盛唐的变化很明显，衣纹和配色真的体现了时代审美。',
    time: '2026-01-14 21:42',
    likes: 74
  }
])

const persistComments = () => {
  try {
    localStorage.setItem(COMMENTS_STORAGE_KEY, JSON.stringify(comments.value))
  } catch (_) {
    // ignore
  }
}

const applyTrack = async (nextIndex) => {
  const audio = feitianAudio.value
  const list = tracks.value
  if (!list.length) return

  const normalizedIndex = ((nextIndex % list.length) + list.length) % list.length
  const shouldPlay = isPlaying.value

  isPlaying.value = false
  currentTime.value = 0
  duration.value = 0
  currentTrackIndex.value = normalizedIndex

  await nextTick()
  if (!audio) return
  audio.volume = volume.value
  audio.currentTime = 0
  audio.load()

  if (shouldPlay) {
    audio.play().then(() => {
      isPlaying.value = true
    }).catch((err) => {
      console.error('音频播放失败', err)
    })
  }
}

const prevTrack = () => applyTrack(currentTrackIndex.value - 1)
const nextTrack = () => applyTrack(currentTrackIndex.value + 1)

const loadComments = () => {
  try {
    const raw = localStorage.getItem(COMMENTS_STORAGE_KEY)
    if (raw) {
      const parsed = JSON.parse(raw)
      if (Array.isArray(parsed)) {
        comments.value = parsed
      }
    }
    // 确保火焰评论始终存在且位于第一位
    const fireCommentIndex = comments.value.findIndex(c => c.id === 'seed-fire')
    const fireComment = {
      id: 'seed-fire',
      name: '蒸蛋',
      content: '制作不易，请给\'葱\'明伶俐小组投一票',
      time: '2026-01-15 10:00',
      likes: 9999,
      isFire: true
    }
    if (fireCommentIndex >= 0) {
      // 如果存在，更新点赞数确保为9999
      comments.value[fireCommentIndex] = { ...comments.value[fireCommentIndex], ...fireComment }
      // 移到第一位
      comments.value.splice(fireCommentIndex, 1)
      comments.value.unshift(fireComment)
    } else {
      // 如果不存在，添加到第一位
      comments.value.unshift(fireComment)
    }

    // 删除时间为 2026-01-15 17:59 的评论
    comments.value = comments.value.filter((c) => c.time !== '2026-01-15 17:59')

    // 覆盖本地存储，确保刷新后也不再出现
    persistComments()
  } catch (_) {
    // ignore
  }
}

const submitComment = async () => {
  commentError.value = ''
  const name = (commentName.value || '').trim()
  const content = (commentContent.value || '').trim()
  if (!name) {
    commentError.value = '请输入用户名'
    return
  }
  if (!content) {
    commentError.value = '请输入评论内容'
    return
  }

  const newItem = {
    id: `c-${Date.now()}`,
    name,
    content,
    time: formatDateTime(new Date()),
    likes: 0
  }
  comments.value = [newItem, ...comments.value]
  persistComments()
  commentContent.value = ''

  await nextTick()
  if (latestListEl.value) {
    latestListEl.value.scrollTop = 0
  }
}

const likeComment = (id) => {
  const item = comments.value.find((c) => c.id === id)
  if (!item) return
  // 火焰评论的点赞数始终保持9999
  if (item.id === 'seed-fire') {
    item.likes = 9999
  } else {
    item.likes += 1
  }
  persistComments()
}

const formatTime = (sec) => {
  if (!sec || Number.isNaN(sec)) return '0:00'
  const s = Math.floor(sec)
  const m = Math.floor(s / 60)
  const rest = s % 60
  return `${m}:${rest.toString().padStart(2, '0')}`
}

const formattedCurrentTime = computed(() => formatTime(currentTime.value))
const formattedDuration = computed(() => formatTime(duration.value))

const progressPercent = computed(() => {
  if (!duration.value || duration.value === 0) return 0
  return Math.min(100, Math.max(0, (currentTime.value / duration.value) * 100))
})

const togglePlay = () => {
  const audio = feitianAudio.value
  if (!audio) return

  if (isPlaying.value) {
    audio.pause()
    isPlaying.value = false
  } else {
    audio.play().then(() => {
      audio.volume = volume.value
      isPlaying.value = true
    }).catch((err) => {
      console.error('音频播放失败', err)
    })
  }
}

const onAudioLoaded = () => {
  const audio = feitianAudio.value
  if (audio) {
    duration.value = audio.duration || 0
  }
}

const onAudioTimeUpdate = () => {
  const audio = feitianAudio.value
  if (audio) {
    currentTime.value = audio.currentTime || 0
    if (!duration.value && audio.duration) {
      duration.value = audio.duration
    }
  }
}

const onAudioEnded = () => {
  isPlaying.value = false
  currentTime.value = 0
}

const onVolumeChange = () => {
  const audio = feitianAudio.value
  if (audio) {
    audio.volume = volume.value
  }
}

const handleCollect = () => {
  ElNotification({
    title: '提示',
    message: '收藏成功',
    type: 'success',
    position: 'top-right',
    duration: 2000,
    showClose: false
  })
}

const carouselItems = ref([
  {
    location: '北凉时期',
    title: '早期飞天形象',
    image: assetUrl('/images/feitian/ft09.jpg')
  },
  {
    location: '北魏时期',
    title: '过渡期飞天',
    image: assetUrl('/images/feitian/ft10.jpg')
  },
  {
    location: '隋代时期',
    title: '成熟期飞天',
    image: assetUrl('/images/feitian/ft11.jpg')
  },
  {
    location: '唐代时期',
    title: '巅峰期飞天',
    image: assetUrl('/images/feitian/ft12.jpg')
  },
  {
    location: '五代时期',
    title: '延续发展',
    image: assetUrl('/images/feitian/ft13.jpg')
  }
])

// 创建包含克隆项的完整数组（最后一张 + 原数组 + 第一张）
const cardsWithClones = computed(() => {
  const lastItem = { ...carouselItems.value[carouselItems.value.length - 1] }
  const firstItem = { ...carouselItems.value[0] }
  return [lastItem, ...carouselItems.value, firstItem]
})

const handleImageError = (event) => {
  console.error('图片加载失败:', event.target.src)
  // 可以设置一个默认图片或隐藏图片
  event.target.style.display = 'none'
}

const prevCard = () => {
  currentCardIndex.value--
  // 如果到了克隆的最后一张（索引0），继续往左，会在transitionEnd中处理跳转
}

const nextCard = () => {
  currentCardIndex.value++
  // 如果到了克隆的第一张（索引6），继续往右，会在transitionEnd中处理跳转
}

// 处理过渡结束事件
const handleTransitionEnd = (event) => {
  // 只处理卡片的transform过渡结束事件
  if (event.target.classList.contains('carousel-card') && event.propertyName === 'transform') {
    const totalItems = carouselItems.value.length // 5
    const totalWithClones = cardsWithClones.value.length // 7
    
    if (currentCardIndex.value === 0) {
      // 到达克隆的最后一张（索引0，实际是第5张），跳转到真正的最后一张（索引5）
      isTransitioning.value = false
      setTimeout(() => {
        currentCardIndex.value = totalItems
        setTimeout(() => {
          isTransitioning.value = true
        }, 50)
      }, 50)
    } else if (currentCardIndex.value === totalWithClones - 1) {
      // 到达克隆的第一张（索引6，实际是第1张），跳转到真正的第一张（索引1）
      isTransitioning.value = false
      setTimeout(() => {
        currentCardIndex.value = 1
        setTimeout(() => {
          isTransitioning.value = true
        }, 50)
      }, 50)
    }
  }
}

// 判断卡片是否应该显示
const isCardVisible = (index) => {
  const distance = Math.abs(index - currentCardIndex.value)
  // 如果距离太远，隐藏
  if (distance > 2) return false
  // 如果是边界克隆项且不在边界状态，隐藏
  if (index === 0 && currentCardIndex.value !== 0 && currentCardIndex.value !== cardsWithClones.value.length - 1) {
    return false
  }
  if (index === cardsWithClones.value.length - 1 && currentCardIndex.value !== 0 && currentCardIndex.value !== cardsWithClones.value.length - 1) {
    return false
  }
  return true
}

// 计算当前显示的索引（用于页码显示，显示1-5）
const displayIndex = computed(() => {
  // cardsWithClones 结构: [克隆最后一张(索引0), 原数组1(索引1), 2(索引2), 3(索引3), 4(索引4), 5(索引5), 克隆第一张(索引6)]
  if (currentCardIndex.value === 0) {
    // 显示克隆的最后一张，实际应该是5
    return carouselItems.value.length
  } else if (currentCardIndex.value === cardsWithClones.value.length - 1) {
    // 显示克隆的第一张，实际应该是1
    return 1
  } else {
    // 显示原数组的索引（1-5）
    return currentCardIndex.value
  }
})

// 飞天海报视频 - 悬停播放控制
const handlePosterMouseEnter = (event) => {
  const container = event.currentTarget
  if (!container) return
  const video = container.querySelector('video')
  if (video) {
    video.muted = true
    const startAttr = video.getAttribute('data-start')
    const startTime = startAttr ? Number(startAttr) || 0 : 0
    try {
      video.currentTime = startTime
    } catch (e) {
      // 某些浏览器可能限制设置 currentTime，忽略即可
    }
    video.play().catch(() => {
      // 自动播放被浏览器拦截时忽略错误
    })
  }
}

const handlePosterMouseLeave = (event) => {
  const container = event.currentTarget
  if (!container) return
  const video = container.querySelector('video')
  if (video) {
    video.pause()
    try {
      video.currentTime = 0
    } catch (e) {
      // 忽略 currentTime 设置错误
    }
  }
}

const currentSection = ref(0) // 0: 首页, 1: 简介, 2: 信息, 3: 海报

const prevMainContent = () => {
  if (currentSection.value > 0) {
    currentSection.value--
    scrollToSection(currentSection.value)
  }
}

const nextMainContent = () => {
  const maxIndex = getMaxSectionIndex()
  if (currentSection.value < maxIndex) {
    currentSection.value++
    scrollToSection(currentSection.value)
  }
}

let scrollContainerEl = null

const getMaxSectionIndex = () => {
  const sections = document.querySelectorAll('.content-section')
  return Math.max(0, sections.length - 1)
}

const findScrollableParent = (el) => {
  let current = el
  while (current && current !== document.body) {
    const style = window.getComputedStyle(current)
    const overflowY = style.overflowY
    const canScroll = (overflowY === 'auto' || overflowY === 'scroll' || overflowY === 'overlay') && current.scrollHeight > current.clientHeight
    if (canScroll) return current
    current = current.parentElement
  }
  return document.scrollingElement || document.documentElement
}

const resolveScrollContainer = () => {
  const root = document.querySelector('.feitian-page')
  if (root) return findScrollableParent(root)
  return document.scrollingElement || document.documentElement
}

const withScrollSnapDisabled = (container, fn) => {
  if (!container || container === document.scrollingElement || container === document.documentElement || container === document.body) {
    fn()
    return
  }

  const original = container.style.scrollSnapType
  container.style.scrollSnapType = 'none'
  fn()
  setTimeout(() => {
    container.style.scrollSnapType = original
  }, 700)
}

const scrollToElement = (el) => {
  if (!el) return
  const container = resolveScrollContainer()
  const offsetTop = 55

  withScrollSnapDisabled(container, () => {
    if (container === document.scrollingElement || container === document.documentElement || container === document.body) {
      const top = el.getBoundingClientRect().top + window.scrollY - offsetTop
      window.scrollTo({ top, behavior: 'smooth' })
      return
    }

    const elRect = el.getBoundingClientRect()
    const containerRect = container.getBoundingClientRect()
    const top = container.scrollTop + (elRect.top - containerRect.top) - offsetTop
    container.scrollTo({ top, behavior: 'smooth' })
  })
}

const scrollToNextSection = async () => {
  await nextTick()
  requestAnimationFrame(() => {
    requestAnimationFrame(() => {
      const targetSection = document.getElementById('feitian-intro')
      if (targetSection) {
        currentSection.value = 1
        scrollToElement(targetSection)
      }
    })
  })
}

const scrollToSection = (index) => {
  nextTick(() => {
    const sections = document.querySelectorAll('.content-section')
    if (sections[index]) {
      scrollToElement(sections[index])
    }
  })
}

// 监听滚动，更新当前区块
let scrollHandler = null

const updateHeroOverlayProgress = () => {
  const container = scrollContainerEl || resolveScrollContainer()
  const heroHeight = heroSectionEl.value?.offsetHeight || window.innerHeight
  const scrollTop = container === document.scrollingElement || container === document.documentElement || container === document.body
    ? (window.scrollY || window.pageYOffset || 0)
    : (container?.scrollTop || 0)

  const p = heroHeight > 0 ? Math.min(Math.max(scrollTop / heroHeight, 0), 1) : 0
  heroOverlayScrollProgress.value = p
}

const scheduleHeroOverlayUpdate = () => {
  if (heroOverlayReduceMotion.value) return
  if (heroOverlayRaf) return
  heroOverlayRaf = requestAnimationFrame(() => {
    heroOverlayRaf = 0
    updateHeroOverlayProgress()
  })
}

onMounted(() => {
  loadComments()

  reduceMotionQuery = window.matchMedia?.('(prefers-reduced-motion: reduce)') || null
  heroOverlayReduceMotion.value = !!reduceMotionQuery?.matches
  if (reduceMotionQuery) {
    reduceMotionChangeHandler = (e) => {
      heroOverlayReduceMotion.value = !!e.matches
      if (heroOverlayReduceMotion.value) {
        heroOverlayScrollProgress.value = 0
      } else {
        scheduleHeroOverlayUpdate()
      }
    }
    if (typeof reduceMotionQuery.addEventListener === 'function') {
      reduceMotionQuery.addEventListener('change', reduceMotionChangeHandler)
    } else if (typeof reduceMotionQuery.addListener === 'function') {
      reduceMotionQuery.addListener(reduceMotionChangeHandler)
    }
  }

  scheduleHeroOverlayUpdate()

  // 确保轮播图初始状态正确
  if (currentCardIndex.value === 1) {
    isTransitioning.value = true
  }
  
  scrollContainerEl = resolveScrollContainer()

  scrollHandler = () => {
    const sections = document.querySelectorAll('.content-section')
    const container = scrollContainerEl || resolveScrollContainer()
    const viewHeight = container === document.scrollingElement || container === document.documentElement || container === document.body
      ? window.innerHeight
      : container.clientHeight

    scheduleHeroOverlayUpdate()
    
    sections.forEach((section, index) => {
      const rect = section.getBoundingClientRect()
      if (rect.top <= viewHeight / 2 && rect.bottom >= viewHeight / 2) {
        currentSection.value = index
      }
    })
  }

  if (scrollContainerEl === document.scrollingElement || scrollContainerEl === document.documentElement || scrollContainerEl === document.body) {
    window.addEventListener('scroll', scrollHandler)
  } else {
    scrollContainerEl.addEventListener('scroll', scrollHandler)
  }
})

onUnmounted(() => {
  if (heroOverlayRaf) {
    cancelAnimationFrame(heroOverlayRaf)
    heroOverlayRaf = 0
  }

  if (reduceMotionQuery && reduceMotionChangeHandler) {
    if (typeof reduceMotionQuery.removeEventListener === 'function') {
      reduceMotionQuery.removeEventListener('change', reduceMotionChangeHandler)
    } else if (typeof reduceMotionQuery.removeListener === 'function') {
      reduceMotionQuery.removeListener(reduceMotionChangeHandler)
    }
  }

  if (scrollHandler) {
    if (scrollContainerEl === document.scrollingElement || scrollContainerEl === document.documentElement || scrollContainerEl === document.body) {
      window.removeEventListener('scroll', scrollHandler)
    } else if (scrollContainerEl) {
      scrollContainerEl.removeEventListener('scroll', scrollHandler)
    }
  }
})
</script>

<style scoped>
.feitian-page {
  min-height: 100vh;
  padding-top: 55px;
  position: relative;
  overflow-x: hidden;
}

/* 首页区域 */
.hero-section {
  position: relative;
  width: 100%;
  min-height: 100vh;
  padding-top: 0;
  overflow: hidden;
}

/* 全屏背景图 */
.hero-section .hero-background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 0;
}

.background-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.hero-overlay-wrap {
  position: absolute;
  inset: 0;
  z-index: 5;
  pointer-events: none;
}

.hero-overlay-float {
  position: absolute;
  inset: 0;
  transform-origin: 80% 70%;
  animation: heroOverlayFloat 5.2s ease-in-out infinite;
  will-change: transform;
}

.hero-overlay-image {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: contain;
  object-position: right bottom;
  display: block;
}

.hero-overlay-watermark-cover {
  position: absolute;
  right: 18px;
  bottom: 18px;
  width: 190px;
  height: 58px;
  background: rgba(0, 0, 0, 0.65);
  border-radius: 10px;
}

@keyframes heroOverlayFloat {
  0% {
    transform: translate3d(0, 0, 0) rotate(-1.2deg);
  }
  25% {
    transform: translate3d(10px, -18px, 0) rotate(1.6deg);
  }
  50% {
    transform: translate3d(-8px, -10px, 0) rotate(-1.0deg);
  }
  75% {
    transform: translate3d(12px, -26px, 0) rotate(1.2deg);
  }
  100% {
    transform: translate3d(0, 0, 0) rotate(-1.2deg);
  }
}

@media (prefers-reduced-motion: reduce) {
  .hero-overlay-float {
    animation: none;
  }
}

/* 主要内容区域 - 左上角 */
.hero-section .main-content {
  position: absolute;
  top: 50%;
  left: 80px;
  transform: translateY(-50%);
  max-width: 450px;
  padding-right: 40px;
  z-index: 10;
  color: white;
}

.location-tag {
  font-size: 14px;
  color: rgba(255, 255, 255, 0.9);
  margin-bottom: 20px;
  letter-spacing: 2px;
}

.main-title {
  font-family: var(--font-title);
  font-size: 72px;
  font-weight: bold;
  color: white;
  margin-bottom: 30px;
  letter-spacing: 4px;
  text-shadow: 2px 2px 10px rgba(0, 0, 0, 0.3);
}

.main-description {
  font-size: 16px;
  line-height: 1.8;
  color: rgba(255, 255, 255, 0.95);
  margin-bottom: 40px;
  text-shadow: 1px 1px 5px rgba(0, 0, 0, 0.3);
}

.discover-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
  padding: 20px 40px;
  background: rgba(255, 255, 255, 0.1);
  border: 2px solid rgba(255, 255, 255, 0.5);
  border-radius: 30px;
  color: white;
  font-size: 22px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  letter-spacing: 2px;
  position: relative;
  overflow: hidden;
  animation: pulse 2s infinite;
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
}

.discover-btn::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  width: 0;
  height: 0;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.2);
  transform: translate(-50%, -50%);
  transition: width 0.6s, height 0.6s;
}

.discover-btn:hover::before {
  width: 300px;
  height: 300px;
}

.discover-btn:hover {
  background: rgba(255, 255, 255, 0.2);
  backdrop-filter: blur(15px);
  -webkit-backdrop-filter: blur(15px);
  transform: translateY(-3px) scale(1.05);
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
  border-color: rgba(255, 255, 255, 0.8);
}

.discover-btn:hover span {
  color: #D4AF37;
  text-shadow: 0 0 10px rgba(212, 175, 55, 0.5);
}

.discover-btn:active {
  transform: translateY(-1px) scale(1.02);
}

@keyframes pulse {
  0%, 100% {
    box-shadow: 0 0 0 0 rgba(255, 255, 255, 0.4);
  }
  50% {
    box-shadow: 0 0 0 10px rgba(255, 255, 255, 0);
  }
}

.main-nav-arrow {
  position: fixed;
  top: 50%;
  transform: translateY(-50%);
  width: 60px;
  height: 60px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.2);
  border: 1px solid rgba(255, 255, 255, 0.3);
  color: white;
  font-size: 32px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  transition: all 0.3s ease;
  backdrop-filter: blur(10px);
}

.main-nav-arrow:hover {
  background: rgba(255, 255, 255, 0.3);
  transform: translateY(-50%) scale(1.1);
}

.main-nav-prev {
  left: 20px;
}

.main-nav-next {
  right: 20px;
}

/* 卡片轮播 - 右下角 */
.hero-section .cards-carousel {
  position: absolute;
  bottom: 60px;
  right: 80px;
  z-index: 100;
}

.cards-container {
  position: relative;
  width: 1400px;
  height: 400px;
  margin-bottom: 30px;
  overflow: hidden;
}

.carousel-card {
  position: absolute;
  width: 260px;
  height: 380px;
  background: rgba(255, 255, 255, 0.95);
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.3);
  transition: box-shadow 0.3s ease;
  cursor: pointer;
  right: 0;
  top: 0;
  will-change: transform, opacity;
  backface-visibility: hidden;
}

.carousel-card:hover {
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.4);
  z-index: 100 !important;
}

.card-image {
  width: 100%;
  height: 280px;
  background: linear-gradient(135deg, rgba(139, 111, 71, 0.2), rgba(212, 175, 55, 0.2));
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.card-image-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.card-content {
  padding: 20px;
  background: white;
}

.card-location {
  font-size: 12px;
  color: var(--dunhuang-medium-gray);
  margin-bottom: 8px;
  letter-spacing: 1px;
}

.card-title {
  font-family: var(--font-title);
  font-size: 18px;
  font-weight: 600;
  color: var(--dunhuang-wall-brown);
  letter-spacing: 1px;
}

/* 轮播控制 */
.carousel-controls {
  display: flex;
  align-items: center;
  gap: 20px;
  justify-content: flex-end;
}

.carousel-nav-btn {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.2);
  border: 1px solid rgba(255, 255, 255, 0.3);
  color: white;
  font-size: 28px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
  backdrop-filter: blur(10px);
}

.carousel-nav-btn:hover {
  background: rgba(255, 255, 255, 0.3);
  transform: scale(1.1);
}

.carousel-page {
  font-size: 18px;
  color: white;
  font-weight: 600;
  letter-spacing: 2px;
  min-width: 40px;
}

@media (max-width: 1200px) {
  .hero-section .main-content {
    left: 40px;
    max-width: 400px;
    padding-right: 30px;
  }
  
  .main-title {
    font-size: 56px;
  }
  
  .hero-section .cards-carousel {
    right: 40px;
    bottom: 40px;
  }
  
  .cards-container {
    width: 1000px;
  }
}

@media (max-width: 768px) {
  .hero-section .main-content {
    left: 20px;
    max-width: calc(100% - 40px);
    padding-right: 20px;
  }
  
  .main-title {
    font-size: 42px;
  }
  
  .hero-section .cards-carousel {
    right: 20px;
    bottom: 20px;
  }
  
  .cards-container {
    width: 600px;
  }
  
  .carousel-card {
    width: 220px;
    height: 320px;
  }
  
  .card-image {
    height: 220px;
  }
  
  .main-nav-arrow {
    width: 50px;
    height: 50px;
    font-size: 28px;
  }
  
  .main-nav-prev {
    left: 10px;
  }
  
  .main-nav-next {
    right: 10px;
  }
}

/* 内容区块 - 拼接式布局 */
.content-section {
  width: 100%;
  min-height: 100vh;
  padding: 100px 60px;
  background: #2a1f15;
  position: relative;
  z-index: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  scroll-snap-align: start;
}

.feitian-page {
  scroll-snap-type: y mandatory;
}

.section-title {
  font-size: 48px;
  font-weight: bold;
  color: white;
  text-align: center;
  margin-bottom: 60px;
  letter-spacing: 4px;
  position: relative;
}

.section-title::after {
  content: '';
  position: absolute;
  bottom: -15px;
  left: 50%;
  transform: translateX(-50%);
  width: 80px;
  height: 3px;
  background: linear-gradient(90deg, transparent, rgba(212, 175, 55, 0.8), transparent);
}

/* 飞天简介区块 */
.section-intro {
  background: #2a1f15;
  min-height: 100vh;
  padding: 50px 60px;
}

.section-intro .section-title {
  margin-bottom: 40px;
}

.intro-content {
  max-width: 1400px;
  width: 100%;
  display: flex;
  gap: 40px;
  align-items: flex-start;
}

.intro-image {
  flex-shrink: 0;
  width: 450px;
  position: relative;
}

.intro-image-swap {
  position: relative;
  width: 100%;
  height: 560px;
  border-radius: 15px;
  overflow: hidden;
  box-shadow: 0 15px 35px rgba(0, 0, 0, 0.3);
}

.intro-image-img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  background: rgba(0, 0, 0, 0.25);
}

.intro-image-img-base {
  opacity: 1;
}

.intro-image-img-hover {
  opacity: 0;
}

@media (hover: hover) and (pointer: fine) {
  .intro-image-img {
    transition: opacity 1.6s ease;
  }

  .intro-image-swap:hover .intro-image-img-base {
    opacity: 0;
  }

  .intro-image-swap:hover .intro-image-img-hover {
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .intro-image-img {
    transition: none;
  }

  .intro-image-swap:hover .intro-image-img-base {
    opacity: 1;
  }

  .intro-image-swap:hover .intro-image-img-hover {
    opacity: 0;
  }
}

.intro-image .image-placeholder {
  width: 100%;
  height: 560px;
  background: linear-gradient(135deg, rgba(139, 111, 71, 0.2), rgba(212, 175, 55, 0.2));
  border: 1px solid rgba(212, 175, 55, 0.3);
  display: flex;
  align-items: center;
  justify-content: center;
  color: rgba(255, 255, 255, 0.5);
  font-size: 14px;
}

.intro-image .image-title {
  position: absolute;
  left: 20px;
  top: 50%;
  transform: translateY(-50%);
  writing-mode: vertical-rl;
  font-size: 56px;
  font-weight: bold;
  color: white;
  letter-spacing: 12px;
  text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.5);
}

.intro-text {
  flex: 1;
  color: rgba(255, 255, 255, 0.9);
  line-height: 2;
  font-size: 18px;
}

.intro-text-title {
  font-size: 32px;
  font-weight: bold;
  color: white;
  margin-bottom: 20px;
  letter-spacing: 2px;
}

.intro-text p {
  margin-bottom: 16px;
  text-align: justify;
}

/* 飞天简介 - 音乐播放器 */
.feitian-player {
  margin-top: 30px;
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.player-card {
  position: relative;
  display: flex;
  align-items: center;
  gap: 28px;
  background: rgba(32, 24, 18, 0.95);
  border-radius: 22px;
  padding: 20px 24px;
  box-shadow: 0 14px 36px rgba(0, 0, 0, 0.55);
  border: 1px solid rgba(212, 175, 55, 0.32);
  backdrop-filter: blur(16px);
}

.player-cover-card {
  position: relative;
  padding: 20px;
  border-radius: 24px;
  background: rgba(42, 31, 21, 0.85);
  border: 1px solid rgba(212, 175, 55, 0.3);
  box-shadow: 0 14px 40px rgba(0, 0, 0, 0.4);
}

.player-cover-square {
  width: 200px;
  height: 200px;
  border-radius: 22px;
  background: rgba(32, 24, 18, 0.95);
  border: 1px solid rgba(212, 175, 55, 0.25);
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 10px 26px rgba(0, 0, 0, 0.3);
}

.player-cover-circle {
  width: 170px;
  height: 170px;
  border-radius: 50%;
  background: radial-gradient(circle at 30% 30%, rgba(212, 175, 55, 0.3), rgba(42, 31, 21, 0.9));
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  position: relative;
}

.player-cover-inner {
  width: 38px;
  height: 38px;
  border-radius: 50%;
  background: rgba(32, 24, 18, 0.95);
  box-shadow: 0 0 0 10px rgba(32, 24, 18, 0.9);
}

.player-cover-img {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  object-fit: cover;
  display: block;
}

.player-cover-circle.is-rotating {
  animation: feitian-disc-rotate 14s linear infinite;
}

@keyframes feitian-disc-rotate {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

.player-main-panel {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 16px;
  padding-right: 24px;
}

.player-text-block {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.player-title {
  font-size: 20px;
  font-weight: 700;
  color: rgba(255, 255, 255, 0.96);
  letter-spacing: 1px;
}

.player-sub {
  font-size: 14px;
  color: rgba(212, 175, 55, 0.9);
}

.player-progress-row {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.player-progress-track {
  width: 100%;
  height: 10px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.14);
  overflow: hidden;
}

.player-progress-fill {
  width: 55%;
  height: 100%;
  background: linear-gradient(90deg, #1db9a8, #46d0c0);
  border-radius: 999px;
}

.player-time-row {
  display: flex;
  justify-content: space-between;
  font-size: 12px;
  color: rgba(255, 255, 255, 0.7);
}

.player-play-float {
  position: absolute;
  left: 50%;
  bottom: -32px;
  transform: translateX(-50%);
  width: 72px;
  height: 72px;
  border-radius: 50%;
  border: none;
  background: #ffffff;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.55);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.player-play-float:hover {
  transform: translateX(-50%) scale(1.06);
  box-shadow: 0 20px 52px rgba(0, 0, 0, 0.65);
}

.player-play-triangle {
  width: 0;
  height: 0;
  border-top: 13px solid transparent;
  border-bottom: 13px solid transparent;
  border-left: 22px solid #1aa796;
  margin-left: 4px;
}

.player-bottom-bar {
  margin-top: 14px;
}

.player-bottom-inner {
  max-width: 380px;
  margin: 0 auto;
  background: #faf7f3;
  border-radius: 22px;
  padding: 10px 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  box-shadow: 0 14px 40px rgba(0, 0, 0, 0.3);
}

.player-small-btn {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  border: none;
  background: transparent;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: transform 0.2s ease, background 0.2s ease;
}

.player-small-btn:hover {
  transform: scale(1.08);
  background: rgba(0, 0, 0, 0.04);
}

.player-icon-double-left,
.player-icon-double-right {
  position: relative;
  width: 0;
  height: 0;
  border-top: 8px solid transparent;
  border-bottom: 8px solid transparent;
}

.player-icon-double-left {
  border-right: 12px solid #1db9a8;
}

.player-icon-double-left::after {
  content: '';
  position: absolute;
  right: 10px;
  top: -8px;
  border-top: 8px solid transparent;
  border-bottom: 8px solid transparent;
  border-right: 12px solid #1db9a8;
}

.player-icon-double-right {
  border-left: 12px solid #1db9a8;
}

.player-icon-double-right::after {
  content: '';
  position: absolute;
  left: 10px;
  top: -8px;
  border-top: 8px solid transparent;
  border-bottom: 8px solid transparent;
  border-left: 12px solid #1db9a8;
}

.player-pause-block {
  width: 82px;
  height: 52px;
  border-radius: 18px;
  border: none;
  background: #b8e3da;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  cursor: pointer;
  box-shadow: 0 12px 34px rgba(0, 0, 0, 0.35);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.player-pause-block:hover {
  transform: translateY(-2px);
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.45);
}

.player-pause-bar {
  width: 8px;
  height: 24px;
  border-radius: 4px;
  background: #ffffff;
}

.player-volume {
  display: flex;
  align-items: center;
  gap: 6px;
  margin: 0 8px;
}

.player-volume-icon {
  font-size: 14px;
}

.player-volume-slider {
  width: 80px;
  accent-color: #1db9a8;
}

.player-play-mini {
  width: 0;
  height: 0;
  border-top: 10px solid transparent;
  border-bottom: 10px solid transparent;
  border-left: 16px solid #1aa796;
  margin-left: 2px;
}

/* 飞天信息区块 */
.section-info {
  background: #1f1812;
}

.section-culture {
  background: radial-gradient(1200px 600px at 30% 10%, rgba(212, 175, 55, 0.14), transparent 60%),
    linear-gradient(180deg, #1f1812 0%, #2a1f15 100%);
  padding: 50px 60px;
  min-height: 100vh;
  justify-content: flex-start;
}

.section-culture .section-title {
  color: rgba(255, 255, 255, 0.95);
}

.section-culture .section-title::after {
  background: linear-gradient(90deg, transparent, rgba(212, 175, 55, 0.7), transparent);
}

.culture-list {
  width: 100%;
  max-width: 1200px;
  display: flex;
  flex-direction: column;
  gap: 34px;
}

.culture-item {
  width: 100%;
  background: rgba(255, 255, 255, 0.04);
  padding: 22px 0;
  display: flex;
  justify-content: center;
}

.culture-card {
  width: 100%;
  max-width: 980px;
  background: rgba(42, 31, 21, 0.88);
  border: 1px solid rgba(212, 175, 55, 0.22);
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.45);
  display: flex;
  gap: 20px;
  padding: 20px;
}

.culture-card.reverse {
  flex-direction: row-reverse;
}

.culture-media {
  flex-shrink: 0;
  width: 320px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.ft-hover-frame {
  width: 100%;
  height: 180px;
  position: relative;
  overflow: hidden;
  border: 6px solid rgba(212, 175, 55, 0.22);
  box-shadow: 0 10px 22px rgba(0, 0, 0, 0.45);
}

.culture-img {
  width: 100%;
  height: 180px;
  object-fit: cover;
  display: block;
  transform: translate3d(0, 0, 0);
}

.ft-hover-caption {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  padding: 16px 14px 14px;
  background: rgba(0, 0, 0, 0.82);
  opacity: 0;
  transform: translate3d(0, 100%, 0);
  transition: transform 0.35s ease, opacity 0.35s ease;
  text-align: center;
  pointer-events: none;
}

.ft-hover-title {
  font-size: 26px;
  font-weight: 800;
  letter-spacing: 4px;
  color: rgba(255, 255, 255, 0.96);
  line-height: 1.2;
  margin-bottom: 6px;
}

.ft-hover-desc {
  font-size: 15px;
  letter-spacing: 2px;
  color: rgba(255, 255, 255, 0.86);
}

@media (hover: hover) and (pointer: fine) {
  .ft-hover-frame .culture-img {
    transition: transform 0.5s ease;
    will-change: transform;
  }

  .ft-hover-frame:hover .culture-img {
    transform: translate3d(0, -14px, 0);
  }

  .ft-hover-frame:hover .ft-hover-caption {
    opacity: 1;
    transform: translate3d(0, 0, 0);
  }
}

@media (prefers-reduced-motion: reduce) {
  .ft-hover-frame .culture-img,
  .ft-hover-caption {
    transition: none;
  }

  .ft-hover-frame:hover .culture-img {
    transform: none;
  }
}

.culture-text {
  flex: 1;
  padding: 4px 6px;
  color: rgba(255, 255, 255, 0.9);
}

.culture-title {
  margin: 0 0 10px;
  font-size: 24px;
  letter-spacing: 2px;
  color: rgba(212, 175, 55, 0.95);
}

.culture-desc {
  margin: 0;
  font-size: 17px;
  line-height: 2;
  color: rgba(255, 255, 255, 0.78);
}

.info-cards {
  max-width: 1400px;
  width: 100%;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 40px;
}

.info-card {
  background: rgba(42, 31, 21, 0.8);
  border: 1px solid rgba(212, 175, 55, 0.3);
  border-radius: 12px;
  padding: 40px 30px;
  text-align: center;
  transition: all 0.3s ease;
  backdrop-filter: blur(10px);
}

.info-card:hover {
  border-color: rgba(212, 175, 55, 0.6);
  transform: translateY(-8px);
  box-shadow: 0 8px 24px rgba(212, 175, 55, 0.2);
}

.info-icon {
  font-size: 48px;
  margin-bottom: 20px;
  filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.3));
}

.info-label {
  font-size: 16px;
  color: rgba(255, 255, 255, 0.7);
  margin-bottom: 15px;
  letter-spacing: 1px;
}

.info-value {
  font-size: 22px;
  font-weight: 600;
  color: rgba(212, 175, 55, 0.95);
  letter-spacing: 1px;
}

/* 飞天海报区块 */
.section-posters {
  background: #2a1f15;
  min-height: 100vh;
  padding: 50px 60px;
}

.section-community {
  background: radial-gradient(900px 520px at 50% 0%, rgba(212, 175, 55, 0.12), transparent 60%),
    linear-gradient(180deg, #1f1812 0%, #2a1f15 100%);
  padding: 50px 60px;
  min-height: 100vh;
  justify-content: center;
}

.community-panel {
  width: 100%;
  max-width: 1400px;
  background: rgba(20, 14, 10, 0.55);
  border: 1px solid rgba(212, 175, 55, 0.22);
  border-radius: 14px;
  box-shadow: 0 14px 46px rgba(0, 0, 0, 0.55);
  padding: 22px 22px 26px;
  backdrop-filter: blur(10px);
}

.community-header {
  text-align: center;
  margin-bottom: 18px;
}

.community-title {
  margin: 0;
  font-size: 30px;
  letter-spacing: 8px;
  color: rgba(212, 175, 55, 0.95);
}

.community-divider {
  height: 1px;
  margin-top: 14px;
  background: linear-gradient(90deg, transparent, rgba(212, 175, 55, 0.6), transparent);
}

.community-grid {
  display: grid;
  grid-template-columns: 1fr 1.6fr;
  gap: 18px;
}

.community-left,
.community-right {
  background: rgba(42, 31, 21, 0.72);
  border: 1px solid rgba(212, 175, 55, 0.18);
  border-radius: 12px;
  padding: 16px;
}

.community-subtitle {
  font-size: 18px;
  color: rgba(212, 175, 55, 0.92);
  letter-spacing: 2px;
  padding-bottom: 10px;
  border-bottom: 1px solid rgba(212, 175, 55, 0.18);
  margin-bottom: 14px;
}

.community-form {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.community-label {
  font-size: 15px;
  color: rgba(255, 255, 255, 0.7);
}

.community-input,
.community-textarea {
  width: 100%;
  background: rgba(0, 0, 0, 0.25);
  border: 1px solid rgba(212, 175, 55, 0.22);
  border-radius: 8px;
  padding: 10px 12px;
  color: rgba(255, 255, 255, 0.9);
  outline: none;
  font-size: 15px;
}

.community-textarea {
  resize: none;
}

.community-input:focus,
.community-textarea:focus {
  border-color: rgba(212, 175, 55, 0.6);
  box-shadow: 0 0 0 3px rgba(212, 175, 55, 0.12);
}

.community-error {
  font-size: 14px;
  color: rgba(255, 147, 147, 0.9);
}

.community-submit {
  margin-top: 6px;
  width: 100%;
  height: 42px;
  border-radius: 999px;
  border: 1px solid rgba(212, 175, 55, 0.28);
  background: linear-gradient(90deg, rgba(212, 175, 55, 0.28), rgba(212, 175, 55, 0.12));
  color: rgba(255, 255, 255, 0.92);
  font-weight: 600;
  letter-spacing: 2px;
  cursor: pointer;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.community-submit:hover {
  transform: translateY(-1px);
  box-shadow: 0 12px 28px rgba(0, 0, 0, 0.45);
}

.community-list {
  height: 360px;
  overflow: auto;
  padding-right: 8px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.community-list::-webkit-scrollbar {
  width: 8px;
}

.community-list::-webkit-scrollbar-thumb {
  background: rgba(212, 175, 55, 0.22);
  border-radius: 999px;
}

.community-list::-webkit-scrollbar-track {
  background: rgba(255, 255, 255, 0.06);
  border-radius: 999px;
}

.comment-item {
  background: rgba(20, 14, 10, 0.55);
  border: 1px solid rgba(212, 175, 55, 0.16);
  border-radius: 12px;
  padding: 12px 14px;
}

.comment-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 8px;
}

.comment-user {
  display: flex;
  align-items: center;
  gap: 10px;
}

.comment-avatar {
  width: 36px;
  height: 36px;
  border-radius: 999px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(212, 175, 55, 0.18);
  border: 1px solid rgba(212, 175, 55, 0.25);
  color: rgba(212, 175, 55, 0.95);
  font-weight: 700;
}

.comment-name {
  font-size: 16px;
  color: rgba(255, 255, 255, 0.92);
  font-weight: 600;
}

.comment-time {
  font-size: 13px;
  color: rgba(255, 255, 255, 0.55);
  margin-top: 2px;
}

.comment-content {
  font-size: 16px;
  line-height: 1.9;
  color: rgba(255, 255, 255, 0.78);
}

.comment-actions {
  display: flex;
  justify-content: flex-start;
  margin-top: 10px;
}

.comment-action {
  background: transparent;
  border: none;
  color: rgba(212, 175, 55, 0.9);
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 14px;
  padding: 4px 0;
}

.comment-action-icon {
  font-size: 13px;
}

/* 火焰特效评论 */
.comment-item-fire {
  position: relative;
  background: rgba(20, 14, 10, 0.75);
  border: 1px solid rgba(212, 175, 55, 0.16);
}

.comment-action-fire {
  color: rgba(255, 150, 0, 0.95) !important;
  font-weight: 600;
  text-shadow: 0 0 8px rgba(255, 100, 0, 0.6);
}

.comment-action-icon-fire {
  font-size: 16px;
  display: inline-block;
  animation: fire-icon 1s ease-in-out infinite;
  filter: drop-shadow(0 0 4px rgba(255, 100, 0, 0.8));
}


@keyframes fire-icon {
  0%, 100% {
    transform: scale(1) rotate(0deg);
    filter: drop-shadow(0 0 4px rgba(255, 100, 0, 0.8));
  }
  25% {
    transform: scale(1.1) rotate(-5deg);
    filter: drop-shadow(0 0 6px rgba(255, 150, 0, 1));
  }
  50% {
    transform: scale(1.15) rotate(0deg);
    filter: drop-shadow(0 0 8px rgba(255, 100, 0, 1));
  }
  75% {
    transform: scale(1.1) rotate(5deg);
    filter: drop-shadow(0 0 6px rgba(255, 150, 0, 1));
  }
}

.contact-section {
  width: 100%;
  padding: 34px 60px 48px;
  background: radial-gradient(900px 240px at 50% 0%, rgba(212, 175, 55, 0.12), transparent 60%),
    linear-gradient(180deg, #1f1812 0%, #120e0a 100%);
  border-top: 1px solid rgba(212, 175, 55, 0.18);
}

.contact-inner {
  max-width: 1400px;
  margin: 0 auto;
  text-align: center;
}

.contact-title {
  font-size: 22px;
  color: rgba(212, 175, 55, 0.95);
  letter-spacing: 8px;
  position: relative;
  display: inline-block;
  text-decoration: none;
  padding-bottom: 14px;
}

.contact-title::after {
  content: '';
  position: absolute;
  left: 50%;
  bottom: 0;
  transform: translateX(-50%);
  width: 140px;
  height: 2px;
  background: linear-gradient(90deg, transparent, rgba(212, 175, 55, 0.6), transparent);
}

.contact-actions {
  margin-top: 22px;
  display: flex;
  justify-content: center;
  gap: 18px;
}

.contact-icon-btn {
  width: 44px;
  height: 44px;
  border-radius: 999px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(212, 175, 55, 0.22);
  color: rgba(255, 255, 255, 0.78);
  transition: transform 0.2s ease, box-shadow 0.2s ease, background 0.2s ease, color 0.2s ease;
}

.contact-icon-btn:hover {
  transform: translateY(-2px);
  color: rgba(212, 175, 55, 0.95);
  background: rgba(212, 175, 55, 0.12);
  box-shadow: 0 12px 28px rgba(0, 0, 0, 0.45);
}

.contact-icon {
  width: 20px;
  height: 20px;
}

.section-roles {
  background: #1f1812;
  padding: 40px 60px;
  min-height: 100vh;
}

.roles-panel {
  max-width: 1400px;
  width: 100%;
  background: rgba(20, 14, 10, 0.55);
  border: 1px solid rgba(212, 175, 55, 0.25);
  border-radius: 14px;
  padding: 22px 22px 26px;
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.35);
  backdrop-filter: blur(10px);
}

.roles-header {
  text-align: center;
  margin-bottom: 18px;
}

.roles-title {
  font-size: 32px;
  color: rgba(212, 175, 55, 0.95);
  letter-spacing: 6px;
  margin: 0;
}

.roles-divider {
  height: 1px;
  margin-top: 14px;
  background: linear-gradient(90deg, transparent, rgba(212, 175, 55, 0.6), transparent);
}

.roles-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 18px;
}

.role-card {
  display: grid;
  grid-template-columns: 240px 1fr;
  background: rgba(42, 31, 21, 0.85);
  border: 1px solid rgba(212, 175, 55, 0.22);
  border-radius: 12px;
  overflow: hidden;
  min-height: 230px;
  height: 100%;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.45);
  transition: transform 0.28s ease, box-shadow 0.28s ease, border-color 0.28s ease;
}

@media (hover: hover) and (pointer: fine) {
  .role-card:hover {
    transform: translate3d(0, -6px, 0);
    box-shadow: 0 18px 44px rgba(0, 0, 0, 0.6);
    border-color: rgba(212, 175, 55, 0.6);
  }
}

@media (prefers-reduced-motion: reduce) {
  .role-card {
    transition: none;
  }

  .role-card:hover {
    transform: none;
  }
}

.role-card.reverse {
  grid-template-columns: 240px 1fr;
}

.role-media {
  background: rgba(0, 0, 0, 0.2);
}

.role-img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  display: block;
  background: rgba(0, 0, 0, 0.25);
}

.role-body {
  padding: 18px 18px 16px;
  color: rgba(255, 255, 255, 0.88);
}

.role-name {
  font-size: 26px;
  font-weight: 700;
  color: rgba(255, 255, 255, 0.95);
  margin-bottom: 6px;
}

.role-sub {
  font-size: 16px;
  color: rgba(212, 175, 55, 0.9);
  margin-bottom: 10px;
}

.role-desc {
  font-size: 16px;
  line-height: 1.8;
  color: rgba(255, 255, 255, 0.78);
}

.role-meta {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  align-items: center;
  margin-top: 12px;
}

.role-badge {
  font-size: 12px;
  padding: 6px 10px;
  border-radius: 999px;
  background: rgba(212, 175, 55, 0.12);
  border: 1px solid rgba(212, 175, 55, 0.25);
  color: rgba(212, 175, 55, 0.95);
}

.role-stars {
  margin-left: auto;
  font-size: 12px;
  letter-spacing: 2px;
  color: rgba(212, 175, 55, 0.95);
}

.section-feitian-inheritors {
  background: #231a13;
}

.inheritors-panel {
  max-width: 1200px;
  margin: 0 auto;
}

.inheritors-header {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 40px;
}

.inheritors-line {
  flex: 1;
  max-width: 200px;
  height: 1px;
  background: linear-gradient(
    to right,
    rgba(212, 175, 55, 0),
    rgba(212, 175, 55, 0.7),
    rgba(212, 175, 55, 0)
  );
}

.inheritors-title {
  margin: 0 32px;
  font-size: 36px;
  letter-spacing: 8px;
  color: rgba(212, 175, 55, 0.95);
}

.inheritors-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 28px 40px;
}

.inheritor-card {
  display: grid;
  grid-template-columns: 200px 1fr;
  gap: 24px;
  padding: 24px 28px;
  background: rgba(42, 31, 21, 0.9);
  border-radius: 16px;
  border: 1px solid rgba(212, 175, 55, 0.3);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.45);
  align-items: center;
  transition: transform 0.28s ease, box-shadow 0.28s ease, border-color 0.28s ease;
}

@media (hover: hover) and (pointer: fine) {
  .inheritor-card:hover {
    transform: translate3d(0, -6px, 0);
    box-shadow: 0 18px 44px rgba(0, 0, 0, 0.6);
    border-color: rgba(212, 175, 55, 0.6);
  }
}

@media (prefers-reduced-motion: reduce) {
  .inheritor-card {
    transition: none;
  }

  .inheritor-card:hover {
    transform: none;
  }
}

.inheritor-avatar {
  width: 180px;
  height: 180px;
  border-radius: 50%;
  overflow: hidden;
  border: 3px solid rgba(212, 175, 55, 0.7);
  background: radial-gradient(circle at 30% 20%, #f6e8c0, #8a5a30);
  margin: 0 auto;
}

.inheritor-avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.inheritor-body {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.inheritor-name {
  font-size: 22px;
  font-weight: 700;
  color: rgba(255, 255, 255, 0.96);
}

.inheritor-tag {
  font-size: 16px;
  color: rgba(212, 175, 55, 0.95);
}

.inheritor-desc {
  margin-top: 4px;
  font-size: 16px;
  line-height: 1.8;
  color: rgba(255, 255, 255, 0.78);
}

.posters-grid {
  max-width: 1400px;
  width: 100%;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 50px;
}

.poster-item {
  position: relative;
}

.poster-image {
  width: 100%;
  height: 400px;
  background: linear-gradient(135deg, rgba(139, 111, 71, 0.2), rgba(212, 175, 55, 0.2));
  border: 1px solid rgba(212, 175, 55, 0.3);
  overflow: hidden;
  margin-bottom: 20px;
  transition: all 0.3s ease;
}

.poster-image:hover {
  border-color: rgba(212, 175, 55, 0.6);
  transform: scale(1.02);
  box-shadow: 0 8px 24px rgba(212, 175, 55, 0.2);
}

.poster-video {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.poster-desc {
  margin-top: 14px;
  padding: 14px 20px;
  max-width: 90%;
  margin-left: auto;
  margin-right: auto;
  background: rgba(42, 31, 21, 0.9);
  border: 1px solid rgba(212, 175, 55, 0.4);
  color: rgba(255, 255, 255, 0.9);
  font-size: 17px;
  line-height: 1.9;
  text-align: justify;
  box-shadow: 0 10px 26px rgba(0, 0, 0, 0.5);
  border-radius: 6px;
}

.poster-fav-btn {
  margin-top: 18px;
  display: block;
  margin-left: auto;
  margin-right: auto;
  padding: 8px 30px;
  border-radius: 999px;
  border: 1px solid rgba(212, 175, 55, 0.8);
  background: rgba(212, 175, 55, 0.12);
  color: rgba(212, 175, 55, 0.96);
  font-size: 16px;
  letter-spacing: 2px;
  cursor: pointer;
  transition: all 0.25s ease;
}

.poster-fav-btn:hover {
  background: rgba(212, 175, 55, 0.3);
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.35);
}

.poster-title {
  writing-mode: vertical-rl;
  font-size: 28px;
  font-weight: bold;
  color: white;
  text-align: center;
  letter-spacing: 6px;
  margin: 0 auto;
}

/* 响应式 */
@media (max-width: 1200px) {
  .content-section {
    padding: 80px 40px;
  }
  
  .section-title {
    font-size: 40px;
  }
  
  .intro-content {
    flex-direction: column;
  gap: 40px;
}

  .intro-image {
  width: 100%;
  }
  
  .intro-image .image-placeholder {
    height: 500px;
  }
  
  .info-cards {
    grid-template-columns: repeat(2, 1fr);
    gap: 30px;
  }

  .inheritors-grid {
    grid-template-columns: 1fr;
  }
  
  .inheritor-card {
    grid-template-columns: 180px 1fr;
  }
  
  .posters-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 40px;
  }

  .section-culture {
    padding: 50px 40px;
  }

  .culture-card {
    max-width: 980px;
  }

  .culture-media {
    width: 300px;
  }

  .contact-section {
    padding: 34px 40px 44px;
  }

  .section-community {
    padding: 50px 40px;
  }

  .community-grid {
    grid-template-columns: 1fr 1.4fr;
  }

  .community-list {
    height: 340px;
  }

  .roles-grid {
    grid-template-columns: 1fr;
  }

  .role-card,
  .role-card.reverse {
    grid-template-columns: 240px 1fr;
  }
  
  .poster-image {
    height: 350px;
  }
}

@media (max-width: 768px) {
  .content-section {
    padding: 60px 20px;
  }
  
  .section-title {
    font-size: 32px;
    margin-bottom: 40px;
  }
  
  .intro-image .image-title {
    font-size: 40px;
  }
  
  .intro-text {
    font-size: 16px;
  }
  
  .intro-text-title {
    font-size: 24px;
  }
  
  .info-cards {
    grid-template-columns: 1fr;
    gap: 20px;
  }

  .inheritors-grid {
    grid-template-columns: 1fr;
  }
  
  .posters-grid {
    grid-template-columns: 1fr;
    gap: 30px;
  }
  
  .poster-image {
    height: 400px;
  }

  .section-roles {
    padding: 50px 20px;
  }

  .role-card,
  .role-card.reverse {
    grid-template-columns: 1fr;
  }

  .role-media {
    height: 220px;
  }

  .section-community {
    padding: 50px 20px;
  }

  .community-grid {
    grid-template-columns: 1fr;
  }

  .community-list {
    height: 320px;
  }
}
</style>

