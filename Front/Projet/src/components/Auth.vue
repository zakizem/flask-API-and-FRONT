<script>
import Vue from 'vue'
import VueSession from 'vue-session'
Vue.use(VueSession)

import vueStore from "../stores/vueStore"


export default {
  name: 'Auth',
  data() {
    return {
      questions: [
        {
            'nom_de_la_question': 'email',
            'texte': 'Adresse mail : '
        },
        {
            'nom_de_la_question': 'password',
            'texte': 'Mot de passe : '
        },
      ],
      reponse: {},
    }
  },
  computed: {
  message () {
    return vueStore.state.message
  }
},

  methods: {
    login: function () {
      var self = this
      var xmlHttp = new XMLHttpRequest();   // new HttpRequest instance
      xmlHttp.open("POST", "http://127.0.0.1:5000/authentification");  //application/x-www-form-urlencoded ??? sécurité ??
      xmlHttp.setRequestHeader("Content-Type", "application/json");
      xmlHttp.send(JSON.stringify(this.reponse));
      xmlHttp.onreadystatechange = function() { //Call a function when the state changes.
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
          var response = JSON.parse(xmlHttp.responseText);
          self.$session.start()
          self.$session.set('jwt', response.token)
          // Vue.http.headers.common['Authorization'] = 'Bearer ' + response.body.token
          self.$router.push('/')
        }
      }
    },
    EcrireMessage (message) {
      vueStore.commit('EcrireMessage', message)
    }
  }
}
</script>

<template>
<div class="">

  <li v-for="question, i in questions">

    {{question.texte}}
<br>
    <input v-model="reponse[question.nom_de_la_question]" type="text" :id="question.nom_de_la_question" :name="question.nom_de_la_question" >
    <!-- <input v-on:blur="addReponse(question.nom_de_la_question, $event )"  v-bind:type="question.type" v-bind:id="question.nom_de_la_question" v-bind:name="question.nom_de_la_question" > -->

    <br><br>

  </li>

  <div class="controls">
    <button v-on:click="login" class="btn btn-primary">Valider</button>
  </div>
  <br>
  {{message}}

</div>
</template>




<style lang="css">
</style>



<!--  coms

<input :required="test ? true : false">


<input v-on:blur="remplirReponse(question.nom_de_la_question ,$event)" v-bind:type="question.type" v-bind:id="question.nom_de_la_question" v-bind:name="question.nom_de_la_question" >
 <input type="text" name="" value="" v-on:click="ajout_machin" > hola


    // // return new Promise(resolve => {
    // //     setTimeout(() => {
    //       self=this;
    //       console.log('1');
    //       this.httpGet();
    //       console.log('uno et demi');
    //       // this.appel_API("http://127.0.0.1:5000/1");
    //       // console.log('tresss');
    //       // alert(this.questions);
    //       console.log('this.questions (dans created) : '+this.questions);
    //
    // //    resolve()
    // //     })
    // // })


    // envoyerRequeteAvecParametres(parametre) {
    //   alert('1')
    //   fetch("http://127.0.0.1:5000/1", {
    //     body: JSON.stringify(parametre),
    //   })
    //   .then(() => {
    //     alert('2')
    //     this.courant[texte]=parametre.texte
    //   })
    // }

  -->
