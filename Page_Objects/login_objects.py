from Libraries.libraries import By
from Database.db_web_objects.db_login_web_objects import login_web_objects as lwo

(objects_names, objects_id_grouper, objects_name_grouper, objects_class_grouper, objects_xpath_grouper) = lwo()

txt_email_object_name = objects_names[0]
txt_email_name = (By.NAME, objects_name_grouper[0])
txt_email_class = (By.CLASS_NAME, objects_class_grouper[0])
txt_email_xpath = (By.XPATH, objects_xpath_grouper[0])

txt_password_object_name = objects_names[1]
txt_password_id = (By.ID, objects_id_grouper[1])
txt_password_name = (By.NAME, objects_name_grouper[1])
txt_password_class = (By.CLASS_NAME, objects_class_grouper[1])
txt_password_xpath = (By.XPATH, objects_xpath_grouper[1])

btn_login_object_name = objects_names[2]
btn_login_class = (By.CLASS_NAME, objects_class_grouper[2])
btn_login_xpath = (By.XPATH, objects_xpath_grouper[2])