<template>
    <div class="select">
        <h1>音声の録音を行います。</h1>
        <p>使用する音声ファイルを選択してください</p>
    </div>
    <div>
        <!--accept="audio/* 音声メディア対応"-->
        <input id="input-file" type="file" v-on:change="file" accept="txt">
    </div>
    <p>{{test}}</p>
    <div>
        <button v-on:click="change">音声録音</button>
        
        <button v-show="isActive">
            <router-link to="/">
            戻る
            </router-link>
        </button>
    </div>
</template>


<script>
export default {
    
    data:function(){
        return {
            test:"",
            isActive:false
        }
    },
    methods: {
        file:function(e) {
            let filedata = e.target.files[0];
            let reader = new FileReader();
            reader.readAsDataURL(filedata)
            //console.log(filedata)
            this.input_data(filedata.name)
            //this.createImage(file)
        },
        input_data:function(data){
            this.test = data
        },
        change:function() {
            this.isActive = true
        }
    }
}

</script>