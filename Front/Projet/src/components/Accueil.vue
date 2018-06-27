<script>
import vueStore from "../stores/vueStore"
import infoStore from "../stores/infoStore"

export default {
  name: 'Accueil',
  data() {
    return {}
  },
  computed: {
    infos () {
      return infoStore.state.infos
    }
  },
  methods: {
    appel: function() {
      var self = this
      var xmlHttp = new XMLHttpRequest();
      xmlHttp.open("GET", "http://127.0.0.1:5000/protected", true); // false for synchronous request
      xmlHttp.setRequestHeader("Content-Type", "application/json");
      xmlHttp.withCredentials = true;
      xmlHttp.send(null);
      xmlHttp.onreadystatechange = function() { //Call a function when the state changes.
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
          var response = JSON.parse(xmlHttp.responseText);
          console.log(response)
        }
        else if (xmlHttp.readyState == 4 && xmlHttp.status == 401) {
          // TEST SI LE MESSAGE : TOKEN EXPIRED
          xmlHttp.open("GET", "http://127.0.0.1:5000/token/refresh", true); // false for synchronous request
          xmlHttp.send(null);
          xmlHttp.onreadystatechange = function() {
            if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
                // access token rafraichi ??
                response = JSON.parse(xmlHttp.responseText);
                console.log(response);
            }
          }
        }
      }
    },
    logout: function () {
      var self = this
      var xmlHttp = new XMLHttpRequest();
      xmlHttp.open("POST", "http://127.0.0.1:5000/token/logout");  //application/x-www-form-urlencoded ??? sécurité ??
      xmlHttp.setRequestHeader("Content-Type", "application/json");
      xmlHttp.withCredentials = true;
      xmlHttp.send(null);
      xmlHttp.onreadystatechange = function() { //Call a function when the state changes.
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
          console.log('lougout réussi ??');
          infoStore.commit('infoInit')
          self.$router.push('/Auth')
        }
        else if (xmlHttp.readyState == 4) {
          var response = JSON.parse(xmlHttp.responseText);
          self.EcrireMessage(response)
        }
      }
    },
  }
}

</script>

<template>
<div class="">
  <h1 v-if="'prenom' in infos && infos['prenom']!=''">Salut {{infos['prenom']}} !</h1>
  <button v-on:click="appel" class="btn btn-primary">Appel api</button>
  <button v-on:click="logout" class="btn btn-primary">Logout</button>
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
