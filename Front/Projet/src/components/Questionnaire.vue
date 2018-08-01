<script>
import infoStore from "../stores/infoStore"
import vueStore from "../stores/vueStore"
import {API} from '../base-url';

export default {
  name: 'Questionnaire',
  data() {
    return {
      EtapeCourante: '',
      questions: {},
      reponses: {},
    }
  },
  computed: {
    message() {
      return vueStore.state.message
    },
    data() {
      return infoStore.state.infos.data
    },
  },

  created: function() {
    var self = this
    this.setEtapeCourante('identite', function() {
      self.setQuestionsAXIOS(self, self['EtapeCourante']);
      self.reponses = Object.assign(self.reponses, self.data[self['EtapeCourante']]);
    })
  },

  // updated: function() {},
  // beforeUpdate: function() {},

  methods: {
    envoiReponses: function() {
      var self = this
       this.$http.post("http://127.0.0.1:8011/envoiReponses", {body :JSON.stringify(self.data) , headers:"'Content-Type', 'application/json'", credentials: true, }).then(response => {
      //this.$http.post("http://127.0.0.1:5001/withoutFlaskRestful", {body :JSON.stringify({'message':'caca'}) , headers:"'Content-Type', 'application/json'", credentials: true }).then(response => {
        // success callback
        console.log('reçu de l API : ');
        console.log(response.body);
        self.EcrireMessage(response.body)
        // if (typeof response === "object") {     // comprendre ce que j'ai fait là
        //   self.reponses = {}
        // }
        }, response => {
          console.log('errorrrr envoiReponses ', response);
          // error callback
      });
    },
    a: function () {
      var self = this
      var xmlHttp = new XMLHttpRequest();   // new HttpRequest instance
      xmlHttp.open("POST", "http://127.0.0.1:5001/getTokens");  //application/x-www-form-urlencoded ??? sécurité ??
      xmlHttp.setRequestHeader("Content-Type", "application/json");
      xmlHttp.withCredentials = true;
      xmlHttp.send(null);
      xmlHttp.onreadystatechange = function() {
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
          var response = JSON.parse(xmlHttp.responseText);
          console.log(response);
        }
        else if (xmlHttp.readyState == 4 && xmlHttp.status == 401) {
          console.log('401111');
        }
        else if (xmlHttp.readyState == 4) {
          console.log('autre erreur');
        }
      }
    },
    envoiReponsesOLD: function() {
      var self = this
      var xmlHttp = new XMLHttpRequest();
      // xmlHttp.open("POST", "http://127.0.0.1:5001/randomURL", true);
      // xmlHttp.open("POST", "http://127.0.0.1:5001/withoutFlaskRestful", true);
      xmlHttp.open("POST", "http://127.0.0.1:8011/envoiReponses", true);

      // xmlHttp.open("POST", "http://127.0.0.1:8011/envoiReponses", true);
      xmlHttp.setRequestHeader("Content-Type", "application/json");
      xmlHttp.withCredentials = true;
      xmlHttp.send(JSON.stringify(self.data));
      //xmlHttp.send(null);
      xmlHttp.onreadystatechange = function() { //Call a function when the state changes.
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
          var response = JSON.parse(xmlHttp.responseText);
          console.log('reçu de l API : ');
          console.log(response);
          self.EcrireMessage(response)
          // if (typeof response === "object") {     // comprendre ce que j'ai fait là
          //   self.reponses = {}
          // }
        }
        else if (xmlHttp.readyState == 4 && xmlHttp.status == 401) {
          // TEST SI LE MESSAGE : TOKEN EXPIRED (éviter confusion avec d'autres 401?)
          xmlHttp.open("GET", "http://127.0.0.1:8011/token/refresh", true);
          console.log('refresh...');
          xmlHttp.send(null);
          xmlHttp.onreadystatechange = function() {
            if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
                response = JSON.parse(xmlHttp.responseText);
                console.log(response);
                self.envoiReponsesOLD()
            }
          }
        }
        else if (xmlHttp.readyState == 4) {
          console.log('else, xmlHttp.status :  ');
          console.log(xmlHttp);
          // response = JSON.parse(xmlHttp.responseText);
          // console.log(response);
          console.log('else fin ! ');
        }
      }
    },
    setQuestionsAXIOS: function(self, categorie){

      API.get("questionsCategorie/"+categorie)
        .then(response => {
          // JSON responses are automatically parsed.
          // console.log("response de AXIOS : ", response);
          self.questions = Object.assign({}, self.questions, response.data)
        })
        .catch(e => {
          console.log("error axios setquestions", e);
        })
    },



    setQuestions: function(self, categorie) {
      var self = this
      this.$http.get("http://127.0.0.1:8011/questionsCategorie/"+categorie, {headers:"'Content-Type', 'application/json'", credentials: true, }).then(response => {
        // success callback
        self.questions = Object.assign({}, self.questions, response.body)
        }, response => {
          console.log('error setQuestions');
          // error callback
      });
    },
    setQuestionsOLD: function(self, categorie) {
      var xmlHttp = new XMLHttpRequest();
      xmlHttp.open("GET", "http://127.0.0.1:8011/questionsCategorie/"+categorie, true);
      xmlHttp.setRequestHeader("Content-Type", "application/json");
      xmlHttp.withCredentials = true;
      xmlHttp.send(null);
      xmlHttp.onreadystatechange = function() {
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
          var response = JSON.parse(xmlHttp.responseText);
          self.questions = Object.assign({}, self.questions, response)
        }
      }
    },
    addInfo(info) {
      infoStore.methods.addInfo(info)
    },
    // addData(info) {
    //   infoStore.commit('addData', info)
    // },
    EcrireMessage(message) {
      vueStore.commit('EcrireMessage', message)
    },
    saveInput(key) {
      var self = this
      var info  = {}
      info[key]=self.reponses[key]
      infoStore.commit('addDataCategorie', {'info' : info, 'categorie' : self.data['EtapeCourante']})
    },
    saveReponses: function() {
      var self = this
      // infoStore.commit('addData', self.data)
      // self.envoiReponses()          // POUR ENREGISTRER DANS LA BDD
    },
    viderChamps(){
      this.reponses= {}
      infoStore.commit('dataInit')
    },
    setEtapeCourante(ec, callback){
      this['EtapeCourante']=ec
      infoStore.commit('addData', {'EtapeCourante': ec})
      callback()
    },
    nextQuestions(){
      var self = this
      var xmlHttp = new XMLHttpRequest();
      xmlHttp.open("GET", "http://127.0.0.1:8011/questionsCategorieSuivante/"+self.EtapeCourante, true);
      xmlHttp.setRequestHeader("Content-Type", "application/json");
      xmlHttp.withCredentials = true;
      xmlHttp.send(null);
      xmlHttp.onreadystatechange = function() {
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {

          var response = JSON.parse(xmlHttp.responseText);
          self.initialisationPage(response['etapeCourante'], response.data)

        }
      }
    },
    previousQuestions(){
      var self = this
      var xmlHttp = new XMLHttpRequest();
      xmlHttp.open("GET", "http://127.0.0.1:8011/questionsCategoriePrecedente/"+self.EtapeCourante, true);
      xmlHttp.setRequestHeader("Content-Type", "application/json");
      xmlHttp.withCredentials = true;
      xmlHttp.send(null);
      xmlHttp.onreadystatechange = function() {
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {

          var response = JSON.parse(xmlHttp.responseText);
          self.initialisationPage(response['etapeCourante'], response.data)

        }
      }
    },
    initialisationPage(etapeCourante, questions){
      var self = this // au cas ou, si ça marche, tester en enlevant ça
      self.setEtapeCourante(etapeCourante, function(){
        self.questions = {}
        self.questions = Object.assign({}, self.questions, questions)
        self.reponses = {}
        self.reponses = Object.assign(self.reponses, self.data[self['EtapeCourante']]);
      })
    },
  }
}
</script>

<template>
<div class="container">

      <button v-on:click="previousQuestions" class="btn btn-primary">previous</button>&emsp;
      <button v-on:click="nextQuestions" class="btn btn-primary">next</button>

  <br><br>

  <li v-for="question, i in questions">

    {{question.label}}
    <br>

    <div v-if="question.type == 'text' || question.type == 'email'">

      <input v-model="reponses[question.nom_de_la_question]" @blur="saveInput(question.nom_de_la_question)" v-bind:type="question.type" v-bind:id="question.nom_de_la_question" v-bind:name="question.nom_de_la_question">
      <!-- <input v-on:blur="addreponses(question.nom_de_la_question, $event )"  v-bind:type="question.type" v-bind:id="question.nom_de_la_question" v-bind:name="question.nom_de_la_question" > -->

    </div>
    <div v-else-if="question.type == 'liste'">

      <select v-model="reponses[question.nom_de_la_question]" @blur="saveInput(question.nom_de_la_question)" name="question.nom_de_la_question">

        <option  v-for="choix in question.choix" data-tokens="choix" class="col-6"> {{choix}} </option>

      </select>

    </div>

    <div v-else-if="question.type == 'radio'">

      <div v-for="choix in question.choix">
        <label>
            <input v-model="reponses[question.nom_de_la_question]" @blur="saveInput(question.nom_de_la_question)" type="radio" v-bind:name="question.nom_de_la_question" v-bind:value="choix">
            {{choix}}
        </label>
        <br>
      </div>

    </div>


    <div v-else>
      <br>autre type de question<br>
    </div>
    <br>
  </li>

  <!-- <button v-on:click="saveReponses" class="btn btn-primary">Sauvegarder les réponses (pas encore géré)</button> -->
  <br>
  <br>

  <div class="controls">
    <button @click="envoiReponsesOLD" class="btn btn-primary">Envoyer</button>
    <br>
    <!-- <button @click="a" class="btn btn-primary">a</button> -->

    <br>

    <button v-on:click="viderChamps" class="btn btn-primary">viderChamps</button>

  </div>
  <br> {{message}} <br>

</div>
</template>

<style lang="css">
/* .row {
  margin: auto !important;
  max-width: 300px;
} */
</style>

<!--  coms

<input v-on:blur="remplirreponses(question.nom_de_la_question ,$event)" v-bind:type="question.type" v-bind:id="question.nom_de_la_question" v-bind:name="question.nom_de_la_question" >
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
