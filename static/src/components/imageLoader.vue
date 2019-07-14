<template>
    <div>
        <label>File
            <input type="file" id="file" ref="file" v-on:change="handleFileUpload()"/>
        </label><br>
        <button v-on:click="submitFile()">Upload</button>
    </div>
</template>

<script>
import axios from 'axios'

  export default {
    data(){
      return {
        file: ''
      }
    },

    methods: {
        submitFile(){
            let formData = new FormData();
            formData.append('file', this.file);
            var self = this
            axios.post('/api/upload_file',
                formData,
                {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
              }
            ).then(function(res){
                self.changePath(res.data)
            })
            .catch(function(err){
                console.log(err)
            });
        },
        handleFileUpload(){
            this.file = this.$refs.file.files[0];
        },
        changePath(path) {
          this.$emit('changePath', {
            path: path
          })
        }
    }
  }
</script>