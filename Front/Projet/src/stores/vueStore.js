// Make sure to call Vue.use(Vuex) first if using a module system
import Vue from 'vue'
import Vuex from 'vuex'

import createPersistedState from "vuex-persistedstate";
import * as Cookies from "js-cookie";

Vue.use(Vuex)

const vueStore = new Vuex.Store({
  strict: true,
  state: {
    count: 0,
    message: ''
  },
  plugins: [createPersistedState({
    storage: {
      getItem: key => Cookies.get(key),
      setItem: (key, value) => Cookies.set(key, value, { expires: 3, secure: true }),
      removeItem: key => Cookies.remove(key)
    }
  })],
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
