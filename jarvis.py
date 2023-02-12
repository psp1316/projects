import speech_recognition as sr
import os
import subprocess
# Initialize the recognizer
recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something!")
    audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        os.system(text)
        
        if "shutdown" in text:
         subprocess.call("shutdown /s /t 1", shell=True)
        elif "restart" in text:
          subprocess.call("shutdown /r /t 1", shell=True)
        elif "notepad" in text:
            #if "notepad" in text:
            subprocess.call("notepad", shell=True)
            #elif "chrome" in text:
                #subprocess.call("chrome", shell=True)
    # add more commands here
        else:
            print("Command not recognized.")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
