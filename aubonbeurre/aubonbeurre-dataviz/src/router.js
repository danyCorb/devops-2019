import Router from 'vue-router'
import Vue from 'vue'

import DataVisualizer from './view/data-visualizer.page'
import AlertingPage from './view/alerting.vue'

Vue.use(Router)

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        { path: '/data-visualizer', component: DataVisualizer },
        { path: '/alertes', component: AlertingPage },
    ]
})