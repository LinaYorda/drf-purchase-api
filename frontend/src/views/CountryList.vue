<script setup>
import { ref, onMounted, watch } from 'vue'
import { FlexRender, tableFeatures, useTable } from '@tanstack/vue-table'

const features=tableFeatures({})
const countries = ref([])
const columns = [
    {
        header: 'Country Name',
        accessorKey: 'name',
    },
    {
        header: 'Local Address',
        accessorKey: 'local_address',
    },

    {
        header: 'Local Code',
        accessorKey: 'local_code',
    }, 
    {
        header: 'Country Code',
        accessorKey: 'country_code',
    },
    {
        header: 'Local VAT',
        accessorKey: 'local_vat',
    }
]


const table = useTable({
    data: countries,
    columns,
    features
})

  const page = ref(1)                                                                                                                                                 
  const totalCount = ref(0)                                                                                                                                           
  const hasNext = ref(false)                                                                                                                                          
  const hasPrevious = ref(false)                                                                                                                                      
                                                                                                                                                                      
  async function fetchCountries() {                                                                                                                                   
      const response = await fetch(`http://localhost:8000/api/countries/?page=${page.value}`)                                                                         
      const data = await response.json()                                                                                                                              
      countries.value = data.results                                                                                                                                  
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
                                                                                                                                                                      
  watch(page, fetchCountries)                                                                                                                                         
  onMounted(fetchCountries)                           

</script>

<template>
    <div class = "country-table">
        <div class = "table-scroll">
            <table>
                <thead>
                    <tr v-for="headerGroup in table.getHeaderGroups()" :key="headerGroup.id">
                        <th v-for="header in headerGroup.headers" :key="header.id">
                            <FlexRender v-if="!header.isPlaceholder" :header="header" />
                        </th>
                    </tr>    
                </thead>
                <tbody>
                    <tr v-for="row in table.getRowModel().rows" :key="row.id">
                        <td v-for="cell in row.getAllCells()" :key="cell.id">
                            <FlexRender :cell="cell" />
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div class = "pagination-bar">
            <button :disabled="!hasPrevious" @click="prevPage">Previous</button>
            <span>Page {{ page }} ({{ totalCount }} total)</span>
            <button :disabled="!hasNext" @click="nextPage">Next</button>
        </div>
    </div>
</template>



<style scoped>

.country-table {
    background: #fff;
    border:1px solid #ddd;
    border-radius:8px;
    box-shadow: hidden;
}

.table-scroll {
    max-height: clamp(300px, 70vh, 1000px); 
    overflow-y: auto;
}

table {
    border-collapse: collapse;
    width: 100%;
}

th, td {
    border: 1px solid #ccc;
    padding: 8px 12px;
    text-align: left;
}

th {
    background-color: #bdcad7;
    font-weight: bold;
    position: sticky;
    top: 0;
    z-index: 1;
}

tbody tr:nth-child(even) {
    background-color: #f5f5f5;
}

tbody tr:hover {
    background-color: #e8f0f7;
}

.pagination-bar {
    display: flex;
    align-items:center;
    justify-content: flex-end;
    gap:16px;
    padding: 12px 16px;
    border-top:1px solid #ddd;
    background: #f9fafb;
}
</style>
