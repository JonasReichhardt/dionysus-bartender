<template>
<div class="container">
  <div id="slider-area-container">
    <div id="pump1">Pumpe 1
      <div class="pump1-slider-area">
        <input type="range" min="0" max="100" value="55" class="" id="range-slider-red">
				<input  type="number" min="0" max="100" value="55" class="input-slider" id="slider-pump1">
      </div>
    </div>
    <div id="pump2">Pumpe 2</div>
    <div id="pump3">Pumpe 3</div>
    <div id="pump4">Pumpe 4</div>
    <div id="pump5">Pumpe 5</div>
    <div id="pump6">Pumpe 6</div>
  </div>
  <div id="pictures-container">pictures</div>
  <div id="buttons-container">buttons</div> 
</div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props:[
    "drinks"
  ]
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.container{
    display: grid;
    width: 100vw;
    height: 100vh;
    grid-auto-columns: minmax(0, 1fr);
    grid-template-columns: 50% 50%;
    grid-template-rows: 40% 40% 1fr;
    grid-template-areas: 
    "slider pictures"
    "slider pictures"
    "buttons buttons";
    gap: 5px;
    padding: 5px;
    box-sizing: border-box;
}

.container div{
  font-size: 0.7em;
  padding: 0.1em;
}

#slider-area-container{
  background-color:powderblue;
  font-size: 0.7em;
  display:flex;
  flex-direction: column;
  grid-area: slider;
  justify-content: space-around;
  align-items: flex-start;
  padding: 0.3em;
  gap: 0.3em;
}

#slider-area-container div{
  height: 15%;
  background-color: #42b983;
  width: 100%;
  align-self: center;
  font-size: 0.5em;
  text-align: left;

}

#pictures-container{
  background-color:red;
  grid-area: pictures;
  
}
#buttons-container{
  background-color:green;
  grid-area: buttons;
}
a{
  color: #42b983;
}
</style>
