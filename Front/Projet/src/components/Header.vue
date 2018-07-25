<script>
import infoStore from "../stores/infoStore"

export default {
  name: 'Header',
  data() {
    return {}
  },
  computed: {
    infos () {
      return infoStore.state.infos
    }
  },
  methods: {
    appel_ressource_protected: function() {
      var self = this
      var xmlHttp = new XMLHttpRequest();
      xmlHttp.open("GET", "http://127.0.0.1:8011/protected", true);
      xmlHttp.setRequestHeader("Content-Type", "application/json");
      xmlHttp.withCredentials = true;
      xmlHttp.send(JSON.stringify({'message':'caca'}));
      xmlHttp.onreadystatechange = function() { //Call a function when the state changes.
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
          var response = JSON.parse(xmlHttp.responseText);
          console.log(response)
        }
        else if (xmlHttp.readyState == 4 && xmlHttp.status == 401) {
          // TEST SI LE MESSAGE : TOKEN EXPIRED
          console.log('refresh (appel a ressource protégée)..');
          xmlHttp.open("GET", "http://127.0.0.1:8011/token/refresh", true);
          xmlHttp.send(null);
          xmlHttp.onreadystatechange = function() {
            if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
                // access token rafraichi ??
                response = JSON.parse(xmlHttp.responseText);
                console.log(response);
                self.appel_ressource_protected()
            }
          }
        }
      }
    },
    logout: function () {
      var self = this
      var xmlHttp = new XMLHttpRequest();
      xmlHttp.open("POST", "http://127.0.0.1:8011/token/logout");  //application/x-www-form-urlencoded ??? sécurité ??
      xmlHttp.setRequestHeader("Content-Type", "application/json");
      xmlHttp.withCredentials = true;
      xmlHttp.send(null);
      xmlHttp.onreadystatechange = function() { //Call a function when the state changes.
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
          console.log('lougout réussi?');
          infoStore.commit('infoInit')
          self.$router.push('/Accueil')
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
  <br>
  <h1 v-if="'prenom' in infos['data']['identite'] && infos['data']['identite']['prenom']!=''">Salut {{infos['data']['identite']['prenom']}} !</h1>
  <button @click="appel_ressource_protected" class="btn btn-primary">appel à une ressource protégée de l'api</button>
  <button @click="logout" class="btn btn-primary">Logout</button>
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
    //       // this.appel_ressource_protected_API("http://127.0.0.1:8011/1");
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
    //     this.courant[texte]=parametre.texte
    //   })
    // }

  -->
