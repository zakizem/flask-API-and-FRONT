
<script>
import Vue from 'vue'
import infoStore from "../stores/infoStore"
import {
  API
} from '../base-url';
import axios from 'axios';

export default {
  name: 'FileUpload',
  data() {
    return {
      // uploadedFiles : [],
      fileNumber : 0,

    }
  },
  computed: {
    formData() {
      return new FormData()
    },
  },
  props: ['nom_de_la_question'],
  // created: function() {
  //   // var self = this
  //   // self.formData = new FormData()
  // },
  methods: {
    onFileChanged(event) {
      var files = event.target.files

      var n = this.fileNumber
      for (var i = 0; i < files.length; i++) {
        this.formData.append('Image_N_' + (i+n) + '_' + this.nom_de_la_question + "_" + (i+n) +"_"+ files[i].name, files[i], this.nom_de_la_question + "_" + (i+n) +"_"+ files[i].name)
        this.fileNumber++

        // console.log("formData.append('photo'+",i,"files[i]",files[i],", files[i].name)",files[i].name);

        // console.log('i = ',i);
        // console.log('files[i] : ', files[i]);
        // console.log('files[i].name : ',files[i].name);

      }

      console.log('n = ', n);
      console.log('this.fileNumber = ',this.fileNumber);
      console.log('this.formData : ', this.formData);
      for (var pair of this.formData.entries()) {
          console.log(pair[0]+ ', ' + pair[1]);
      }

      // for (var i = 0; i < files.length; i++) {
      //   // console.log('file', i, " : ", files[i]);
      //   this.uploadedFiles.push(files[i]);
      // }
    },
    onUpload() {
      if (this.uploadedFiles != []) {

            // const formData = new FormData()

            // var files = this.uploadedFiles
            // for (var i = 0; i < files.length; i++) {
            //   formData.append('Image_N_' + i, files[i], this.nom_de_la_question + "_" + i +"_"+ files[i].name)
            //   // console.log("formData.append('photo'+",i,"files[i]",files[i],", files[i].name)",files[i].name);
            // }

            this.formData.append("nom_de_la_question", this.nom_de_la_question)

            var self = this
            var xmlHttp = new XMLHttpRequest();
            xmlHttp.open("POST", "http://127.0.0.1:8011/saveImage");
            // xmlHttp.setRequestHeader("Content-Type", "multipart / form-data");
            xmlHttp.withCredentials = true;
            xmlHttp.send(this.formData);
            xmlHttp.onreadystatechange = function() {
              if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
                var response = JSON.parse(xmlHttp.responseText);
                console.log('file uploaded ', response);
              } else if (xmlHttp.readyState == 4 && (xmlHttp.status == 401 || xmlHttp.status == 0)) {
                console.log('40111 Fonction onUpload');

                xmlHttp.open("GET", "http://127.0.0.1:8011/token/refresh", true);
                console.log('refresh...');
                xmlHttp.send(null);
                xmlHttp.onreadystatechange = function() {
                  if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
                      response = JSON.parse(xmlHttp.responseText);
                      console.log(response);
                      self.onUpload()
                  }
                }
              }
            }

        // console.log("formData : " ,formData);


        // axios({
        //   method: 'post',
        //   url: 'http://127.0.0.1:8011/saveImage',
        //   data: this.formData
        //   })
        //   .then(function (response) {
        //       //handle success
        //       console.log("response de AXIOS : ", response);
        //   })
        //   .catch(function (response) {
        //       //handle error
        //       console.log("error axios setquestions", response);
        //   });


        // API.post('saveImage', formData, {
        //     headers: {
        //       'Content-Type': 'multipart/form-data'
        //     }
        // })
        // .then(response => {
        //   // JSON responses are automatically parsed.
        //   // console.log("response de AXIOS : ", response);
        //   self.questions = Object.assign({}, self.questions, response.data)
        // })
        // .catch(e => {
        //   console.log("error axios setquestions", e);
        // })


        // this.$http.post('http://127.0.0.1:8011/saveImage', formData)   // Vue-resource


      }
      else {
        console.log("No files selected ! ");
      }
    },
  }
}
</script>

<template>
<div>
  <input type="file" @change="onFileChanged" multiple="multiple" accept="image/*" name="nom_de_la_question">
  <button @click="onUpload">Upload!</button>


    <li v-for="pair of formData.entries()">
      {{pair[0]}}
    </li>


</div>
</template>
