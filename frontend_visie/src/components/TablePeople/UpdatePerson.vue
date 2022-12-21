<template>
    <div class="popup">
        <div class="popup-inner">
            <div class="title">
                <h2>Editar Pessoa</h2>
            </div>
            <form class="update-item">
                <div id="item">
                    <label>Uuid</label>
                    <input id="uuid-inp" type="text" placeholder="uuid" :value="this.id_pessoa" disabled>
                </div>
                <div id="item"> <label>Nome</label>
                    <input type="text" v-model=this.new_nome placeholder="Name">
                </div>
                <div id="item"> <label>cpf</label>
                    <input type="text" v-maska data-maska="###.###.###-##" v-model=this.new_cpf placeholder="CPF">
                </div>
                <div id="item"> <label>RPG</label>
                    <input type="text" v-maska data-maska="##.###.###-#" v-model=this.new_rg placeholder="RG">
                </div>
                <div id="item"> <label>Funcao</label>
                    <input type="text" v-model=this.new_funcao  placeholder="Funcao">
                </div>
            </form>

            <div class="buttons">
                <button type="button" class="btn-save" @click="UpdatePerson(); TogglePopup()">
                    Salvar
                </button>
                <button type="button" class="btn-cancel" @click="TogglePopup()">
                    Cancelar
                </button>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";

import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"

import { vMaska } from "maska"


export default {
    name: "UpdatePerson",
    props: ['id_pessoa', 'nome', 'cpf', 'rg', 'funcao', 'TogglePopup'],
    directives: { maska: vMaska },
    data() {
        return {
            new_nome: this.nome,
            new_cpf: this.cpf,
            new_rg: this.rg,
            new_funcao: this.funcao
        }
    },
    methods: {
        async UpdatePerson() {
            var update_data = {
                nome: this.new_nome,
                cpf: this.new_cpf,
                rg: this.new_rg,
                funcao: this.new_funcao
            };

            console.log(update_data)

            try {
                let response = await axios.patch(`http://localhost:5000/person/${this.id_pessoa}`, update_data, { headers: { "Access-Control-Allow-Origin": "*", 'Content-Type': 'application/json' }})
                console.log(response)

            }
            catch (error) {
                this.login_error = true
            };
        }
    }
}
</script>

<style lang="scss" scoped>
.popup {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    z-index: 99;
    background-color: rgba(0, 0, 0, 0.2);

    display: flex;
    align-items: center;
    justify-content: center;

    .popup-inner {
        background: #FFF;
        padding: 100px;
    }
}

#uuid-inp {
    width: 280px;
}

.title {
    display: flex;
    justify-content: center;
    margin-bottom: 2%;
}

.popup-inner {
    display: flex;
    justify-content: center;
    flex-direction: column;
}

.buttons {
    display: flex;
    justify-content: center;
    flex-direction: row;
}

#item {
    margin-bottom: 10px;
}

label {
    display: inline-block;
    width: 40%;
}

.btn-save {
    border-radius: 12px;
    width: 70px;
    height: 40px;
    border-color: #fff;
    color: #fff;
    background-color: #006c0b;
    transition: 0.5s ease-in-out;
    margin-top: 2%;
}


.btn-cancel {
    border-radius: 12px;
    width: 70px;
    height: 40px;
    border-color: #fff;
    color: #fff;
    background-color: #a10404;
    transition: 0.5s ease-in-out;
    margin-top: 2%;
}

.btn-save:hover {
    background-color: #00a310;
}

.btn-cancel:hover {
    background-color: #b72d2d;
}

.update-item {
    display: grid;
    grid-gap: 20px 200px;

}
</style>