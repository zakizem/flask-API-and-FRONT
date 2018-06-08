<script>
import infoStore from "../stores/infoStore"
export default {
  name: 'MonComposant',
  data() {
    return {
      questions: [],
      reponse: {},
      message: '',
      friends: [],
      infoStore: infoStore.data,
    }
  },

  created: function() {
    var self = this
    this.setQuestions(self);
  },

  beforeUpdate: function() {
    var self = this

    console.log('reponse : ');
    console.log(this.reponse);
    console.log('message : ');
    console.log(this.message);
  },

  methods: {
    envoiAPI: function() {
      var self = this
      var xmlHttp = new XMLHttpRequest();   // new HttpRequest instance
      xmlHttp.open("POST", "http://127.0.0.1:5000/envoi");
      xmlHttp.setRequestHeader("Content-Type", "application/json");
      xmlHttp.send(JSON.stringify(this.reponse));
      xmlHttp.onreadystatechange = function() { //Call a function when the state changes.
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
          var response = JSON.parse(xmlHttp.responseText);
          console.log('reçue par l API : ');
          console.log(response);
          self.message = response;
          self.addInfo(self.message)
          console.log('self.message');
          console.log(self.message);
          // self.message = Object.assign('', self.message, response)
          // console.log('self.message 2 ');
          // console.log(self.message);


        }
      }
    },
    setQuestions: function(self) {
      var xmlHttp = new XMLHttpRequest();
      xmlHttp.open("GET", "http://127.0.0.1:5000/1", true); // false for synchronous request
      xmlHttp.send(null);
      xmlHttp.onreadystatechange = function() { //Call a function when the state changes.
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
          var response = JSON.parse(xmlHttp.responseText);
          self.questions = Object.assign({}, self.questions, response)
          // self.questions = response;
        }
      }
    },
    addInfo(info) {
      infoStore.methods.addInfo(info)
    },
    initialiserQuestions: function() {
      fetch("http://127.0.0.1:5000/1", {
          method: 'get'
        })
        .then(response => response.json())
        .then((data) => {
          self.questions = data;
        }).catch(function(error) {
          console.log('Request initialiserQuestions failed')
          console.log(error);
        });
    },
    addReponse: function (question, r) {
      console.log('yooo');
      this.$set(this.reponse, question, r.target.value)
      console.log(self.reponse);
    }
  }
}
</script>

<template>
<div class="container">

  <li v-for="question, i in questions">

    {{question.texte}}
    <br>

    <div v-if="question.type == 'text' || question.type == 'email'">

      <input v-model="reponse[question.nom_de_la_question]" v-bind:type="question.type" v-bind:id="question.nom_de_la_question" v-bind:name="question.nom_de_la_question" >
      <!-- <input v-on:blur="addReponse(question.nom_de_la_question, $event )"  v-bind:type="question.type" v-bind:id="question.nom_de_la_question" v-bind:name="question.nom_de_la_question" > -->

    </div>
    <div v-else-if="question.type == 'liste'">

      <select name="question.nom_de_la_question">

                <option v-for="choix in question.choix" data-tokens="choix" class="col-6"> {{choix}} </option>

      </select>

    </div>
    <div v-else>
      <br>autre que text<br>
    </div>
    <br>
  </li>

  <div class="controls">
    <button v-on:click="envoiAPI" class="btn btn-primary">Valider</button>
  </div>
<br>
  {{message}}



  <li v-for="friend, i in friends">
    <div v-if="editFriend === friend.id">
      <input v-on:keyup.13="updateFriend(friend)" v-model="friend.name" />
      <button v-on:click="updateFriend(friend)">save</button>
    </div>
    <div v-else>
      <button v-on:click="editFriend = friend.id">edit</button>
      <button v-on:click="deleteFriend(friend.id, i)">x</button> {{friend.name}}
    </div>
  </li>

</div>
</template>




<style lang="css">
</style>



<!--  coms

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
