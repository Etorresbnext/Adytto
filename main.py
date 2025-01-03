from Libraries.mkdir import (
    main_directory as maindir,
    action_logs_directory as actiondir,
    action_logs_before_directory as actionbf
)
from Database import db_active_test_cases
from Test_Cases.login_test_case import login_test_case_execution as loginexe
#from Test_Cases.configuration_pages_test_case import executions as configexe
from Test_Cases.new_configuration import open_configuration_pages_test_case_execution as configexe

is_tc_active = True
maindir()
actiondir()
actionbf()

def login_test_case():
    if is_tc_active == db_active_test_cases.tco:
        loginexe()
    else:
        print("No se encuentra activo el C.P.")

def open_config_pages():
    if is_tc_active == db_active_test_cases.tco:
        configexe()
    else:
        print("No se encuentra activo el C.P.")


login_test_case()
open_config_pages()