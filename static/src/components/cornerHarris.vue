<template>
    <div>
        <p>Block Size: {{ blockSize }}</p>
        <input type="range" min="1" max="31" @mouseup="changeCorners()" v-model="blockSize" step="2">
        <p>k Size: {{ kSize }}</p>
        <input type="range" min="1" max="31" @mouseup="changeCorners()" v-model="kSize" step="2">
        <p>k: {{ k/100000 }}</p>
        <input type="range" min="1000" max="20000" @mouseup="changeCorners()" v-model="k" step="1000"><br>
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
        blockSize: 7,
        kSize: 9,
        k: 4000,
      }
    },
    methods: {
        changeCorners() {
          var self = this
          axios.post('/api/corner_harris',{
            name: this.name,
            blockSize: this.blockSize,
            kSize: this.kSize,
            k: this.k / 100000
          }).then(function(res){
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
