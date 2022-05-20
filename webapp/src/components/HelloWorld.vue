<template>
<div class="container">
  <sliders_area/>
  <pictures_area/>
  <buttons_area/>
</div>
</template>

<script>
import sliders_area from './sliders.vue';
import pictures_area from './pictures.vue';
import buttons_area from './buttons.vue';

export default {
  name: 'HelloWorld',
  components:{
    sliders_area,
    pictures_area,
    buttons_area
  }
  
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.container{
    display: grid;
    width: 100vw;
    height: 100vh;
    grid-auto-columns: minmax(0, 1fr);
    grid-template-columns: 50% 50%;
    grid-template-rows: 85% 1fr;
    grid-template-areas: 
    "slider pictures"
    "slider buttons";
    gap: 5px;
    padding: 5px;
    box-sizing: border-box;
}

.container div{
  font-size: 0.7em;
  padding: 0.1em;
}
</style>
