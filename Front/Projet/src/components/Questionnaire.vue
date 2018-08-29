<script>
import infoStore from "../stores/infoStore"
import vueStore from "../stores/vueStore"
import {API} from '../base-url';

import FileUpload from './FileUpload'

export default {
  name: 'Questionnaire',
  data() {
    return {
      EtapeCourante: '',
      questions: {},
      reponses: {},
    }
  },
  components: {
    FileUpload,
  },
  computed: {
    message() {
      return vueStore.state.message
    },
    data() {
      return infoStore.state.infos.data
    },
    EtapeCouranteMaj() {
      return this.EtapeCourante.charAt(0).toUpperCase() + this.EtapeCourante.slice(1);
    }
  },

  created: function() {
    var self = this
    this.setEtapeCourante('identite', function() {
      self.setQuestionsAXIOS(self, self['EtapeCourante']);

      // AJOUT DE PROPRIETE REACTIVE : LA BONNE METHODE
      var monObjet = Object.assign({}, monObjet, self.data[self['EtapeCourante']])
      self.$set( self, 'reponses', monObjet )

      // self.reponses = Object.assign(self.reponses, self.data[self['EtapeCourante']]);
    })
  },

  // watch: {
  //   currentBranch: 'fetchData'
  // },

  // updated: function() {},
  // beforeUpdate: function() {},

  methods: {
    envoiReponsesOLD: function() {
      var self = this
      var xmlHttp = new XMLHttpRequest();
      // xmlHttp.open("POST", "http://127.0.0.1:5001/randomURL", true);
      // xmlHttp.open("POST", "http://127.0.0.1:5001/withoutFlaskRestful", true);
      xmlHttp.open("POST", "http://127.0.0.1:8011/envoiReponses", true);

      xmlHttp.setRequestHeader("Content-Type", "application/json");
      xmlHttp.withCredentials = true;
      // xmlHttp.send(JSON.stringify(self.data));

      var jsonData = {}
      jsonData[self.EtapeCourante] = self.data[self.EtapeCourante]

      xmlHttp.send(JSON.stringify(jsonData));

      console.log("contenu envoyé : ",jsonData);
      //xmlHttp.send(null);
      xmlHttp.onreadystatechange = function() {
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
          // TEST SI LE MESSAGE : TOKEN EXPIRED (éviter confusion avec d'autres 401? sinon récursivité infinie..)
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

          var monObjet = Object.assign({}, monObjet,  response.data)
          self.$set( self, 'questions', monObjet )

          // self.questions = Object.assign({}, self.questions, response.data)
        })
        .catch(e => {
          console.log("error axios setquestions", e);
        })
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
    viderChamps(){
      this.reponses[this.etapeCourante]= {}
      infoStore.commit('dataInitEtape', {'etapeCourante': this.etapeCourante})
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
      var self = this
      self.setEtapeCourante(etapeCourante, function(){
        self.questions = {}
        self.questions = Object.assign({}, self.questions, questions)

        self.reponses = {}
        var monObjet = Object.assign({}, monObjet, self.data[self['EtapeCourante']])
        self.$set( self, 'reponses', monObjet )

        // self.reponses = Object.assign(self.reponses, self.data[self['EtapeCourante']]);
      })
    },
  }
}
</script>

<template>
<div class="container ">

      <button v-on:click="previousQuestions" class="btn btn-primary">previous</button>&emsp;
      <button v-on:click="nextQuestions" class="btn btn-primary">next</button>

  <br><br> <h3>{{EtapeCouranteMaj}}</h3> <br>
<ul>

  <li v-for="question, i in questions" class=" col ">
<div class="col d-flex justify-content-between">

<div class="">
  {{question.label}}
</div>
    <div class=" ">
      
    <div v-if="question.type == 'text' || question.type == 'email'">

      <input v-model="reponses[question.nom_de_la_question]" @blur="saveInput(question.nom_de_la_question)" v-bind:type="question.type" v-bind:id="question.nom_de_la_question" v-bind:name="question.nom_de_la_question">
      <!-- <input v-on:blur="addreponses(question.nom_de_la_question, $event )"  v-bind:type="question.type" v-bind:id="question.nom_de_la_question" v-bind:name="question.nom_de_la_question" > -->

    </div>

    <div v-else-if="question.type == 'nombre'">

      <input v-model="reponses[question.nom_de_la_question]" @blur="saveInput(question.nom_de_la_question)" type="number" v-bind:id="question.nom_de_la_question" v-bind:name="question.nom_de_la_question">

    </div>

    <div v-else-if="question.type == 'liste'">

      <select v-model="reponses[question.nom_de_la_question]" @blur="saveInput(question.nom_de_la_question)" name="question.nom_de_la_question" class="custom-select">

        <option  v-for="choix in question.choix" data-tokens="choix" class="col-6"> {{choix}} </option>

      </select>

    </div>

    <div v-else-if="question.type == 'radio'">

      <div class="row">
        <div v-for="choix in question.choix" class="col">
          <label>
              <input v-model="reponses[question.nom_de_la_question]" @change="saveInput(question.nom_de_la_question)" type="radio" v-bind:name="question.nom_de_la_question" v-bind:value="choix">
              {{choix}}
          </label>
          <br>
        </div>
      </div>

      <div v-if= " 'sioui' in question && reponses[question.nom_de_la_question] == 'oui' " class="sioui col" >

            <li v-for="question_nested, i in question['sioui']" >

              {{question_nested.label}}
              <br>

              <div v-if="question_nested.type == 'text' || question_nested.type == 'email'">

                <input v-model="reponses[question_nested.nom_de_la_question]" @blur="saveInput(question_nested.nom_de_la_question)" v-bind:type="question_nested.type" v-bind:id="question_nested.nom_de_la_question" v-bind:name="question_nested.nom_de_la_question">
                <!-- <input v-on:blur="addreponses(question_nested.nom_de_la_question, $event )"  v-bind:type="question_nested.type" v-bind:id="question_nested.nom_de_la_question" v-bind:name="question_nested.nom_de_la_question" > -->

              </div>
              <div v-else-if="question_nested.type == 'liste'">

                <select v-model="reponses[question_nested.nom_de_la_question]" @blur="saveInput(question_nested.nom_de_la_question)" name="question_nested.nom_de_la_question" class="custom-select ">

                  <option  v-for="choix in question_nested.choix" data-tokens="choix" class="col"> {{choix}} </option>

                </select>

              </div>

              <div v-else-if="question_nested.type == 'radio'">

                <div v-for="choix in question_nested.choix">
                  <label>
                      <input v-model="reponses[question_nested.nom_de_la_question]" @change="saveInput(question_nested.nom_de_la_question)" type="radio" v-bind:name="question_nested.nom_de_la_question" v-bind:value="choix">
                      {{choix}}
                  </label>
                  <br>
                </div>


                </div>

                <div v-else-if="question_nested.type == 'nombre'">

                  <input v-model="reponses[question_nested.nom_de_la_question]" @blur="saveInput(question_nested.nom_de_la_question)" type="number" v-bind:id="question_nested.nom_de_la_question" v-bind:name="question_nested.nom_de_la_question">

                </div>

                <div v-else-if="question_nested.type == 'fichier'">

                  <br>
                  <FileUpload v-bind:nom_de_la_question="question_nested.nom_de_la_question" ></FileUpload>
                  <br>

                </div>

                <div v-else>
                  <br>autre type de question_nested<br>
                </div>
                <br>
              </li>

      </div>

      </div>
      <!-- <div v-bind:class="reponses[question.nom_de_la_question]+'-display'" class="hide">
        <h3>iiiiiiiiii</h3>
      </div> -->



    <div v-else-if="question.type == 'fichier'">


      <FileUpload v-bind:nom_de_la_question="question.nom_de_la_question" ></FileUpload>


    </div>

    <div v-else>
      <br>autre type de question<br>
    </div>
    <br>

    </div>

    </div>
  </li>
  </ul>

  <!-- <button v-on:click="saveReponses" class="btn btn-primary">Sauvegarder les réponses (pas encore géré)</button> -->
  <br>
  <br>

  <div class="controls">
    <button @click="envoiReponsesOLD" class="btn btn-primary">Enregistrer les réponses</button>
    <br>
    <!-- <button @click="a" class="btn btn-primary">a</button> -->

    <br>

    <button v-on:click="viderChamps" class="btn btn-primary">viderChamps</button>

  </div>




</div>
</template>

<style lang="css">
.oui-display{
  display: block !important;
}
.oui-display{
  display: none;
}
.hide{
  display: none;
}
.sioui{
  right: 2%;
  border: 1px solid black;
}
ul {
  list-style-type: none;
}
</style>
