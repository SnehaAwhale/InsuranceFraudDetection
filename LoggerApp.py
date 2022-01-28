from datetime import datetime


def logger(filename,logmessage):
    date=datetime.now()
    time= date.time
    with open(filename,'a+') as f:
        f.write(str(date)+":"+logmessage+'\n')

