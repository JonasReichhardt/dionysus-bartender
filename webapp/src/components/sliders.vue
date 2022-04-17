<template>
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
</template>

<script>
export default{
    name: 'sliders_area'
}
</script>


<style scoped>
#slider-area-container{
  background-color:powderblue;
  font-size: 0.7em;
  display:flex;
  flex-direction: column;
  grid-area: slider;
  justify-content: space-around;
  align-items: flex-start;
  padding: 0.4em;
  gap: 0.3em;
  flex-wrap: wrap;
}

</style>