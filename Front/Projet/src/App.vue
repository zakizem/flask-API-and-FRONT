<template>
<div id="app">

  <!-- <img src="./assets/logo.png"> -->

  <Header></Header>
  <br>
  <router-link :to="{ name: 'Questionnaire' }">Questionnaire</router-link>&nbsp;
  <router-link :to="{ name: 'Accueil' }">Accueil</router-link>&emsp;
  <router-link :to="{ name: 'Protected' }">Protected</router-link>&nbsp;

  <br><br><br>
  <router-view/>

  <br><br>
  <br> {{message}} <br>

</div>
</template>

<script>
import Header from './components/Header'

import vueStore from "./stores/vueStore"

export default {
  name: 'App',
  components: {
    Header,
  },
  computed: {
    message() {
      return vueStore.state.message
    },
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 5px;
}
</style>
