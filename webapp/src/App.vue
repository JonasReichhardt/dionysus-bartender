<template>
  <h1>Dionysus Bartender</h1>
  <HelloWorld />
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  data(){
    return{
    }
  },
  components: {
    HelloWorld
  }     
}
</script>

<style>
html{
  font-size: 5vh;
  -webkit-text-size-adjust:auto;
}
body{
  margin: 0;
  background-color:aliceblue;

}
h1 {
  font-size: 1em;
  margin-block: 0!important;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>