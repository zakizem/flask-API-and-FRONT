<script>
import Vue from 'vue'
// import VueSession from 'vue-session'
// Vue.use(VueSession)

import vueStore from "../stores/vueStore"
import infoStore from "../stores/infoStore"

export default {
  name: 'Auth',
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
  message () {
    return vueStore.state.message
  }
},
// watch:{
// 		reponse(value){
// 			// this.eventName();
// 			value = this.reponse['email'];
// 			this.check_email(value);
// 		}
// 	},
  methods: {
    login: function () {
      var self = this
      var xmlHttp = new XMLHttpRequest();   // new HttpRequest instance
      xmlHttp.open("POST", "http://127.0.0.1:8011/authentification");  //application/x-www-form-urlencoded ??? sécurité ??
      xmlHttp.setRequestHeader("Content-Type", "application/json");
      xmlHttp.withCredentials = true;
      xmlHttp.send(JSON.stringify(this.reponse));
      xmlHttp.onreadystatechange = function() {   // Call a function when the state changes.
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
          var response = JSON.parse(xmlHttp.responseText);
          self.addInfo(response)
          // infoStore.commit('login')
          self.$router.push('/Questionnaire')
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

    EcrireMessage (message) {
      vueStore.commit('EcrireMessage', message)
    },
    addInfo (info) {
      infoStore.commit('addInfo', info)
    },
    // check_email(value){
    // 			if (/^\w+([\.-]?\ w+)*@\w+([\.-]?\ w+)*(\.\w{2,3})+$/.test(value))
    // 			{
    //         this.EcrireMessage('');
    // 			}
    //       else
    //       {
    //         this.EcrireMessage('Adresse mail incorrecte')
    // 			}
    // }
  }
}
</script>

<template>
<div class="">
AUTHENTIFICATION
<br>
  <br>

  <li v-for="question, i in questions">

    {{question.label}}
<br>
    <input v-model="reponse[question.nom_de_la_question]" type="text" :id="question.nom_de_la_question" :name="question.nom_de_la_question" >
    <!-- <input v-on:blur="addReponse(question.nom_de_la_question, $event )"  v-bind:type="question.type" v-bind:id="question.nom_de_la_question" v-bind:name="question.nom_de_la_question" > -->
    <br><br>

  </li>

  <div class="controls">
    <button v-on:click="login" class="btn btn-primary">S'authentifier</button>
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
    //       // this.appel_API("http://127.0.0.1:8011/1");
    //       // console.log('tresss');
    //       // alert(this.questions);
    //       console.log('this.questions (dans created) : '+this.questions);
    //
    // //    resolve()
    // //     })
    // // })

    // envoyerRequeteAvecParametres(parametre) {
    //   alert('1')
    //   fetch("http://127.0.0.1:8011/1", {
    //     body: JSON.stringify(parametre),
    //   })
    //   .then(() => {
    //     alert('2')
    //     this.courant[label]=parametre.label
    //   })
    // }

  -->
