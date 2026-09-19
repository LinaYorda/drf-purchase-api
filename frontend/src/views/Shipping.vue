<script setup>

import { ref } from 'vue'

const trackingNumber = ref('')
const result = ref(null)
const error = ref(null)
const loading = ref(false)
const TRACKING_PATTERN = /^TRACK\d{6}$/

async function search() { 
    error.value = ''
    result.value = null

    const value = trackingNumber.value.trim().toUpperCase()
    if (!TRACKING_PATTERN.test(value)) {
        error.value = 'Invalid tracking number format. Please use TRACK followed by 6 digits.'
        return
    }

    loading.value = true
    try {
        const response = await fetch(`http://localhost:8000/api/shipping-status/${value}/`)
        if (response.status === 404) {
            error.value = 'Tracking number not found.'
            return
        }
        if (!response.ok) {
            error.value = 'Something went wrong. Please try again.'
            return
        }
        result.value = await response.json()
    } catch {
        error.value = 'Could not reach the server. Please try again.'
    } finally {
        loading.value = false
    }
}

function clear() { 
    trackingNumber.value = ''
    result.value = null
    error.value = ''
}


</script>



<template>

    <div class="flex flex-1 flex-col items-center justify-center gap-4">
    <h1 class="text-2xl font-bold text-gray-500">Shipping Status</h1>
    <fieldset class="fieldset w-80">
        <label class="label" for="tracking-number">Tracking number</label>
        <input v-model="trackingNumber" @keyup.enter="search" type="text" id="tracking-number" class="input w-full" placeholder="e.g. TRACK123456" />
        <p class="label">Format: TRACK followed by 6 digits. You can find it in your shipping confirmation.</p>
        <div class="flex gap-2">
    <button class="btn btn-primary flex-1" :disabled="loading" @click="search">Search</button>
    <button class="btn btn-ghost" :disabled="!trackingNumber && !result && !error" @click="clear">Clear</button>
</div>

    </fieldset>

    <p v-if="error" class="text-error">{{ error }}</p>

    <div v-if="result" class="card bg-base-100 shadow-sm w-80">
        <div class="card-body text-left">
            <p><strong>Tracking number:</strong> {{ result.tracking_number }}</p>
            <p><strong>Carrier:</strong> {{ result.carrier }}</p>
            <p><strong>Status:</strong> {{ result.status }}</p>
            <p><strong>Estimated delivery:</strong> {{ result.estimated_delivery }}</p>
        </div>
    </div>
</div>







</template>


<style scoped>
</style>
