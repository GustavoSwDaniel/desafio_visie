<template>
    <div class="person">
        <TableMasterVue/>
    </div>
</template>
  
<script>
// @ is an alias to /src
import TableMasterVue from '@/components/TablePeople/TableMaster.vue';

export default {
    name: 'PersonView',
    components: {
        TableMasterVue
    }
}
</script>
  