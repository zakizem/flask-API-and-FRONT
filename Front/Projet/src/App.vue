<template>
<div id="app">

  <!-- <img src="./assets/logo.png"> -->

  <Accueil></Accueil>
  <br>
  <router-link :to="{ name: 'MonComposant' }">Formulaire</router-link>&nbsp;
  <router-link :to="{ name: 'Auth' }">Authentification avec sessions</router-link>&emsp;
  <router-link :to="{ name: 'Protected' }">Protected</router-link>&nbsp;

  <br><br><br>
  <router-view/>
  <br>
</div>
</template>

<script>
// import MonComposant from './components/MonComposant'
import Accueil from './components/Accueil'
// import Protected from './components/Protected'
// import Identification from './components/Identification'

export default {
  name: 'App',
  components: {
    // MonComposant,
    Accueil,
    // Identification
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
