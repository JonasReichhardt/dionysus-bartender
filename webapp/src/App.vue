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
      drinks:[
        {
          id: 0,
          title: "Drink 0",
          pump1val: 0,
          pump2val: 0,
          pump3val: 0,
          pump4val: 0,
          pump5val: 0,
          pump6val: 0,
        }
      ],
      pumps:[
      ]
    }
  },
  components: {
    HelloWorld
  }     
}
</script>

<style>
html{
  font-size: 10vh;
  -webkit-text-size-adjust: 100%;
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