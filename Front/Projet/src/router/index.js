import Vue from 'vue'
import Router from 'vue-router'
import Accueil from '@/components/Accueil'
import Identification from '@/components/Identification'
import MonComposant from '@/components/MonComposant'
import Auth from '@/components/Auth'



Vue.use(Router)



export default new Router({
  routes: [
    {
      path: '/',
      name: 'Accueil',
      component: Accueil
    },
    {
      path: '/Identification',
      name: 'Identification',
      component: Identification
    },
    {
      path: '/Formulaire',
      name: 'MonComposant',
      component: MonComposant
    },
    {
      path: '/Auth',
      name: 'Auth',
      component: Auth
    }
  ]
})
