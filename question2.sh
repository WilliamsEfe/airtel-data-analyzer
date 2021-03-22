#! /bin/sh


"""
    1. First, the file is opened and contents are read
    2. The contents are filtered by transaction type, namely: AIRTIME, DATA or TALKTTIME
    3. The contents are filtered to contain msisdn
    4. The contents are ascertained to be responses from PARTNER NOTIFICATION as indicated in the requirements
    5. The position of the msisdns are pin-pointed and surrounding quotes are trailed
"""
#AIRTIME
testvar=sudo cat <replace with path_to_log_file> | grep "AIRTIME" | grep "msisdn" | grep "response from PARTNER NOTIFICATION" | awk -F"\t" {' print $3'} | cut -d, -f5 | grep "msisdn" | awk -F':' '{ print $4 }'|tr -d '}' | tr -d "'"

#DATA
testvar=sudo cat <replace with path_to_log_file> | grep "DATA" | grep "msisdn" | grep "response from PARTNER NOTIFICATION" | awk -F"\t" {' print $3'} | cut -d, -f5 | grep "msisdn" | awk -F':' '{ print $4 }'|tr -d '}' | tr -d "'"

#TALKTTIME
testvar=sudo cat <replace with path_to_log_file> | grep "TALKTTIME" | grep "msisdn" | grep "response from PARTNER NOTIFICATION" | awk -F"\t" {' print $3'} | cut -d, -f5 | grep "msisdn" | awk -F':' '{ print $4 }'|tr -d '}' | tr -d "'"