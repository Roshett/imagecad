<template>
    <div>
        <p>Intensity (0 - 255): {{ value }}</p>
        <input type="range" min="1" max="255" @mouseup="changeIntensity()" v-model="value"><br>
        <button @click="apply()">Apply!</button>
    </div>
</template>

<script>
import axios from 'axios'

  export default {
    props: {
        name: {
          type: String,
          default: '',
        },
    },
    data(){
      return {
        value: 0,
      }
    },
    methods: {
      changeIntensity() {
        var self = this
        axios.post('/api/intensity',{
          name: this.name,
          intensity: this.value
        }).then(function(res){
          console.log(res.data)
          self.changeImg(res.data)
        })
        .catch(function(err){
            console.log(err)
        });
      },
      changeImg(data) {
        this.$emit('changeImg', {hash: data})
      },
      apply() {
        this.$emit('changeStage')
      },
    }
  }
</script>

<style lang="scss" scoped>

</style>
