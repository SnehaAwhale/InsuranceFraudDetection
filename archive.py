from os import listdir

import pandas as pd
import os

for file in listdir("G:/IneuronProject/waferPractice/TrainingValidatedRowFile/Good_Raw"):
    files=pd.read_csv("G:/IneuronProject/waferPractice/TrainingValidatedRowFile/Good_Raw/"+file)
    for i in files :
        print(len(files[i]))


