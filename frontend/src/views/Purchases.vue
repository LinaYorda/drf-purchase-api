    <script setup>
    import { ref, onMounted, watch } from 'vue'
    import { FlexRender, tableFeatures, useTable } from '@tanstack/vue-table'
    import { apiFetch } from '../api.js'

    const features = tableFeatures({})
    const purchases = ref([])
    const columns = [
        { header: 'Title', accessorKey: 'title' },
        { header: 'City', accessorKey: 'city' },
        { header: 'Country', accessorKey: 'country' },
        { header: 'Continent', accessorKey: 'continent' },
        { header: 'Purchase Date', accessorKey: 'purchase_date' }, 
        { header: 'Price', accessorKey: 'price' }, 
        
    ]

    const table = useTable({
        data: purchases,
        columns,
        features
    })

    const page = ref(1)
    const totalCount = ref(0)
    const hasNext = ref(false)
    const hasPrevious = ref(false)
    const searchValue = ref('')

    const expanded = ref(new Set())
    function toggle(id) {
        expanded.value.has(id) ? expanded.value.delete(id) : expanded.value.add(id)
    }

    async function fetchCountries() {
        const params = new URLSearchParams({ page: page.value })
        if (searchValue.value) {
            params.set('search', searchValue.value)
        }
        const response = await apiFetch(`/purchases/?${params.toString()}`)
        if (!response.ok) return
        const data = await response.json()
        purchases.value = data.results
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

    watch([searchValue, page], fetchCountries)
    onMounted(fetchCountries)
    </script>

    <template>
      <div class="card bg-base-100 shadow-sm w-full">
        <div class="card-body">
          <div class="flex items-center justify-between gap-2 mb-4">
            <h2 class="text-lg font-bold text-gray-500">Purchases Table</h2>

            <label class="input">
              <svg class="h-[1em] opacity-50" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                <g stroke-linejoin="round" stroke-linecap="round" stroke-width="2.5" fill="none" stroke="currentColor">
                  <circle cx="11" cy="11" r="8"></circle>
                  <path d="m21 21-4.3-4.3"></path>
                </g>
              </svg>
              <input v-model="searchValue" type="search" placeholder="Search countries..." />
            </label>
          </div>

          <div class="relative overflow-auto" style="max-height: clamp(200px, calc(100vh - 348px), 900px)">
            <table class="table table-zebra text-sm">
              <thead>
                <tr v-for="headerGroup in table.getHeaderGroups()" :key="headerGroup.id">
                  <th class="sticky top-0 bg-base-100 z-10"></th>
                  <th
                    v-for="header in headerGroup.headers"
                    :key="header.id"
                    class="sticky top-0 bg-base-100 z-10"
                  >
                    <FlexRender v-if="!header.isPlaceholder" :header="header" />
                  </th>
                </tr>
              </thead>
              <tbody>
                <template v-for="row in table.getRowModel().rows" :key="row.id">
                  <tr class="hover:bg-base-200 cursor-pointer" @click="toggle(row.original.id)">
                    <td>{{ expanded.has(row.original.id) ? '▾' : '▸' }}</td>
                    <td v-for="cell in row.getAllCells()" :key="cell.id">
                      <FlexRender :cell="cell" />
                    </td>
                  </tr>

                  <tr v-if="expanded.has(row.original.id)">
                    <td :colspan="columns.length + 1" class="bg-base-200">
                      <table v-if="row.original.items.length" class="table table-xs">
                        <thead>
                          <tr><th>Product</th><th>Quantity</th><th>Unit price</th></tr>
                        </thead>
                        <tbody>
                          <tr v-for="item in row.original.items" :key="item.id">
                            <td>{{ item.product_name }}</td>
                            <td>{{ item.quantity }}</td>
                            <td>{{ item.unit_price }}</td>
                          </tr>
                        </tbody>
                      </table>
                      <span v-else class="opacity-60">No items for this purchase</span>
                    </td>
                  </tr>
                </template>
              </tbody>
            </table>
          </div>

          <div class="flex items-center justify-end gap-4 mt-4">
            <button class="btn btn-sm" :disabled="!hasPrevious" @click="prevPage">Previous</button>
            <span>Page {{ page }} ({{ totalCount }} total)</span>
            <button class="btn btn-sm" :disabled="!hasNext" @click="nextPage">Next</button>
          </div>
        </div>
      </div>
    </template>