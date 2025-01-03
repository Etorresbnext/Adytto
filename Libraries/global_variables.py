from Libraries.libraries import WebDriverWait, ec, time, logging

element_located = lambda driver, by_method, identifier: WebDriverWait(driver, 30).until(ec.presence_of_element_located((by_method, identifier)))
btn_located = lambda driver, by_method, identifier: WebDriverWait(driver, 1).until(ec.presence_of_element_located((by_method, identifier)))
wait = time.sleep
info = logging.info
error = logging.error

def take_action_screenshot(driver, file_path):
    save_screenshot = driver.save_screenshot(file_path)
    return save_screenshot