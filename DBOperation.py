import sqlite3
from LoggerApp import logger

#creates the db , if db already exist then connects to it
def createnewdb(DBname):
    logPath='G:\IneuronProject\waferPractice\DBLog.txt'
    try:
        logger(logPath,'DB connection has started')
        conn=sqlite3.connect('TrainingDB/'+DBname+'.db')

    except ConnectionError as ce:
        logger(logPath,'DB could not get creted due to ' + str(ce))
        raise ce

    return conn

def createDBtable(DBname,column_names):
    logpath='G:\IneuronProject\waferPractice\DBLog.txt'
    try:
        conn=sqlite3.connect(DBname)
        c=conn.cursor()
        c.execute("SELECT count(name)  FROM sqlite_master WHERE type = 'table'AND name = 'Good_Raw_Data'")
        if c.fetchone()[0]==1:
            conn.close()

            logger(logpath,'table have been created in the ' + DBname)

        else:

            for key in column_names.keys():
                type = column_names[key]

                # in try block we check if the table exists, if yes then add columns to the table
                # else in catch block we will create the table
                try:
                    # cur = cur.execute("SELECT name FROM {dbName} WHERE type='table' AND name='Good_Raw_Data'".format(dbName=DatabaseName))
                    conn.execute('ALTER TABLE Good_Raw_Data ADD COLUMN "{column_name}" {dataType}'.format(column_name=key,
                                                                                                          dataType=type))
                except:
                    conn.execute(
                        'CREATE TABLE  Good_Raw_Data ({column_name} {dataType})'.format(column_name=key, dataType=type))

            conn.close()

            logger(logpath,'table crated and db closed')

    except Exception as e:
        logger(logpath,'Error while crating the table')
        conn.close()
        raise e


createDBtable('arcgDB')


