<template>
    <div>
        <!--<button v-on:click="download">開始</button>-->
        <p>実行と同時に録音がはじまり、10秒程かけて音声データを生成します。
        <br>録音が終わるとアラートが表示されます。
        <br>ダウンロードボタンから音声ファイルをダウンロードして、ファイル選択後にアップロードしてください。
        </p>
    </div>
    <div>
        <a id="dl">ダウンロード</a>
    </div>
    <div>
        <input @change="selectedFile" type="file" name="file">
        <button @click="upload" type="submit">アップロード</button>
    </div>
</template>

<script>
import axios from 'axios';

export default {

    data:function(){
        return {
        }
    },
    methods:{
        test:function(){
            this.msg = this.msg + 1
        },
        //録音用関数
        recording:function(){
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
                //
            
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
        },
        selectedFile:function(file){
            console.log(file)
            let files = file
            this.uploadFile = files[0];
        },
        upload: function() {
            let formData = new FormData();
            formData.append("yourFileKey", this.uploadFile);
            let config = {
                headers: {
                    "content-type": "multipart/form-data",
                },
            };
        axios
            .post("flaskURL/xxxx", formData, config)
            .then(function (response) {
            // response 処理
            console.log(response.data);
        }).catch(function (error) {
            // error 処理
            console.log(error);
            });
        }
    }
}
</script>