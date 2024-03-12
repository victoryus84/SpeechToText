import assemblyai as aai
import os
from pathlib import Path
import functools

def addNewLineAfterDot(text):
    array_text = text.split(". ")
    # print(array_text)
    text_with_n = ""
    for i in range(len(array_text)):
        text_with_n += array_text[i] + '\n' 
    
    return text_with_n

def writeDataFile(file_path, text):
    try:
        with open(file_path, 'w') as f:
            f.write(text)
            print("Created transcript: " + file_path)
    except  FileNotFoundError:
        print("The 'docs' directory does not exist")
    
    return True    

def transcript(transcriber):
    
    # transcript = transcriber.transcribe("https://storage.googleapis.com/aai-web-samples/news.mp4")
    # transcript = transcriber.transcribe('.\\audio\\20.56​.m4a')

    audio_dir = '.\\audio'
    docs_dir = '.\\docs'
    n = 0
    for filename in os.listdir(audio_dir):
        n += 1
        
        # if n > 1: 
        #     continue
        
        if filename.endswith('.m4a'):
            audio_path = os.path.join(audio_dir, filename)
            transcript = transcriber.transcribe(audio_path)
            if transcript.status == aai.TranscriptStatus.error:
                print(transcript.error)
            else:
                file_path = os.path.join(docs_dir, Path(audio_path).stem + '.txt')
                result_text = addNewLineAfterDot(transcript.text)
                writeDataFile(file_path, result_text)  
            
if __name__ == "__main__":
    aai.settings.api_key = "6d44a79cadff48ddac89f3685f0a19cf"
    transcriber = aai.Transcriber()
    print("Function called!")
    transcript(transcriber)    
    