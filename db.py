#!/usr/bin/env python3

import mysql.connector
import configparser
import os

conf=configparser.ConfigParser()
conf.read(os.path.expanduser('~/monitor.auth'))

db = mysql.connector.connect(
    host=conf['client']['host'],
    user=conf['client']['user'],
    passwd=conf['client']['password'],
    db=conf['client']['database']
    )

def query(sql):
    cursor = db.cursor()
    cursor.execute(sql)
    if sql.lower().startswith('select'):
        return cursor.fetchall()
    else:
        db.commit()
        return True


