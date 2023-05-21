// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import axios from 'axios'
import Echarts from 'echarts'
import VueCookies from 'vue-cookies'
import VueNeo4j from 'vue-neo4j'
import lottie from 'vue-lottie'
Vue.component('lottie', lottie)
Vue.use(VueNeo4j)
Vue.prototype.echarts = Echarts
Vue.use(Echarts)
Vue.prototype.axios = axios
Vue.config.productionTip = false
Vue.use(VueCookies)
Vue.use(ElementUI)
new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
