# eophis

## 技術選定

- フロントエンド  
   HTML  
   JavaScript

- バックエンド  
   Python  
   Flask  
   Firebase  
   Firebase Realtime Database

## タスク設計

１．音声登録（ニックネームも）  
２．発話（鍵を開けたいとき）  
３．照合  
４．結果を表示

## フロントエンド

### 音声登録

- 音声データ or テキストデータを送る

### 音声認識

- 音声データを送る
- 正否 json を受け取る
- 画面遷移

## バックエンド

- 音声の受け取り
- 正否 json の返し
- データベースにテキストか音声を保存

### 音声ファイルの扱い

- NoSQL (Firebase Realtime Database)に登録出来た場合  
  そのままデータベースに登録する

- NoSQL (Firebase Realtime Database)に登録出来なかった場合  
  フォルダにファイルを保存  
  データベースにはパスを保存
