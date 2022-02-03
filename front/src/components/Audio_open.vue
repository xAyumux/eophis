<template>
    <div>
        <h2>{{msg}}</h2>
        <!--<button v-on:click="download">開始</button>-->
        <p>実行と同時に録音がはじまり、10秒程かけて音声データを生成します</p>
        <a id="dl">ダウンロード</a>
    </div>
</template>

<script>
export default {

    data:function(){
        return {
            msg:"音声登録中です。登録には10秒程かかります。"
        }
    },
    methods:{
        
        //録音用関数
        recording:function(){

            console.log("audio_open")
            navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia;

            navigator.getUserMedia({
                audio: true,
                video: false
            }, this.successFunc, this.errorFunc);
        },

        successFunc:function(stream) {
            var recorder = new MediaRecorder(stream, { 
                mimeType: 'video/webm;codecs=vp9'
                });

            //音を拾い続けるための配列。chunkは塊という意味
            var chunks = [];

            //集音のイベントを登録する
            recorder.addEventListener('dataavailable', function(ele) {
                if (ele.data.size > 0) {
                    chunks.push(ele.data);
                }
            });

            // recorder.stopが実行された時のイベント
            recorder.addEventListener('stop', function() {

                var dl = document.querySelector("#dl");

                //集音したものから音声データを作成する
                dl.href = URL.createObjectURL(new Blob(chunks));
                dl.download = 'sample.mp3';
            
            });

            recorder.start();

            //10秒後に集音を終了する。
            setTimeout(function() {
                alert("音声登録が完了しました。");
                recorder.stop();
            }, 10000);
        },
        errorFunc(){
            alert("error");
        }


    }
}
</script>