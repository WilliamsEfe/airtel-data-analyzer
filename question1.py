import pandas as pd
import csv



AIRTIME_TRANSFER_COUNT = 0
ACCOUNT_TRANSFER_COUNT = 0


def no_of_sessions_estimator(val):
    if (val % 20 > 0) and (val // 20 != 0):
        return (val // 20) + 1
    else:
        return ((val // 20))



def transaction_type_estimator(val):
    global AIRTIME_TRANSFER_COUNT, ACCOUNT_TRANSFER_COUNT
    AIRTIME_TRANSFER_COUNT, ACCOUNT_TRANSFER_COUNT = 0, 0

    try:
        result = val.split("*")
        if (len(result) == 3 and len(result[-1]) == 11) or (len(result) == 2):
            AIRTIME_TRANSFER_COUNT += 1
            return "AIRTIME_TRANSFER"
        elif (len(result[-1]) == 10) and (len(result) == 3):
            ACCOUNT_TRANSFER_COUNT += 1
            return "ACCOUNT_TRANSFER"
        else:
            return "INVALID TRANSACTION"
    except:
        return "INVALID_TRANSACTION"


def main():
    #to open the csv file and set rows... note to self: make it more interactive"
    df = pd.read_csv (r'<input file in csv format>', names=["msisdn", "session_id", "session_start_time", "session_end_time", "short_code", "dialled_string"])

    #to convert string in [YEAR][MONTH][DAY][HOUR][MINUTE][SECOND] to datetime object
    df['session_start_time'] = pd.to_datetime(df['session_start_time'], format='%Y%m%d%H%M%S'
    )

    #to convert string in [YEAR][MONTH][DAY][HOUR][MINUTE][SECOND] to datetime object
    df['session_end_time'] = pd.to_datetime(df['session_end_time'], format='%Y%m%d%H%M%S')
    df['session_length'] = (df['session_end_time'] - df['session_start_time']).dt.seconds

    #using helper function to estimate number of sessions column
    df['no_of_session'] =  [no_of_sessions_estimator(i) for i in df['session_length']]

    #using helper function to estimate transaction type column
    df['transaction_type'] =  [transaction_type_estimator(i) for i in df['dialled_string']]

    #to display all the columns
    pd.options.display.max_columns = None

    #to replace null values with 0 to guarantee data consistency... in this case, it's the best thing since null essentially means zero 

    print("TOTAL AIRTIME: ", AIRTIME_TRANSFER_COUNT)
    print("TOTAL TRANSFER: ", ACCOUNT_TRANSFER_COUNT)




    #to output the results in a csv file
    df.to_csv('file_name.csv')
    return True





#running the function
main()