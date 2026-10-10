<script setup>
import { user } from '../auth.js';

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
    <div class="grid grid-cols-2 gap-4 w-full ">
      <div class="bg-base-100 p-4 rounded-lg shadow">
        <h3 class="font-semibold mb-2">Details</h3>
        <p class="text-sm opacity-60">Email</p>
        <p class="mb-2">{{ user?.email }}</p>
        <p class="text-sm opacity-60">Last login</p>
        <p>{{ user?.last_login?.slice(0,10) }}</p>

      </div>
      <div class="bg-base-100 p-4 rounded-lg shadow text-center">
        <h3 class="font-semibold mb-2">Status</h3>
        <div class="flex gap-2 justify-center">
          <span v-if="user?.is_active" class="badge badge-success badge-sm">Active</span>
          <span v-if="user?.is_staff" class="badge badge-info badge-sm">Staff</span>
        </div>
      </div>
    </div>


  </div>
</template>



<style scoped>


</style>