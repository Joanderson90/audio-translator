# audio-translator
Audio translator using python.



<!-- ABOUT THE PROJECT -->
## About The Project

A program that can translate audio.
Work in progress.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Speech Recognition](https://pypi.org/project/SpeechRecognition/)
* [Google Trans](https://pypi.org/project/googletrans/)
* [Pyttsx3](https://pypi.org/project/pyttsx3/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started


### Prerequisites

*  Python 3.6+.
  
* SpeechRecognition 3.8.1
  ```sh
    pip install SpeechRecognition
  ```
  
* googletrans 4.0.0
  ```sh
    pip install googletrans==4.0.0-rc1
  ```

* pyttsx3 2.90
  ```sh
     pip install pyttsx3
  ```
  

<!-- USAGE EXAMPLES -->
## Usage

```py


  from Classes.Audio_Translator import AudioTranslator

  path_audio = os.path.join('testAudio3.wav')

  language_my_audio = 'en'
  language_to_translate_my_audio = 'pt'

  audio_translate = AudioTranslator(language_my_audio, language_to_translate_my_audio, path_audio)
  audio_translate.translate_audio()

  text_translated = audio_translate.get_text_translated()
  print(text_translated)

```




