import speech_recognition as sr


def transcribe_audio_from_video(audio_path):
    sr_instance = sr.Recognizer()

    with sr.AudioFile(audio_path) as source:
        audio = sr_instance.record(source, duration=120)

    audio_text = sr_instance.recognize_google(audio_data=audio, language='ko-KR')
    return audio_text