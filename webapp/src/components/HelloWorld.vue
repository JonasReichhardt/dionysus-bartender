<template>
<div class="container">
   <div id="slider-area" style="background-color:powderblue;">sliders</div>
  <div id="pictures" style="background-color:red;">pictures</div>
  <div id="buttons" style="background-color:green;">buttons</div> 
</div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.container{
    display: grid;
    width: 100vw;
    height: 100vh;
    grid-template-columns: 1fr 1fr;
    grid-template-rows: 80% 1fr;
    gap: 5px;
    padding: 5px;
    box-sizing: border-box;
}
.container div{
  padding: 10px;
  border: 1px solid black;
}
#slider-area{
  display: grid;
  grid-column-start: 1;
  grid-column-end: 2;
  grid-row-start: 1;
  grid-row-end: 2;
}
#pictures{
  display: grid;
  grid-column-start: 2;
  grid-column-end: 3;
  grid-row-start: 1;
  grid-row-end: 2;
  
}
#buttons{

  grid-column-start: 1;
  grid-column-end: 3;
  grid-row-start: 2;
  grid-row-end: 3;
}
a{
  color: #42b983;
}
</style>
