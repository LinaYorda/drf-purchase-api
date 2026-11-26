<script setup>
import { ref, onMounted, computed } from 'vue'
import { apiFetch } from '../api.js'



const dialogRef = ref(null)
const countries = ref([])
const streetAddress = ref('')
const city = ref('')
const postalCode = ref('')
const countryId = ref('')
const purchaseDate = ref('')


const items = ref([
  {
    product_name: '', quantity: 1, unit_price: ''
  }
])

function addItem() {
  items.value.push({ product_name: '', quantity: 1, unit_price: ''})
}

function removeItem(index) {
  items.value.splice(index,1)
}

const total = computed(() =>
  items.value.reduce((sum, item) => sum + (Number(item.quantity) || 0) * (Number(item.unit_price) || 0), 0)
)

async function fetchCountries() {
  const response = await apiFetch('/countries/all/')
  if(!response.ok) return
  countries.value = await response.json()
}

function open() {
  dialogRef.value?.showModal()
}

function close() {
  dialogRef.value?.close()
}

onMounted(fetchCountries)

defineExpose({ open, close })
</script>

<template>
  <dialog ref="dialogRef" class="modal">
    <div class="modal-box">
      <h3 class="text-lg font-bold">Add purchases</h3>
      <form class="flex flex-col gap-3 py-4">

        <fieldset class="fieldset">
          <legend class="fieldset-legend">Purchase details</legend>

          <label class="label" for="street-address">Street address</label>
          <input v-model="streetAddress" id="street-address" type="text" class="input w-full" />

          <label class="label" for="city">City</label>
          <input v-model="city" id="city" type="text" class="input w-full" />

          <label class="label" for="postal-code">Postal code</label>
          <input v-model="postalCode" id="postal-code" type="text" class="input w-full" />

          <label class="label" for="country">Country</label>
          <select v-model="countryId" id="country" class="select w-full">
            <option value="" disabled>Select a country...</option>
            <option v-for="country in countries" :key="country.id" :value="country.id">{{ country.name }}</option>
          </select>

          <label class="label" for="purchase-date">Purchase date</label>
          <input v-model="purchaseDate" id="purchase-date" type="date" class="input w-full" />
        </fieldset>

        <div>
          <div class="flex items-center justify-between">
            <label class="label">Items</label>
            <button type="button" class="btn btn-xs btn-warning" @click="addItem">+ Add item</button>
          </div>
          <div v-for="(item, index) in items" :key="index" class="flex gap-2 items-center mt-2">
            <input v-model="item.product_name" type="text" placeholder="Book title" class="input input-sm flex-1" />
            <input v-model.number="item.quantity" type="number" min="1" placeholder="Qty" class="input input-sm w-20" />
            <input v-model.number="item.unit_price" type="number" min="0" step="0.01" placeholder="Unit price" class="input input-sm w-28" />
            <button type="button" class="btn btn-xs btn-ghost" @click="removeItem(index)">x</button>
          </div>
          <p class="text-right font-semibold mt-3">Total: {{ total.toFixed(2) }}</p>
        </div>

      </form>
      <div class="modal-action">
        <button class="btn" @click="close">Close</button>
      </div>
    </div>
    <form method="dialog" class="modal-backdrop">
      <button>close</button>
    </form>
  </dialog>
</template>
