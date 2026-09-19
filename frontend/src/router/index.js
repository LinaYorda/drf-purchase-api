 import { createRouter, createWebHistory } from 'vue-router';                                                                                                                                                          
import CountryList from '../views/CountryList.vue';     
import HomeView from '../views/HomeView.vue';  
import Login from '../views/Login.vue';                                                                                                                                                     
                                                                                                                                                                                                                        
const routes = [
      { path: '/', component: HomeView },
      { path: '/countries', component: CountryList },
      { path: '/login', component: Login, meta: { hideChrome: true } },
    ]                                                                                                                                                                                                                   
                                                                                                                                                                                                                        
const router = createRouter({                                                                                                                                                                                         
      history: createWebHistory(),                                                                                                                                                                                      
      routes,                                                                                                                                                                                                           
  })                                                                                                                                                                                                                    
                                                                                                                                                                                                                        
export default router                               
