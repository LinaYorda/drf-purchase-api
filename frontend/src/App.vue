<script setup>
import { ref, onMounted } from 'vue'

const countries = ref([])

onMounted(async () => {
  const response = await fetch('http://localhost:8000/api/countries/')
  const data = await response.json()
  countries.value = data.results
})
</script>

<template>
  <h1>Countries</h1>
  <ul>
    <li v-for="country in countries" :key="country.id">
      {{ country.name }}
    </li>
  </ul>
  
</template>
