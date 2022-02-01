from os import listdir

import pandas as pd
from LoggerApp import logger

def dataTranform():
    logPath='G:\IneuronProject\waferPractice\generalLog'
    logger(logPath,'DataTranfrom has started')
    filepath=[file for file in listdir('G:\IneuronProject\waferPractice\TrainingValidatedRowFile\Good_Raw')]
    try :
        for file in filepath:
            data= pd.read_csv('G:/IneuronProject/waferPractice/TrainingValidatedRowFile/Good_Raw/'+file)
            columns = ["policy_bind_date", "policy_state", "policy_csl", "insured_sex", "insured_education_level",
                       "insured_occupation", "insured_hobbies", "insured_relationship", "incident_state", "incident_date",
                       "incident_type", "collision_type", "incident_severity", "authorities_contacted", "incident_city",
                       "incident_location", "property_damage", "police_report_available", "auto_make", "auto_model",
                       "fraud_reported"]
            for col in columns:
                data[col]=data[col].apply(lambda x: "'"+str(x)+"'")
            logger(logPath,"Data Transition was successful")
            data.to_csv('G:/IneuronProject/waferPractice/TrainingValidatedRowFile/Good_Raw/'+file,index=None,header=None)
    except Exception as e:
        logger(logPath,'data Tranformation was not sucessfull because of '+str(e))
        raise e


dataTranform()


