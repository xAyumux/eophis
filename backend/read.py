import os
import io
from google.cloud import speech
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:/Users/tennp/Downloads/boxwood-magnet-340107-ad5f6a210636.json'


# Instantiates a client
client = speech.SpeechClient()
### 音声データを指定
speech_file = './output.wav'

### rb(read binary)でデータを読み込む
with io.open(speech_file, 'rb') as f:
    content = f.read()



### RecognitionAudioにデータを渡す
audio = speech.RecognitionAudio(content=content)

diarization_config = speech.SpeakerDiarizationConfig(
  enable_speaker_diarization=True,
  min_speaker_count=1,
  max_speaker_count=3,
)

config = speech.RecognitionConfig(
    ### encodeでエラーが出たのでENCODING_UNSPECIFIEDに変更
    encoding=speech.RecognitionConfig.AudioEncoding.ENCODING_UNSPECIFIED,
    language_code="ja-JP",
    diarization_config=diarization_config
)



### 音声を抽出
response = client.recognize(config=config, audio=audio)

### 抽出結果をprintで表示
"""
for result in response.results:
    print("Transcript: {}".format(result.alternatives[0].transcript))
"""
result = response.results[-1]

words_info = result.alternatives[0].words

# Printing out the output:
for word_info in words_info:
    print(
        u"word: '{}', speaker_tag: {}".format(word_info.word, word_info.speaker_tag)
    )