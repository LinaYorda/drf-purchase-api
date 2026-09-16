 import { createRouter, createWebHistory } from 'vue-router';                                                                                                                                                          
import CountryList from '../views/CountryList.vue';     
import HomeView from '../views/HomeView.vue';                                                                                                                                                              
                                                                                                                                                                                                                        
const routes = [                                                                                                                                                                                                      
      {                                                                                                                                                                                                                 
          path: '/',                                                                                                                                                                                                    
          component: HomeView                                                                                                                                                                                           
      },
      {                                                                                                                                                                                                                 
          path: '/countries',                                                                                                                                                                                           
          component: CountryList                                                                                                                                                                                        
      },
]                                                                                                                                                                                                                     
                                                                                                                                                                                                                        
const router = createRouter({                                                                                                                                                                                         
      history: createWebHistory(),                                                                                                                                                                                      
      routes,                                                                                                                                                                                                           
  })                                                                                                                                                                                                                    
                                                                                                                                                                                                                        
export default router                               
