<script setup>
import { user } from '../auth.js';


</script>

<template>
    <header>
       <label for="app-drawer" aria-label="toggle sidebar" class="btn btn-square btn-ghost drawer-button">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" stroke-linejoin="round" stroke-linecap="round" stroke-width="2" fill="none" stroke="currentColor" class="my-1.5 inline-block size-4"><path d="M4 4m0 2a2 2 0 0 1 2 -2h12a2 2 0 0 1 2 2v12a2 2 0 0 1 -2 2h-12a2 2 0 0 1 -2 -2z"></path><path d="M9 4v16"></path><path d="M14 10l2 2l-2 2"></path></svg>
        </label>

        <div class="ml-auto flex items-center gap-2">
            <input type="text" placeholder="Search" class="input input-sm w-24 md:w-auto" />

            <div v-if="user" class="dropdown dropdown-end">
                <div tabindex="0" role="button" class="btn btn-ghost btn-circle avatar avatar-placeholder">
                    <div class="bg-neutral text-neutral-content w-10 rounded-full">
                        <span>{{ user.username[0].toUpperCase() }}</span>
                    </div>
                </div>
                <ul tabindex="0" class="menu menu-sm dropdown-content mt-3 p-2 shadow bg-base-100 rounded-box w-52 text-left">
                    <li class="menu-title">{{ user.username }}</li>
                    <li><router-link to="/profile">Profile</router-link></li>
                    <li><router-link to="/logout">Logout</router-link></li>
                </ul>
            </div>
        </div>
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
    padding: 10px 16px;
  }

</style>
