<template>
    <div class="popup">
        <div class="popup-inner">
            <div class="title">
                <h2>Criar novo Pessoa</h2>
            </div>
            <form class="create-item">
                <div id="item"> <label>Nome</label>
                    <input type="text" v-model=this.name placeholder="Nome">
                </div>
                <div id="item"> <label>CPF</label>
                    <input type="text" v-maska data-maska="###.###.###-##" v-model=this.cpf placeholder="CPF">
                </div>
                <div id="item"> <label>RG</label>
                    <input type="text" v-maska data-maska="##.###.###-#" v-model=this.rg placeholder="RG">
                </div>
                <div id="item"> <label>data de nacimento</label>
                    <input type="date" v-model=this.data_nascimento placeholder="Data nascimento">
                </div>
                <div id="item"> <label>Função</label>
                    <input type="text" v-model=this.funcao placeholder="Funcão">
                </div>
            </form>

            <div class="buttons">
                <button type="button" class="btn-save" @click="createPerson(); TogglePopup()"> 
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
    name: "CreatePerson",
    directives: { maska: vMaska },
    data() {
        return {
            name: '',
            cpf: '',
            rg: '',
            data_nascimento: '',
            funcao: ''
        }
    },
    props: ['TogglePopup'],
    methods: {
        onFileChange(e) {
            this.file = e.target.files[0]
            if (!this.file.length)
                return;
        },
        async createPerson(){

            let register_data = {
                nome: this.name,
                cpf: this.cpf,
                rg: this.rg,
                data_nascimento: this.data_nascimento,
                funcao: this.funcao
            }
            
            console.log(register_data)

            axios.post("http://localhost:5000/person", register_data, { headers: { "Access-Control-Allow-Origin": "*", } })
                .then((res) => {
                    console.log(res.data)
                })
                .catch((error) => {
                    console.log(error);
                });
        },
    },
    mounted() {
        this.getCategory()
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
    display: grid;
    margin-right: 20%;


}

#item-dropdown {
    display: grid;
    /* justify-items: center; */
}

label {
    display: inline-block;
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


.create-item {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    grid-template-rows: 1fr 1fr 1fr;
    gap: 0px 42px
}
</style>