<template>
    <div id="slider-area-container">
    <div id="pump1">Pumpe 1
      <span class="pump1-slider-area">
        <input type="range" min="0" max="100"  class="" id="slider-pump1" v-model.lazy="pumpvals[0]" @change="normalizeVals(0)">
				<input  type="number" min="0" max="100" class="input-slider" id="input-pump1" v-model.lazy="pumpvals[0]" @change="normalizeVals(0)">
      </span>
    </div>
    <div id="pump2">Pumpe 2
      <span class="pump2-slider-area">
        <input type="range" min="0" max="100" class="" id="slider-pump2" v-model.lazy="pumpvals[1]" @change="normalizeVals(1)">
				<input  type="number" min="0" max="100" class="input-slider" id="input-pump2" v-model.lazy="pumpvals[1]" @change="normalizeVals(1)">
      </span>
    </div>
    <div id="pump3">Pumpe 3
      <span class="pump3-slider-area">
        <input type="range" min="0" max="100" class="" id="slider-pump3" v-model.lazy="pumpvals[2]" @change="normalizeVals(2)">
				<input  type="number" min="0" max="100" class="input-slider" id="input-pump3" v-model.lazy="pumpvals[2]" @change="normalizeVals(2)">
      </span>
    </div>
    <div id="pump4">Pumpe 4
      <span class="pump4-slider-area">
        <input type="range" min="0" max="100" class="" id="slider-pump4" v-model.lazy="pumpvals[3]" @change="normalizeVals(3)">
				<input  type="number" min="0" max="100" class="input-slider" id="input-pump4" v-model.lazy="pumpvals[3]" @change="normalizeVals(3)">
      </span>
    </div>
    <div id="pump5">Pumpe 5
      <span class="pump5-slider-area">
        <input type="range" min="0" max="100" class="" id="slider-pump5" v-model.lazy="pumpvals[4]" @change="normalizeVals(4)">
				<input  type="number" min="0" max="100" class="input-slider" id="input-pump5" v-model.lazy="pumpvals[4]" @change="normalizeVals(4)">
      </span>
    </div>
    <div id="pump6">Pumpe 6
      <span class="pump6-slider-area">
        <input type="range" min="0" max="100" class="" id="slider-pump6" v-model.lazy="pumpvals[5]" @change="normalizeVals(5)">
				<input  type="number" min="0" max="100" class="input-slider" id="input-pump6" v-model.lazy="pumpvals[5]" @change="normalizeVals(5)">
      </span>
    </div>
  </div>
</template>

<script>
export default{
    name: 'sliders_area',
    data(){
      return{
        pumpvals: [20,20,15,15,15,15],
        pumpvalscopy: [20, 20, 15, 15, 15, 15],
        enablepump: [true, true, true, true, true, true],
        counter: 0 //used for remainder handling in pumpvals
      }
    },
    methods:{
        normalizeVals: function(index){
        console.log("Before values of og pumpvals: " + this.pumpvals[0] + " " + this.pumpvals[1] + " " + this.pumpvals[2] + " " + this.pumpvals[3] + " " + this.pumpvals[4] + " " + this.pumpvals[5])
          let absDiff = this.pumpvals[index] - this.pumpvalscopy[index];
          let currPump = index;
          let nActivePumps = 0;

          for(let i in this.enablepump){ //compute num of active pumps
            if(this.enablepump[i]){
              nActivePumps++;
            }
          }
          let DiffPerPump = (-1) * (absDiff < 0 ? absDiff/(nActivePumps-1) : absDiff/(nActivePumps-1));

          for(var i = 0; i < this.pumpvals.length; i++){
            if(this.enablepump[i] && i != index){
              let x = this.pumpvals[i] + Math.round(DiffPerPump);
              this.pumpvals[i] = x < 0 ? 0:x;
            }
          }

          for (let i = 0; i < this.pumpvals.length; i++){ //update pumpvalscopy
            this.pumpvalscopy[i] = this.pumpvals[i]
            }
          var sum = 0;
          for(let i = 0; i < this.pumpvals.length; i++){
            sum += this.pumpvals[i]*1;
          }
          

          console.log("absDiff: " + absDiff + "\ncurrPump: " + currPump +  "\nnActivePumps: " + nActivePumps + "\nDiffPerPump: " + DiffPerPump + "\nsum: " + sum);
          console.log("After the function: " + this.pumpvalscopy[0] + " " + this.pumpvalscopy[1] + " " + this.pumpvalscopy[2] + " " + this.pumpvalscopy[3] + " " + this.pumpvalscopy[4] + " " + this.pumpvalscopy[5]);
        }
    }
  
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