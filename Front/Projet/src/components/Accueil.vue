<template>
<div id="accueil" class="row">
  <br>
  <div class="col-md-4">

  </div>

  <div class="col-md-3">
    <Auth></Auth>
  </div>
  <div class="col-md-3">
    <Signup></Signup>
  </div>

</div>
</template>

<script>
import Vue from 'vue'

import Auth from './Auth'
import Signup from './Signup'

export default{
  name: 'Accueil',
  components: {
    Auth,
    Signup,
  },
}
</script>

<style>
.row {
  text-align: center;
}
.col-md-3 {
  display:inline-block!important;
  float:none!important;
  text-align:left;
  margin-right:-4px;
}
</style>
