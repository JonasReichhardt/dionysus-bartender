<template>
<div class="container">
  <div id="slider-area-container" style="background-color:powderblue;">
    <div>Pumpe 1</div>
    <div>Pumpe 2</div>
    <div>Pumpe 3</div>
    <div>Pumpe 4</div>
    <div>Pumpe 5</div>
    <div>Pumpe 6</div>
  </div>
  <div id="pictures-container" style="background-color:red;">pictures</div>
  <div id="buttons-container" style="background-color:green;">buttons</div> 
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
    grid-template-areas: 
    "slider pictures"
    "slider pictures"
    "buttons buttons";
    gap: 5px;
    padding: 5px;
    box-sizing: border-box;
}

.container div{
  font-size: 0.8em;
}

#slider-area-container{
  display:flex;
  flex-direction: column;
  grid-area: slider;
  width: 100%;
  justify-content: space-between;
}
#pictures-container{

  grid-area: pictures;
  
}
#buttons-container{
  grid-area: buttons;
}
a{
  color: #42b983;
}
</style>
