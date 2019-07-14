<template>
  <div id="app">
    <div class="header-wrapper">
      <div class="container">
        <div class="row">
          <div class="col-md-6">
            <h1 class="logo">ImgCAD</h1>
          </div>
          <div class="col-md-6"></div>
        </div>
      </div>
      </div>
      <div class="content-wrapper">
        <div class="container">
          <div class="row">
            <div class="col-md-6">
              <image-loader @changePath="pathToImg"></image-loader>
            </div>
            <div class="col-md-6">
              <div v-if="stage === 1">
                <black-intensity :name="nameImg" @changeImg="changeIntensity" @changeStage="changeStage(2)"></black-intensity>
                <image-viewer :path="pathImg"></image-viewer>
              </div>
              <div v-if="stage === 2">
                <corner-harris :name="nameImg" @changeImg="changeCoord" @changeStage="changeStage(3)"></corner-harris>
                <image-viewer :path="pathImg"></image-viewer>
              </div>
              <div v-if="stage === 3">
                <choose-side :name="nameImg" @changeImg="changeCoord" @changeStage="changeStage(3)"></choose-side> 
                <image-viewer :path="bufferImg"></image-viewer>
              </div>
            </div>
          </div>
        </div>
      </div>
  </div>
</template>

<script>
import axios from 'axios'
import imageLoader from './components/imageLoader.vue';
import imageViewer from './components/imageViewer.vue';
import blackIntensity from './components/blackIntensity.vue';
import cornerHarris from './components/cornerHarris.vue';
import chooseSide from './components/chooseSide.vue';

export default {
    name: 'app',
    components: {
      imageLoader,
      imageViewer,
      blackIntensity,
      cornerHarris,
      chooseSide,
    },
    data() {
        return {
          pathImg: '',
          nameImg: '',
          bufferImg: '',
          stage: 0,
        }
    },
    methods: {
      pathToImg(data) {
        this.nameImg = data.path
        this.pathImg = './src/assets/img/' + data.path
        this.changeStage(1)
      },
      changeIntensity(data) {
        this.pathImg = './src/assets/img/bp_' + data.hash + this.nameImg
      },
      changeCoord(data) {
        this.pathImg = data.hash
      },
      changeStage(stage) {
        this.stage = stage
        if(stage === 2) {
          this.nameImg = this.pathImg
          this.bufferImg = this.pathImg
        }
      }
    }
}
</script>

<style lang="scss">
  @import url(~normalize.css/normalize.css);
  @import 'node_modules/bootstrap/scss/bootstrap';
  @import 'node_modules/bootstrap-vue/src/index.scss';

  body {
    margin-top: 0;
  }

  .header-wrapper {
    height: 70px;
    width: 100%;
    background-color: #2c3e50;
  }

  .content-wrapper {
    margin-top: 50px;
  }

  .logo {
    color: white;
    font-size: 24px;
    font-family: arial;
    font-weight: normal;
    margin-top: 15px;
  }
</style>
