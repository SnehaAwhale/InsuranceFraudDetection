import os

from LoggerApp import logger
import json
# data sharing agreement
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


def gooddatafolder():
    Path = os.path.join('TrainingValidatedRowFile/'+'GoodRow')
    if not Path:








