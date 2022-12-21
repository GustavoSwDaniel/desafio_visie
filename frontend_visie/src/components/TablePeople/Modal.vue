<template>
	<div class="popup">
		<div class="popup-inner">
            <p>Tem certeza que deseja excluir este Pessoa?</p>
            <div class="buttons">
                <button type="button" class="btn-yes" @click="TogglePopup(); DeletePerson()">
                    Sim
                </button>
                <button type="button" class="btn-not" @click="TogglePopup()">
                    Não
                </button>
            </div>
		</div>
	</div>
</template>

<script>
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"
import axios from "axios";


import UpdatePersonVue from "./UpdatePerson.vue";

export default {
	props: ['TogglePopup', 'id_pessoa'],
    components: {
        UpdatePersonVue
    },

    methods: {
        async DeletePerson() {
            try {
                let response = await axios.delete(`http://localhost:5000/person/${this.id_pessoa}`, { headers: { "Access-Control-Allow-Origin": "*", 'Content-Type': 'application/json' }})
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
		padding: 32px;
	}
}

.popup-inner{
    display: flex;
    justify-content: center;
    flex-direction: column;
}

.buttons {
    display: flex;
    justify-content: center;
    flex-direction: row;
}


.btn-yes{
    border-radius: 12px;
    width: 70px;
    height: 40px;
    border-color: #fff;
    color: #fff;
    background-color: #006c0b;
    transition: 0.5s ease-in-out;
}


.btn-not{
    border-radius: 12px;
    width: 70px;
    height: 40px;
    border-color: #fff;
    color: #fff;
    background-color: #a10404;
    transition: 0.5s ease-in-out;
}


.btn-yes:hover {
    background-color: #29a836;
}

.btn-not:hover {
    background-color: #e60202;
}
</style>