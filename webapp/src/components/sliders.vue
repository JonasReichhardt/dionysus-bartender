<template>
    <div id="slider-area-container">
    <div id="pump1">Pumpe 1
      <span class="pump1-slider-area">
        <input type="range" min="0" max="100" value="55" class="" id="slider-pump1">
				<input  type="number" min="0" max="100" value="55" class="input-slider" id="input-pump1">
      </span>
    </div>
    <div id="pump2">Pumpe 2
      <span class="pump2-slider-area">
        <input type="range" min="0" max="100" value="55" class="" id="slider-pump2">
				<input  type="number" min="0" max="100" value="55" class="input-slider" id="input-pump2">
      </span>
    </div>
    <div id="pump3">Pumpe 3
      <span class="pump3-slider-area">
        <input type="range" min="0" max="100" value="55" class="" id="slider-pump3">
				<input  type="number" min="0" max="100" value="55" class="input-slider" id="input-pump3">
      </span>
    </div>
    <div id="pump4">Pumpe 4
      <span class="pump4-slider-area">
        <input type="range" min="0" max="100" value="55" class="" id="slider-pump4">
				<input  type="number" min="0" max="100" value="55" class="input-slider" id="input-pump4">
      </span>
    </div>
    <div id="pump5">Pumpe 5
      <span class="pump5-slider-area">
        <input type="range" min="0" max="100" value="55" class="" id="slider-pump5">
				<input  type="number" min="0" max="100" value="55" class="input-slider" id="input-pump5">
      </span>
    </div>
    <div id="pump6">Pumpe 6
      <span class="pump6-slider-area">
        <input type="range" min="0" max="100" value="55" class="" id="slider-pump6">
				<input  type="number" min="0" max="100" value="55" class="input-slider" id="input-pump6">
      </span>
    </div>
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
  flex: 1 1 auto;
  flex-wrap: wrap;
}

</style>