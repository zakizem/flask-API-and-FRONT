// Make sure to call Vue.use(Vuex) first if using a module system
import Vue from 'vue'
import Vuex from 'vuex'

import createPersistedState from "vuex-persistedstate";
import * as Cookies from "js-cookie";

Vue.use(Vuex)

const infoStore = new Vuex.Store({
  state: {
    infos: {'login': false, 'prenom': ''},
  },
  plugins: [createPersistedState({
    // storage: {
    //   getItem: key => Cookies.get(key),
    //   setItem: (key, value) => Cookies.set(key, value, { expires: 3, secure: true }),
    //   removeItem: key => Cookies.remove(key)
    // }
  })],
  mutations: {
    addInfo(state, info) {
      state.infos = Object.assign(state.infos, info);
      // localStorage.setItem('monChat', 'Tom');
    },
    infoInit(state) {
      state.infos= {'prenom': '', 'login': false}
    },
    login(state) {
      state.infos['login']= true
    }
  },
})

export default infoStore;
