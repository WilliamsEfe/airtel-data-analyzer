AIRTEL DATA ANALYZER

# DESCRIPTION
Airtel Data Analyzer is a project that helps to analyze data in order to meet more customers' needs by talking to data
properly and making logical decisions for more informed business protocols


# STRUCTURE

/question1.py
/question2.sh

question1.py is a python script that receives input with four columns: msisdn, session_id, session_start_time, session_end_time, short_code, dialled_string it estimates number of sessions and transaction type.

question2.sh is a shell script that gets list of msisdns of different notification types (AIRTIME, DATA, TALKTTIME) from server logs.


# PREQUSITES
First replace the input/output paths in your PC
1. #38 of question1.py for input path of the csv file
2. #66 of question1.py for output path of the csv file
3. #12, #15 and #18 of question2.py for path to input log file

# HOW TO RUN

1. In order to run it first download python from: https://www.python.org/downloads/ and choose a suitable version for your operating system

2. Download the needed requirements  using: `pip install -r requirements.txt`

3. - To run #1, enter `python question1.py` in your terminal
   - To run #2, enter `./question2.sh` in your terminal


# Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

Last updated: 2021.03.22

