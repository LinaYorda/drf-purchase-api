<script setup>
import { user } from '../auth.js';

const faqs = [
    { question: 'How do I see the items in a purchase?', answer: 'Open Purchases and click a row. It expands to show its items.' },
    { question: 'What format is a tracking number?', answer: 'TRACK followed by 6 digits, for example TRACK646850.' },
    { question: "Why can't I open Shipping Status?", answer: 'Only users in the Managers group can look up shipments.' },
    { question: 'Where does this data come from?', answer: 'It is demo data generated with Faker, for practice.' },
]

</script>


<template>
    <div>
        <h1 class="text-3xl font-bold mb-3">Welcome back, {{ user?.username }}!</h1>
        <p class="mb-12 text/lg opacity-70">Pick a section below to browse your data, or look up a shipment by its tracking number.</p>

        <div class="stats shadow w-full mb-12">
            <div class="stat">
                <div class="stat-title">Total Purchases</div>
                <div class="stat-value">1,000</div>
                <div class="stat-desc">all time</div>
                <div class="stat-figure text-secondary">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="inline-block h-8 w-8 stroke-current">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                    </svg>
                </div>
            </div>

            <div class="stat">
                <div class="stat-title">Shipments</div>
                <div class="stat-value">1,000</div>
                <div class="stat-desc">tracked</div>
                <div class="stat-figure text-secondary">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="inline-block h-8 w-8 stroke-current">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                    </svg>
                </div>
            </div>

            <div class="stat">
                <div class="stat-title">Purchased Items</div>
                <div class="stat-value">1,000</div>
                <div class="stat-desc">all time</div>
                <div class="stat-figure text-secondary">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="inline-block h-8 w-8 stroke-current">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                    </svg>
                </div>
            </div>
        </div>

        <div class="grid grid-cols-3 gap-8">
            <div class="bg-base-100 p-4 rounded-lg shadow flex flex-col gap-3">
                <h2 class="text-lg font-bold">Countries</h2>
                <p class="flex-1">Reference data for every country: codes, addresses and VAT.</p>
                <router-link to="/countries" class="btn btn-sm self-center">Open countries</router-link>
            </div>

            <div class="bg-base-100 p-4 rounded-lg shadow flex flex-col gap-3">
                <h2 class="text-lg font-bold">Shipments</h2>
                <p class="flex-1">Look up a shipment by its tracking number.</p>
                <router-link to="/shipping-status" class="btn btn-sm self-center">Open shipments</router-link>
            </div>

            <div class="bg-base-100 p-4 rounded-lg shadow flex flex-col gap-3">
                <h2 class="text-lg font-bold">Purchases</h2>
                <p class="flex-1">Browse all purchases, and open a row to see its items.</p>
                <router-link to="/purchases" class="btn btn-sm self-center">Open purchases</router-link>
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