import base64
import json
import logging
import os
import pandas as pd
import csv
import requests
from flask import Flask, render_template, request
from mysql import connector

app = Flask(__name__, template_folder='static')
env_var = os.environ["VCAP_SERVICES"]
vcap = json.loads(env_var)
mysql_creds = vcap['cleardb'][0]['credentials']
lt_creds = vcap['language_translator'][0]['credentials']
SCHEMA = mysql_creds['name']

def get_mysql_conn():
    conn = connector.connect(host=mysql_creds['hostname'],
                             user=mysql_creds['username'],
                             password=mysql_creds['password'],
                             port=mysql_creds['port'])
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute("USE {}".format(SCHEMA))
    return conn, cursor



if __name__ == '__main__':
    df = pd.read_csv('data/full_course_data.csv',header=0,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)

    conn, cursor = get_mysql_conn()

    cursor.execute('''DROP TABLE `course_info`''')
    sql_query = '''CREATE TABLE IF NOT EXISTS `course_info`
                  (cid        INT NOT NULL AUTO_INCREMENT, 
                  subj_num    VARCHAR(99) NOT NULL,
                  subj_full   VARCHAR(299) NOT NULL,
                  title       VARCHAR(299) NOT NULL,
                  crn         INT NOT NULL,
                  start_end   VARCHAR(299) NOT NULL,
                  bldg        VARCHAR(99) NOT NULL,
                  bldg_full   VARCHAR(299) NOT NULL,
                  room        VARCHAR(99) NOT NULL,
                  instructor   VARCHAR(299) NOT NULL,
                  email       VARCHAR(299) NOT NULL,
                  PRIMARY KEY (cid),
                  INDEX subjI (subj_num),
                  INDEX subj_fullI (subj_full),
                  INDEX crnI (crn),
                  INDEX bldgI (bldg),
                  INDEX bldg_fullI (bldg_full),
                  INDEX instructorI (instructor)
                  ) ENGINE=InnoDB DEFAULT CHARSET=utf8;'''
    cursor.execute(sql_query)

    for i in range(len(df)):
        subj_num = ' '.join([df.Subj[i],str(df.Num[i])])
        subj_full = str(df["Subj_full"][i]).lower()
        title = str(df["Title"][i]).lower()
        crn = int(df["Comp Numb"][i])
        start_end = ' '.join([str(df["Start Time"][i]),str(df["End Time"][i])])
        bldg = str(df["Bldg"][i]).lower()
        bldg_full = str(df["Bldg_full"][i]).lower()
        room = str(df["Room"][i]).lower()
        instructor = str(df["Instructor"][i]).lower()
        email = df["Email"][i]

        try:
            sql_query = '''INSERT INTO `course_info` ( subj_num,subj_full,title,crn,start_end,bldg,bldg_full,room,instructor,email ) 
            VALUES ("{}","{}","{}",{},"{}","{}","{}","{}","{}","{}")'''.format(subj_num,subj_full,title,crn,start_end,bldg,bldg_full,room,instructor,email)
            cursor.execute(sql_query)
        except:
            print(i) 
            continue
    conn.disconnect()



