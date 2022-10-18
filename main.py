import random
import os
import pickle
import savelist

def cs():
  os.system("clear")

runvar = 1
print("Loading Combinations...")
happenings = savelist.load("happenings.txt")
extenders = savelist.load("extenders.txt")
gotitems = savelist.load("gotitems.txt")
verbs = savelist.load("verbs.txt")
charinstances = savelist.load("charinstances.txt")

while runvar == 1:
  cs()
  print("Random Scenario Generator v0.3 by hxd2772 and schhax")
  they = "they"
  because = "because"
  chappening = random.choice(happenings)
  chappening2 = random.choice(happenings)
  chappening3 = random.choice(happenings)
  cextender = random.choice(extenders)
  cextender2 = random.choice(extenders)
  cextender3 = random.choice(extenders)
  cextender4 = random.choice(extenders)
  tinstance1 = random.choice(charinstances)
  print("Combinations: " + str(len(verbs) +  len(charinstances)) + " verbs, " + str(len(happenings)) + " places, " + str(len(extenders)), " conjunctions.")
  print("\n")
  amountofnames = input("Enter amount of names, the currently supported range is 1-5 names: ")
  if amountofnames == "1":
    cs()
    name1 = input("Enter name 1: ")
    sentence = name1 + " " + random.choice(gotitems) + " " + random.choice(verbs) + " " +   chappening
    cs()
    print("Generated Sentence: ")
    print(sentence)
    input("Press ENTER to restart")
  elif amountofnames == "2":
    cs()
    name1 = input("Enter name 1: ")
    cs()
    name2 = input("Enter name 2: ")
    cs()
    sentence = name1 + " " + random.choice(gotitems) + " " + random.choice(verbs) + " " + chappening + " " + cextender + " " + name2 + " " + random.choice(gotitems) + " " + random.choice(verbs) + " " + chappening2
    cs()
    print("Generated Sentence: ")
    print(sentence)
    input("Press ENTER to restart")
  elif amountofnames == "3":
    cs()
    name1 = input("Enter name 1: ")
    cs()
    name2 = input("Enter name 2: ")
    cs()
    name3 = input("Enter name 3: ")
    cs()
    sentence = name1 + " " + random.choice(gotitems) + " " + random.choice(verbs) + " " +      chappening + " " + cextender + " " + name2 + " " + random.choice(gotitems) + " " + random.choice(verbs) + " " + chappening2 + " " + cextender2 + " " + name3 + " " + random.choice(gotitems) + " " + random.choice(verbs) + " "+ chappening3
    cs()
    print("Generated Sentence:")
    print(sentence)
    input("Press ENTER to restart")
  elif amountofnames == "4":
    cs()
    name1 = input("Enter name 1: ")
    cs()
    name2 = input("Enter name 2: ")
    cs()
    name3 = input("Enter name 3: ")
    cs()
    name4 = input("Enter name 4: ")
    cs()
    sentence = name1 + " " + random.choice(gotitems) + " " + random.choice(verbs) + " " + chappening + " " + cextender + " " + name2 + " " + tinstance1 + " " + name3 + " " + cextender4 + " " + name4 + " " + random.choice(gotitems) + " " + random.choice(verbs)
    cs()
    print("Generated Sentence:")
    print(sentence)
    input("Press ENTER to restart")
  elif amountofnames == "5":
    cs()
    name1 = input("Enter name 1: ")
    cs()
    name2 = input("Enter name 2: ")
    cs()
    name3 = input("Enter name 3: ")
    cs()
    name4 = input("Enter name 4: ")
    cs()
    name5 = input("Enter name 5: ")
    cs()
    sentence = name1 + " " + random.choice(gotitems) + " " + random.choice(verbs) + " " + chappening + " " + cextender + " " + name2 + " " + tinstance1 + " " + name3 + " " + cextender4 + " " + name4 + " " + random.choice(gotitems) + " " + random.choice(verbs) + " " + because + " " + name5 + " " + random.choice(gotitems) + " " + random.choice(verbs)
    print("Generated Sentence:")
    print(sentence)
    input("Press ENTER to restart")