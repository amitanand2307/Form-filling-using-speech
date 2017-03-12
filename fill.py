from pytesseract import *
from PIL import Image, ImageEnhance, ImageFilter
from gtts import gTTS
import os
from pygame import mixer # Load the required library
from cStringIO import StringIO
import pyttsx
import speech_recognition as sr
import time

im = Image.open("forms/name.jpg") # the second one
text1 = image_to_string(im)
print text1
f=open('text.txt','w')
f.write(text1)
f.close()


r = sr.Recognizer()
m = sr.Microphone()
source = m;

r.pause_threshold = 0.5
r.dynamic_energy_threshold = True

def unique_list(l):
            ulist = []
            [ulist.append(x) for x in l if x not in ulist]
            return ulist

WIT_AI_KEY = "7KEIGRAXVNP7F2XSLLCHVFCN5FTQZHQJ" # Wit.ai keys are 32-character uppercase alphanumeric strings
BING_KEY = "29915520dd2447b6ba479a1878ba239e"
BING_KEY1="183e1074883f4d26afa25d242f961e11" 
f1=open('text1.txt','w')
f=open('text.txt','r')
#f1=open('text1.txt','w')
engine = pyttsx.init()
line=f.readline()
#print line
i=0
while line:
    flag=0
    if(line!="\n"):
        if "yes" in line and "no" in line:
            line.replace('yes','')
            line.replace('no','')
            line1="yes or no"
            flag=1
        if "male" in line:
            line=line.replace('female','')
            line=line.replace('male','')
            line1="male or female"
            flag=1
        if "date" in line:
            flag=1
            line1="please say slash after date, month and year"
            
        engine.say(line)
        engine.runAndWait()    
        f1.write(line.rstrip('\n'))

        if flag==1:
            engine.say(line1)
            engine.runAndWait()
        
        print("say something")   
        with m as source:                # use the default microphone as the audio source
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)                   # listen for the first phrase and extract it into audio data
    
        try:
        #print("You said " + r.recognize_google(audio))    # recognize speech using Google Speech Recognition
            u=r.recognize_google(audio, show_all=False)
            #u=r.recognize_wit(audio, WIT_AI_KEY, show_all=False)
            u=' '.join(unique_list(u.split()))
            print u
            if(u.lower()=="skip"):
                u="";
            f1.write(u+"\n")
        except LookupError:                            # speech is unintelligible
            print("Could not understand audio")  
    
      
        print("stop")    
      
    line=f.readline()
    
#print i
f.close()
f1.close()    



