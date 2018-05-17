import sqlite3
import re
import os

#in this code, what i wanna do is find stuff in .txt through regex
#after finding the data, I wanna store it in sql data base
# I would need 3 types of functions
#1. text(), string from the .txt file, input: file, output: string
#2. regex(), find specific data, input: string, output: iterator
#3. sql3(), put stuff in data base, input: iterator
#4. sql3_int(), initiate sql data base with header stuff
def main():
    #create a header for sql data base
    sql3_int()

    #go through all of .txt files
    files = []
    for f in os.listdir():
        if f.endswith(".txt"):
            files.append(f)
    
    #start regex
    for file in files:
        data = text(file)
        rows = regex(data)
        sql3(rows)

def text(file):
    with open(file, 'r') as raw:
        return raw.read()

def regex(data):
    pattern = re.compile(r'([0-9A-F]{8,12});(\S{344});(\S{344});([0-9A-Z]{4});(\d{8});(X-HM://.+)')
    return pattern.finditer(data)

def sql3_int():
    conn = sqlite3.connect('log_provision.db')
    c = conn.cursor()

    #start by creating a table
    c.execute('''CREATE TABLE log_provision
                (mac VARCHAR(15),
                unique_id VARCHAR(500),
                public_key VARCHAR(500),
                home_id VARCHAR(8),
                homekit_code VARCHAR(8),
                homekit_payload VARCHAR(30)
               )''')
    
    conn.commit()
    conn.close()

def sql3(rows):
    #rows is a iterator, we gotta access row.group stuff
    for row in rows:
        conn = sqlite3.connect(':memory:')
        c = conn.cursor()


        #start inserting stuff
        c.execute("INSERT INTO log_provision VALUES (?,?,?,?,?,?)", (row.group(1), row.group(2), row.group(3), row.group(4), row.group(5), row.group(6)))

        conn.commit()
        conn.close()


if __name__ == "__main__":
    main()