import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import './styles/main.css'

// Handle 404 redirect from GitHub Pages SPA fallback
const params = new URLSearchParams(window.location.search)
const redirect = params.get('redirect')
if (redirect) {
  window.history.replaceState({}, '', window.location.pathname)
  router.replace(decodeURIComponent(redirect))
}

const app = createApp(App)

app.use(router)
app.use(ElementPlus)
app.mount('#app')

