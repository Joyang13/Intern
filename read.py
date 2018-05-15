import os
import csv
import linecache
import itertools

os.chdir('/Users/joseph/Desktop/sample')

#renaming the file to make it look better
# for f in os.listdir():
#     file_name, file_type = os.path.splitext(f)
#     log, provision, code = file_name.split('_')
#     new_name = '{}{}' .format(code, file_type)
#     os.rename(f , new_name)

#create csv file with header
with open('intern.csv', 'w', newline='') as csv_file:
    the_writer = csv.writer(csv_file)
    the_writer.writerow(['mac', 'unique_id', 'public_key', 'home_id', 'homekit_code', 'homekit_payload'])


#start looping over the files to save it in csv file
for f in os.listdir():
    #there are two extra files that we dont need
    if f == '.DS_Store' or f == 'intern.csv' or f == '.git' or f == 'read.py' or f == '.vscode' or f == 'regex_to_csv.py':
        continue
    
    #start getting data from the .txt's
    with open(f , 'r') as txt:
        theline = linecache.getline('/Users/joseph/Desktop/sample/' + f, 17)     #line 17 is where the juice are
        data = os.path.splitext(theline)    #for some reason, there's a space in line 17

        #parse the data to mac, unique, blah blah
        mac_, unique, key, home, code, payload = data[0].split(';')

    #putting stuff in csv file
    with open('intern.csv' , 'a', newline='') as csv_f:
        csv_writer = csv.writer(csv_f)
        csv_writer.writerow([mac_, unique, key, home, code, payload])

