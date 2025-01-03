from OUTDATED.outdated_login_test_case_copy import open_web_site_copy
from Libraries.mkdir import main_directory as md, action_logs_directory as ald
from Database import db_active_test_cases

is_tc_active = True
md()
ald()

def login_test_case():
    if is_tc_active == db_active_test_cases.tco:
        open_web_site_copy()
    else:
        print("No se encuentra activo el C.P.")

login_test_case()