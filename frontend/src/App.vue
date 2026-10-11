<script setup>
    import { useRoute } from 'vue-router'
    import Header from './components/Header.vue'
    import Footer from './components/Footer.vue'
    import Sidebar from './components/Sidebar.vue'

    const route = useRoute()
</script>

<template>
  <div class="drawer lg:drawer-open">
    <input id="app-drawer" type="checkbox" class="drawer-toggle" />

    <div class="drawer-content">
      <div class="page">
        <Header v-if="!route.meta.hideChrome" />
        <main :class="{ 'scroll-contained': route.meta.scrollContained }">
          <router-view />
        </main>
        <Footer v-if="!route.meta.hideChrome" />
      </div>
    </div>

    <Sidebar v-if="!route.meta.hideChrome" />
  </div>
</template>


<style scoped>
    .page {
        height: 100vh;
        display: flex;
        flex-direction: column;
    }

    main {
        padding: 40px 20px 20px;
        text-align: center;
        flex: 1;
        display: flex;
        overflow-y: auto;
        flex-direction: column;
        background-color: var(--color-base-200);
    }
    main.scroll-contained {
        min-height: 0;
        overflow: hidden;
        display: flex;
        flex-direction: column;
    }
</style>

