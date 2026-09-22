 <script setup>


import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { login } from '../auth.js'

const router = useRouter()
const username = ref('')
const password = ref('')
const error = ref('')
const loading = ref(false)

async function submit() {
    error.value = ''
    if (!username.value.trim() || !password.value) {
        error.value = 'Please enter both username and password.'
        return
    }

    loading.value = true
    try {
        const ok = await login(username.value.trim(), password.value)
        if (ok) {
            router.push('/home')
        } else {
            error.value = 'Invalid username or password.'
        }
    } catch {
        error.value = 'Could not reach the server. Please try again.'
    } finally {
        loading.value = false
    }
}


</script>



<template>
  <div class="hero flex-1 bg-base-200">
    <div class="hero-content flex-col gap-10 lg:flex-row">
      <div class="max-w-md text-center lg:text-left">
        <h1 class="text-5xl font-bold">Welcome to Purchase Management</h1>
        <p class="py-6">
          Track purchases, items and shipments for your bookstore in one place.
          Log in to get started.
        </p>
      </div>

      <div class="card bg-base-100 w-full max-w-sm shrink-0 shadow-2xl">
        <form class="card-body" @submit.prevent="submit">
          <fieldset class="fieldset">
            <label class="label" for="username">Username</label>
            <input v-model="username" id="username" type="text" class="input w-full" placeholder="Username" autocomplete="username" />

            <label class="label" for="password">Password</label>
            <input v-model="password" id="password" type="password" class="input w-full" placeholder="Password" autocomplete="current-password" />

            <p v-if="error" class="text-error mt-2">{{ error }}</p>

            <button type="submit" class="btn btn-neutral mt-4" :disabled="loading">Login</button>
          </fieldset>
        </form>
      </div>
    </div>
  </div>
</template>






