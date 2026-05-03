<template>
  <div class="login-page">
    <NavBar />
    
    <!-- 主内容区域 -->
    <div class="login-container">
      <div class="login-card">
        <!-- 左侧欢迎区域 -->
        <div class="welcome-section">
          <div class="welcome-background">
            <img src=assetUrl("/images/login/dl1.jpg") alt="登录背景" class="welcome-image" />
          </div>
          <div class="welcome-content">
            <h1 class="welcome-title">欢迎来到敦煌文化</h1>
            <p class="welcome-subtitle">登录您的账户,继续探索千年敦煌艺术瑰宝</p>
            <div class="welcome-footer">
              <span class="welcome-question">还没有账号?</span>
              <button class="register-btn" @click="goToRegister">立即注册</button>
            </div>
          </div>
        </div>

        <!-- 右侧登录表单 -->
        <div class="login-form-section">
          <h2 class="form-title">用户登录</h2>
          <p class="form-subtitle">请输入您的账号和密码</p>
          
          <el-form 
            :model="loginForm" 
            :rules="rules" 
            ref="loginFormRef"
            class="login-form"
            @submit.prevent="handleLogin"
          >
            <el-form-item prop="username">
              <label class="form-label">用户名/邮箱</label>
              <el-input
                v-model="loginForm.username"
                placeholder="请输入用户名或邮箱"
                class="form-input"
              >
                <template #prefix>
                  <el-icon><User /></el-icon>
                </template>
              </el-input>
            </el-form-item>

            <el-form-item prop="password">
              <label class="form-label">密码</label>
              <el-input
                v-model="loginForm.password"
                type="password"
                placeholder="请输入密码"
                class="form-input"
                show-password
              >
                <template #prefix>
                  <el-icon><Lock /></el-icon>
                </template>
              </el-input>
            </el-form-item>

            <div class="form-options">
              <el-checkbox v-model="rememberMe">记住我</el-checkbox>
              <a href="#" class="forgot-password">忘记密码?</a>
            </div>

            <el-button 
              type="primary" 
              class="login-btn"
              @click="handleLogin"
              :loading="loading"
            >
              登录
            </el-button>
          </el-form>

          <div class="divider">
            <span>或使用以下方式登录</span>
          </div>

          <div class="social-login">
            <div class="social-icon social-wechat">微信</div>
            <div class="social-icon social-weibo">微博</div>
            <div class="social-icon social-qq">QQ</div>
          </div>

          <div class="form-footer">
            <span>还没有账号?</span>
            <a href="#" class="register-link" @click.prevent="goToRegister">立即注册</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'
import { useRouter } from 'vue-router'
import { ElMessage } from 'element-plus'

const baseURL = import.meta.env.BASE_URL || '/'
const assetUrl = (path) => path.startsWith('/') ? baseURL + path.slice(1) : path

import NavBar from '../components/NavBar.vue'

const router = useRouter()
const loginFormRef = ref(null)
const loading = ref(false)
const rememberMe = ref(false)

const loginForm = reactive({
  username: '',
  password: ''
})

// 验证规则
const validateUsername = (rule, value, callback) => {
  if (!value) {
    callback(new Error('请输入用户名或邮箱'))
  } else if (value !== '蒸蛋' && value !== '雪顶小艺') {
    callback(new Error('用户名不正确'))
  } else {
    callback()
  }
}

const validatePassword = (rule, value, callback) => {
  if (!value) {
    callback(new Error('请输入密码'))
  } else if (value !== '20260121') {
    callback(new Error('密码不正确'))
  } else {
    callback()
  }
}

const rules = {
  username: [
    { validator: validateUsername, trigger: 'blur' }
  ],
  password: [
    { validator: validatePassword, trigger: 'blur' }
  ]
}

// 跳转到注册页
const goToRegister = () => {
  router.push('/register')
}

// 登录处理
const handleLogin = async () => {
  if (!loginFormRef.value) return
  
  await loginFormRef.value.validate((valid) => {
    if (valid) {
      // 验证用户名和密码
      const validUsernames = ['蒸蛋', '雪顶小艺']
      const validPassword = '20260121'
      
      if (validUsernames.includes(loginForm.username) && loginForm.password === validPassword) {
        loading.value = true
        
        // 模拟登录请求
        setTimeout(() => {
          loading.value = false
          // 保存登录状态
          localStorage.setItem('isLoggedIn', 'true')
          localStorage.setItem('username', loginForm.username)
          
          ElMessage.success('登录成功！')
          router.push('/')
        }, 500)
      } else {
        ElMessage.error('用户名或密码错误')
      }
    } else {
      ElMessage.error('请填写正确的登录信息')
    }
  })
}
</script>

<style scoped>
.login-page {
  height: 100vh;
  background-color: #000;
  background-image: url('/images/login/dl02.jpg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  position: relative;
  overflow: hidden;
}

/* 主容器 */
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: calc(100vh - 55px);
  padding-top: 100px;
  padding-bottom: 40px;
  padding-left: 40px;
  padding-right: 40px;
}

.login-card {
  display: flex;
  width: 100%;
  max-width: 1200px;
  background: white;
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 10px 50px rgba(0, 0, 0, 0.15);
}

/* 左侧欢迎区域 */
.welcome-section {
  flex: 1;
  background: var(--dunhuang-wall-brown);
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 30px 35px;
  min-height: 450px;
}

.welcome-background {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  opacity: 0.8;
  overflow: hidden;
}

.welcome-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
}

.welcome-content {
  position: relative;
  z-index: 10;
  color: white;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100%;
  text-align: center;
  gap: 20px;
}

.welcome-title {
  font-family: var(--font-title);
  font-size: 48px;
  font-weight: bold;
  color: white;
  margin-bottom: 15px;
  line-height: 1.3;
  text-align: center;
  width: 100%;
}

.welcome-subtitle {
  font-size: 18px;
  line-height: 1.6;
  opacity: 0.9;
  text-align: center;
  width: 100%;
}

.welcome-footer {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 15px;
}

.welcome-question {
  font-size: 18px;
  opacity: 0.9;
}

.register-btn {
  padding: 12px 32px;
  background: rgba(255, 255, 255, 0.15);
  border: 1px solid rgba(255, 255, 255, 0.6);
  border-radius: 25px;
  color: white;
  font-size: 16px;
  cursor: pointer;
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.25);
  transition: all 0.3s ease;
}

.register-btn:hover {
  background: rgba(255, 255, 255, 0.25);
  transform: translateY(-2px);
}

/* 右侧登录表单 */
.login-form-section {
  flex: 1;
  padding: 30px 35px;
  display: flex;
  flex-direction: column;
}

.form-title {
  font-family: var(--font-title);
  font-size: 28px;
  color: var(--dunhuang-dark-gray);
  margin-bottom: 8px;
}

.form-subtitle {
  font-size: 14px;
  color: var(--dunhuang-medium-gray);
  margin-bottom: 25px;
}

.login-form {
  flex: 1;
}

.form-label {
  display: block;
  font-size: 14px;
  color: var(--dunhuang-dark-gray);
  margin-bottom: 8px;
  font-weight: 500;
}

:deep(.el-form-item) {
  margin-bottom: 20px;
}

:deep(.el-input__wrapper) {
  border-radius: 8px;
  box-shadow: 0 0 0 1px var(--dunhuang-light-gray) inset;
  padding: 12px 15px;
}

:deep(.el-input__wrapper:hover) {
  box-shadow: 0 0 0 1px var(--dunhuang-sand-gold) inset;
}

:deep(.el-input__wrapper.is-focus) {
  box-shadow: 0 0 0 2px var(--dunhuang-sand-gold) inset;
}

.form-options {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 25px;
}

.forgot-password {
  color: var(--dunhuang-wall-brown);
  text-decoration: none;
  font-size: 14px;
  transition: color 0.3s ease;
}

.forgot-password:hover {
  color: var(--dunhuang-sand-gold);
}

.login-btn {
  width: 100%;
  height: 50px;
  font-size: 16px;
  font-weight: 600;
  border-radius: 8px;
  background: var(--dunhuang-wall-brown);
  border: none;
}

.login-btn:hover {
  background: var(--dunhuang-sand-gold);
}

.divider {
  display: flex;
  align-items: center;
  text-align: center;
  margin: 20px 0;
  color: var(--dunhuang-medium-gray);
  font-size: 14px;
}

.divider::before,
.divider::after {
  content: '';
  flex: 1;
  border-bottom: 1px solid var(--dunhuang-light-gray);
}

.divider span {
  padding: 0 15px;
}

.social-login {
  display: flex;
  justify-content: center;
  gap: 20px;
  margin-bottom: 20px;
}

.social-icon {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 12px;
  cursor: pointer;
  transition: transform 0.3s ease;
}

.social-icon:hover {
  transform: scale(1.1);
}

.social-wechat {
  background: #07c160;
}

.social-weibo {
  background: #e6162d;
}

.social-qq {
  background: #12b7f5;
}

.form-footer {
  text-align: center;
  color: var(--dunhuang-medium-gray);
  font-size: 14px;
}

.register-link {
  color: var(--dunhuang-wall-brown);
  text-decoration: none;
  margin-left: 5px;
  transition: color 0.3s ease;
}

.register-link:hover {
  color: var(--dunhuang-sand-gold);
}

@media (max-width: 968px) {
  .login-card {
    flex-direction: column;
  }
  
  .welcome-section {
    min-height: 300px;
    padding: 40px 30px;
  }
  
  .welcome-title {
    font-size: 36px;
  }
  
  .login-form-section {
    padding: 40px 30px;
  }
  
  .login-container {
    min-height: calc(100vh - 60px);
    padding-top: 60px;
    padding-bottom: 40px;
    padding-left: 20px;
    padding-right: 20px;
  }
}
</style>

