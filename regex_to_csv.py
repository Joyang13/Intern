import os
import csv
import re
import time

#in this code, we wanna first read the .txt file and find things through regex
#then, you wanna store it in csv file
#we can have 3 sub functions
#1. txt_read(), reads a given file that outputs the text in it
#2. regex(), takes in the text, outputs an array that has groups of the things we need
#3. csv_write(), takes in data, write stuff in the csv, no output


def main():
    startime = time.time()

    #create a csv file with header
    with open('intern_regex.csv', 'w', newline = '') as csv_file:   
        the_writer = csv.writer(csv_file)
        the_writer.writerow(['mac', 'unique_id', 'public_key', 'home_id', 'homekit_code', 'homekit_payload'])

    #put all .txt files in files
    files = []              #contains different files of txt
    for f in os.listdir():
        if f.endswith(".txt"):
            files.append(f)
    
    #open file one by one and store them in a list of tuples
    tuples_list = []
    for file in files:
        text = txt_read(file)
        tup = regex(text)          #now we returned a tuple
        tuples_list.append(tup)
    
    #you only wanna open and write once, so the input should be a list of tuples
    csv_write(tuples_list)            #passing in a list of tuples to access

    endtime = time.time()
    print(endtime - startime)


def txt_read(file):        #inputs a file, outputs a string of the file
    with open(file, 'r') as raw:
        return raw.read()

def regex(text):           #inputs a string, outputs an array of things
    #set up patterns for regex
    pattern = re.compile(r'([0-9A-F]{12});(\S{344});(\S{344});([A-Z0-9]{4});(\d{8});(X-HM://.+)')
    results = pattern.finditer(text)
    tup = ()
    for result in results:
        for i in range(1,7):
            tup = tup + (result.group(i), )
    return tup

def csv_write(tuples_list):       #inputs iterator, which contains data that should be written in csv
    with open('intern_regex.csv', 'a', newline = '') as csv_f:
        for i in range (0, 13):
            the_writer = csv.writer(csv_f)
            the_writer.writerow([tuples_list[i][0], tuples_list[i][1], tuples_list[i][2], tuples_list[i][3], tuples_list[i][4], tuples_list[i][5]])

if __name__ == "__main__":
    main()