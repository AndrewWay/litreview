from sys import argv
from string import punctuation
from collections import *
from difflib import SequenceMatcher



maxFrequency = 5

keyWords = ['']
source_keyWords = ['Waters','OmniSpray','Prosolia','Custom','custom','lab-built']
year_keyWords = ['2018','2017','2016']
DESI_keyWords = ['DESI-MSI','DESI','DESI-MS','desorption electrospray ionization']
mz_keyWords = ['m/z','range','to']


matches=[]
matchness=[]
word_freq = Counter()

for one_filename in argv[1:]:

    print("Text file to import and read:", one_filename)
    print("\nReading file...\n")

    text_file = open(one_filename, 'r')
    all_lines = text_file.readlines()
    text_file.close()

    print("\nFile read finished!")

    for line in all_lines:
      keyWords = mz_keyWords
      matchFrequency=0
      for key in keyWords:
        if key in line:
          if matchFrequency == 0:
            matches.append(line)
            matchness.append(1)
            matchFrequency = 1
          else:
            matchness[-1]+=1
          
 
    matchness,matches = zip(*sorted(zip(matchness,matches)))
    
    matchness,matches = (list(t) for t in zip(*sorted(zip(matchness,matches))))
    matchness = matchness[::-1]
    matches = matches[::-1]
    
    exit = True
    i=0
    while(exit and i<len(matches)):
      print(matchness[i],matches[i])
      user_input = input()  
      if not user_input:
        pass# Do nothing. Just go to next string
      else:
        exit = False
        # ENTER STRING INTO APPROPRIATE SPREADSHEET CELL
        # MOVE TO NEXT COLUMN  
