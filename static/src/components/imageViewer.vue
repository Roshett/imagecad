<template>
    <div>
        <img :src="path" alt="">
    </div>
</template>

<script>
import axios from 'axios'

  export default {
    props: {
        path: {
          type: String,
          default: '',
        },
    },
    data(){
      return {
        
      }
    },
  }
</script>

<style lang="scss" scoped>
    img {
        width: 400px;
        height: 100%;
    }
</style>
