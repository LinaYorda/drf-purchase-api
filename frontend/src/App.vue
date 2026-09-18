<script setup>
import { onMounted } from 'vue';
import Header from './components/Header.vue';
import Footer from './components/Footer.vue';
import Login from './views/Login.vue';
import router from './router/index.js';


</script>

  <template>                                                                                                                                                          
    <div class="page">                                                                                                                                                
      <Header />                                                                                                                                                      
      <main>                                                                                                                                                          
        <router-view />                                                                                                                                               
      </main>                                                                                                                                                         
      <Footer />                                                                                                                                                      
    </div>                                                                                                                                                            
  </template>  

<style scoped>

.page {                                                                                                                                                             
      min-height: 100vh;                                                                                                                                              
      display: flex;                                                                                                                                                  
      flex-direction: column;                                                                                                                                         
  }                        

main {
    margin-top: 100px;
    margin-bottom: 20px;
    text-align: center;
    flex: 1;
  }
</style>

