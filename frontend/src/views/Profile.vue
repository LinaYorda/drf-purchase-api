<script setup>
import { user } from '../auth.js';
import { ref, computed } from 'vue';
import { apiFetch} from '../api.js'

const oldPassword= ref('');
const newPassword=ref('');
const passwordError=ref('');
const passwordSuccess=ref('')
const changingPassword=ref(false)

const accountAgeDays=computed(() => {
  if (!user.value?.date_joined) return null;
  return Math.floor((Date.now() - new Date(user.value.date_joined)) / (1000 * 60 * 60 * 24));
});

const daysSinceLastLogin = computed(() => {
  if (!user.value?.last_login) return null;
  return Math.floor((Date.now() - new Date(user.value.last_login)) / (1000 * 60 * 60 * 24));

});

const joinedWeekday = computed(() => {
  if (!user.value?.date_joined) return null;
  return new Date(user.value.date_joined).toLocaleDateString('en-US', { weekday: 'long'});
})


async function submitPasswordChange() {
  passwordError.value = '';
  passwordSuccess.value = '';
  changingPassword.value = true;

  try {
    const response = await apiFetch('/change-password/', {
      method: 'POST',
      body: JSON.stringify({ old_password: oldPassword.value, new_password: newPassword.value }),
    });
    const data = await response.json();
    if (!response.ok) {
      passwordError.value = Array.isArray(data.detail) ? data.detail.join(' ') : data.detail;
      return;
    }
    passwordSuccess.value = data.detail;
    oldPassword.value = '';
    newPassword.value = '';
  } finally {
    changingPassword.value = false;
  }
}





</script>




<template>
   <div>
    <h2 class="text-3xl font-bold mb-3">Profile</h2>
    <div class="card bg-base-100 shadow-sm w-full mb-6">
      <div class="card-body items-center text-center gap-2">
        <div class="flex flex-col items-center gap-2">
          <div class="avatar avatar-placeholder">
            <div class="bg-neutral text-neutral-content w-20 rounded-full">
              <span class="text-2xl">{{ user?.username[0]?.toUpperCase() }}</span>
            </div>
          </div>
          <h3 class="text-xl font-semibold">{{ user?.username }}</h3>
          <p v-if="user?.first_name || user?.last_name" class="opacity-70">
            {{ user?.first_name }} {{ user?.last_name}}
          </p>
          <div class="flex gap-2">
            <span v-for="group in user?.groups" :key="group" class="badge badge-outline">{{ group }}</span>
          </div>
        </div>

        <div class="flex flex-col justify-center gap-2 text-left">
          <p class="text-sm opacity-60">Member since: {{ user?.date_joined?.slice(0,10) }}</p>
        </div>
      </div>
    </div>
    <div class="grid grid-cols-3 gap-4 w-full">
      <div class="bg-base-100 p-4 rounded-lg shadow">
        <h3 class="font-semibold mb-2">Details</h3>
        <div class="flex flex-col gap-3">
          <div>
            <p class="text-sm opacity-60">Email</p>
            <p class="mb-2">{{ user?.email }}</p>
          </div>
          <div>
            <p class="text-sm opacity-60">Last login</p>
            <p>{{ user?.last_login?.slice(0,10) }}</p>
          </div>
          <div>
            <p class="font-semibold mb-2">Status</p>
            <span v-if="user?.is_active" class="badge badge-success badge-sm">Active</span>
            <span v-if="user?.is_staff" class="badge badge-info badge-sm">Staff</span>
          </div>
        </div>
      </div>
      <div class="bg-base-100 p-4 rounded-lg shadow text-center">
        <form @submit.prevent="submitPasswordChange" class="text-left flex flex-col gap-2">
          <h3 class="font-semibold mb-1">Change password</h3>
          <label class="label" for="old-password">Current password</label>
          <input v-model="oldPassword" id="old-password" type="password" class="input input-sm w-full" autocomplete="current-password" />
          <label class="label" for="new-password">New password</label>
          <input v-model="newPassword" id="new-password" type="password" class="input input-sm w-full" autocomplete="new-password" />
          <p v-if="passwordError" class="text-error text-sm mt-1">{{ passwordError }}</p>
          <p v-if="passwordSuccess" class="text-success text-sm mt-1">{{ passwordSuccess }}</p>
          <button type="submit" class="btn btn-sm btn-warning mt-2" :disabled="changingPassword">Change password</button>
        </form>
      </div>
      <div class="bg-base-100 p-4 rounded-lg shadow">
        <h3 class="font-semibold mb-2">Statistics</h3>
        <div class="flex flex-col gap-3">
          <div>
            <p class="text-sm opacity-60">Account age</p>
            <p class="mb-2">{{ accountAgeDays }} day{{ accountAgeDays === 1 ? '' : 's'}}</p>
          </div>
          <div>
            <p class="text-sm opacity-60">Last Active</p>
            <p>{{ daysSinceLastLogin}} day{{ daysSinceLastLogin === 1 ? '' : 's' }} ago</p>
          </div>
          <div>
            <p class="text-sm opacity-60">Joined on a</p>
            <p>{{ joinedWeekday }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>



<style scoped>


</style>