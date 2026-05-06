<template>
  <nav class="navbar" :style="{ opacity: navbarOpacity }">
    <div class="navbar-container">
      <router-link to="/" class="navbar-logo">
        <span class="logo-main">敦煌</span>
        <span class="logo-subtitle">之美</span>
      </router-link>
      <el-menu
        mode="horizontal"
        :default-active="activeIndex"
        class="navbar-menu"
        @select="handleSelect"
      >
        <el-menu-item index="/">首页</el-menu-item>
        <el-menu-item index="/history">历史</el-menu-item>
        <el-menu-item index="/mural">壁画</el-menu-item>
        <el-menu-item index="/mogao">莫高窟</el-menu-item>
        <el-menu-item index="/feitian">飞天</el-menu-item>
      </el-menu>
      <div class="navbar-right">
        <el-button 
          type="text" 
          class="logout-btn"
          @click="confirmLogout"
        >
          <span class="logout-text">退出</span>
          <span :class="['logout-avatar', { 'logout-avatar--logged-in': isLoggedIn }]"></span>
        </el-button>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { ElMessageBox } from 'element-plus'

const router = useRouter()
const route = useRoute()
const navbarOpacity = ref(1)
const isLoggedIn = computed(() => localStorage.getItem('isLoggedIn') === 'true')

// 滚动控制导航栏透明度
const handleScroll = () => {
  const scrollTop = window.pageYOffset || document.documentElement.scrollTop
  navbarOpacity.value = Math.max(1 - scrollTop / 300, 0.3)
}

// 当前激活的菜单
const activeIndex = computed(() => {
  const path = route.path
  if (path === '/' || path === '/home') return '/'
  return path
})

// 导航跳转
const handleSelect = (index) => {
  router.push(index)
}

const confirmLogout = () => {
  ElMessageBox.confirm('确定要退出登录吗？', '提示', {
    confirmButtonText: '确定',
    cancelButtonText: '取消',
    type: 'warning'
  }).then(() => {
    localStorage.removeItem('isLoggedIn')
    localStorage.removeItem('username')
    router.push('/login')
  }).catch(() => {})
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
})
</script>

<style scoped>
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  border-bottom: 1px solid rgba(139, 111, 71, 0.15);
  box-shadow: 0 2px 20px rgba(0, 0, 0, 0.05), 
              0 1px 0 rgba(255, 255, 255, 0.5) inset;
  padding: 0;
  transition: opacity 0.3s ease-out;
  overflow: hidden;
  height: 55px;
}

.navbar::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 1px;
  background: linear-gradient(
    90deg,
    transparent,
    rgba(212, 175, 55, 0.3),
    transparent
  );
}

.navbar-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 50px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 55px;
  position: relative;
  z-index: 1;
}

.navbar-logo {
  display: flex;
  align-items: baseline;
  gap: 0;
  text-decoration: none;
  position: relative;
  padding: 8px 0;
  transform: translateX(-20px);
  user-select: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
}


.logo-main {
  font-family: var(--font-calligraphy);
  font-size: 43px;
  font-weight: normal;
  color: var(--dunhuang-wall-brown);
  line-height: 1;
  letter-spacing: 4px;
  position: relative;
  background: linear-gradient(
    90deg,
    var(--dunhuang-wall-brown) 0%,
    var(--dunhuang-wall-brown) 45%,
    var(--dunhuang-sand-gold) 50%,
    var(--dunhuang-wall-brown) 55%,
    var(--dunhuang-wall-brown) 100%
  );
  background-size: 200% 100%;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: glowMove 3s linear infinite;
  -webkit-text-stroke: 1px rgba(128, 128, 128, 0.9);
  text-stroke: 1px rgba(128, 128, 128, 0.9);
  filter: drop-shadow(0 0 2px rgba(120, 120, 120, 0.6));
}

.logo-subtitle {
  font-family: var(--font-calligraphy);
  font-size: 23px;
  letter-spacing: 6px;
  font-weight: normal;
  padding-left: 12px;
  position: relative;
  background: linear-gradient(
    90deg,
    #A68B5B 0%,
    #A68B5B 45%,
    var(--dunhuang-sand-gold) 50%,
    #A68B5B 55%,
    #A68B5B 100%
  );
  background-size: 200% 100%;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: glowMove 3s linear infinite;
  -webkit-text-stroke: 1px rgba(128, 128, 128, 0.9);
  text-stroke: 1px rgba(128, 128, 128, 0.9);
  filter: drop-shadow(0 0 2px rgba(120, 120, 120, 0.6));
}

@keyframes glowMove {
  0% {
    background-position: 100% 0;
  }
  100% {
    background-position: -100% 0;
  }
}

.navbar-menu {
  flex: 1;
  justify-content: flex-end;
  background: transparent !important;
  border: none !important;
  display: flex;
  align-items: center;
  transform: translateX(35px);
}

.navbar-menu .el-menu-item {
  font-family: var(--font-calligraphy);
  font-size: 20px;
  padding: 0 24px;
  height: 55px;
  line-height: 55px;
  color: var(--dunhuang-dark-gray);
  font-weight: normal;
  position: relative;
  transition: var(--transition-base);
  border-bottom: none !important;
  margin: 0 2px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.navbar-menu .el-menu-item::before {
  content: '';
  position: absolute;
  bottom: 15px;
  left: 50%;
  transform: translateX(-50%);
  width: 0;
  height: 2px;
  background: linear-gradient(90deg, var(--dunhuang-sand-gold), var(--dunhuang-wall-brown));
  transition: width 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.navbar-menu .el-menu-item:hover {
  color: var(--dunhuang-sand-gold);
  background: rgba(212, 175, 55, 0.08) !important;
  transform: translateY(-2px);
}

.navbar-menu .el-menu-item:hover::before {
  width: 80%;
}

.navbar-menu .el-menu-item.is-active {
  color: var(--dunhuang-wall-brown);
  background: transparent !important;
  font-weight: normal;
}

.navbar-menu .el-menu-item.is-active::before {
  width: 80%;
  background: linear-gradient(90deg, var(--dunhuang-wall-brown), var(--dunhuang-sand-gold));
}

.navbar-right {
  display: flex;
  align-items: center;
  gap: 15px;
  margin-left: 30px;
  margin-right: -70px;
}

.user-info {
  font-family: var(--font-calligraphy);
  font-size: 16px;
  color: var(--dunhuang-dark-gray);
  padding: 0 12px;
}

.logout-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 4px 14px 4px 18px !important;
  height: 38px;
  border-radius: 999px !important;
  border: 2px solid #f8a8a8 !important;
  background-color: #3f3f3f !important;
  color: #f8a8a8 !important;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.25);
}

.logout-text {
  font-family: var(--font-calligraphy);
  font-size: 18px;
  letter-spacing: 2px;
}

.logout-avatar {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background-color: #f5f5f5;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  position: relative;
  overflow: hidden;
}

.logout-avatar::before {
  content: '';
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background-color: #9e9e9e;
}

.logout-avatar.logout-avatar--logged-in {
  background-image: url('/images/login/dl03.jpg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

.logout-avatar.logout-avatar--logged-in::before {
  content: none;
}

.logout-btn:hover {
  background-color: #505050 !important;
  border-color: #ffb3b3 !important;
  transform: translateY(-1px);
}

@media (max-width: 768px) {
  .navbar {
    height: 60px;
  }
  
  .navbar-container {
    padding: 0 20px;
    height: 60px;
  }
  
  .navbar-menu .el-menu-item {
    padding: 0 16px;
    font-size: 16px;
    height: 60px;
    line-height: 60px;
  }
  
  .logo-main {
    font-size: 33px;
  }
  
  .logo-subtitle {
    font-size: 19px;
  }
  
  .navbar-menu .el-menu-item {
    font-size: 18px;
  }
  
  .navbar-menu .el-menu-item::before {
    bottom: 12px;
  }
  
  .navbar-right {
    gap: 10px;
    margin-left: 10px;
  }
  
  .user-info {
    font-size: 14px;
    padding: 0 8px;
  }
  
  .logout-btn {
    font-size: 16px;
    padding: 0 12px !important;
    height: 60px;
    line-height: 60px;
  }
  
  .logout-btn::before {
    bottom: 12px;
  }
}
</style>

