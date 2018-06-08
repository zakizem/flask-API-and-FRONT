const app = new Vue({
    el: "#app",
    data: {
      questions: [],
      courant:{},
      friends: [],
    },
    methods: {
      faireQqChose(parametre) {
        fetch("http://127.0.0.1:5000/1", {
          body: JSON.stringify(parametre),
        })
        .then(() => {
          this.courant[texte]=parametre.texte
        })
      }
    },
    mounted() {
      fetch("http://127.0.0.1:5000/1")
        .then(response => response.json())
        .then((data) => {
          this.questions = data;
        })
    },
    template: `
    <div>
      <li v-for="question, i in questions">

        {{question.texte}}
        <br>


        <div v-if="question.type == 'text' || question.type == 'email'">

        <input v-on:unfocus.13="faireQqChose(question)" v-bind:type="question.type" v-bind:id="question.nom_de_la_question" v-bind:name="question.nom_de_la_question" v-model="question.texte" >

        </div>
        <div v-else-if="question.type == 'liste'" >


        <select name="question.nom_de_la_question">

                <option v-for="choix in question.choix" data-tokens="choix" class="col-6"> {{choix}} </option>

        </select>


        </div>
        <div v-else>
          <br>autre que text<br>
        </div>
        <br>
      </li>


      <li v-for="friend, i in friends">
        <div v-if="editFriend === friend.id">
          <input v-on:keyup.13="updateFriend(friend)" v-model="friend.name" />
          <button v-on:click="updateFriend(friend)">save</button>
        </div>
        <div v-else>
          <button v-on:click="editFriend = friend.id">edit</button>
          <button v-on:click="deleteFriend(friend.id, i)">x</button>
          {{friend.name}}
        </div>
      </li>
    </div>
    `,
});
