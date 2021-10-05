import speech_recognition as sr
import pyttsx3
from googletrans import Translator


class AudioTranslator:

    text_translated = ''

    def __init__(self, audio_language, audio_language_translate, audio_path):
        self.audio_language = audio_language
        self.audio_path = audio_path
        self.audio_language_translate = audio_language_translate

    def translate_audio(self):
        self.change_audio_to_text()

    def change_audio_to_text(self):
        recognizer = sr.Recognizer()

        with sr.AudioFile(self.audio_path) as source:
            recognizer.adjust_for_ambient_noise(source)

            audio = recognizer.record(source)

            text = recognizer.recognize_google(audio, language=self.audio_language)

            self.translate_text(text)

    def translate_text(self, text):
        translate = Translator()
        trad = translate.translate(text, dest=self.audio_language_translate)
        self.text_translated = trad.text

        self.change_text_to_audio()

    def change_text_to_audio(self):
        engine = pyttsx3.init()

        engine.save_to_file(self.text_translated, f'translated_{self.audio_path}')
        engine.runAndWait()

    def get_text_translated(self):

        return self.text_translated
