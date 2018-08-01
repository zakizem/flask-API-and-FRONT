
<script>
  import Vue from 'vue'
  import infoStore from "../stores/infoStore"
  import {API} from '../base-url';
  import axios from 'axios';

export default {
    name: 'FileUpload',
    data() {
      return {
        selectedFile: null
      }
    },
    methods: {
      onFileChanged (event) {
        this.selectedFile = event.target.files[0]
        console.log('file changed, file : ', this.selectedFile);
      },
      onUpload() {
        const formData = new FormData()
        formData.append('photo', this.selectedFile, this.selectedFile.name)

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

        var self = this
        var xmlHttp = new XMLHttpRequest();
        xmlHttp.open("POST", "http://127.0.0.1:8011/saveImage");
        // xmlHttp.setRequestHeader("Content-Type", "multipart / form-data");
        xmlHttp.withCredentials = true;
        xmlHttp.send(formData);
        xmlHttp.onreadystatechange = function() {
          if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
            var response = JSON.parse(xmlHttp.responseText);
            console.log('file uploaded ',response);
          }
          else if (xmlHttp.readyState == 4 && xmlHttp.status == 401) {
            console.log('40111 Fonction onUpload');
          }
        }
      },
    }
  }

</script>

<template>
  <div class="container">

    <input type="file" @change="onFileChanged" multiple="multiple" accept="image/*">
    <button @click="onUpload">Upload!</button>

  </div>
</template>
