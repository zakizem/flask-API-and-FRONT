// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import VueResource from 'vue-resource'
import App from './App'

import BootstrapVue from 'bootstrap-vue'


import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import VueRouter from 'vue-router';
// import { store } from './store/store';
import { routes } from './router/index';

Vue.use(VueRouter);
Vue.use(BootstrapVue);
Vue.use(VueResource);

Vue.config.productionTip = false

import infoStore from "./stores/infoStore"
import vueStore from "./stores/vueStore"

const router = new VueRouter({
  routes: routes,
});

// window.onbeforeunload = function(){
//     return "Are you sure you want to close the window?";
//     console.log('ibezzz');
// },

// GLobal BEFORE hooks:
router.beforeEach((to, from, next) => {
  // console.log("\n");
  // console.log('Global -- beforeEach - fired')

  if (to.path === '/Protected' || to.path === '/Questionnaire') {
    if (infoStore.state.infos['login']===false) {
      next('/Accueil')
      // afficher message ?
    }
    else {
      next()
    }
  }
  else if (to.path === '/Accueil') {
    if (infoStore.state.infos['login']===true) {
      next(false)
    }
    else {
      next()
    }
  }
  else if (to.path === '/error') {
    const err = new Error('My Error Message')
    // pass the error to onError() callback.
    next(err)
  }
  else {
    next()
  }

})

// Global beforeResolve
router.beforeResolve((to, from, next) => {
  // console.log('Global -- beforeResolve - fired.')
  next()
})

// GLobal AFTER hooks:
router.afterEach((to, from) => {
  // This fires after each route is entered.
  // console.log(`Global -- afterEach - Just moved from '${from.path}' to '${to.path}'`)
})

// $(window).unload(function(){
//   localStorage.removeItem(vuex);
//   alert('ibezs')
// });


new Vue({
  el: '#app',
  router: router,
  components: { App },
  template: '<App/>',
})
