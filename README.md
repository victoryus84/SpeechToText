Program Description: SPEECH TO TEXT

Overview:
The Audio to Text Converter is a command-line tool designed to transcribe speech from audio files into text format. It provides a convenient way to convert audio recordings, particularly in the M4A format, into readable text files.

Features:

M4A Audio Support: The program supports input audio files in the M4A format commonly used in various recording devices and applications.

Speech Recognition: Utilizing advanced speech recognition technology, the program accurately transcribes spoken words from the audio files into text format.

Text Output: Upon conversion, the program generates a text file containing the transcribed text. Each spoken word or phrase is accurately captured and organized in the text file.

Customization Options: Users have the flexibility to specify additional parameters such as language models, speaker recognition, and transcription accuracy levels to tailor the conversion process according to their requirements.

Batch Processing: The program supports batch processing, allowing users to convert multiple audio files sequentially. This feature enhances productivity by automating the conversion process for large volumes of audio recordings.

Error Handling: Robust error handling mechanisms are implemented to detect and handle common issues during the conversion process, ensuring reliable and consistent performance.

Usage:
Before running the program, ensure that your audio files are organized within a folder named "audio" in the same directory as the main script. This folder should contain all the M4A audio files that you wish to convert to text format. Add .env file with your API_KEY exemple: API_KEY=6d44a7scadfd48ddac89f3685f0a19cf

To initiate the conversion process, execute the main script (main.py) from the command line or terminal, providing any necessary parameters such as language settings or output file location.

Example Command:

python main.py 

If you know the audio language then add a parameter --language=[view supported languages]
Default language code is "en_us" 

Supported languages:
    https://www.assemblyai.com/docs/concepts/supported-languages

Output:
Upon execution, the program will process all audio files located within the "audio" folder and generate corresponding text files in "docs" folder containing the transcribed speech.

This program serves as a valuable tool for various applications such as transcription services, automated note-taking, and accessibility solutions, offering users a convenient way to convert spoken content from audio recordings into readable text format.





