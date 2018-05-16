import os
import csv
import re

#in this code, we wanna first read the .txt file and find things through regex
#then, you wanna store it in csv file
#we can have 3 sub functions
#1. txt_read(), reads a given file that outputs the text in it
#2. regex(), takes in the text, outputs an array that has groups of the things we need
#3. csv_write(), takes in data, write stuff in the csv, no output

def main():
    #create a csv file with header
    with open('intern_regex.csv', 'w', newline = '') as csv_file:   
        the_writer = csv.writer(csv_file)
        the_writer.writerow(['mac', 'unique_id', 'public_key', 'home_id', 'homekit_code', 'homekit_payload'])

    #put all .txt files in files
    files = []              #contains different files of txt
    for f in os.listdir():
        if f.endswith(".txt"):
            files.append(f)
    
    for file in files:
        text = txt_read(file)
        rows = regex(text)          #to access mac we needa: for row in rows; row.group(1)
        csv_write(rows)            #for row in rows: print (row.group(0))


def txt_read(file):        #inputs a file, outputs a string of the file
    with open(file, 'r') as raw:
        return raw.read()

def regex(text):           #inputs a string, outputs an array of things
    #set up patterns for regex
    pattern = re.compile(r'([0-9A-F]{12});(\S{344});(\S{344});([A-Z0-9]{4});(\d{8});(X-HM://.+)')
    return pattern.finditer(text)

def csv_write(rows):       #inputs iterator, which contains data that should be written in csv
    for row in rows:
        with open('intern_regex.csv', 'a', newline = '') as csv_f:
            the_writer = csv.writer(csv_f)
            the_writer.writerow([row.group(1), row.group(2), row.group(3), row.group(4), row.group(5), row.group(6)])

if __name__ == "__main__":
    main()