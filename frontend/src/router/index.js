import { createRouter, createWebHistory } from 'vue-router';
import CountryList from '../views/CountryList.vue';
import HomeView from '../views/HomeView.vue';
import Login from '../views/Login.vue';
import Purchases from '../views/Purchases.vue';
import Shipping from '../views/Shipping.vue';
import { isLoggedIn, checkAuth } from '../auth.js';
import Logout from '../views/Logout.vue';
import Profile from '../views/Profile.vue';

const routes = [
    { path: '/', redirect: '/home' },
    { path: '/home', component: HomeView },
    { path: '/countries', component: CountryList },
    { path: '/purchases', component: Purchases },
    { path: '/shipping-status', component: Shipping },
    { path: '/login', component: Login, meta: { hideChrome: true, public: true } },
    { path: '/logout', component: Logout},
    { path: '/profile', component: Profile},

]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

router.beforeEach(async (to) => {
    await checkAuth()
    if (!isLoggedIn.value && !to.meta.public) return '/login'
    if (isLoggedIn.value && to.path === '/login') return '/home'
})

export default router
                         
