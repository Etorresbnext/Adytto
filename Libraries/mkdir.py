from Libraries.libraries import datetime, os, logging
from Database.db_inputs import db_start_inputs as dsi, db_login_inputs as dli
from Database.db_web_browsers import db_web_browser_info as wbi
from Database.db_web_objects import db_login_web_objects as lwo
from Libraries.global_variables import info, error


def main_directory():
    mkdir_test_set = dsi.select_test_set
    mkdir_tester = dsi.select_user
    main_directory = "C:/BnextWebDelivery_Automation_Tests_Logs"
    suite_date = datetime.now().strftime("%Y%m%d - %H%M%S")
    global logs_directory
    logs_directory = os.path.join(main_directory, f"{suite_date} - {mkdir_test_set} - {mkdir_tester}")
    log_file_name = f"{suite_date}_{mkdir_test_set}_{mkdir_tester}_information.log"
    global log_path
    log_path = os.path.join(logs_directory, log_file_name)
    os.makedirs(main_directory, exist_ok=True)
    os.makedirs(logs_directory, exist_ok=True)

def action_logs_directory():
    logging.basicConfig(filename=log_path, level=logging.INFO, format='%(levelname)s: %(message)s')

def action_logs_before_directory():
    info(dsi.connection_success)
    info(dsi.script_progress)
    info(dsi.script_success)
    info(dsi.script_select_user)
    info(dsi.script_select_test_set)
    info(wbi.script_progress)
    info(wbi.script_success)
    info(wbi.script_web_browser_name)
    info(wbi.script_web_browser_code)
    info(wbi.script_web_browser_web_driver)
    info(dli.script_progress)
    info(dli.script_success)
    info(dli.total_active_users_log)

    #info(lwo.login_web_objects_info)




def image_logs_directory():
    logs_img_directory = os.path.join(logs_directory, "ScreenShots_Logs")
    os.makedirs(logs_img_directory, exist_ok=True)
    return logs_img_directory