<script setup>

import Header from './components/Header.vue';
import Footer from './components/Footer.vue';
import router from './router/index.js';


</script>

<template>
  <Header />
  <main>
    <router-view />
  </main>
  <Footer />
</template>

<style scoped>
main {
    margin-top: 200px;
    margin-bottom: 100px;
    padding: 20px;
    text-align: center;
  }
</style>
