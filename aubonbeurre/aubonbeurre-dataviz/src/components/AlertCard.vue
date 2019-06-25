<template>
    <div class="alert-card">
        <p>Le {{alerte.date_recording}}</p>
        <p>Unit: {{alerte.unit_number}} - {{alerte.unit_name}} / {{alerte.unit_location}}</p>
        <p>Automate: {{alerte.automat_number}} / Type 0x{{alerte.automate_type.toString(16)}}</p>
        <p><strong>{{alerte.field_name}}  =  {{alerte.level.toFixed(2)}}</strong></p>
        <p>Valeur atendue : {{alerte.critical_level_min.toFixed(2)}} &gt &lt {{alerte.critical_level_max.toFixed(2)}} </p>
        
    </div>
</template>

<script>
export default {
    props: {
        'alerte': Object
    },
}
</script>

<style scoped>
.alert-card {
    min-width: 300px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    background-color: #ffdddd;
    padding: 20px 40px;
}

</style>
