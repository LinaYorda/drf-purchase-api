<script setup>
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { logout } from '../auth.js'

const router = useRouter()

onMounted(async () => {
    await logout()
    router.push('/login')
})

</script>

<template>
    <div class="flex flex-1 items-center justify-center ">
        <p>Logging out...</p>
    </div>
</template>


<style scoped>
</style>