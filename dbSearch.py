import os
import requests
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
    ins === a string, can be a fileld of 
            subject + course number (WORKING NOW!)
            course title
            crn number
            building full name
            building abbreviation
    infield === choose filed ""
    outs === output, string of lowercase bldg abbreviation
    """

    conn, cursor = get_mysql_conn()
    cursor.execute('''SELECT bldg FROM `course_info` WHERE subj_num="{}" '''.format(interm))
    results = cursor.fetchall()
    outerm = results["bldg"]
    conn.disconnect()
    return outerm


