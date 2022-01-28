import json
import re
import shutil
from datetime import datetime
from os import listdir


class logging():
    def __init__(self):
        pass

    def log(self,fileobject,message):
        self.fileobject = fileobject
        self.message = message
        self.now = datetime.now()
        self.date = self.now.date()
        fileobject.write(str(self.date) + "/" + str(self.now) + "\t\t" + message +"\n")


class DSA():
    def __init__(self):
        pass

    with open('schema_training.json') as f:
        dic=json.load(f)
        pattern=dic['SampleFileName']
        LengthOfDateStampInFile=dic['LengthOfDateStampInFile']
        LengthOfTimeStampInFile=dic['LengthOfTimeStampInFile']
        NumberofColumns=dic['NumberofColumns']
        ColName=dic['ColName']
        filepath=open("Training_Main_Log.txt", 'a+')
        log1st=logging()
        log1st.log(filepath, 'just to chck')

directory='Training_Batch_Files'

def regexcreation():
    regex="['wafer']+['\_'']+[\d_]+[\d]+\.csv"
    return regex

filename=[f for f in listdir('Training_Batch_Files')]

for filenames in filename:
    LengthOfDateStampInFile=8
    LengthOfTimeStampInFile=6
    regex = "['wafer']+['\_'']+[\d_]+[\d]+\.csv"
    if (re.match(regex,filenames)):
        splitatdot=re.split('.csv',filenames)
        splitatdot=re.split('_',splitatdot[0])
        if len(splitatdot[1])==LengthOfDateStampInFile:
             if len(splitatdot[2])==LengthOfTimeStampInFile:
                 shutil.move("Training_Batch_Files/" + filenames, "Training_Raw_files_validated/Good_Raw")
                 print(filenames)


    else:
        pass





