<template>
<div class="container">
  <div class="sliders">
    <div id="pump1">Pumpe 1
      <span class="pump1-slider-area">
        <input type="range" min="0" max="100"  class="" id="slider-pump1" v-model.number="pumpvals[0]" @change="normalizeVals(0); roundVals()">
				<input  type="number" min="0" max="100" class="input-slider" id="input-pump1" v-model.number="roundedPumpVals[0]" @change="passNewVal(0); normalizeVals(0); roundVals()">
      </span>
    </div>
    <div id="pump2">Pumpe 2
      <span class="pump2-slider-area">
        <input type="range" min="0" max="100" class="" id="slider-pump2" v-model.number="pumpvals[1]" @change="normalizeVals(1); roundVals()">
				<input  type="number" min="0" max="100" class="input-slider" id="input-pump2" v-model.number="roundedPumpVals[1]" @change="passNewVal(1); normalizeVals(1); roundVals()">
      </span>
    </div>
    <div id="pump3">Pumpe 3
      <span class="pump3-slider-area">
        <input type="range" min="0" max="100" class="" id="slider-pump3" v-model.number="pumpvals[2]" @change="normalizeVals(2); roundVals()">
				<input  type="number" min="0" max="100" class="input-slider" id="input-pump3" v-model.number="roundedPumpVals[2]" @change="passNewVal(2); normalizeVals(2); roundVals()">
      </span>
    </div>
    <div id="pump4">Pumpe 4
      <span class="pump4-slider-area">
        <input type="range" min="0" max="100" class="" id="slider-pump4" v-model.number="pumpvals[3]" @change="normalizeVals(3); roundVals()">
				<input  type="number" min="0" max="100" class="input-slider" id="input-pump4" v-model.number="roundedPumpVals[3]" @change="passNewVal(3); normalizeVals(3); roundVals()">
      </span>
    </div>
    <div id="pump5">Pumpe 5
      <span class="pump5-slider-area">
        <input type="range" min="0" max="100" class="" id="slider-pump5" v-model.number="pumpvals[4]" @change="normalizeVals(4); roundVals()">
				<input  type="number" min="0" max="100" class="input-slider" id="input-pump5" v-model.number="roundedPumpVals[4]" @change="passNewVal(4); normalizeVals(4); roundVals()">
      </span>
    </div>
    <div id="pump6">Pumpe 6
      <span class="pump6-slider-area">
        <input type="range" min="0" max="100" class="" id="slider-pump6" v-model.number="pumpvals[5]" @change="normalizeVals(5); roundVals()">
				<input  type="number" min="0" max="100" class="input-slider" id="input-pump6" v-model.number="roundedPumpVals[5]" @change="passNewVal(5); normalizeVals(5); roundVals()">
      </span>
    </div>
  </div>
  <div class="pictures">pictures</div>
  <div class="buttons">buttons</div>
</div>
</template>

<script>

export default {
  name: 'HelloWorld',
  data(){
      return{
        pumpvals: [20,20,15,15,15,15],
        pumpvalscopy: [20, 20, 15, 15, 15, 15],
        roundedPumpVals:[20,20,15,15,15,15],
        enablepump: [true, true, true, true, true, true]
      }
    },
    
    methods:{
        normalizeVals: function(index){
        console.log("Before values of pumpvals: " + this.pumpvals[0] + " " + this.pumpvals[1] + " " + this.pumpvals[2] + " " + this.pumpvals[3] + " " + this.pumpvals[4] + " " + this.pumpvals[5])
          let absDiff = this.pumpvals[index] - this.pumpvalscopy[index];
          let currPump = index;
          let nActivePumps = 0;

          if(this.pumpvals[index] > 1){this.enablepump[index] = true} 

          for(let i in this.enablepump){ //compute num of active pumps
            if(this.enablepump[i]){
              nActivePumps++;
            }
          }
          let DiffPerPump = (-1) * (absDiff/(nActivePumps-1));

          for(var i = 0; i < this.pumpvals.length; i++){
            if(this.enablepump[i] && i != index){
              let x = this.pumpvals[i] + Math.round(DiffPerPump);
              if(x< 0.5){ this.enablepump[i] = false} //disable pumps with val < 0.5, if x>= 0.5 it is rounded up to 1
              this.pumpvals[i] = x <= 0 ? 0:x;
            }
          }

          nActivePumps = 0;
          for(let i in this.enablepump){ //compute num of the current active pumps
            if(this.enablepump[i]){
              nActivePumps++;
            }
          }

          let sum = 0;
          for(let i = 0; i < this.pumpvals.length; i++){ //get sum of pumpvals
            sum += this.pumpvals[i]*1;
          }

          let sumDiff = sum - 100; // check if the new sum is bigger than 100
          let newDiffPer = sumDiff/nActivePumps;

          for(let i in this.enablepump){ //subtract the diff to 100, so the sum of all vals equal to 100
            if(this.enablepump[i]){
              this.pumpvals[i] -= newDiffPer;
            }
          }

          let newSum = 0;
          for(let i = 0; i < this.pumpvals.length; i++){
            newSum += this.pumpvals[i]*1;
          }
        

          for (let i = 0; i < this.pumpvals.length; i++){ //update pumpvalscopy
            this.pumpvalscopy[i] = this.pumpvals[i]
          }
          
          console.log(this.enablepump[0] + " " + this.enablepump[1] + " " + this.enablepump[2] + " " + this.enablepump[3] + " " + this.enablepump[4] + " " + this.enablepump[5])
          console.log("absDiff: " + absDiff + "\ncurrPump: " + currPump +  "\nnActivePumps: " + nActivePumps + "\nDiffPerPump: " + DiffPerPump + "\nsum: " + sum + "\nnewSum: " + newSum);
          console.log("After the function: " + this.pumpvalscopy[0] + " " + this.pumpvalscopy[1] + " " + this.pumpvalscopy[2] + " " + this.pumpvalscopy[3] + " " + this.pumpvalscopy[4] + " " + this.pumpvalscopy[5]);
          console.log(" ");
        },
        roundVals: function(){
          for (let i = 0; i < this.pumpvals.length; i++){
            this.roundedPumpVals[i] = this.pumpvals[i].toFixed(0)
          }
        },
        changeCheckBox: function(index){
          this.enablepump[index] = !this.enablepump[index]
          if(!this.enablepump[index]){
            this.pumpvals[index] = 0;
          }
        },
        passNewVal: function(index){ //pass new roundedVal to pumpvals, otherwise "normalizeVals()" doesnt work or new val in number input isnt updated
          this.pumpvals[index] = this.roundedPumpVals[index]
        }
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
.sliders{
  grid-area: slider;
  background-color:powderblue;
  font-size: 0.7em;
  display:flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: flex-start;
  padding: 0.4em;
  gap: 0.3em;
  flex: 1 1 auto;
  flex-wrap: wrap;
}
.sliders input[type = "number"]{
  width:2.5em
}
.pictures{
  grid-area: pictures;
  background-color:red;
}
.buttons{
  grid-area: buttons;
  background-color:green;
}
.container div{
  font-size: 0.7em;
  padding: 0.1em;
}
</style>
