import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router'
import { setUnauthorizedHandler } from './api.js'
import { user } from './auth.js'

setUnauthorizedHandler(() => {
    user.value = null
    if (router.currentRoute.value.path !== '/login') router.push('/login')
})

createApp(App).use(router).mount('#app')

