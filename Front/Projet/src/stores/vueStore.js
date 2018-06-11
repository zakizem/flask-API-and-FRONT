// Make sure to call Vue.use(Vuex) first if using a module system
import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)

const vueStore = new Vuex.Store({
  state: {
    count: 0,
    message: ''
  },
  mutations: {
    increment (state) {
      state.count++
    },
    decrement (state) {
      state.count--
    },
    EcrireMessage (state, message) {
      state.message = message
    }
  }
})

export default vueStore;
