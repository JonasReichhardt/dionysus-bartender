<template>
  <div>
    <div>
      <p>Pump 1:</p>
      <select v-model="pumpConfig[0]">
        <option v-for="option in options" :value="option.value" :key="option.text">
          {{ option.text }}
        </option>
      </select>
    </div>
    <div>
      <p>Pump 2:</p>
      <select v-model="pumpConfig[1]">
        <option v-for="option in options" :value="option.value" :key="option.text">
          {{ option.text }}
        </option>
      </select>
    </div>
    <div>
      <p>Pump 3:</p>
      <select v-model="pumpConfig[2]">
        <option v-for="option in options" :value="option.value" :key="option.text">
          {{ option.text }}
        </option>
      </select>
    </div>
    <div>
      <p>Pump 4:</p>
      <select v-model="pumpConfig[3]">
        <option v-for="option in options" :value="option.value" :key="option.text">
          {{ option.text }}
        </option>
      </select>
    </div>
    <div>
      <p>Pump 5:</p>
      <select v-model="pumpConfig[4]">
        <option v-for="option in options" :value="option.value" :key="option.text">
          {{ option.text }}
        </option>
      </select>
    </div>
    <div>
      <p>Pump 6:</p>
      <select v-model="pumpConfig[5]">
        <option v-for="option in options" :value="option.value" :key="option.text">
          {{ option.text }}
        </option>
      </select>
    </div>
  </div>
</template>


<script>
export default {
  name: "PumpConfiguration",
  data() {
    return {
      pumpConfig: ['osaft', 'osaft', 'osaft', 'osaft', 'osaft', 'osaft'],
      selected: 'A',
      options: [
        {text: 'OSaft', value: 'A'},
        {text: 'Vodka', value: 'B'},
        {text: 'Cola', value: 'C'}
      ],
      serverAddr: "192.168.178.157"
    }
  },
  methods: {
    sendPost() {
      fetch.post("http://" + this.serverAddr + ":8081/ingredients", this.pumpConfig)
          .then(res => {
            console.log(res)
          })
    }
  }
};
</script>

<style>
p {
  font-size: 40%;
}
</style>
