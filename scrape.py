from sys import argv
from string import punctuation
from collections import *
from difflib import SequenceMatcher


mz_keyWords = ['m/z','range','to']


topics = []
headers = []

#TODO fix this initialization

#Year
year_keyWords = ['2018','2017','2016']
topics.append(year_keyWords)
headers.append("Year")
#Source
source_keyWords = ['Waters','OmniSpray','Prosolia','Custom','custom','lab-built']
topics.append(source_keyWords)
headers.append("Source")
#MS
MS_keyWords = ["Xevo","xevo","LTQ","Thermo","Thermofisher","Orbitrap"]
topics.append(MS_keyWords)
headers.append("MS")
#Modality
modality_keyWords = ["linear","ion","trap"]
topics.append(modality_keyWords)
headers.append("Modality")
#Inlet-to-capillary distance
inletToCap_keyWords = ["inlet","capillary","mm","to","inlet-to-capillary"]
topics.append(inletToCap_keyWords)
headers.append("inlet-to-cap (mm)")
#Tip-to-surface distance
tipToSurface_keyWords = ["tip","surface","to","-","tip-to-surface"]
topics.append(tipToSurface_keyWords)
headers.append("tip-to-surface (mm)")
#Solvent
solvent_keyWords = ["solvent","methanol","water","1:1","acetonitrile","leucine","ACN","DMF","dimethylformamide","formic acid"]
topics.append(solvent_keyWords)
headers.append("Solvent")
#Flowrate
flowrate_keyWords = ["flowrate","min"]
topics.append(flowrate_keyWords)
headers.append("Flow uL/min")
#Pressure
pressure_keyWords = ["pressure","psi","PSI","N2"]
topics.append(pressure_keyWords)
headers.append("N2 Pressure (PSI)")
#Ion mode
ionMode_keyWords = ["ion","mode","positive","negative"]
topics.append(ionMode_keyWords)
headers.append("Ion Mode")



#For each file in the arguments
for one_filename in argv[1:]:
  output_string=""
  #Open the file and read its contents
  print("Text file to import and read:", one_filename)
  print("\nReading file...\n")

  text_file = open(one_filename, 'r')
  all_lines = text_file.readlines()
  text_file.close()

  print("\nFile read finished!")
  
  #For each topic's keywords
  for keyWords in topics:
    print("Current keywords: ",keyWords)
    matches=[]
    matchness=[]

    # Search through all lines within the current text file
    for line in all_lines:
      matchFrequency=0 #Keeps track of how many key words appears in a line

      # Store how many key words appear in the line
      for key in keyWords:
        # Check to see if the line contains one of the topic's keywords
        if key in line:
          if matchFrequency == 0:
            matches.append(line) # Add the current line to array containing all lines containing keywords
            matchness.append(1)
            matchFrequency = 1
          else:
            matchness[-1]+=1
          
    # Sort the lines based on how many keywords they contain in ascending order
    matchness,matches = zip(*sorted(zip(matchness,matches)))
    
    matchness,matches = (list(t) for t in zip(*sorted(zip(matchness,matches))))
    matchness = matchness[::-1]
    matches = matches[::-1]
    
    # USER PROCESSING SECTION
    
    exit = True
    i=0
    #Loop through all lines containing keywords for the current topic
    #Loop until the user enters some text
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
      i+=1
      if(i>=len(matches)):
        print("No more matches. Put in best guess?")
        user_input = input()
        if not user_input:
          output_string = output_string + ",-" # Add - into cell indicating it was not found
        else:
          exit = False
          # ENTER STRING INTO APPROPRIATE SPREADSHEET CELL
          output_string = output_string + "," + user_input
          # MOVE TO NEXT COLUMN
  print(headers)
  print(output_string)
    
    
