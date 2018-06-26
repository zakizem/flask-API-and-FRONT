// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import BootstrapVue from 'bootstrap-vue'

import VueRouter from 'vue-router';
// import { store } from './store/store';
import { routes } from './router/index';

Vue.use(VueRouter);

Vue.config.productionTip = false

const router = new VueRouter({
  routes: routes,
});

// GLobal BEFORE hooks:
router.beforeEach((to, from, next) => {
  console.log("\n");
  console.log('Global -- beforeEach - fired')

  if (to.path === '/Protected') {

    next('/Auth')
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
  console.log('Global -- beforeResolve - fired.')
  next()
})

// GLobal AFTER hooks:
router.afterEach((to, from) => {
  // This fires after each route is entered.
  console.log(`Global -- afterEach - Just moved from '${from.path}' to '${to.path}'`)
})

new Vue({
  el: '#app',
  router: router,
  components: { App },
  template: '<App/>'
})
