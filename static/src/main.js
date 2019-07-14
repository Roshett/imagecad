import Vue from 'vue'
import BootstrapVue from 'bootstrap-vue'
import Vuex from 'vuex'
import App from './App.vue'
import store from './store'

Vue.use(BootstrapVue)
Vue.use(Vuex)

new Vue({
  el: '#app',
  render: h => h(App)
})
