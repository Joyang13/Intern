import os
import csv
import re

with open ('Log_Provision_0002BDF21A00.txt', 'r') as raw:
    txt = raw.read()

#set up patterns
#for mac, the length of digits ranges from 8 to 12, all numbers or caps
    #sneaky son!!! You just need the space in front haha
    p_mac = re.compile(r' [A-Z0-9]{8,12}')
    results = p_mac.finditer(txt)

    for result in results:
        r_mac = result          #r_mac is our mac

#for unique, suuper duper longd
    #thought process: bound it with mac; and ==; then split it
    # tx = '0002BDF21A00'
    # p_unique = re.compile(tx + r';.*==;')
    # matches = p_unique.finditer(txt)

    # for match in matches:
    #     print(match)

#for home id, 4 digits, caps or num, a bit trickier, it's in between to colons
    # p_id = re.compile(r';[0-9A-Z]{4};')
    # matches = p_id.finditer(txt)

    # for match in matches:
    #     _id = match         #now you gotta split id, which idk how

#for key
    #thought process: bounded with ; and ==;homeid 
    # tx = _id`1`
    # p_key = re.compile(r';.*==;' + tx)
    # matches = p_key.finditer(txt)

    # for match in matches:
    #     print(match)

#for code, easy money lol, 8 digits and only numbers
    p_code = re.compile(r'[0-9]{8}')
    results = p_code.finditer(txt)

    for result in results:
        r_code = result

#for payload, got 'em!
    p_payload = re.compile(r'X-HM://.+')

    results = p_payload.finditer(txt)

    for result in results:
        r_payload =  result
    