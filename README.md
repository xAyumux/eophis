# eophis

ハッカソン

## 概要

話者認識を使用した声による解錠システム

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

### 音声登録

- 音声データの受け取り
- データベースにテキストか音声を保存

### 音声認識

- 音声データの受け取り
- API を使い、音声データからテキストの読み取りと話者認識
- データベースの情報と照合
- 正否 json を返す

## 音声ファイルの扱い

- NoSQL (Firebase Realtime Database)に登録出来た場合  
  そのままデータベースに登録する

- NoSQL (Firebase Realtime Database)に登録出来なかった場合  
  フォルダにファイルを保存  
  データベースにはパスを保存
