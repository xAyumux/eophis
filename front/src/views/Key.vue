<template>
    <div>
        <span>
            <p>{{ msg }}</p>
            <img :src="image_src">
        </span>
    </div>
    <div>
        <span>
            <button v-on:click="changeimage">開錠開始</button>
        </span>
        <span>
            <button v-show="flag">
                <router-link to="/">
                    {{ button_msg }}
                </router-link>
            </button>
        </span>
    </div>
    <div v-show="audioflag">
        <Audio ref="audio" />
    </div>

</template>

<script>
import Audio from '../components/Audio_open.vue'

export default {
    name: 'Key',
    components:{
        Audio
    },
    data:function(){
        return {
            flag: false,
            audioflag: false,
            image_src: require("@/assets/key.png"),
            msg: "鍵を開けます。音声を入力してください",
            button_msg : "ホームへ戻る"
        }
    },
    methods:{
        changeimage:function(){
            console.log("ang")
            this.$refs.audio.recording()
            //this.image_src = require("@/assets/car.png")
            this.flag = true
            this.audioflag = true
            this.msg = "鍵が開きました"
        }
    }
}
</script>