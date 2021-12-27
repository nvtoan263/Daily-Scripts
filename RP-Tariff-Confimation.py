import os
import os
import json
import logging
import sqlite3
from dateutil import parser
import datetime
import configparser

def create_connection(db):
    # Create connection to DB
    # Parameters:
    #    db (path): Path to the db file
    # Returns:
    #    conn (sqlite3.Connection): DB connection
    try:
        db_path = os.path.normpath(db)
        conn = sqlite3.connect(db_path,timeout=20)
        logging.info("Connected to DB %s" % db_path)
        return conn
    except Exception as error:
        logging.error("Failed to create connection to %s" % db_path)
        raise Exception("Failed to create connection to %s" % db_path)


def close_db_connection(conn):
    # Close DB connection
    # Parameters:
    #    conn (sqlite3.Connection): Connection to DB
    # Returns:
    #    None
    if conn:
        conn.close()
        logging.info("Closed DB connection")
def fetchall_sql_command(conn, sql_command):
    # Fetch all rows of a query result with SQL command
    # Parameters:
    #    conn (sqlite3.Connection): Connection to DB
    #    sql_command (str): SQL command
    # Returns:
    #    list of rows
    try:
        c = conn.cursor()
        c.execute(sql_command)
        return c.fetchall()
    except Exception as msg:
        raise

sql_file_distance = open("課金額取得SQL_A面用_distance.sql", 'r')
sql_file_entry_exit = open("課金額取得SQL_A面用_entryexit.sql", 'r')
sql_file_point = open("課金額取得SQL_A面用_point.sql", 'r')

sql_string_distance = sql_file_distance.read()
sql_file_distance.close()
sql_string_entry_exit = sql_file_entry_exit.read()
sql_file_entry_exit.close()
sql_string_point = sql_file_point.read()
sql_file_point.close()

sql_types = [sql_string_distance, sql_string_entry_exit, sql_string_point]

f = open("confirmation_output.csv", "w")

file_location = r'RoadPricing.db'


db_conn = create_connection(file_location)
#TODO get from charge_object_B
sql_cmd = "drop table if exists SELECT_DATA"
result = fetchall_sql_command(db_conn, sql_cmd)

sql_cmd = "create table SELECT_DATA (ChargeObjectID, YYYYMMDD)"
result = fetchall_sql_command(db_conn, sql_cmd)

sql_cmd = "INSERT INTO SELECT_DATA (ChargeObjectID, YYYYMMDD) values ('ToAddChargeObjectID', 'yyyy-mm-dd')"
result = fetchall_sql_command(db_conn, sql_cmd)
db_conn.commit()
sql_cmd = "select * FROM SELECT_DATA "
result = fetchall_sql_command(db_conn, sql_cmd)


sql_cmd = "select Distinct charge_object_id FROM charge_object_A "
chargeObjectID = fetchall_sql_command(db_conn, sql_cmd)
cnt = 0
for sql in sql_types:
    if (cnt == 0 ): 
        f.write('******** DISTANCE BASE ********\n')
    elif (cnt == 1): 
        f.write('******** ENTRY_EXIT BASE ********\n')
    else:
        f.write('******** PONT BASE ********\n')
    cnt += 1
    for obj in chargeObjectID:
        #print(obj[0])
        #break
        start_date_str = '2021-12-12'
        start_date = parser.parse(start_date_str)
        for d in range(2):#Range is number of days to check
            update_1 = "update SELECT_DATA set ChargeObjectID='" + obj[0] + "' WHERE ROWID='1'"
            update_2 = "update SELECT_DATA set YYYYMMDD='" + start_date.strftime("%Y-%m-%d") + "' WHERE ROWID='1'"
            result = fetchall_sql_command(db_conn, update_1)
            db_conn.commit()
            result = fetchall_sql_command(db_conn, update_2)
            db_conn.commit()
            #fetch result
            #print(obj[0] + ',' + start_date.strftime("%Y-%m-%d") + '\n')
            result = fetchall_sql_command(db_conn, sql)
            if (len(result) > 0):
                f.write(str(obj) + ',' + start_date.strftime("%Y-%m-%d") + '\n')
                for item in result:
                    f.write(str(item) + '\n')
            start_date += datetime.timedelta(days=1)

close_db_connection(db_conn)

f.close()