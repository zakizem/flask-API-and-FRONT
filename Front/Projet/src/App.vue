<template>
<div id="app">

  <!-- <img src="./assets/logo.png"> -->

  <Header></Header>
  <br>
  <router-link :to="{ name: 'Questionnaire' }">Formulaire</router-link>&nbsp;
  <router-link :to="{ name: 'Accueil' }">Accueil</router-link>&emsp;
  <router-link :to="{ name: 'Protected' }">Protected</router-link>&nbsp;

  <br><br><br>
  <router-view/>

  <br>
</div>
</template>

<script>
// import Questionnaire from './components/Questionnaire'
import Header from './components/Header'
// import Protected from './components/Protected'
// import Identification from './components/Identification'

export default {
  name: 'App',
  components: {
    // Questionnaire,
    Header,
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
  margin-top: 5px;
}
</style>
