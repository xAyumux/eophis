<template>
    <div class="select">
        <h2>音声の録音を行います。<br>下の音声登録ボタンを押すとパソコンのマイクにアクセスして登録します。</h2>
    </div>
    <div>
        <button v-on:click="audio">
            音声登録
        </button>
    </div>
    <div v-show="flag">
        <Audio ref="audio" />
    </div>
    <br>
    <br>
    <button v-show="isActive">
            <router-link to="/">
            戻る
            </router-link>
        </button>
</template>

<script>
import Audio from '../components/Audio.vue' 

export default {
    components:{
        Audio
    },
    data:function(){
        return {
            //非表示解除用トリガー
            isActive:false,
            flag: false
        }
    },
    methods: {

        //audioコンポーネントを起動
        audio:function(){
            //録音の処理.recording関数
            this.$refs.audio.recording()
            this.flag = true
            this.isActive = true
        },
    }
}

</script>