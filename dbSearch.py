import os
import requests
import json
from flask import Flask, render_template, request
from mysql import connector

env_var = os.environ["VCAP_SERVICES"]
vcap = json.loads(env_var)
mysql_creds = vcap['cleardb'][0]['credentials']
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

def mysql_search(interm):
    """
    inerm === a string, can be a fileld of 
            subject + course number (WORKING NOW!)
            course title
            crn number
            building full name
            building abbreviation
    infield === choose filed ""
    outerm === output, string of lowercase bldg abbreviation
    """

    conn, cursor = get_mysql_conn()
    cursor.execute('''SELECT bldg FROM `course_info` WHERE subj_num="{}" LIMIT 1'''.format(interm))
    results = cursor.fetchall()
    conn.disconnect()
    try:
        outerm = results[0][0]
        if outerm=='nan':
            print("Sorry, no results found.")
            outerm = ""
    except IndexError:
        print("Sorry, no results found.")
        outerm = ""
    return outerm

# if __name__ == '__main__':
#     print(mysql_search('anfs 491'))


