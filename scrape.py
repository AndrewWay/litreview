#TODO: Add option to go back to previous lines through COMMAND
#TODO: Make a database that holds keywords to use for search, and also contains the entered info for each header for a particular paper
#TODO: After entering COMMAND:MORE, return to the normal state where entering text causes move to next topic

from sys import argv
from string import punctuation
from collections import *
from difflib import SequenceMatcher
from isText import istext

#Check if file names passed to script

if((len(argv)<2)):
    print("Usage: python scrape.py file1.txt file2.txt etc.txt")


topics = []
headers = []

#TODO fix this initialization so that the key words are read from files

#Year
#year_keyWords = ['2018','2017','2016','2015','2014','2013']
#topics.append(year_keyWords)
#headers.append("Year")
#Source
source_keyWords = ['Waters','OmniSpray','Prosolia','Custom','custom','lab-built',"source","ion"]
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
#Sprayer angle distance
angle_keyWords = ["sprayer","angle","incidence","degree","°"]
topics.append(angle_keyWords)
headers.append("Sprayer angle °")
#Solvent
solvent_keyWords = ["solvent","methanol","water","1:1","acetonitrile","leucine","ACN","DMF","dimethylformamide","formic acid"]
topics.append(solvent_keyWords)
headers.append("Solvent")
#Flowrate
flowrate_keyWords = ["flow","rate","ml","mL","flowrate","min"]
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
#injection
injection_keyWords = ["injection","ms"]
topics.append(injection_keyWords)
headers.append("Injection ms")
#Microscans
microscans_keyWords = ["microscan","microscans"]
topics.append(microscans_keyWords)
headers.append("Microscans")
#Spray voltage
sprayVoltage_keyWords = ["spray","voltage","V","v","kV","volts"]
topics.append(sprayVoltage_keyWords)
headers.append("Spray voltage kV")
#Capillary voltage
capillaryVoltage_keyWords = ["capillary","voltage","V","v","kV","volts","cap"]
topics.append(capillaryVoltage_keyWords)
headers.append("Capillary Voltage V")
#Tube lens
tubeLens_keyWords = ["tube","lens","voltage","V","kV"]
topics.append(tubeLens_keyWords)
headers.append("Tube Lens V")
#Capillary Temperature
capillaryTemperature_keyWords = ["capillary","temperature","C","°C","°"]
topics.append(capillaryTemperature_keyWords)
headers.append("Capillary Temperature °C")
#m/z range
mzRange_keyWords = ["m/z","range","to"]
topics.append(mzRange_keyWords)
headers.append("m/z range")
#Resolution
resolution_keyWords = ["pixel","resolution","um"]
topics.append(resolution_keyWords)
headers.append("Resolution um")
#Resolving Power
resolvingPower_keyWords = ["resolving","power","kV"]
topics.append(resolvingPower_keyWords)
headers.append("Resolving Power kV")
#Length
length_keyWords = ["length","m","mm","cm"]
topics.append(length_keyWords)
headers.append("Length mm")
#Line Seperation
lineSeperation_keyWords = ["line","seperation","mm","cm","step","size"]
topics.append(lineSeperation_keyWords)
headers.append("Line Seperation mm")
#Step 
step_keyWords = ["step","x-axis","axis","size"]
topics.append(step_keyWords)
headers.append("Step um")
#Scan duration
scanDuration_keyWords = ["scan","duration","time","ms"]
topics.append(scanDuration_keyWords)
headers.append("Scan duration ms")
#Velocity
velocity_keyWords = ["scan","surface","velocity","rate","um/sec","um/s","mm/s"]
topics.append(velocity_keyWords)
headers.append("Velocity um/s")
#Substrate
substrate_keyWords = ["substrate","slide","glass"]
topics.append(substrate_keyWords)
headers.append("Substrate")
#Acquisition Software
acquisitionSoftware_keyWords = ["software","acquisition","Xcalibur","data","MassLynx"]
topics.append(acquisitionSoftware_keyWords)
headers.append("Acquisition Software")
#Conversion Software
conversionSoftware_keyWords = ["software","conversion","convert","process","processing","raw","firefly","FireFly"]
topics.append(conversionSoftware_keyWords)
headers.append("Conversion software")
#Visualization Software
visualizationSoftware_keyWords = ["software","visualization","visualize","visual","image","images","processed"]
topics.append(visualizationSoftware_keyWords)
headers.append("Visualization Software")


output_file = "output.txt"

def append(output):
  with open(output_file,"a") as myfile:
    myfile.write(output)
    
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
  
  topicIndex=0
  #For each topic's keywords
  for keyWords in topics:
    print("Current key words",keyWords)
    print("Current Topic: ",headers[topicIndex])
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
    
    if(len(matches)>0):      
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
    if len(matches) == 0:
      print("No lines found with matches for topic: "+headers[topicIndex])
      output_string = output_string+",-"
      
    topicIndex=topicIndex+1
    while(exit and i<len(matches)):
      print(matchness[i],matches[i])
      user_input = input()
      #maybe make this into a function that can call itself
      if not user_input:
        pass# Do nothing. Just go to next string
      elif user_input == "COMMAND:MORE":
        line_index = all_lines.index(matches[i])
        startIndex=line_index-1
        endIndex=line_index+1
      
        # Add more context if the user wants to see more
        while user_input == "COMMAND:MORE":
          #TODO Check if line_index-1 is not out of bounds 
          for moreIndex in range(startIndex,endIndex):       
            print(all_lines[moreIndex])

          startIndex=startIndex-1
          endIndex=endIndex+1
          user_input = input()
      else:
          
        exit = False
        # ENTER STRING INTO APPROPRIATE SPREADSHEET CELL
        output_string = output_string + "," + user_input
        # MOVE TO NEXT COLUMN
      i+=1
      if(i>=len(matches) and exit):
        print("No more matches. Put in best guess?")
        user_input = input()
        if not user_input:
          output_string = output_string + ",-" # Add - into cell indicating it was not found
        else:
          exit = False
          # ENTER STRING INTO APPROPRIATE SPREADSHEET CELL
          output_string = output_string + "," + user_input
          # MOVE TO NEXT COLUMN

  append(one_filename[:3]+output_string+"\n")
    
    
