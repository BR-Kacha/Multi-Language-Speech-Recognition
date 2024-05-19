# Multi-Language-Speech-Recognition
# Automatic Speech Recognition with Translation (SSIP Hackathon Project)

This project, which earned an appreciation prize at an SSIP hackathon, implements automatic speech recognition (ASR) with translation capabilities in Python. Users can convert spoken words into text and translations (English, Hindi, Gujarati) for both live speech and pre-recorded audio files.

**User Guide:**

**Live Speech:**

1. Enter your user name.
2. Select the language you intend to speak.
3. The microphone will activate automatically upon language selection.
4. Speak the phrase clearly that you want converted into text and translated.
5. Allow some processing time. The program will generate text files with your user name and display the output on screen.

**Recorded Audio:**

1. Enter your user name.
2. Specify the path to your audio file (WAV format recommended for optimal support).
3. Select the language of the audio file.
4. Processing will start upon language selection. Give it time to complete.
5. The program will generate text files with your user name and display the output on screen.

**Features:**

* User-friendly interface for live and recorded audio processing
* Language selection for accurate speech recognition
* Text file generation with user names for organized storage
* Multi-language translation (English, Hindi, Gujarati)
* Supports both live and pre-recorded audio formats (WAV recommended)

**Applications:**

* Report writing
* Document preparation
* Video platforms (transcription)
* Media monitoring
* Virtual meetings (live captioning)
* Converting audio to text from social media platforms like YouTube

**Project Structure:**

* `live_speech.py`: Script for live speech recognition and translation
* `recorded_audio.py`: Script for pre-recorded audio recognition and translation (replace with your actual file names)
* `exe` folder : Contains compiled executable files for the scripts 

**Installation:**

1. Clone this repository: `git clone https://github.com/BR-Kacha/Multi-Language-Speech-Recognition.git`
2. Install dependencies : `pip install tk-tools`
                          `pip install SpeechRecognition`
                          `pip install translate`

**Usage:**

1. Refer to the instructions within the respective Python scripts (`live_speech.py` or `recorded_audio.py`) for user input and language selection.
2. Speak clearly for live speech or provide the path to your audio file.
3. The program will generate text files and translations upon successful processing.

**Contribution:**

Feel free to submit pull requests for improvements or bug fixes.

**Author:**

Brijraj Kacha, 
GitHub: [https://github.com/BR-Kacha]
Linkedin: [https://www.linkedin.com/in/brijraj-kacha/]

**Additional Notes:**

(Mention any specific requirements, limitations, or future enhancements)
