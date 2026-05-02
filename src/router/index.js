import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import History from '../views/History.vue'
import Mural from '../views/Mural.vue'
import Mogao from '../views/Mogao.vue'
import Feitian from '../views/Feitian.vue'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'

const routes = [
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/register',
    name: 'Register',
    component: Register
  },
  {
    path: '/',
    name: 'Home',
    component: Home,
    meta: { requiresAuth: true }
  },
  {
    path: '/history',
    name: 'History',
    component: History,
    meta: { requiresAuth: true }
  },
  {
    path: '/mural',
    name: 'Mural',
    component: Mural,
    meta: { requiresAuth: true }
  },
  {
    path: '/mogao',
    name: 'Mogao',
    component: Mogao,
    meta: { requiresAuth: true }
  },
  {
    path: '/feitian',
    name: 'Feitian',
    component: Feitian,
    meta: { requiresAuth: true }
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    } else if (to.hash) {
      return {
        el: to.hash,
        behavior: 'auto'
      }
    } else {
      return { top: 0 }
    }
  }
})

// 路由守卫 - 检查登录状态
router.beforeEach((to, from, next) => {
  const isLoggedIn = localStorage.getItem('isLoggedIn') === 'true'
  
  if (to.meta.requiresAuth && !isLoggedIn) {
    // 需要登录但未登录，跳转到登录页
    next('/login')
  } else if (to.path === '/login' && isLoggedIn) {
    // 已登录访问登录页，跳转到首页
    next('/')
  } else {
    next()
  }
})

export default router

