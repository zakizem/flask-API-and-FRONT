<script>
import Vue from 'vue'
import vueStore from "../stores/vueStore"
import infoStore from "../stores/infoStore"

export default {
  name: 'Signup',
  data() {
    return {
      questions: [
        {
            'nom_de_la_question': 'email',
            'label': 'Adresse mail : '
        },
        {
            'nom_de_la_question': 'password',
            'label': 'Mot de passe : '
        },
      ],
      reponse: {},
    }
  },

  computed: {
  },

  created: function() {
  },

  // updated: function() {},
  // beforeUpdate: function() {},

  methods: {
    Signup: function (){
      var self = this
      var xmlHttp = new XMLHttpRequest();   // new HttpRequest instance
      xmlHttp.open("POST", "http://127.0.0.1:8011/signup");  //application/x-www-form-urlencoded ??? sécurité ??
      xmlHttp.setRequestHeader("Content-Type", "application/json");
      xmlHttp.withCredentials = true;

      console.log('JSON.stringify(this.reponse)');
      console.log(JSON.stringify(this.reponse));

      xmlHttp.send(JSON.stringify(this.reponse));
      xmlHttp.onreadystatechange = function() { //Call a function when the state changes.
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {

          console.log("sig");

          var response = JSON.parse(xmlHttp.responseText);

          console.log(response);

          self.addInfo(response)
          // infoStore.commit('login')
          self.$router.push('/Protected')
          self.EcrireMessage("")
        }
        else if (xmlHttp.readyState == 4 && xmlHttp.status == 401) {
          var response = JSON.parse(xmlHttp.responseText);
          self.EcrireMessage(response)
        }
        else if (xmlHttp.readyState == 4) {
          self.EcrireMessage("Erreur inattendue")
        }
      }
    },
    addInfo (info) {
      infoStore.commit('addInfo', info)
    },
    EcrireMessage (message) {
      vueStore.commit('EcrireMessage', message)
    },
  },

}
</script>

<template>
<div class="container">

    INSCRIPTION
    <br><br>

    <li v-for="question, i in questions">

      {{question.label}}
  <br>
      <input v-model="reponse[question.nom_de_la_question]" type="text" :id="question.nom_de_la_question" :name="question.nom_de_la_question" >
      <!-- <input v-on:blur="addReponse(question.nom_de_la_question, $event )"  v-bind:type="question.type" v-bind:id="question.nom_de_la_question" v-bind:name="question.nom_de_la_question" > -->
      <br><br>

    </li>

    <div class="controls">
      <button v-on:click="Signup" class="btn btn-primary">S'inscrire</button>
    </div>
    <br>


</div>
</template>




<style lang="css">
</style>
