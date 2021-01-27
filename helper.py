# Helper functions for Blackfoot project
# CMPT 120 
# Date: Dec 6, 2020

import wave
from replit import audio
import random
import cmpt120image

def concat(infiles,outfile):
  """
  Input: 
  - infiles: a list containing the filenames of .wav files to concatenate,
    e.g. ["hello.wav","there.wav"]
  - outfile: name of the file to write the concatenated .wav file to,
    e.g. "hellothere.wav"
  Output: None
  """
  data= []

  for infile in infiles:
      w = wave.open(infile, 'rb')
      data.append( [w.getparams(), w.readframes(w.getnframes())] )
      w.close()    

  output = wave.open(outfile, 'wb')
  output.setparams(data[0][0])

  for i in range(len(data)):
      output.writeframes(data[i][1])

  output.close()

# Give csv files a variable
scene1 = open("Scenes/Scene1.csv")
scene2 = open("Scenes/Scene2.csv")
scene3 = open("Scenes/Scene3.csv")
scene4 = open("Scenes/Scene4.csv")
scene5 = open("Scenes/Scene5.csv")

# Score Counters (#1 is for the regular test, S is for the specialized test)
def global_varibles():
  global test_sc1
  global Stest_sc1 
  global test_sc2
  global Stest_sc2 
  global test_sc3
  global Stest_sc3 
  global test_sc4
  global Stest_sc4 
  global test_sc5
  global Stest_sc5 
  global score_lst
  global Spscore_lst
  test_sc1 = 0
  Stest_sc1 = 0
  test_sc2 = 0
  Stest_sc2 = 0
  test_sc3 = 0
  Stest_sc3 = 0
  test_sc4 = 0
  Stest_sc4 = 0
  test_sc5 = 0
  Stest_sc5 = 0
  score_lst = [test_sc1,test_sc2,test_sc3,test_sc4,test_sc5]
  Spscore_lst = [Stest_sc1,Stest_sc2,Stest_sc3,Stest_sc4,Stest_sc5]

# sets the golobal varibles so the other functions can use them
global_varibles()

# updates the high score of normal tests
def update(SC,score):

  if SC == 0:
    global test_sc1
    test_sc1 = score

  if SC == 1:
    global test_sc2
    test_sc2 = score

  if SC == 2:
    global test_sc3
    test_sc3 = score

  if SC == 3:
    global test_sc4
    test_sc4 = score

  if SC == 4:
    global test_sc5
    test_sc5 = score

  global score_lst
  score_lst = [test_sc1,test_sc2,test_sc3,test_sc4,test_sc5]

# updates the high score of the specialized test
def update2(SC,score2):

  if SC == 0:
    global Stest_sc1 
    Stest_sc1 = score2

  if SC == 1:
    global Stest_sc2
    Stest_sc2 = score2

  if SC == 2:
    global Stest_sc3
    Stest_sc3 = score2

  if SC == 3:
    global Stest_sc4
    Stest_sc4 = score2

  if SC == 4:
    global Stest_sc5
    Stest_sc5 = score2

  global Spscore_lst
  Spscore_lst = [Stest_sc1,Stest_sc2,Stest_sc3,Stest_sc4,Stest_sc5]

# creates a dictionary of all the words
def create_dic():

  class AutoTree(dict):

     def __missing__(self, key):
        value = self[key] = type(self)()
        return value

  dic = AutoTree()

  # creates a list for the for loop to go though
  lst = [scene1,scene2,scene3,scene4,scene5]

  for z in lst:
    BF = []
    EN = []

    # skips the first two lines of the text doc
    z.readline()
    z.readline()

    for i in z:  
      i = i.strip().lower()
      lst = i.split(",")
      BF.append(lst[0])
      EN.append(lst[1])

    # resets the position in the text file back to the top
    z.seek(0)

    # scene and lang are used to index the data into their respective catagories 
    scene = z.readline().strip()

    # seperates lang into english words and blackfoot words
    lang = z.readline().strip().split(",")
    dic[scene][lang[0]] = EN
    dic[scene][lang[1]] = BF

  # returnes the dictionary so it can be used
  return(dic)

# assiigns a varible to the dictionary
dic = create_dic()

# the learn function
def learn(SC):
  print("Great, let's learn! Look around here and tell me a word in English.")

  # learn loop
  while True:
    learning = input("What do you want to learn the Blackfoot word for? When you're done, type done \n")

    # Use boolean to see if the user input is valid when compared with the list of translation words
    A = False

    # x is used to help index the dictionary
    x = 0

    # Checks each row in the .csv file for the user input, if the user input is in the .csv file, the translated word is printed and the corresponding audio file is played
    for i in dic[SC]["EN"]:

      if learning.lower() == i.lower():
        print(dic[SC]["BF"][x]) 

        # replace() and strip() are used so they don't interfere with finding the audio file
        Input = learning.replace(" ","_").strip("?!").replace("'","").replace(".","").lower()
        audio.play_file('sounds/' + Input + '.wav')

        # Sets boolean to true to show that user input is valid
        A = True 

      x += 1

    # BREAK for town learn loop
    if learning.lower() == "done": 
        break  

    # if the user enters a inproper input
    if A == False:
      print("Sorry, I don't know that one. Try another word!")  

# the test function
# x is used to check which scene the score is from
# SC is used to determine the scene
def test(x,SC):

  # Declares variables 
  score = 0

  # Main loop repeats 10x
  for a in range(10):

    # Sets a constant random number that can be used to index both the Blackfoot and Enslish lists
    rand = random.randrange(0,5)

    # Asks for the English translation of a Blackfoot word
    answer = input("What is " + dic[SC]["BF"][rand] + "\n")

    # Checks if the answer is correct or not
    if answer == dic[SC]["EN"][rand]:
      print("Goodjob")

      # Adds 1 to the overall score
      score+=1
    else:

      # Corrects the user if they get it wrong
      print("Nope, It's " + dic[SC]["EN"][rand])

  # Shows the final score at the end
  print("You got " + str(score)+"/10")

  # Used to find the user's overall high score for normal tests
  if score > score_lst[x]:
    update(x,score)

# Specialized test that asks the user to choose the right Blackfoot translation of an English word between two Blackfoot terms
# x is used to check which scene the score is from
# SC is used to determine the scene
def specialized_test(x,SC):

      # Sets varables
      score2 = 0    

      # Second random number used to help generate the incorect answer
      rand2 = random.randrange(0,5)

      # Main loop repeats 10x
      for a in range(10):

        # A list used to help switch up the order of correct and incorect answers
        randlst = []

        # Sets a constant random number that can be used to index both the Blackfoot and Enslish lists
        rand = random.randrange(0,5)

        # Checks to make sure the two answers are not the same
        while rand == rand2:
          rand2 = random.randrange(0,5)

        # Creates the two answers, with the correct one being the first
        random2 = [dic[SC]["BF"][rand],dic[SC]["BF"][rand2]]

        # Creates a random order for the two answers to appear in
        # Makes it so randlst will always have two elements
        while len(randlst) < 2: 
          r = random.randint(0,1)

          # Checks if randlst recieves two of the same element
          if r not in randlst:
            randlst.append(r)

        # Asks the question
        answer = input("\nIs '" + dic[SC]["EN"][rand] + "'\n'" + random2[randlst[0]] + "' or '" + random2[randlst[1]] + "'?\n").lower()

        # Checks if the answer is correct or incorrect
        if answer == dic[SC]["BF"][rand].strip().lower():
          print("Goodjob")

          # Adds one to the overall score
          score2 += 1

        else:

          # Corrects the user if they got it wrong
          print("Nope, It's " + str(dic[SC]["BF"][rand]))

      print("You got " + str(score2)+"/10")

      # Updates the high-score
      if score2 >= Spscore_lst[x]:
        update2(x,score2)

# prints the high-score
def high_score(x):
  # x is used to index which score is accessed
  print("Your high-score on the normal test is " + str(score_lst[x]) + "/10")
  print("Your high-score on the specialized test is " + str(Spscore_lst[x]) + "/10")

# z is user input (specifically a food)
# check user input against dictionairy
def sentencemaker():

  # Use boolean to see if the user input is valid
  Bsen = False
  print("You can make sentences and choose what to eat here.")

  # Restraunt sentences loop
  while True:
    sentence = input("what would you like to eat? Listen to the sentences closely after you choose\n")

    # checks if the input is valid
    if sentence in dic["SC2"]["EN"]:  
      concat(["sounds/i_will_eat.wav","sounds/" + sentence + ".wav"], "sounds/i_will_eat_" + sentence + ".wav")
      audio.play_file('sounds/i_will_eat_' + sentence + '.wav')
      
      # Sets boolean to true to show that user input is valid
      Bsen = True

    if sentence.lower() == "done": 
      break  

    if Bsen == False:
      print("Sorry, I don't know what that is, pick something else!")
      
    print("enter 'done' when you want to leave")

# town function
def town():

  # displays the background
  img = cmpt120image.getImage('images/town.jpg')
  cmpt120image.showImage(img,'img')

  # opening message
  print("Oki (Hello)! Welcome to Brocket, Alberta!") 
  print("I can teach you some Blackfoot while you are here!")

  # Main town loop
  while True:

    # Town Introduction
    Introduction = input("Do you want to learn some words around you (learn), have me test you (test/specialized test), check your high-score (score), go somewhere else (move), or leave (exit?) \n")

    # checks the user's input and runs the required function
    if Introduction.lower() == "learn":
      learn("SC1")

    elif Introduction.lower() == "test":
      test(0,"SC1")

    elif Introduction.lower() == "specialized test":
      specialized_test(0,"SC1")

    if Introduction.lower() == "score":
      high_score(0)

    elif Introduction.lower() == "move":
      break

    elif Introduction.lower() == "exit":
      print("Goodbye")
      quit()

# RESTAURANT 
def restaurant():

  # displays the background
  img = cmpt120image.getImage('images/restaurant.jpg')
  cmpt120image.showImage(img,'img')
  print("Welcome to the spaget facori")

  # Main restaurant loop
  while True:

    # Restaurant introduction
    Introduction = input("Do you want to learn some words around you (learn), have me test you (test/specialized test), practice making sentences by deciding what to eat (sentences), check your high-score (score), go somewhere else (move) or leave (exit)? \n")

    # checks the user's input and runs the required function
    if Introduction.lower() == "learn":
      learn("SC2")

    elif Introduction.lower() == "test":
      test(1,"SC2")

    elif Introduction.lower() == "specialized test":
      specialized_test(1,"SC2")

    if Introduction.lower() == "score":
      high_score(1)

    elif Introduction.lower() == "sentences":
       helper.sentencemaker()

    elif Introduction.lower() == "move":
      break

    elif Introduction.lower() == "exit":
      print("Goodbye")
      quit()

# HOME
def home():

  # displays the background
  img = cmpt120image.getImage('images/home.jpg')
  cmpt120image.showImage(img,'img')

  # opening message
  print("This is our humble abode")

  # Main home loop
  while True:

    # Home introduction
    Introduction = input("Do you want to learn some words around you (learn), have me test you (test/specialized test), check your high-score (score), go somewhere else (move) or leave (exit)? \n")
    # checks the user's input and runs the required function
    if Introduction.lower() == "learn":
      learn("SC3")

    elif Introduction.lower() == "test":
      test(2,"SC3")

    elif Introduction.lower() == "specialized test":
      specialized_test(2,"SC3")

    if Introduction.lower() == "score":
      high_score(2)

    elif Introduction.lower() == "move":
      break

    elif Introduction.lower() == "exit":
      print("Goodbye")
      quit()

def family():

  # displays the background
  img = cmpt120image.getImage('images/family.jpg')
  cmpt120image.showImage(img,'img')

  # opening message
  print("This is one happy family")
  while True:
    Introduction = input("Do you want to learn some words around you (learn), have me test you (test/specialized test), check your high-score (score), go somewhere else (move) or leave (exit?) \n")

    # checks the user's input and runs the required function
    if Introduction.lower() == "learn":
      learn("SC4")

    elif Introduction.lower() == "test":
      test(3,"SC4")

    elif Introduction.lower() == "specialized test":
      specialized_test(3,"SC4")

    if Introduction.lower() == "score":
      high_score(3)
    
    elif Introduction.lower() == "move":
      break

    elif Introduction.lower() == "exit":
      print("Goodbye")
      quit()

def greetings():

  # displays the background
  img = cmpt120image.getImage('images/greetings.jpg')
  cmpt120image.showImage(img,'img')

  # opening message
  print("A conversation for the ages!")
  while True:
    Introduction = input("Do you want to learn some words around you (learn), have me test you (test/specialized test), check your high-score (score), go somewhere else (move) or leave (exit?) \n")

    # checks the user's input and runs the required function
    if Introduction.lower() == "learn":
      learn("SC5")
   
    elif Introduction.lower() == "test":
      test(4,"SC5")

    elif Introduction.lower() == "specialized test":
      specialized_test(4,"SC5")

    if Introduction.lower() == "score":
      high_score(4)
    
    elif Introduction.lower() == "move":
      break

    elif Introduction.lower() == "exit":
      print("Goodbye")
      quit()