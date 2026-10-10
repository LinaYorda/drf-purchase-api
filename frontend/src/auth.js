import { ref, computed } from 'vue'
import { apiFetch } from './api.js'

export const user = ref(null)   // { username } or null
export const isLoggedIn = computed(() => user.value !== null)

let checked = false

export async function checkAuth() {
    if (checked) return
    try {
        const response = await apiFetch('/me/')
        user.value = response.ok ? await response.json() : null
    } catch (error) {
        console.error('Error checking authentication:', error)
        user.value = null
    } finally {
        checked = true
    }
}

export async function login(username, password) {
    await apiFetch('/csrf/')   // GET request: makes sure the csrftoken cookie exists
    const response = await apiFetch('/login/', {
        method: 'POST',
        body: JSON.stringify({ username, password }),
    })
    if (response.status === 400) return false   // wrong username or password
    if (!response.ok) throw new Error('Login failed')

    const meResponse = await apiFetch('/me/')
    user.value = await meResponse.json()
    return true
}

export async function logout() {
    try {
        await apiFetch('/logout/', { method: 'POST' })
    } finally {
        user.value = null
    }
}
