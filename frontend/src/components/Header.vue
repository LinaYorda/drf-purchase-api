<script setup>
</script>

<template>
    <header>
    <nav>
        <router-link to="/">Home</router-link>
        </nav>
        <nav>
        <router-link to ="/countries">Countries</router-link>
        </nav>
    </header>
</template>

<style scoped>

header {
    position:fixed;
    top:0;
    width:100%;
    background-color:#bdcad7;
    padding:10px 0;
    text-align:center;
    box-shadow:0 2px 4px rgba(0,0,0,0.1);
  }
</style>
