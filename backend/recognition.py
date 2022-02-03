import os
import io
from google.cloud import speech
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './key/boxwood-magnet-340107-ad5f6a210636.json'

def speech_recognition(binary_file):
    # Instantiates a client
    client = speech.SpeechClient()
    ### 音声データを指定
    speech_file = './output.wav'
    content = binary_file

    ### RecognitionAudioにデータを渡す
    audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.ENCODING_UNSPECIFIED,
        language_code="ja-JP",
    )

    ### 音声を抽出
    response = client.recognize(config=config, audio=audio)

    ### 抽出結果をprintで表示
    for result in response.results:
        print("{}".format(result.alternatives[0].transcript))


def speaker_recognition(binary_file):
    # Instantiates a client
    client = speech.SpeechClient()
    ### 音声データを指定
    speech_file = './output.wav'
    content = binary_file

    ### RecognitionAudioにデータを渡す
    audio = speech.RecognitionAudio(content=content)

    diarization_config = speech.SpeakerDiarizationConfig(
    enable_speaker_diarization=True,
    min_speaker_count=1,
    max_speaker_count=3,
    )

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.ENCODING_UNSPECIFIED,
        language_code="ja-JP",
        diarization_config=diarization_config
    )

    ### 音声を抽出
    response = client.recognize(config=config, audio=audio)

    ### 抽出結果をprintで表示
 
    result = response.results[-1]

    words_info = result.alternatives[0].words

    # Printing out the output:
    for word_info in words_info:
        print(
            u"word: '{}', speaker_tag: {}".format(word_info.word, word_info.speaker_tag)
        )