<template>
    <div>
        <span>
            <p>{{ msg }}</p>
            <img :src="image_src">
        </span>
    </div>
    <div>
        <span>
            <button v-on:click="changeimage">交換</button>
        </span>
        <span>
            <button v-show="flag">
                <router-link to="/">
                    {{ button_msg }}
                </router-link>
            </button>
        </span>
    </div>

</template>

<script>
export default {
    name: 'Key',
    data:function(){
        return {
            flag: false,
            image_src: require("@/assets/key.png"),
            msg: "鍵を開けます。音声を入力してください",
            button_msg : "ホームへ戻る"
        }
    },
    methods:{
        changeimage:function(){
            console.log("ang")
            this.image_src = require("@/assets/car.png")
            this.flag = true
            this.msg = "鍵が開きました"
        }
    }
}
</script>