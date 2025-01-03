from Libraries.libraries import datetime, itertools

def print_action_logs(action):
    current_date = datetime.now()
    print_logs = f"{current_date} -- {action}"
    print(print_logs)
    return print_logs

def get_image_action_date():
    img_log_date = datetime.now().strftime("%Y%m%d - %H%M%S")
    return img_log_date

img_count = itertools.count(start=1)

def get_image_action_count():
    global img_count
    return img_count
