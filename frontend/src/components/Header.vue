<script setup>
</script>

<template>
    <header>
        <label for="app-drawer" aria-label="toggle sidebar" class="btn btn-square btn-ghost drawer-button">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" stroke-linejoin="round" stroke-linecap="round" stroke-width="2" fill="none" stroke="currentColor" class="my-1.5 inline-block size-4"><path d="M4 4m0 2a2 2 0 0 1 2 -2h12a2 2 0 0 1 2 2v12a2 2 0 0 1 -2 2h-12a2 2 0 0 1 -2 -2z"></path><path d="M9 4v16"></path><path d="M14 10l2 2l-2 2"></path></svg>
        </label>
        <router-link to="/login" class="ml-auto">Login</router-link>
    </header>
</template>

<style scoped>

header {
    position:sticky;
    top:0;
    width:100%;
    background-color:#b1cbe7;
    padding:10px 0;
    display:flex;
    text-align:center;
    box-shadow:0 2px 4px rgba(0,0,0,0.1);
  }
</style>
