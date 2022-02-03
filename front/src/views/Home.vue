<template>
  <div class="home">
    <div id="nav">
      <h1>アプリタイトル</h1>
      <p>車の音声認識を行います。音声登録前なら音声録音を押してください。
      <br>音声登録後には音声判定で実際に鍵を開けてください</p>

      <button>
        <router-link to="/Select">音声録音</router-link>
      </button>
      <button>
        <router-link to="/about">音声判定</router-link>
      </button>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
//import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  components: {
    //HelloWorld
  }
}
</script>
