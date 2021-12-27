import os
import csv
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

#print("test '%s' '%s'" % (a,b))
#print("select * FROM gui_log WHERE content like '2-1' and (display_time >= '%s' and display_time <= '%s')" % (a, b))



def recursive_dir (root):
    if (os.path.isdir(root) is False):
        return
    subdirs = os.listdir(root)
    if 'log' in subdirs and 'conf' in subdirs:
        proceed(root)
    for dir in subdirs:
        recursive_dir(os.path.join(root, dir))

def proceed(dir):
    detail_info.append(dir)
    db_conn = create_connection(os.path.join(dir, "log", "BusinessFunctionLog.db"))
    sql_cmd = "select * FROM gui_log WHERE content like '%2-1-1%' and (display_time >= '2021-12-23 08:00:00' and display_time <= '2022-12-31 23:00:00')"
    result_2_1_1 = fetchall_sql_command(db_conn, sql_cmd)
    detail_info.append("gui_2_1_1")
    for record in result_2_1_1 : detail_info.append(record[1])
    
    sql_cmd = "select * FROM gui_log WHERE content like '%2-1,%' and (display_time >= '2021-12-23 08:00:00' and display_time <= '2022-12-31 23:00:00')"
    result_2_1 = fetchall_sql_command(db_conn, sql_cmd)
    detail_info.append("gui_2_1")
    for record in result_2_1 : detail_info.append(record[1])

    sql_cmd = "select * FROM gui_log WHERE content like '%2-2%' and (display_time >= '2021-12-23 08:00:00' and display_time <= '2022-12-31 23:00:00')"
    result_2_2 = fetchall_sql_command(db_conn, sql_cmd)
    detail_info.append("gui_2_2")
    for record in result_2_2 : detail_info.append(record[1])
    
    sql_cmd = "select * FROM gui_log WHERE content like '%2-3%' and (display_time >= '2021-12-23 08:00:00' and display_time <= '2022-12-31 23:00:00')"
    result_2_3 = fetchall_sql_command(db_conn, sql_cmd)
    detail_info.append("gui_2_3")
    for record in result_2_3 : detail_info.append(record[1])
    
    sql_cmd = "select * FROM gui_log WHERE content like '%2-4%' and (display_time >= '2021-12-23 08:00:00' and display_time <= '2022-12-31 23:00:00')"
    result_2_4 = fetchall_sql_command(db_conn, sql_cmd)
    detail_info.append("gui_2_4")
    for record in result_2_4 : detail_info.append(record[1])
    
    sql_cmd = "select * FROM gui_log WHERE content like '%2-5%' and (display_time >= '2021-12-23 08:00:00' and display_time <= '2022-12-31 23:00:00')"
    result_2_5 = fetchall_sql_command(db_conn, sql_cmd)
    detail_info.append("gui_2_5")
    for record in result_2_5 : detail_info.append(record[1])
    
    sql_cmd = "select * FROM gui_log WHERE content like '%2-6%' and (display_time >= '2021-12-23 08:00:00' and display_time <= '2022-12-31 23:00:00')"
    result_2_6 = fetchall_sql_command(db_conn, sql_cmd)
    detail_info.append("gui_2_6")
    for record in result_2_6 : detail_info.append(record[1])
    
    sql_cmd = "select * FROM gui_log WHERE content like '%2-7%' and (display_time >= '2021-12-23 08:00:00' and display_time <= '2022-12-31 23:00:00')"
    result_2_7 = fetchall_sql_command(db_conn, sql_cmd)
    detail_info.append("gui_2_7")
    for record in result_2_7 : detail_info.append(record[1])
    
    sql_cmd = "select * FROM gui_log WHERE content like '%2-8%' and (display_time >= '2021-12-23 08:00:00' and display_time <= '2022-12-31 23:00:00')"
    result_2_8 = fetchall_sql_command(db_conn, sql_cmd)
    detail_info.append("gui_2_8")
    for record in result_2_8 : detail_info.append(record[1])
    
    sql_cmd = "select * FROM gui_log WHERE content like '%2-9%' and (display_time >= '2021-12-23 08:00:00' and display_time <= '2022-12-31 23:00:00')"
    result_2_9 = fetchall_sql_command(db_conn, sql_cmd)
    detail_info.append("gui_2_9")
    for record in result_2_9 : detail_info.append(record[1])

    sql_cmd = "select * FROM gui_log WHERE content like '%2-10%' and (display_time >= '2021-12-23 08:00:00' and display_time <= '2022-12-31 23:00:00')"
    result_2_1_10 = fetchall_sql_command(db_conn, sql_cmd)
    detail_info.append("gui_2_10")
    for record in result_2_1_10 : detail_info.append(record[1])

    #For getting deduction amount
    dedection_amount = 0        
    sql_cmd = "select content FROM gui_log WHERE content like '%2-2%' and (display_time >= '2021-12-23 08:00:00' and display_time <= '2022-12-31 23:00:00')"
    point_base_dedection_list = fetchall_sql_command(db_conn, sql_cmd)
    for record in point_base_dedection_list :
        dedection_amount += float(record[0].split('"')[1].replace('$',''))
        print(float(record[0].split('"')[1].replace('$','')))

    sql_cmd = "select content FROM gui_log WHERE content like '%2-9%' and (display_time >= '2021-12-23 08:00:00' and display_time <= '2022-12-31 23:00:00')"
    distance_base_dedection_list = fetchall_sql_command(db_conn, sql_cmd)
    for record in distance_base_dedection_list :
        dedection_amount += float(record[0].split('"')[1].replace('$',''))
        print(float(record[0].split('"')[1].replace('$','')))  
    dedection_amount = round(dedection_amount,2)
    #print(dedection_amount)


    sql_cmd = "select *, strftime('%Y-%m-%d %H:%M:%S.', create_date/1000, 'unixepoch','08:00') || (printf('%0.3d', create_date%1000)) as SG_TIME from charging_log where (SG_TIME >= '2021-12-23 08:00:00' and SG_TIME <= '2022-12-31 23:00:00') AND charge_object_id like '%537870977%' AND charge_event_text like '%Successful%'"
    success_payment_1 = fetchall_sql_command(db_conn, sql_cmd)
    sql_cmd = "select *, strftime('%Y-%m-%d %H:%M:%S.', create_date/1000, 'unixepoch','08:00') || (printf('%0.3d', create_date%1000)) as SG_TIME from charging_log where (SG_TIME >= '2021-12-23 08:00:00' and SG_TIME <= '2022-12-31 23:00:00') AND charge_object_id like '%808306370%' AND charge_event_text like '%Successful%'"
    success_payment_2 = fetchall_sql_command(db_conn, sql_cmd)
    
    close_db_connection(db_conn)

    #Query from Communication Log
    db_conn = create_connection(os.path.join(dir, "log", "CommunicationLog.db"))
    sql_cmd = "select *, strftime('%Y-%m-%d %H:%M:%S.', create_date/1000, 'unixepoch','08:00') || (printf('%0.3d', create_date%1000)) as SG_TIME from dsrc_comm_data_log where (SG_TIME >= '2021-12-23 08:00:00' and SG_TIME <= '2022-12-31 23:00:00') AND dsrc_info_list like '%70350%'"
    result_dsrc_1 = fetchall_sql_command(db_conn, sql_cmd)
    detail_info.append('dsrc_70350')
    for item in result_dsrc_1:detail_info.append(item[7])
    
    sql_cmd = "select *, strftime('%Y-%m-%d %H:%M:%S.', create_date/1000, 'unixepoch','08:00') || (printf('%0.3d', create_date%1000)) as SG_TIME from dsrc_comm_data_log where (SG_TIME >= '2021-12-23 08:00:00' and SG_TIME <= '2022-12-31 23:00:00') AND dsrc_info_list like '%70360%'"
    result_dsrc_2 = fetchall_sql_command(db_conn, sql_cmd)
    detail_info.append('dsrc_70360')
    for item in result_dsrc_2:detail_info.append(item[7])
    
    sql_cmd = "select *, strftime('%Y-%m-%d %H:%M:%S.', create_date/1000, 'unixepoch','08:00') || (printf('%0.3d', create_date%1000)) as SG_TIME from dsrc_comm_data_log where (SG_TIME >= '2021-12-23 08:00:00' and SG_TIME <= '2022-12-31 23:00:00') AND dsrc_info_list like '%70370%'"
    result_dsrc_3 = fetchall_sql_command(db_conn, sql_cmd)
    detail_info.append('dsrc_70370')
    for item in result_dsrc_3:detail_info.append(item[7])
    
    sql_cmd = "select *, strftime('%Y-%m-%d %H:%M:%S.', create_date/1000, 'unixepoch','08:00') || (printf('%0.3d', create_date%1000)) as SG_TIME from dsrc_comm_data_log where (SG_TIME >= '2021-12-23 08:00:00' and SG_TIME <= '2022-12-31 23:00:00') AND dsrc_info_list like '%70380%'"
    result_dsrc_4 = fetchall_sql_command(db_conn, sql_cmd)
    detail_info.append('dsrc_70380')
    for item in result_dsrc_4:detail_info.append(item[7])

    sql_cmd = "select *, strftime('%Y-%m-%d %H:%M:%S.', create_date/1000, 'unixepoch','08:00') || (printf('%0.3d', create_date%1000)) as SG_TIME from dsrc_comm_data_log where (SG_TIME >= '2021-12-23 08:00:00' and SG_TIME <= '2022-12-31 23:00:00') AND dsrc_info_list like '%70390%'"
    result_dsrc_5 = fetchall_sql_command(db_conn, sql_cmd)
    detail_info.append('dsrc_70390')
    for item in result_dsrc_5:detail_info.append(item[7])
    
    sql_cmd = "select *, strftime('%Y-%m-%d %H:%M:%S.', create_date/1000, 'unixepoch','08:00') || (printf('%0.3d', create_date%1000)) as SG_TIME from dsrc_comm_data_log where (SG_TIME >= '2021-12-23 08:00:00' and SG_TIME <= '2022-12-31 23:00:00') AND dsrc_info_list like '%703a0%'"
    result_dsrc_6 = fetchall_sql_command(db_conn, sql_cmd)
    detail_info.append('dsrc_703a0')
    for item in result_dsrc_6:detail_info.append(item[7])

    sql_cmd = "select *, strftime('%Y-%m-%d %H:%M:%S.', create_date/1000, 'unixepoch','08:00') || (printf('%0.3d', create_date%1000)) as SG_TIME from dsrc_comm_data_log where (SG_TIME >= '2021-12-23 08:00:00' and SG_TIME <= '2022-12-31 23:00:00') AND dsrc_info_list like '%703b0%'"
    result_dsrc_7 = fetchall_sql_command(db_conn, sql_cmd)
    detail_info.append('dsrc_703b0')
    for item in result_dsrc_7:detail_info.append(item[7])

    sql_cmd = "select *, strftime('%Y-%m-%d %H:%M:%S.', create_date/1000, 'unixepoch','08:00') || (printf('%0.3d', create_date%1000)) as SG_TIME from wwan_comm_data_log where (SG_TIME >= '2021-12-23 08:00:00' and SG_TIME <= '2022-12-31 23:00:00') AND dt_cd like '%0001%'"
    dtcd_0001 = fetchall_sql_command(db_conn, sql_cmd)
    detail_info.append('dtcd_0001')
    for item in dtcd_0001:detail_info.append(item[8])

    sql_cmd = "select *, strftime('%Y-%m-%d %H:%M:%S.', create_date/1000, 'unixepoch','08:00') || (printf('%0.3d', create_date%1000)) as SG_TIME from wwan_comm_data_log where (SG_TIME >= '2021-12-23 08:00:00' and SG_TIME <= '2022-12-31 23:00:00') AND dt_cd like '%004c%'"
    dtcd_004c = fetchall_sql_command(db_conn, sql_cmd)
    detail_info.append('dtcd_004c')
    for item in dtcd_0001:detail_info.append(item[8])

    close_db_connection(db_conn)
    
    f.write(dir + ',' +  \
        str(len(result_2_1_1)) + ',' + str(len(result_2_1)) + ',' + str(len(result_2_2)) + ',' + str(len(result_2_3)) + ',' + \
        str(len(result_2_4)) + ',' + str(len(result_2_5)) + ',' + str(len(result_2_6)) + ',' +\
        str(len(result_2_7)) + ',' + str(len(result_2_8)) + ',' + str(len(result_2_9)) + ',' + str(len(result_2_1_10)) + ',' +\
        str(dedection_amount) + ',' + \
        str(len(success_payment_1)) + ',' + str(len(success_payment_2))  + ',' + \
        str(len(dtcd_0001)) + ',' + str(len(dtcd_004c))  + ',' + \
        str(len(result_dsrc_1)) + ',' + str(len(result_dsrc_2)) + ',' + str(len(result_dsrc_3)) + ',' + str(len(result_dsrc_4)) + ',' + str(len(result_dsrc_5)) + ',' + str(len(result_dsrc_6)) + ',' + str(len(result_dsrc_7))  + \
        '\n')
    with open(detail_info_file_name, 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(detail_info)
    detail_info.clear()

rootdir = r'C:\Users\nguye\Desktop\OBU_LOG\20211223'
f = open("confirmation_output.csv", "w")
f.write('id,"gui_2-1-1","gui_2-1","gui_2-2","gui_2-3","gui_2-4","gui_2-5","gui_2-6","gui_2-7","gui_2-8","gui_2-9","gui_2-10","deduction_amount",success_payment_537870977,success_payment_808306370,dtcd_0001,dtcd_004c,fee_id_70350,fee_id_70360,fee_id_70370,fee_id_70380,fee_id_70390,fee_id_703a0,fee_id_703b0' + '\n')

detail_info_file_name = "detail_info.csv"
if os.path.exists(detail_info_file_name):
    os.remove(detail_info_file_name)

detail_info = []

recursive_dir(rootdir)

f.close()