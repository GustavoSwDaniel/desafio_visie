<template>

    <tr>
        <td>{{this.id_pessoa}}</td>
        <td>{{this.nome}}</td>
        <td>{{this.cpf}}</td>
        <td>{{this.rg}}</td>
        <td>{{this.data_nascimento}}</td>
        <td>{{this.data_admissao}}</td>
        <td>{{this.funcao}}</td>
        <td>
            <button type="button" class="btn-edit" @click="() => TogglePopup('buttonTeste')">
                Editar
            </button>
            <button type="button" class="btn-delete" @click="() => TogglePopup('buttonTrigger')">
                Remover
            </button>
        </td>
    </tr>
    <ModalVue v-if="popupTriggers.buttonTrigger" :TogglePopup="() => TogglePopup('buttonTrigger')" :id_pessoa="this.id_pessoa">
    </ModalVue>
    <UpdatePersonVue v-if="popupTriggers.buttonTeste" :TogglePopup="() => TogglePopup('buttonTeste')" :id_pessoa="this.id_pessoa" :nome="this.nome" :cpf="this.cpf" :rg="this.rg" :funcao="this.funcao">
    </UpdatePersonVue>
</template>


<script>
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"

import ModalVue from './Modal.vue';
import UpdatePersonVue from "./UpdatePerson.vue";

import { ref } from 'vue';

export default {
    name: 'TableRow',
    props: ["id_pessoa", "nome", "cpf", "rg", "data_nascimento", "data_admissao", "funcao"],
    components: {
        ModalVue,
        UpdatePersonVue
    },
    setup() {
        const popupTriggers = ref({
            buttonTrigger: false,
            buttonTeste: false,
            timedTrigger: false
        });
        const TogglePopup = (trigger) => {
            popupTriggers.value[trigger] = !popupTriggers.value[trigger]
        }
        
        return {
            ModalVue,
            popupTriggers,
            TogglePopup
        }
    }
}
</script>



<style lang="scss" scoped>
table td {
    width: 110px;
    border: 1px solid #ff000017;
    padding: 10px 15px;
    box-sizing: unset;

}

.btn-edit {
    border-radius: 12px;
    width: 70px;
    height: 40px;
    border-color: #fff;
    color: #fff;
    background-color: #1a008f;
    transition: 0.5s ease-in-out;

}

.btn-edit:hover {
    background-color: #3c24a7;
}

.btn-delete {
    border-radius: 12px;
    width: 70px;
    height: 40px;
    border-color: #fff;
    color: #fff;
    background-color: #a10404;
    transition: 0.5s ease-in-out;
}

.btn-delete:hover {
    background-color: #330404;
}

tr>td>img {
    display: inline-block;
    width: 60px;
    height: 60px;
    object-fit: cover;
    border-radius: 50%;
    border: 4px solid #fff;
    box-shadow: 0 2px 6px #0003;
}

.action_btn {
    display: flex;
    justify-content: center;
    gap: 10px;
}

.action_btn>a {
    text-decoration: none;
    color: #444;
    background: #fff;
    border: 1px solid;
    display: inline-block;
    padding: 7px 20px;
    font-weight: bold;
    border-radius: 3px;
    transition: 0.3s ease-in-out;
}

.action_btn>a:nth-child(1) {
    border-color: #a62626;
}

.action_btn>a:nth-child(2) {
    border-color: orange;
}

.action_btn>a:hover {
    box-shadow: 0 3px 8px #0003;
}

tr:hover {
    filter: drop-shadow(0px 2px 6px rgba(255, 0, 0, 0.291));
}
</style>