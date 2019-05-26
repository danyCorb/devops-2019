<template>
  <div id="app">
    <h1>Au Bon Beurre - Data Visualizer</h1>
    <li id="routing-list">
      <router-link to="/data-visualizer">Unit Graphs</router-link>
      <router-link to="/alertes">Alertes</router-link>
    </li>
    <router-view />
  </div>
</template>

<script>

import LineChart from './components/LineChart.vue'

export default {
  name: 'line-chart',
  components: {
    LineChart
  }
}
</script>

<style>

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 10px;
}

#routing-list {
  display: flex;
  flex-direction: row;
  justify-content: center;
}

#routing-list a {
  margin: 5px;
  padding: 6px;
  background-color: mediumseagreen;
  color: #fff;
  text-decoration: none;
  transition: background-color 200ms, box-shadow 200ms;
}

#routing-list a.router-link-active {
  background-color: rgb(40, 124, 78);
}


#routing-list a:hover {
  background-color: rgb(40, 124, 78);
  box-shadow: 0 0 3px black;
}


</style>
