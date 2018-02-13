from sys import argv
from string import punctuation
from collections import *
from difflib import SequenceMatcher


mz_keyWords = ['m/z','range','to']


keyWords = []
headers = []

#Year
year_keyWords = ['2018','2017','2016']
keyWords.append(year_keyWords)
headers.append("Year")
#Source
source_keyWords = ['Waters','OmniSpray','Prosolia','Custom','custom','lab-built']
keyWords.append(source_keyWords)
headers.append("Source")
#MS
MS_keyWords = ["Xevo","xevo","LTQ","Thermo","Thermofisher","Orbitrap"]
keyWords.append(MS_keyWords)
headers.append("MS")
#Modality
modality_keyWords = ["linear","ion","trap"]
keyWords.append(modality_keyWords)
headers.append("Modality")
#Inlet-to-capillary distance
inletToCap_keyWords = ["inlet","capillary","mm","to"]
keyWords.append(inletToCap_keyWords)
headers.append("inlet-to-cap (mm)")
#Tip-to-surface distance

keyWords.append(tipToSurface_keyWords)
headers.append("tip-to-surface (mm)")
#Solvent

keyWords.append(solvent_keyWords)
headers.append("Solvent")
#Flowrate

keyWords.append(flowrate_keyWords)
headers.append("Flow uL/min")
#Pressure

keyWords.append(pressure_keyWords)
headers.append("N2 Pressure (PSI)")
#Ion mode

keyWords.append(ionMode_keyWords)
headers.append("Ion Mode")

keys = keyWords['source']
for i in keys:
  print(i)


matches=[]
matchness=[]
word_freq = Counter()
output=""

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
        output_string = output_string + "," + user_input
        # MOVE TO NEXT COLUMN
      i++
      if(i>=len(matches)):
        print("No more matches. Put in best guess?")
        if not user_input:
          pass# Do nothing. Just go to next string
        else:
          exit = False
          # ENTER STRING INTO APPROPRIATE SPREADSHEET CELL
          output_string = output_string + "," + user_input
          # MOVE TO NEXT COLUMN
    
    
