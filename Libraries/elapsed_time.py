from Libraries.libraries import datetime
import time

def test_case_start_date():
    global start_date
    start_date = datetime.now()
    return start_date

def test_case_end_date():
    global end_date
    end_date = datetime.now()
    return end_date

def test_case_elapsed_time():
    test_case_start_date()
    test_case_end_date()
    elapsed_time = end_date - start_date
    print(elapsed_time)