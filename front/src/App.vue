<template>
  <!-- <Startmain/> -->
  <router-view/>  
</template>


<script>
//import Startmain from './views/Start_main.vue'

export default {

  name: 'Start_main',
  components: {
    //Startmain
  }
  
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
