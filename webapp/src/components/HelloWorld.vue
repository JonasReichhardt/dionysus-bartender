<template>
<img src="../assets/cocktail-logo_without_background.png" width="200">
  <div class="hello">
    <h2 style="font-size:40px;">"Hello"</h2>
  </div>
  <input type="number" min="0" max="100" value="99" class="input-slider" >
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
.input-slider {
    width: 45px;
    background-color: aqua;
}
.range-sliders .input-slider {
    border: 1px solid #e6e6e6;
    padding: 0.5rem;
    -moz-appearance: textfield;
}
a {
  color: #42b983;
}
</style>
