// Make sure to call Vue.use(Vuex) first if using a module system
import Vue from 'vue'
import Vuex from 'vuex'

import createPersistedState from "vuex-persistedstate";
import * as Cookies from "js-cookie";

Vue.use(Vuex)

const infoStore = new Vuex.Store({
  strict: true,
  state: {
    infos:{
      'login': false,
      'data': {               // doit être comme dans la BDD, car c'est ce qui s'envoie
        'EtapeCourante': '',
        'identite': {
          'prenom': ''
        },
      },
    },
  },
  plugins: [createPersistedState()],
  mutations: {
    addInfo(state, info) {
      state.infos = Object.assign(state.infos, info);
      // localStorage.setItem('monChat', 'Tom');
    },
    addData(state, input) {
      state.infos['data'] = Object.assign(state.infos['data'], input);
    //   let { key , value } = data
    // console.log("Updating form: ", key, value)
    // if(state.form[key]){
    //   state.form[key] = value
    // }
    },
    addDataCategorie(state, donnees) {
      if (donnees['categorie'] in state.infos['data']){
        state.infos['data'][donnees['categorie']] = Object.assign(state.infos['data'][donnees['categorie']], donnees['info']);
      }
      else {
        state.infos['data'][donnees['categorie']] = donnees['info'];
      }
    },
    infoInit(state) {
      state.infos= {'login': false, 'data': {
        'EtapeCourante': 'identite',
        'identite': {
          'prenom': ''
        },
      },
    }
    },
    dataInit(state){
      state.infos['data']={
        'EtapeCourante': 'identite',
        'identite': {
          'prenom': ''
        },
      }
    },
    login(state) {
      state.infos['login']= true
    }
  },
})

export default infoStore;
