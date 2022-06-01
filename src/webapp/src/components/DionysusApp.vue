<template>
  <div class="container" v-if="loaded">
    <div class="sliders">
      <div>
        <label >Choose a drink size: <br></label>
        <select @change="drinkSizeChanged($event)">
          <option value="150">150</option>
          <option selected value="200">200</option>
          <option value="250">250</option>
          <option value="300">300</option>
          <option value="350">350</option>
          <option value="400">400</option>
        </select> ml
      </div>
      <div v-for="(ing, index) in ingredients" :key="ing">
        {{ ing }}
        <span>
          <input
            type="range"
            min="0"
            max="100"
            v-model.number="pumpvals[index]"
            @change="
              normalizeVals(index);
              roundVals();
            "
          />
          <input
            type="number"
            min="0"
            max="100"
            v-model.number="roundedPumpVals[index]"
            @change="
              passNewVal(index);
              normalizeVals(index);
              roundVals();
            "
          />
        </span>
      </div>
    </div>
    <div class="pictures">
      <div v-for="(cock, index) in cocktails" :key="cock">
        <button @click="passCockVal(index)">
          {{ cock.name }}
        </button>
      </div>
    </div>
    <div class="buttons">
      <button @click="sendCocktailReq()">MOCH MA MEI DRANGL HEAST!!!!!!</button><br/>
      <button @click="cancelCocktailReq()">HEA AUF I WÜ DES DRINGA NED!!!!!</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "DionysusApp",
  data() {
    return {
      pumpvals: null,
      pumpvalscopy: null,
      roundedPumpVals: null,
      enablepump: null,
      ingredients: null,
      loaded: false,
      cocktails: null,
      selectedCocktail: null,
      selectedSize: 200,
      serverAddr: "192.168.250.74"
    };
  },
  created: async function () {
    let ingResponse = await fetch("http://"+this.serverAddr+":8081/ingredients");

    if (ingResponse.ok) {
      this.ingredients = await ingResponse.json();
      let initialVal = 100 / this.ingredients.length;
      this.pumpvals = Array(this.ingredients.length).fill(initialVal);
      this.pumpvalscopy = this.pumpvals.map((x) => x);
      this.roundedPumpVals = this.pumpvals.map((x) => x.toFixed(0));
      this.enablepump = Array(this.ingredients.length).fill(true);
    } else {
      alert("HTTP-Error: " + ingResponse.status);
      return;
    }

    let cocktailsResponse = await fetch("http://"+this.serverAddr+":8081/cocktails");

    if (cocktailsResponse.ok) {
      this.cocktails = await cocktailsResponse.json();
    } else {
      alert("HTTP-Error: " + cocktailsResponse.status);
      return;
    }

    this.loaded = true;
  },
  methods: {
    normalizeVals: function (index) {
      let absDiff = this.pumpvals[index] - this.pumpvalscopy[index];
      let currPump = index;
      let nActivePumps = 0;

      if (this.pumpvals[index] > 1) {
        this.enablepump[index] = true;
      }

      for (let i in this.enablepump) {
        //compute num of active pumps
        if (this.enablepump[i]) {
          nActivePumps++;
        }
      }
      let DiffPerPump = -1 * (absDiff / (nActivePumps - 1));

      for (var i = 0; i < this.pumpvals.length; i++) {
        if (this.enablepump[i] && i != index) {
          let x = this.pumpvals[i] + Math.round(DiffPerPump);
          if (x < 0.5) {
            this.enablepump[i] = false;
          } //disable pumps with val < 0.5, if x>= 0.5 it is rounded up to 1
          this.pumpvals[i] = x <= 0 ? 0 : x;
        }
      }

      nActivePumps = 0;
      for (let i in this.enablepump) {
        //compute num of the current active pumps
        if (this.enablepump[i]) {
          nActivePumps++;
        }
      }

      let sum = 0;
      for (let i = 0; i < this.pumpvals.length; i++) {
        //get sum of pumpvals
        sum += this.pumpvals[i] * 1;
      }

      let sumDiff = sum - 100; // check if the new sum is bigger than 100
      let newDiffPer = sumDiff / nActivePumps;

      for (let i in this.enablepump) {
        //subtract the diff to 100, so the sum of all vals equal to 100
        if (this.enablepump[i]) {
          this.pumpvals[i] -= newDiffPer;
        }
      }

      let newSum = 0;
      for (let i = 0; i < this.pumpvals.length; i++) {
        newSum += this.pumpvals[i] * 1;
      }

      for (let i = 0; i < this.pumpvals.length; i++) {
        //update pumpvalscopy
        this.pumpvalscopy[i] = this.pumpvals[i];
      }
      console.log(this.pumpvals);
      console.log("rounded: " + this.roundedPumpVals);

      console.log(
        "absDiff: " +
          absDiff +
          "\ncurrPump: " +
          currPump +
          "\nnActivePumps: " +
          nActivePumps +
          "\nDiffPerPump: " +
          DiffPerPump +
          "\nsum: " +
          sum +
          "\nnewSum: " +
          newSum
      );
    },

    roundVals: function () {
      for (let i = 0; i < this.pumpvals.length; i++) {
        this.roundedPumpVals[i] = this.pumpvals[i].toFixed(0);
      }
    },
    changeCheckBox: function (index) {
      this.enablepump[index] = !this.enablepump[index];
      if (!this.enablepump[index]) {
        this.pumpvals[index] = 0;
      }
    },

    passNewVal: function (index) {
      //pass new roundedVal to pumpvals, otherwise "normalizeVals()" doesnt work or new val in number input isnt updated
      this.pumpvals[index] = this.roundedPumpVals[index];
    },

    passCockVal: function (index) {
      let ctail = this.cocktails[index];
      let ctailIng = [];
      ctail.ingredients.forEach((ing) => {
        ctailIng.push(ing.name);
      });

      let amounts = [];
      ctail.ingredients.forEach((ing) => {
        amounts.push(ing.amount);
      });

      let amount = amounts.reduce((a, b) => a + b);

      for (let i = 0; i < ctail.ingredients.length; i++) {
        for (let j = 0; j < this.ingredients.length; j++) {
          if (ctail.ingredients[i].name == this.ingredients[j]) {
            this.pumpvals[j] = (amounts[i] / amount) * 100;
          }
        }
      }

      for (let i = 0; i < this.ingredients.length; i++) {
        if (!ctailIng.includes(this.ingredients[i])) {
          this.enablepump[i] = false;
          this.pumpvals[i] = 0;
        }
      }
      this.roundVals();
      this.selectedCocktail = index;
    },

    sendCocktailReq: function () {
      let cocktail = {
        name:"custom",
        ingredients: []
      }

      this.pumpvals.forEach((val, index) =>{
        if(val > 0){
          cocktail.ingredients.push({name: this.ingredients[index], amount: this.selectedSize*(val/100)})
        }
      })

      fetch("http://"+this.serverAddr+":8081/cocktails/custom", {
        method: "post",
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(cocktail)
      });
    },

    drinkSizeChanged: function($event){
      this.selectedSize = parseInt($event.target.options[$event.target.options.selectedIndex].text);
    },

    cancelCocktailReq: function(){
      fetch("http://"+this.serverAddr+":8081/cocktails/standard/cancel", {
        method: "post",
      });
    }
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.container {
  display: grid;
  width: 100vw;
  height: 100vh;
  grid-auto-columns: minmax(0, 1fr);
  grid-template-columns: 50% 50%;
  grid-template-rows: 85% 1fr;
  grid-template-areas:
    "slider pictures"
    "slider pictures"
    "buttons buttons";
  gap: 5px;
  padding: 5px;
  box-sizing: border-box;
}
.sliders {
  grid-area: slider;
  background-color: powderblue;
  font-size: 0.7em;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: flex-start;
  padding: 0.4em;
  gap: 0.3em;
  flex: 1 1 auto;
  flex-wrap: wrap;
}
.sliders input[type="number"] {
  width: 2.5em;
}
.pictures {
  grid-area: pictures;
}
.buttons {
  grid-area: buttons;
  background-color: green;
}
.container div {
  font-size: 0.7em;
  padding: 0.1em;
}
</style>
