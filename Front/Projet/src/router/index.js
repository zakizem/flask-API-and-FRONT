import Vue from 'vue'
import Router from 'vue-router'
import Accueil from '@/components/Accueil'
import Protected from '@/components/Protected'
import Identification from '@/components/Identification'
import MonComposant from '@/components/MonComposant'
import Auth from '@/components/Auth'

Vue.use(Router)

export const routes = [
      {
        path: '/',
        name: 'Accueil',
        component: Accueil
      },
      {
        path: '/Protected',
        name: 'Protected',
        component: Protected
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
