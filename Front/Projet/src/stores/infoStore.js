// Make sure to call Vue.use(Vuex) first if using a module system
import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)

const infoStore = new Vuex.Store({
  state: {
    infos: {'login': false, 'prenom': ''},
  },
  mutations: {
    addInfo(state, info) {
      state.infos = Object.assign(state.infos, info);
    },
    infoInit(state) {
      state.infos= {'prenom': '', 'login': false}
    },
    login(state) {
      state.infos['login']= true
    }
  }
})

export default infoStore;
