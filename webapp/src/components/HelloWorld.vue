<template>
<div id="slider-area" style="background-color:powderblue;">sliders</div>
<div id="pictures" style="background-color:red;">pictures</div>
<div id="buttons" style="background-color:green;">buttons</div>
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
#slider-area{
  display: grid;
  position: static;
  float: left;
  width: 50vw;
  height: 80vh;
}
#pictures{
  display: grid;
  position:static;
  width:50vw;
  height: 80vh;
  float:right;
}
#buttons{
  
}
a{
  color: #42b983;
}
</style>
