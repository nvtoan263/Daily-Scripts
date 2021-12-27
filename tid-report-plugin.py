from csv import reader
from dateutil import parser
# open file in read mode
state_1 = 'waiting_tunnel_msg'
state_2 = 'waiting_home_screen'
kpe_tunnel_msg = 'Follow Traffic Signs'
other_tid_msg = 'PIE'
home_sreen_msg = '0,1-1,2'
tunnel_linkid_list = ['0', '48207', '164178', '49931', '49932', '49877', '49878', '49755']
exit_tunnel_linkid_list = ['48207', '164178', '49931', '49932', '49877', '49878', '49755']
exit_tunnel_valid_linkid_list = ['49848', '49849']
dict_issue_count = {} 
dict_obu_state = {}
def time_compare(t1, t2, reference):
    a = parser.parse(t2.replace('"',''))  - parser.parse(t1.replace('"',''))
    return a.total_seconds() < reference
exit_tunnel_count = 0
entry_tunnel_count = 0
tunnel_message_not_clear_count = 0
rows = 1

with open(r'C:\Users\nguye\Desktop\TrafficInfo.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    header = next(csv_reader)
    # Iterate over each row in the csv using reader object
    for row in csv_reader:
        # Check if message displayed at linkid 49848 and 49849
        if (row[2] == '49848' or row[2] == '49849') and kpe_tunnel_msg in row[3]:print('9-1 At Exit: ' + row[0] + ',' + row[1] + ',' + row[2])
        # Check if contain tunnel message
        if (row[2] == '48220' or row[2] == '48207' or row[2] == '20881' or row[2] == '0') and kpe_tunnel_msg in row[3]:
            #if dict_obu_state[row[0]] != state_1: print(row[0])
            dict_obu_state[row[0]] = row[1]
            entry_tunnel_count += 1
        #Check if other TID or Home Screen after tunnel at correct linkID
        elif row[0] in dict_obu_state and dict_obu_state[row[0]] != state_1 \
        and (other_tid_msg in row[3] and row[7] in exit_tunnel_valid_linkid_list \
            or (home_sreen_msg in row[3] and row[2] in exit_tunnel_valid_linkid_list )):
            dict_obu_state[row[0]] = state_1 # Reset state after detect OBU show other TID message
            exit_tunnel_count += 1
        elif (home_sreen_msg in row[3] \
            and row[0] in dict_obu_state \
            and dict_obu_state[row[0]] != state_1 \
            and time_compare(dict_obu_state[row[0]], row[1],90)):
            if row[0] in dict_issue_count:
                dict_issue_count[row[0]] += 1
                dict_obu_state[row[0]] = state_1 # Reset state after detect OBU showing home inside tunnel
                print('HomeScreen: ' + row[0] + ',' + row[1] + ',' + row[2])
                #print(row[0])B
                #if row[2] != '0': print(row[0] + ',' + row[1] + ',' + row[2])
        elif row[0] in dict_obu_state and dict_obu_state[row[0]] != state_1 and time_compare(dict_obu_state[row[0]], row[1], 90) == False:
            print('No 9-2-2 At Exit: ' + row[0] + ',' + dict_obu_state[row[0]])
            tunnel_message_not_clear_count += 1
            dict_obu_state[row[0]] = state_1
        elif row[0] not in dict_obu_state:
            dict_obu_state[row[0]] = state_1
            if row[0] not in dict_issue_count:
                dict_issue_count[row[0]] = 0
        rows += 1
count = 0
for item in dict_issue_count:
    count += dict_issue_count[item]
    #if dict_issue_count[item] != 0 :
        #print(item + ',' + str(dict_issue_count[item]))
print('Entry count: ' + str(entry_tunnel_count))
print('HomeScreen In Tunnel: ' + str(count))
print('Tunnel message not cleared: ' + str(tunnel_message_not_clear_count))
print('Correct pattern count: ' + str(exit_tunnel_count))
