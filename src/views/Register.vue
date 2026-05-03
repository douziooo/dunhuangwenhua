<template>
  <div class="register-page">
    <NavBar />
    
    <!-- 主内容区域 -->
    <div class="register-container">
      <div class="register-card">
        <!-- 左侧欢迎区域 -->
        <div class="welcome-section">
          <div class="welcome-background">
            <img src=assetUrl("/images/login/zc1.jpg") alt="注册背景" class="welcome-image" />
          </div>
          <div class="welcome-content">
            <h1 class="welcome-title">加入敦煌文化</h1>
            <p class="welcome-subtitle">注册账号,开启您的敦煌艺术探索之旅</p>
            <div class="welcome-footer">
              <span class="welcome-question">已有账号?</span>
              <button class="login-btn" @click="goToLogin">立即登录</button>
            </div>
          </div>
        </div>

        <!-- 右侧注册表单 -->
        <div class="register-form-section">
          <h2 class="form-title">用户注册</h2>
          <p class="form-subtitle">请填写以下信息完成注册</p>
          
          <el-form 
            :model="registerForm" 
            :rules="rules" 
            ref="registerFormRef"
            class="register-form"
            @submit.prevent="handleRegister"
          >
            <el-form-item prop="username">
              <label class="form-label">用户名</label>
              <el-input
                v-model="registerForm.username"
                placeholder="请输入用户名(4-16位字符)"
                class="form-input"
              >
                <template #prefix>
                  <el-icon><User /></el-icon>
                </template>
              </el-input>
            </el-form-item>

            <el-form-item prop="email">
              <label class="form-label">电子邮箱</label>
              <el-input
                v-model="registerForm.email"
                placeholder="请输入电子邮箱"
                class="form-input"
              >
                <template #prefix>
                  <el-icon><Message /></el-icon>
                </template>
              </el-input>
            </el-form-item>

            <el-form-item prop="phone">
              <label class="form-label">手机号码</label>
              <el-input
                v-model="registerForm.phone"
                placeholder="请输入手机号码"
                class="form-input"
              >
                <template #prefix>
                  <el-icon><Phone /></el-icon>
                </template>
              </el-input>
            </el-form-item>

            <el-form-item prop="password">
              <label class="form-label">密码</label>
              <el-input
                v-model="registerForm.password"
                type="password"
                placeholder="请输入密码(6-20位字符)"
                class="form-input"
                show-password
              >
                <template #prefix>
                  <el-icon><Lock /></el-icon>
                </template>
              </el-input>
            </el-form-item>

            <el-form-item prop="confirmPassword">
              <label class="form-label">确认密码</label>
              <el-input
                v-model="registerForm.confirmPassword"
                type="password"
                placeholder="请再次输入密码"
                class="form-input"
                show-password
              >
                <template #prefix>
                  <el-icon><Lock /></el-icon>
                </template>
              </el-input>
            </el-form-item>

            <el-form-item prop="verifyCode">
              <label class="form-label">验证码</label>
              <div class="verify-code-wrapper">
                <el-input
                  v-model="registerForm.verifyCode"
                  placeholder="请输入验证码"
                  class="form-input verify-code-input"
                >
                  <template #prefix>
                    <el-icon><Shield /></el-icon>
                  </template>
                </el-input>
                <el-button 
                  class="get-code-btn"
                  @click="getVerifyCode"
                  :disabled="codeDisabled"
                >
                  {{ codeDisabled ? `${countdown}秒后重试` : '获取验证码' }}
                </el-button>
              </div>
            </el-form-item>

            <el-form-item prop="agreement">
              <el-checkbox v-model="registerForm.agreement">
                我已阅读并同意<span class="link-text">《用户协议》</span>和<span class="link-text">《隐私政策》</span>
              </el-checkbox>
            </el-form-item>

            <el-button 
              type="primary" 
              class="register-btn"
              @click="handleRegister"
              :loading="loading"
            >
              立即注册
            </el-button>
          </el-form>

          <div class="form-footer">
            <span>已有账号?</span>
            <a href="#" class="login-link" @click.prevent="goToLogin">立即登录</a>
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
const registerFormRef = ref(null)
const loading = ref(false)
const codeDisabled = ref(false)
const countdown = ref(60)

const registerForm = reactive({
  username: '',
  email: '',
  phone: '',
  password: '',
  confirmPassword: '',
  verifyCode: '',
  agreement: false
})

// 验证规则
const validateUsername = (rule, value, callback) => {
  if (!value) {
    callback(new Error('请输入用户名'))
  } else if (value.length < 4 || value.length > 16) {
    callback(new Error('用户名长度为4-16位字符'))
  } else {
    callback()
  }
}

const validateEmail = (rule, value, callback) => {
  if (!value) {
    callback(new Error('请输入电子邮箱'))
  } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value)) {
    callback(new Error('请输入正确的邮箱格式'))
  } else {
    callback()
  }
}

const validatePhone = (rule, value, callback) => {
  if (!value) {
    callback(new Error('请输入手机号码'))
  } else if (!/^1[3-9]\d{9}$/.test(value)) {
    callback(new Error('请输入正确的手机号码'))
  } else {
    callback()
  }
}

const validatePassword = (rule, value, callback) => {
  if (!value) {
    callback(new Error('请输入密码'))
  } else if (value.length < 6 || value.length > 20) {
    callback(new Error('密码长度为6-20位字符'))
  } else {
    callback()
  }
}

const validateConfirmPassword = (rule, value, callback) => {
  if (!value) {
    callback(new Error('请再次输入密码'))
  } else if (value !== registerForm.password) {
    callback(new Error('两次输入的密码不一致'))
  } else {
    callback()
  }
}

const validateVerifyCode = (rule, value, callback) => {
  if (!value) {
    callback(new Error('请输入验证码'))
  } else {
    callback()
  }
}

const validateAgreement = (rule, value, callback) => {
  if (!value) {
    callback(new Error('请先同意用户协议和隐私政策'))
  } else {
    callback()
  }
}

const rules = {
  username: [
    { validator: validateUsername, trigger: 'blur' }
  ],
  email: [
    { validator: validateEmail, trigger: 'blur' }
  ],
  phone: [
    { validator: validatePhone, trigger: 'blur' }
  ],
  password: [
    { validator: validatePassword, trigger: 'blur' }
  ],
  confirmPassword: [
    { validator: validateConfirmPassword, trigger: 'blur' }
  ],
  verifyCode: [
    { validator: validateVerifyCode, trigger: 'blur' }
  ],
  agreement: [
    { validator: validateAgreement, trigger: 'change' }
  ]
}

// 获取验证码
const getVerifyCode = () => {
  if (!registerForm.phone) {
    ElMessage.warning('请先输入手机号码')
    return
  }
  
  codeDisabled.value = true
  ElMessage.success('验证码已发送')
  
  const timer = setInterval(() => {
    countdown.value--
    if (countdown.value <= 0) {
      clearInterval(timer)
      codeDisabled.value = false
      countdown.value = 60
    }
  }, 1000)
}

// 跳转到登录页
const goToLogin = () => {
  router.push('/login')
}

// 注册处理
const handleRegister = async () => {
  if (!registerFormRef.value) return
  
  await registerFormRef.value.validate((valid) => {
    if (valid) {
      loading.value = true
      
      // 模拟注册请求
      setTimeout(() => {
        loading.value = false
        ElMessage.success('注册成功！请登录')
        router.push('/login')
      }, 500)
    } else {
      ElMessage.error('请填写正确的注册信息')
    }
  })
}
</script>

<style scoped>
.register-page {
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
.register-container {
  display: flex;
  justify-content: center;
  align-items: flex-start;
  min-height: calc(100vh - 55px);
  padding-top: 90px;
  padding-bottom: 20px;
  padding-left: 20px;
  padding-right: 20px;
}

.register-card {
  display: flex;
  width: 100%;
  max-width: 1000px;
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
  padding: 25px 30px;
  min-height: 400px;
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
  margin-bottom: 12px;
  line-height: 1.3;
  text-align: center;
  width: 100%;
}

.welcome-subtitle {
  font-size: 18px;
  line-height: 1.5;
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

.login-btn {
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

.login-btn:hover {
  background: rgba(255, 255, 255, 0.25);
  transform: translateY(-2px);
}

/* 右侧注册表单 */
.register-form-section {
  flex: 1;
  padding: 15px 20px;
  display: flex;
  flex-direction: column;
}

.form-title {
  font-family: var(--font-title);
  font-size: 20px;
  color: var(--dunhuang-dark-gray);
  margin-bottom: 3px;
}

.form-subtitle {
  font-size: 12px;
  color: var(--dunhuang-medium-gray);
  margin-bottom: 10px;
}

.register-form {
  flex: 1;
}

.form-label {
  display: block;
  font-size: 12px;
  color: var(--dunhuang-dark-gray);
  margin-bottom: 5px;
  font-weight: 500;
}

:deep(.el-form-item) {
  margin-bottom: 4px;
}

:deep(.el-input__wrapper) {
  border-radius: 6px;
  box-shadow: 0 0 0 1px var(--dunhuang-light-gray) inset;
  padding: 5px 10px;
  min-height: 26px;
}

:deep(.el-input__inner) {
  font-size: 13px;
  line-height: 1.2;
}

:deep(.el-input__wrapper:hover) {
  box-shadow: 0 0 0 1px var(--dunhuang-sand-gold) inset;
}

:deep(.el-input__wrapper.is-focus) {
  box-shadow: 0 0 0 2px var(--dunhuang-sand-gold) inset;
}

.verify-code-wrapper {
  display: flex;
  gap: 8px;
  margin-top: 25px;
}

.verify-code-input {
  flex: 1;
  max-width: calc(100% - 15px);
}

.verify-code-input :deep(.el-input__wrapper) {
  min-height: 24px !important;
  height: 24px !important;
  padding: 5px 10px !important;
}

.get-code-btn {
  height: 26px;
  padding: 0 12px;
  background: var(--dunhuang-wall-brown);
  border: none;
  color: white;
  border-radius: 6px;
  font-size: 12px;
  white-space: nowrap;
  flex-shrink: 0;
}

.get-code-btn:hover {
  background: var(--dunhuang-sand-gold);
}

.get-code-btn:disabled {
  background: var(--dunhuang-light-gray);
  color: var(--dunhuang-medium-gray);
  cursor: not-allowed;
}

:deep(.el-checkbox__label) {
  font-size: 12px;
  color: var(--dunhuang-dark-gray);
}

:deep(.el-checkbox) {
  margin-bottom: 0;
}

.link-text {
  color: var(--dunhuang-wall-brown);
  cursor: pointer;
  text-decoration: underline;
}

.link-text:hover {
  color: var(--dunhuang-sand-gold);
}

.register-btn {
  width: 100%;
  height: 38px;
  font-size: 14px;
  font-weight: 600;
  border-radius: 6px;
  background: var(--dunhuang-wall-brown);
  border: none;
  margin-top: 5px;
}

.register-btn:hover {
  background: var(--dunhuang-sand-gold);
}

.form-footer {
  text-align: center;
  color: var(--dunhuang-medium-gray);
  font-size: 12px;
  margin-top: 8px;
}

.login-link {
  color: var(--dunhuang-wall-brown);
  text-decoration: none;
  margin-left: 5px;
  transition: color 0.3s ease;
}

.login-link:hover {
  color: var(--dunhuang-sand-gold);
}

@media (max-width: 968px) {
  .register-card {
    flex-direction: column;
  }
  
  .welcome-section {
    min-height: 250px;
    padding: 25px 20px;
  }
  
  .welcome-title {
    font-size: 36px;
  }
  
  .register-form-section {
    padding: 15px 15px;
  }
  
  .register-container {
    min-height: calc(100vh - 60px);
    padding-top: 80px;
    padding-bottom: 20px;
    padding-left: 15px;
    padding-right: 15px;
  }
}
</style>

