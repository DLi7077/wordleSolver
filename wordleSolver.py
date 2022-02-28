import pandas as pd
import re
wordfile= open('all5letter.txt','r')
word= wordfile.read()
wordList= word.split('\n')
letterList = []
for word in wordList:
  letterList.append([char for char in word])

worddf= pd.DataFrame(letterList,columns=['0','1','2','3','4'])

#BUG: TOAST with 00002 fails, bc first T removes all instances of T
# but second instance tells us theres only 1 T in the word.

userIn= input('Enter any key to start..')
print("Welcome to wordle solver. Type \'Q\' to quit\n")

dfcopy= worddf
while(userIn.lower()!='q' and dfcopy.size>1):
  userIn= input("Enter a 5 letter word:\n")

  # prompt for letter input
  while(len(userIn)!=5):
    userIn= input("that wasn't 5 letters\nEnter a 5 letter word:\n")
  
  #prompt for outcome on board
  outcome =input("Enter outcome in boolean\nex: 0 is none, 1 exists, 2 is at position\n")
  outcome= str(outcome)
  
  while (re.fullmatch(r'[0-2]{5}',outcome)is None):
    outcome =input("That was invalid; Enter outcome in boolean:\n")
  
  #update outcomes
  print("previous size:",dfcopy.size)
  
  for idx in range (len(outcome)):
    if outcome[idx]=='0':
      dfcopy=dfcopy[~dfcopy.eq(userIn[idx]).any(1)]
      
    elif outcome[idx]=='1':
      #update dataframe to be rows that contain the letter
      dfcopy=dfcopy[dfcopy.eq(userIn[idx]).any(1)]
      
      #remove words where letter is at curr column
      #update dataframe to be rows where cols doesnt have the character
      dfcopy=dfcopy[dfcopy[str(idx)]!=userIn[idx]]
      
    elif outcome[idx]=='2':
      dfcopy=dfcopy[dfcopy[str(idx)]== userIn[idx]]

  print("updated size:",dfcopy.size)
  print(dfcopy)

print('good job!! the word was\n',dfcopy)