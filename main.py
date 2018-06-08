# Dylan AI alpha
# Version 0.1

import random;
import pyttsx3;

print(" Hey, I'm Dylan AI. Ask me anything!");
print(" Try help first!");
print("");
print("");

engine = pyttsx3.init();
engine.say("Hey, I'm Dylan AI. Ask me anything!");
engine.runAndWait();

def usrinp():
 usrinput = input(" Say Something: ");

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
 core_dai();

def info_dai():
 print("");
 print(" ------ INFO ------ ");
 print(" Current Version: 0.1 alpha ");
 print(" Using pyttsx3 ");
 print("");
 core_dai();

def random_dai():
 print("");
 rndnmb = [' 0',' 1' ,' 2',' 86',' 20',' 34',' 11'];
 print(random.choice(rndnmb));
 print("");
 core_dai();

def word_dai():
 print("");
 rndwrd = [' wat',' lol',' hey',' carrot',' car'];
 print(random.choice(rndwrd));
 print("");
 core_dai();

def core_dai():
 usrinput = input(" Say Something: ");
 if(usrinput == "help"):
  help_dai();
 elif(usrinput == "info"):
  info_dai();
 elif(usrinput == "random"):
  random_dai();
 elif(usrinput == "word"):
  word_dai();
 else:
  print(" Wrong command!");
  core_dai();

core_dai();

