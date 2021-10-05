
import os

from Classes.Audio_Translator import AudioTranslator

path_audio = os.path.join('testAudio3.wav')

language_my_audio = 'en'
language_to_translate_my_audio = 'pt'

audio_translate = AudioTranslator(language_my_audio, language_to_translate_my_audio, path_audio)
audio_translate.translate_audio()

text_translated = audio_translate.get_text_translated()
print(text_translated)
