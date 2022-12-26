<template>
    <div class="table_responsive">
        <div class="title">
            <h1>Pessoas</h1>
        </div>
        <div class="btn-actions">
            <button class="btn-create" @click="TogglePopup('buttonTrigger')">
                <div class="btn-inside">
                    <font-awesome-icon class="create-ico" icon="fa-solid fa-circle-plus" color="#832727" size="2x" />
                    <p>Cadastrar novas pessoas</p>
                </div>
            </button>
            <button class="refresh-list" @click="this.getPeople()">
                <div class="btn-inside">
                    <font-awesome-icon class=" refresh-icon" icon="fa-solid fa-arrows-rotate" color="#832727"
                        size="2x" />
                    <p>Atualizar lista de pessoas</p>
                </div>
            </button>
        </div>
        <button :disabled="pagination.currentPage <= 1" @click="this.PrevPage()">
            Prev Page
        </button>
        Page {{ pagination.currentPage }} of {{ pagination.totalPages }}
        <button :disabled="pagination.currentPage >= pagination.totalPages" @click.stop.prevent="this.nextPage()">
            Next Page
        </button>
        <table>
            <thead>
                <tr>
                    <th>id pessoa</th>
                    <th>nome</th>
                    <th>cpf</th>
                    <th>rg</th>
                    <th>data de nacimento</th>
                    <th>data de admissão</th>
                    <th>funcao</th>
                    <th>Action</th>
                </tr>
            </thead>
            <tbody v-if="peopleData">
                <TableRowVue v-for="(person, index) in peopleData.data" v-bind:key="index" :id_pessoa="person.id_pessoa"
                    :nome="person.nome" :cpf="person.cpf" :rg="person.rg" :data_nascimento="person.data_nascimento"
                    :data_admissao="person.data_admissao" :funcao="person.funcao" />
            </tbody>
        </table>
    </div>
    <CreatePersonVue v-if="popupTriggers.buttonTrigger" :TogglePopup="() => TogglePopup('buttonTrigger')">
    </CreatePersonVue>
</template>


<script>
import TableRowVue from './TableRow.vue';
import axios from "axios";
import CreatePersonVue from "@/components/TablePeople/Modal/CreatePerson.vue";
import { ref } from 'vue';
import { computed, reactive, watch } from 'vue';


const pagination = reactive({
    currentPage: 1,
    perPage: 12,
    responseLength: 0,
    totalPages: computed(() =>
        Math.ceil(pagination.responseLength / pagination.perPage)
    ),
});

export default {
    name: 'TablePeople',
    components: {
        TableRowVue,
        CreatePersonVue
    },
    data: () => {
        return {
            peopleData: null,
            limit: 12,
            offset: 0
        }
    },
    methods: {
        async getPeople() {
            try {
                let response = await axios.get(`http://localhost:5000/people?limit=${this.limit}&offset=${this.offset}`, { headers: { "Access-Control-Allow-Origin": "*", } })
                this.peopleData = response.data
                this.pagination.responseLength = this.peopleData.total
            }
            catch (error) {
                this.login_error = true
            };
        },

        async nextPage() {
            this.offset += 12
            this.pagination.currentPage++
            await this.getPeople()

        },

        async PrevPage() {
            this.offset -= 12
            this.pagination.currentPage--
            await this.getPeople()

        }
    },
    setup() {
        const popupTriggers = ref({
            buttonTrigger: false,
            timedTrigger: false
        });
        const TogglePopup = (trigger) => {
            popupTriggers.value[trigger] = !popupTriggers.value[trigger]
        };


        return {
            pagination,
            popupTriggers,
            TogglePopup,
            CreatePersonVue
        }
    },
    async mounted() {
        this.getPeople()
    },
}
</script>


<style lang="scss" scoped>
p {
    margin-bottom: 0;
}

.title {
    display: flex;
    justify-content: center;
    margin-bottom: 2%;
}

.table_responsive {
    justify-items: center;
}

table {
    width: 100%;
    font-size: 13px;
    color: #444;
    white-space: nowrap;
    border-collapse: collapse;
}

table>thead {
    background-color: #d40000;
    color: #fff;
}

table>thead th {
    padding: 15px;
}

table>tbody>tr {
    background-color: #fff;
    transition: 0.3s ease-in-out;
}

table>tbody>tr:nth-child(even) {
    background-color: rgb(238, 238, 238);
}

table>tbody>tr:hover {
    filter: drop-shadow(0px 2px 6px rgba(255, 0, 0, 0.291));
}

.btn-actions {
    display: flex;
    justify-content: center;
    margin-bottom: 0.2%;
}

.btn-actions {
    margin-right: 10%;
}

.create-ico {
    color: #b60000;
    transition: 0.3s ease-in-out;
}

.btn-create,
.refresh-list {
    display: inline-flex;
    margin-right: 10%;
    border: 0;
    background-color: transparent;
    transition: 0.3s ease-in-out;
    border-radius: 12px;
}

.btn-create:hover,
.refresh-list:hover {
    background-color: rgba(182, 0, 0, .2);
    font-weight: bold;
    color: #fff;
}

.btn-inside {
    width: 200px;
    display: inline-flex;
    justify-content: space-around;
    /* center the content horizontally */
    align-items: center;
    /* center the content vertically */
    margin-right: 10%;
}

.refresh-icon {
    color: #b60000;
    transition: 0.3s ease-in-out;
}
</style>