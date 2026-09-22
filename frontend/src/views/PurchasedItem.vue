<script setup>

import { ref, onMounted, watch } from 'vue'
import { FlexRender, tableFeatures, useTable } from '@tanstack/vue-table'

const features = tableFeatures({})
const purchasedItems = ref([])
const columns = [
    { header: 'Purchase', accessorKey: 'purchase' },
    { header: 'Product Name', accessorKey: 'product_name' },
    { header: 'Quantity', accessorKey: 'quantity' },
    { header: 'Unit Price', accessorKey: 'unit_price' },
]

const table = useTable({
    data: purchasedItems,
    columns,
    features
})

const page = ref(1)
const totalCount = ref(0)
const hasNext = ref(false)
const hasPrevious = ref(false)

async function fetchPurchasedItems() {
    const params = new URLSearchParams({ page: page.value })
    const response = await fetch(`http://localhost:8000/api/purchased-items/?${params.toString()}`)
    const data = await response.json()
    purchasedItems.value = data.results
    totalCount.value = data.count
    hasNext.value = !!data.next
    hasPrevious.value = !!data.previous
}

function nextPage() {
    if (hasNext.value) page.value++
}
function prevPage() {
    if (hasPrevious.value) page.value--
}   

watch(page, fetchPurchasedItems)
onMounted(fetchPurchasedItems)

</script>
