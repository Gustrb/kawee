import speech_recognition as sr


class SpeechRecognizer:
    DEFAULT_LOCALE = 'pt-BR'

    def __init__(self, locale=DEFAULT_LOCALE):
        self.recognizer = sr.Recognizer()
        self.locale = locale

    def listen(self):
        with sr.Microphone() as sound_source:
            print('Listening...')
            raw_audio = self.recognizer.listen(sound_source)

            return self.__parse_audio_into_text(raw_audio)

    def __parse_audio_into_text(self, raw_audio):
        try:
            voice_data = self.recognizer.recognize_google(raw_audio, language=self.locale)
            return voice_data

        except sr.UnknownValueError:
            return None
