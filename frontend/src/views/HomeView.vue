<script setup>
import { user } from '../auth.js';
import {apiFetch} from "../api.js";
import {onMounted, ref} from "vue";


const total_purchases = ref(0)
const purchased_items = ref(0)
const shipments = ref(0)

async function fetchStats() {
  const response = await apiFetch('/stats/');
  if (!response.ok) return;
  const data = await response.json()
  total_purchases.value = data.total_purchases;
  purchased_items.value = data.purchased_items;
  shipments.value = data.shipments;
}

onMounted(fetchStats)



const faqs = [
    { question: 'How do I see the items in a purchase?', answer: 'Open Purchases and click a row. It expands to show its items.' },
    { question: 'What format is a tracking number?', answer: 'TRACK followed by 6 digits, for example TRACK646850.' },
    { question: "Why can't I open Shipping Status?", answer: 'Only users in the Managers group can look up shipments.' },
    { question: 'Where does this data come from?', answer: 'It is demo data generated with Faker, for practice.' },
]

</script>


<template>
    <div>
        <h1 class="text-3xl font-bold mb-3">Welcome back, {{ user?.first_name }}!</h1>
        <p class="mb-12 text/lg opacity-70">Pick a section below to browse your data, or look up a shipment by its tracking number.</p>

        <div class="stats shadow w-full mb-12">
            <div class="stat">
                <div class="stat-title">Total Purchases</div>
                <div class="stat-value">{{ total_purchases.toLocaleString() }}</div>
                <div class="stat-desc">all time</div>
                <div class="stat-figure text-secondary">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="inline-block h-8 w-8 stroke-current">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.75 10.5V6a3.75 3.75 0 1 0-7.5 0v4.5m11.356-1.993 1.263 12c.07.665-.45 1.243-1.119 1.243H4.25a1.125 1.125 0 0 1-1.12-1.243l1.264-12A1.125 1.125 0 0 1 5.513 7.5h12.974c.576 0 1.059.435 1.119 1.007ZM8.625 10.5a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm7.5 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Z"></path>
                    </svg>
                </div>
            </div>

            <div class="stat">
                <div class="stat-title">Shipments</div>
                <div class="stat-value">{{ shipments.toLocaleString() }}</div>
                <div class="stat-desc">tracked</div>
                <div class="stat-figure text-secondary">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="inline-block h-8 w-8 stroke-current">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.25 18.75a1.5 1.5 0 0 1-3 0m3 0a1.5 1.5 0 0 0-3 0m3 0h6m-9 0H3.375a1.125 1.125 0 0 1-1.125-1.125V14.25m17.25 4.5a1.5 1.5 0 0 1-3 0m3 0a1.5 1.5 0 0 0-3 0m3 0h1.125c.621 0 1.129-.504 1.09-1.124a17.902 17.902 0 0 0-3.213-9.193 2.056 2.056 0 0 0-1.58-.86H14.25M16.5 18.75h-2.25m0-11.177v-.958c0-.568-.422-1.048-.987-1.106a48.554 48.554 0 0 0-10.026 0 1.106 1.106 0 0 0-.987 1.106v7.635m12-6.677v6.677m0 4.5v-4.5m0 0h-12"></path>
                    </svg>
                </div>
            </div>

            <div class="stat">
                <div class="stat-title">Purchased Items</div>
                <div class="stat-value">{{ purchased_items.toLocaleString() }}</div>
                <div class="stat-desc">all time</div>
                <div class="stat-figure text-secondary">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="inline-block h-8 w-8 stroke-current">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.25 3h1.386c.51 0 .955.343 1.087.835l.383 1.437M7.5 14.25a3 3 0 0 0-3 3h15.75m-12.75-3h11.218c1.121-2.3 2.1-4.684 2.924-7.138a60.114 60.114 0 0 0-16.536-1.84M7.5 14.25 5.106 5.272M6 20.25a.75.75 0 1 1-1.5 0 .75.75 0 0 1 1.5 0Zm12.75 0a.75.75 0 1 1-1.5 0 .75.75 0 0 1 1.5 0Z"></path>
                    </svg>
                </div>
            </div>
        </div>

        <div class="grid grid-cols-3 gap-8">
            <div class="bg-base-100 p-4 rounded-lg shadow flex flex-col gap-3">
                <h2 class="text-lg font-bold">Countries</h2>
                <p class="flex-1">Reference data for every country: codes, addresses and VAT.</p>
                <router-link to="/countries" class="btn btn-sm btn-warning self-center">Open countries</router-link>
            </div>

            <div class="bg-base-100 p-4 rounded-lg shadow flex flex-col gap-3">
                <h2 class="text-lg font-bold">Shipments</h2>
                <p class="flex-1">Look up a shipment by its tracking number.</p>
                <router-link to="/shipping-status" class="btn btn-sm btn-warning self-center">Open shipments</router-link>
            </div>

            <div class="bg-base-100 p-4 rounded-lg shadow flex flex-col gap-3">
                <h2 class="text-lg font-bold">Purchases</h2>
                <p class="flex-1">Browse all purchases, and open a row to see its items.</p>
                <router-link to="/purchases" class="btn btn-sm btn-warning self-center">Open purchases</router-link>
            </div>
        </div>

        <h2 class="text-xl font-semibold mt-12 mb-4">Frequently asked questions</h2>

        <div class="join join-vertical w-full">
            <div v-for="(faq, i) in faqs" :key="i" class="collapse collapse-arrow join-item border border-base-300 bg-base-100">
                <input type="radio" name="faq" :checked="i === 0" />
                <div class="collapse-title font-semibold text-left">{{ faq.question }}</div>
                <div class="collapse-content text-left text-sm">{{ faq.answer }}</div>
            </div>
        </div>
    </div>
</template>

<style scoped>
</style>