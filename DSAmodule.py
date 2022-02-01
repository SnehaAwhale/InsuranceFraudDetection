import os
import re
import shutil
from os import listdir
import pandas as pd

from LoggerApp import logger
import json
# data sharing agreement#for training



def DSA():
    try:
        with open('G:\IneuronProject\waferPractice\schema_training.json','r') as f :
            schema_training_dict=json.load(f)
            print(f)

            pattern = schema_training_dict['SampleFileName']
            LengthOfDateStampInFile = schema_training_dict['LengthOfDateStampInFile']
            LengthOfTimeStampInFile = schema_training_dict['LengthOfTimeStampInFile']
            column_names = schema_training_dict['ColName']
            NumberofColumns = schema_training_dict['NumberofColumns']

            readfile='G:/IneuronProject/waferPractice/ReadSchemaTraining.txt'
            message= "LengthOfDateStampInFile:: %s" %LengthOfDateStampInFile + "\t" + "LengthOfTimeStampInFile:: %s" % LengthOfTimeStampInFile +"\t " + "NumberofColumns:: %s" % NumberofColumns + "\n"
            logger(readfile,message)

    except Exception as e :
            readfile='G:/IneuronProject/waferPractice/ReadSchemaTraining.txt'
            message = f'exception has occured : {e}'
            print('exception',e)

#create a folder to save the goodfiles
def goodbaddatafoldercreation():

    try:
        Path = os.path.join('TrainingValidatedRowFile/'+'Good_Raw')
        if not os.path.isdir(Path):
            os.makedirs(Path)
        Path = os.path.join('TrainingValidatedRowFile/' + 'Bad_raw')
        if not os.path.isdir(Path):
            os.makedirs(Path)

    except Exception as ex:
        print('error aaya')
        file='generalLog'
        logger(file,"Error while creating Directory %s:" % ex)

# before going  for the training validation the existing file needs to be removed
def delExistingGoodRawfolder():
    try:
        path= os.path.join('TrainingValidatedRowFile/'+'Good_Raw')
        if os.path.isdir(path):
            shutil.rmtree(path)
            file='G:\IneuronProject\waferPractice\generalLog'
            message='existing good raw folder is deleted'
            logger(file,message)
        else :
            file = 'G:\IneuronProject\waferPractice\generalLog'
            message = 'Existing good raw folder is not available'
            logger(file, message)
    except OSError as er:
        file='G:\IneuronProject\waferPractice\generalLog'
        message = 'Could not delete the existing good file becasue of '
        logger(file,message % er)

def delExistingbadRawfolder():
    try:
        path= os.path.join('TrainingValidatedRowFile/'+'Bad_Raw')
        if os.path.isdir(path):
            shutil.rmtree(path)
            file='G:\IneuronProject\waferPractice\generalLog'
            message='existing bad raw folder is deleted'
            logger(file,message)
        else :
            file = 'G:\IneuronProject\waferPractice\generalLog'
            message = 'Existing good raw folder is not available'
            logger(file, message)
    except OSError as er:
        file='G:\IneuronProject\waferPractice\generalLog'
        message = 'Could not delete the existing good file becasue of '
        logger(file,message % er)

def manualregexcreation():
    regex = "['fraudDetection']+['\_'']+[\d_]+[\d]+\.csv"
    return regex


# read file name given by the client and classify to good and bad data # validating file name
def validatetrainingfile():
    delExistingGoodRawfolder()
    #
    delExistingbadRawfolder()
    goodbaddatafoldercreation()
    # manualregexcreation()
    regex = "['fraudDetection']+['\_'']+[\d_]+[\d]+\.csv"
    try :
        path='G:\IneuronProject\waferPractice\Batchfile'
        pathtogoodraw='G:\IneuronProject\waferPractice\TrainingValidatedRowFile\Good_Raw'
        pathtobadraw = 'G:\IneuronProject\waferPractice\TrainingValidatedRowFile\Bad_raw'
        logfilepath='G:\IneuronProject\waferPractice\generalLog'
        files=[f for f in listdir(path)]
        for file in files:
            if (re.match(regex,file)):
                splitfilename=re.split('.csv',file)
                splitfilename=re.split('_',splitfilename[0])

                if len(splitfilename[1])==9:
                    if len(splitfilename[2])==6:
                        shutil.copy('G:/IneuronProject/waferPractice/Batchfile/'+file,pathtogoodraw)
                        logger(logfilepath,'Timestamp (name) is matched ,file has been moved to goodrawdata:  %s' %file)
                    else:
                        shutil.copy('G:/IneuronProject/waferPractice/Batchfile/'+file, pathtobadraw)
                        logger(logfilepath, 'Timestamp (name) is not matched, file has been moved to badrawdata:' % file)
                else:
                    shutil.copy('G:/IneuronProject/waferPractice/Batchfile/'+file, pathtobadraw)
                    logger(logfilepath, 'datetime (name) is not matched, file has been moved to badrawdata:' % file)
            else:
                shutil.copy('G:/IneuronProject/waferPractice/Batchfile/'+file, pathtobadraw)
                logger(logfilepath, 'file name  is not matched, file has been moved to badrawdata:' % file)

    except Exception as ex:
        logpath='G:\IneuronProject\waferPractice\generalLog'
        logger(logpath, 'Some exception has occured while validating the file name ')
        raise ex

def validatecolumnlenght():
    NumberofColumns=39
    logpath='G:\IneuronProject\waferPractice\generalLog'
    try:
        for files in listdir('G:/IneuronProject/waferPractice/TrainingValidatedRowFile/Good_Raw'):
            file=pd.read_csv("G:/IneuronProject/waferPractice/TrainingValidatedRowFile/Good_Raw/"+files)
            columnlenght=file.shape[1]
            if columnlenght==NumberofColumns:
                logger(logpath, 'Column lenght is matching' % file)
                pass
            else:
                shutil.copy("G:/IneuronProject/waferPractice/TrainingValidatedRowFile/Good_Raw/"+files,'G:/IneuronProject/waferPractice/TrainingValidatedRowFile/Bad_raw')
                logger(logpath, 'Column length is not matching , moving file to bad folder' %file)

    except Exception as e:
        logger(logpath,'Could not validate the column length because of exception ' %e)
        raise e

#validation for missing value , if column lenghts are rows are missing or uneven

def validationMissingcolumns():
    logPath='G:\IneuronProject\waferPractice\generalLog'
    logger(logPath,'validation for missing values in file has started')

    try:

        for file in listdir('G:/IneuronProject/waferPractice/TrainingValidatedRowFile/Good_Raw'):
            datafile=pd.read_csv('G:/IneuronProject/waferPractice/TrainingValidatedRowFile/Good_Raw/'+file)
            count=0
            for column in datafile:
                if (len(datafile[column])) - (datafile[column].count())==len(datafile[column]):
                    count+=1
                    shutil.move('G:/IneuronProject/waferPractice/TrainingValidatedRowFile/Good_Raw/'+file,'G:/IneuronProject/waferPractice/TrainingValidatedRowFile/Bad_raw')
                    logger(logPath,'Missing column found, moving data to bad file' +str(file))
                    break
                if count==0:
                    logger(logPath,'Columns are not present in the file'+ str(file))
                    datafile.to_csv('G:/IneuronProject/waferPractice/TrainingValidatedRowFile/Good_Raw/'+file)

    except OSError:
        logger(logPath,"OSError has occured while finding  the missing columns")
        raise OSError

    except Exception as e:
        logger(logPath, "Exception has occured while finding  the missing columns" +str(e))
        raise e

validationMissingcolumns()


validationMissingcolumns()


























