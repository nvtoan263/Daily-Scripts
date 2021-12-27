import os
import os
import json
import logging
import sqlite3
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
#Step 1: Root folder to all obu id
#Step 2: Modify charge object id, currently has 2 object
#Step 3: Modify fee id, currently has 7
a='2021-10-27 20:00:00'
b='2021-10-28 06:00:00'
#print("test '%s' '%s'" % (a,b))
#print("select * FROM gui_log WHERE content like '2-1' and (display_time >= '%s' and display_time <= '%s')" % (a, b))

f = open("confirmation_output.csv", "w")

rootdir = r'C:\Users\nguye\Desktop\OBU_LOG\OS-5-7-Team4-RPL-02'
f.write('id,"gui_2-1","gui_2-2","gui_2-3","gui_2-4","gui_2-5","gui_2-6","gui_2-7","gui_2-8","gui_2-9","gui_2-10",success_payment_537870917,success_payment_537870919,dtcd_0001,dtcd_004c,fee_id_50031,fee_id_50030,fee_id_70040,fee_id_50010,fee_id_70010,fee_id_703a0,fee_id_703b0' + '\n')
for file in os.listdir(rootdir):
    d = os.path.join(rootdir, file)
    print(d)
    if os.path.isdir(d):
        db_conn = create_connection(os.path.join(d, "log", "BusinessFunctionLog.db"))
        sql_cmd = "select * FROM gui_log WHERE content like '%2-1%' and (display_time >= '2021-10-27 20:00:00' and display_time <= '2021-10-28 06:00:00')"
        result_2_1 = fetchall_sql_command(db_conn, sql_cmd)
        print("gui_2_1")
        for record in result_2_1 : print(record[1])
        
        sql_cmd = "select * FROM gui_log WHERE content like '%2-2%' and (display_time >= '2021-10-27 20:00:00' and display_time <= '2021-10-28 06:00:00')"
        result_2_2 = fetchall_sql_command(db_conn, sql_cmd)
        print("gui_2_2")
        for record in result_2_2 : print(record[1])
        
        sql_cmd = "select * FROM gui_log WHERE content like '%2-3%' and (display_time >= '2021-10-27 20:00:00' and display_time <= '2021-10-28 06:00:00')"
        result_2_3 = fetchall_sql_command(db_conn, sql_cmd)
        print("gui_2_3")
        for record in result_2_3 : print(record[1])
        
        sql_cmd = "select * FROM gui_log WHERE content like '%2-4%' and (display_time >= '2021-10-27 20:00:00' and display_time <= '2021-10-28 06:00:00')"
        result_2_4 = fetchall_sql_command(db_conn, sql_cmd)
        print("gui_2_4")
        for record in result_2_4 : print(record[1])
        
        sql_cmd = "select * FROM gui_log WHERE content like '%2-5%' and (display_time >= '2021-10-27 20:00:00' and display_time <= '2021-10-28 06:00:00')"
        result_2_5 = fetchall_sql_command(db_conn, sql_cmd)
        print("gui_2_5")
        for record in result_2_5 : print(record[1])
        
        sql_cmd = "select * FROM gui_log WHERE content like '%2-6%' and (display_time >= '2021-10-27 20:00:00' and display_time <= '2021-10-28 06:00:00')"
        result_2_6 = fetchall_sql_command(db_conn, sql_cmd)
        print("gui_2_6")
        for record in result_2_6 : print(record[1])
        
        sql_cmd = "select * FROM gui_log WHERE content like '%2-7%' and (display_time >= '2021-10-27 20:00:00' and display_time <= '2021-10-28 06:00:00')"
        result_2_7 = fetchall_sql_command(db_conn, sql_cmd)
        print("gui_2_7")
        for record in result_2_7 : print(record[1])
        
        sql_cmd = "select * FROM gui_log WHERE content like '%2-8%' and (display_time >= '2021-10-27 20:00:00' and display_time <= '2021-10-28 06:00:00')"
        result_2_8 = fetchall_sql_command(db_conn, sql_cmd)
        print("gui_2_8")
        for record in result_2_8 : print(record[1])
        
        sql_cmd = "select * FROM gui_log WHERE content like '%2-9%' and (display_time >= '2021-10-27 20:00:00' and display_time <= '2021-10-28 06:00:00')"
        result_2_9 = fetchall_sql_command(db_conn, sql_cmd)
        print("gui_2_9")
        for record in result_2_9 : print(record[1])

        sql_cmd = "select * FROM gui_log WHERE content like '%2-10%' and (display_time >= '2021-10-27 20:00:00' and display_time <= '2021-10-28 06:00:00')"
        result_2_10 = fetchall_sql_command(db_conn, sql_cmd)
        print("gui_2_10")
        for record in result_2_10 : print(record[1])

        sql_cmd = "select *, strftime('%Y-%m-%d %H:%M:%S.', create_date/1000, 'unixepoch','08:00') || (printf('%0.3d', create_date%1000)) as SG_TIME from charging_log where (SG_TIME >= '2021-10-27 20:00:00' and SG_TIME <= '2021-10-28 06:00:00') AND charge_object_id like '%537870917%' AND charge_event_text like '%Successful%'"
        success_payment_1 = fetchall_sql_command(db_conn, sql_cmd)
        sql_cmd = "select *, strftime('%Y-%m-%d %H:%M:%S.', create_date/1000, 'unixepoch','08:00') || (printf('%0.3d', create_date%1000)) as SG_TIME from charging_log where (SG_TIME >= '2021-10-27 20:00:00' and SG_TIME <= '2021-10-28 06:00:00') AND charge_object_id like '%537870919%' AND charge_event_text like '%Successful%'"
        success_payment_2 = fetchall_sql_command(db_conn, sql_cmd)
        
        close_db_connection(db_conn)

        #Query from Communication Log
        db_conn = create_connection(os.path.join(d, "log", "CommunicationLog.db"))
        sql_cmd = "select *, strftime('%Y-%m-%d %H:%M:%S.', create_date/1000, 'unixepoch','08:00') || (printf('%0.3d', create_date%1000)) as SG_TIME from dsrc_comm_data_log where (SG_TIME >= '2021-10-27 20:00:00' and SG_TIME <= '2021-10-28 06:00:00') AND dsrc_info_list like '%50031%'"
        result_dsrc_1 = fetchall_sql_command(db_conn, sql_cmd)
        print('dsrc_50031')
        for item in result_dsrc_1:print(item[7])
        
        sql_cmd = "select *, strftime('%Y-%m-%d %H:%M:%S.', create_date/1000, 'unixepoch','08:00') || (printf('%0.3d', create_date%1000)) as SG_TIME from dsrc_comm_data_log where (SG_TIME >= '2021-10-27 20:00:00' and SG_TIME <= '2021-10-28 06:00:00') AND dsrc_info_list like '%50030%'"
        result_dsrc_2 = fetchall_sql_command(db_conn, sql_cmd)
        print('dsrc_50030')
        for item in result_dsrc_2:print(item[7])
        
        sql_cmd = "select *, strftime('%Y-%m-%d %H:%M:%S.', create_date/1000, 'unixepoch','08:00') || (printf('%0.3d', create_date%1000)) as SG_TIME from dsrc_comm_data_log where (SG_TIME >= '2021-10-27 20:00:00' and SG_TIME <= '2021-10-28 06:00:00') AND dsrc_info_list like '%70040%'"
        result_dsrc_3 = fetchall_sql_command(db_conn, sql_cmd)
        print('dsrc_70040')
        for item in result_dsrc_3:print(item[7])
        
        sql_cmd = "select *, strftime('%Y-%m-%d %H:%M:%S.', create_date/1000, 'unixepoch','08:00') || (printf('%0.3d', create_date%1000)) as SG_TIME from dsrc_comm_data_log where (SG_TIME >= '2021-10-27 20:00:00' and SG_TIME <= '2021-10-28 06:00:00') AND dsrc_info_list like '%50010%'"
        result_dsrc_4 = fetchall_sql_command(db_conn, sql_cmd)
        print('dsrc_50010')
        for item in result_dsrc_4:print(item[7])

        sql_cmd = "select *, strftime('%Y-%m-%d %H:%M:%S.', create_date/1000, 'unixepoch','08:00') || (printf('%0.3d', create_date%1000)) as SG_TIME from dsrc_comm_data_log where (SG_TIME >= '2021-10-27 20:00:00' and SG_TIME <= '2021-10-28 06:00:00') AND dsrc_info_list like '%70010%'"
        result_dsrc_5 = fetchall_sql_command(db_conn, sql_cmd)
        print('dsrc_70010')
        for item in result_dsrc_5:print(item[7])
        
        sql_cmd = "select *, strftime('%Y-%m-%d %H:%M:%S.', create_date/1000, 'unixepoch','08:00') || (printf('%0.3d', create_date%1000)) as SG_TIME from dsrc_comm_data_log where (SG_TIME >= '2021-10-27 20:00:00' and SG_TIME <= '2021-10-28 06:00:00') AND dsrc_info_list like '%703a0%'"
        result_dsrc_6 = fetchall_sql_command(db_conn, sql_cmd)
        print('dsrc_703a0')
        for item in result_dsrc_6:print(item[7])

        sql_cmd = "select *, strftime('%Y-%m-%d %H:%M:%S.', create_date/1000, 'unixepoch','08:00') || (printf('%0.3d', create_date%1000)) as SG_TIME from dsrc_comm_data_log where (SG_TIME >= '2021-10-27 20:00:00' and SG_TIME <= '2021-10-28 06:00:00') AND dsrc_info_list like '%703b0%'"
        result_dsrc_7 = fetchall_sql_command(db_conn, sql_cmd)
        print('dsrc_703b0')
        for item in result_dsrc_7:print(item[7])

        sql_cmd = "select *, strftime('%Y-%m-%d %H:%M:%S.', create_date/1000, 'unixepoch','08:00') || (printf('%0.3d', create_date%1000)) as SG_TIME from wwan_comm_data_log where (SG_TIME >= '2021-10-27 20:00:00' and SG_TIME <= '2021-10-28 06:00:00') AND dt_cd like '%0001%'"
        dtcd_0001 = fetchall_sql_command(db_conn, sql_cmd)
        print('dtcd_0001')
        for item in dtcd_0001:print(item[8])

        sql_cmd = "select *, strftime('%Y-%m-%d %H:%M:%S.', create_date/1000, 'unixepoch','08:00') || (printf('%0.3d', create_date%1000)) as SG_TIME from wwan_comm_data_log where (SG_TIME >= '2021-10-27 20:00:00' and SG_TIME <= '2021-10-28 06:00:00') AND dt_cd like '%004c%'"
        dtcd_004c = fetchall_sql_command(db_conn, sql_cmd)
        print('dtcd_004c')
        for item in dtcd_0001:print(item[8])

        close_db_connection(db_conn)
        
        f.write(d + ',' +  \
            str(len(result_2_1)) + ',' + str(len(result_2_2)) + ',' + str(len(result_2_3)) + ',' + \
            str(len(result_2_4)) + ',' + str(len(result_2_5)) + ',' + str(len(result_2_6)) + ',' +\
            str(len(result_2_7)) + ',' + str(len(result_2_8)) + ',' + str(len(result_2_9)) + ',' + str(len(result_2_10)) + ',' +\
            str(len(success_payment_1)) + ',' + str(len(success_payment_2))  + ',' + \
            str(len(dtcd_0001)) + ',' + str(len(dtcd_004c))  + ',' + \
            str(len(result_dsrc_1)) + ',' + str(len(result_dsrc_2)) + ',' + str(len(result_dsrc_3)) + ',' + str(len(result_dsrc_4)) + ',' + str(len(result_dsrc_5)) + ',' + str(len(result_dsrc_6)) + ',' + str(len(result_dsrc_7))  + \
            '\n')
f.close()