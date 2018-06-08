# Dylan AI alpha
# Version 0.1

import random;
import pyttsx3;
import speech_recognition as sr;
import pyaudio;

print(" Hey, I'm Dylan AI. Ask me anything!");
print(" Say 'help' for a full list of commands!");
print("");
print("");

engine = pyttsx3.init();
engine.say("Hey, I'm Dylan AI. Ask me anything!");
engine.runAndWait();

def help_dai():
 print("");
 print(" ------ HELP ------ ");
 print(" Here's a list of available commands!");
 engine.say("Here's a list of available commands!");
 engine.runAndWait();
 print("");
 print(" info - will show You current version and some other info");
 print(" random - will tell You a random number");
 print(" word - will tell You a random word");
 print("");
 wake_dai();

def info_dai():
 print("");
 print(" ------ INFO ------ ");
 print(" Current Version: 0.1 alpha ");
 print(" Using pyttsx3 ");
 print("");
 wake_dai();

def random_dai():
 print("");
 rndnmb = [' 0',' 1' ,' 2',' 86',' 20',' 34',' 11'];
 print(random.choice(rndnmb));
 print("");
 wake_dai();

def word_dai():
 print("");
 rndwrd = [' wat',' lol',' hey',' carrot',' car'];
 print(random.choice(rndwrd));
 print("");
 wake_dai();

def wake_dai():
 r = sr.Recognizer();
 with sr.Microphone() as source:
  print(" Say 'Hey Dylan' to activate listening");
  audio = r.listen(source,timeout=1,phrase_time_limit=5);

 usrinput_wake = r.recognize_sphinx(audio);

 if(usrinput_wake == "hey dylan"): # Change to Hey to increase sensitivity
  core_dai();
 else:
  print(" Say that again!");
  wake_dai();

def core_dai():
 r = sr.Recognizer();
 with sr.Microphone() as source:
  print(" Say something!");
  audio = r.listen(source,timeout=1,phrase_time_limit=5);

 usrinput = r.recognize_sphinx(audio);

 try:
  #print(r.recognize_sphinx(audio)); Enable for Debug
  if(usrinput == "help"):
   help_dai();
  elif(usrinput == "info"):
   info_dai();
  elif(usrinput == "random"):
   random_dai();
  elif(usrinput == "word"):
   word_dai();
 except sr.UnknownValueError:     # Looks like that part doesn't work. Instead of printing,
   print(" Wrong command! / Say that again!");  # it quietly closes the program
 except sr.RequestError as e:
   print(" We got an error!");

wake_dai();

