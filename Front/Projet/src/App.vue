<template>
  <div id="app">

    <!-- <img src="./assets/logo.png"> -->

    <router-link :to="{ name: 'Identification'}">Identification</router-link>
    <router-link :to="{ name: 'MonComposant' }">Formulaire</router-link>
    <br><br><br>
    <router-view/>

  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld'
import MonComposant from './components/MonComposant'
import Accueil from './components/Accueil'
import Identification from './components/Identification'

export default {
  name: 'App',
  components: {
    MonComposant,
    Accueil,
    Identification
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
  margin-top: 60px;
}
</style>
