<template>
    <div>
         <select @change="updateData($event)">
            <option v-for="alertes_type in alertes_types" :key="alertes_type.name" v-bind:value="alertes_type.name">{{alertes_type.name}}</option>
        </select>
        <ul>
            <li v-for="alerte in alertes" :key="alerte.id">
                <AlertCard v-bind:alerte="{...alerte, field_name:field_value}"/>
            </li>
        </ul>
    </div>
</template>

<script>
import config from '../config'
import axios from "axios";
import AlertCard from '../components/AlertCard.vue'

export default {
    components: {
        AlertCard
    },
    data () {
        return {
            alertes: [],
            alertes_types: [],
            field_value: ''
        }
    },
    created: async function () {
        let url_types = "http://"+config.host+':'+config.port+"/alertes-types"
        this.$data.alertes_types = (await axios.get(url_types)).data;
        this.$data.field_value = this.$data.alertes_types[0].name
        let url_data = "http://"+config.host+':'+config.port+"/alertes/"+this.$data.field_value;
        this.$data.alertes = (await axios.get(url_data)).data;
    },
    methods: {
        updateData: async function(evt) {
            let url_data = "http://"+config.host+':'+config.port+"/alertes/"+evt.target.value;
            this.$data.field_value = evt.target.value
            this.$data.alertes = (await axios.get(url_data)).data;
        }
    }
}
</script>

<style scoped>
    ul {
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;
        justify-content: center;
    }
    li {
        list-style-type: none;
        width: 20vw;
        margin: 10px;
    }
</style>
