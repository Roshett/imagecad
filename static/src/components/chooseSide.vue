<template>
    <div>
        <input type="text" placeholder="20" v-model="size">
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
        size: '',
      }
    },
    mounted() {

    },
    methods: {
      apply() {
        // this.$emit('changeStage')
      },
    }
  }
</script>

<style lang="scss" scoped>

</style>
