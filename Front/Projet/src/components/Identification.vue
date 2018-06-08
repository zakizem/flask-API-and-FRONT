<script>
import infoStore from "../stores/infoStore"
export default {
  name: 'Identification',
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
      message: '',
      infoStore: infoStore.data,
    }
  },
  created: function() {
    console.log('document.cookie');
    console.log(document.cookie);
  },

  methods: {
    authentification: function() {
      console.log("$window.sessionStorage.accessToken");
      console.log(window);
      var self = this
      var xmlHttp = new XMLHttpRequest();   // new HttpRequest instance
      xmlHttp.open("POST", "http://127.0.0.1:5000/authentification");  //application/x-www-form-urlencoded ??? sécurité ??
      xmlHttp.setRequestHeader("Content-Type", "application/json");
      xmlHttp.send(JSON.stringify(this.reponse));
      xmlHttp.onreadystatechange = function() { //Call a function when the state changes.
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
          var response = JSON.parse(xmlHttp.responseText);  // TESTER SI IL Y A 'TOKEN' ICI pour le mettre dans un endroit précis dans le store
          console.log('reçu de l API : ');
          console.log(response);
          self.message = response;
          self.addInfo(self.message)
          window.sessionStorage.accessToken = response.token;
          console.log("$window.sessionStorage.accessToken");
          console.log(window);

          document.cookie = "usernamessdq=John dqsdqsDoe";


          // response.body

        }
        else if (xmlHttp.status == 401){
          self.message = "ERREUR 401 ! "
        }
      }
    },
    addInfo(info) {
      infoStore.methods.addInfo(info)
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
    <button v-on:click="authentification" class="btn btn-primary">Valider</button>
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
