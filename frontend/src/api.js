export const API_URL = 'http://localhost:8000/api'

let onUnauthorized = () => { }
export function setUnauthorizedHandler(fn) {
    onUnauthorized = fn
}

function getCookie(name) {
    const match = document.cookie.split('; ').find(row => row.startsWith(`${name}=`))
    return match ? decodeURIComponent(match.split('=')[1]) : ''
}

export async function apiFetch(path, options = {}) {
    const method = (options.method || 'GET').toUpperCase()
    const headers = {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken'),
        ...options.headers,
    }
    const response = await fetch(API_URL + path, { ...options, method, headers, credentials: 'include' })

    if (response.status === 401 && !path.startsWith('/me')) {
        onUnauthorized()
    } else if (response.status === 403 && !path.startsWith('/me')) {
        // 403 means either "not logged in" or "not allowed": ask the server which
        const me = await fetch(API_URL + '/me/', { credentials: 'include' })
        if (!me.ok) onUnauthorized()
    }
    return response
}
