from Libraries.libraries import By
from Database.db_web_objects import db_home_web_objects as hwo

# Agrupadores para el objeto btn_initials
btn_initials_object_name = hwo.btn_initials_object_name
btn_initials_id = (By.ID, hwo.btn_initials_grouper_id)
btn_initials_class = (By.CLASS_NAME, hwo.btn_initials_grouper_class)
btn_initials_xpath = (By.XPATH, hwo.btn_initials_grouper_xpath)

# Agrupadores para el objeto card_initials
card_initials_object_name = hwo.card_initials_object_name
card_initials_class = (By.CLASS_NAME, hwo.card_initials_grouper_class)
card_initials_xpath = (By.XPATH, hwo.card_initials_grouper_xpath)

# Agrupadores para el objeto btn_logout
btn_logout_object_name = hwo.btn_logout_object_name
btn_logout_class = (By.CLASS_NAME, hwo.btn_logout_grouper_class)
btn_logout_xpath = (By.XPATH, hwo.btn_logout_grouper_xpath)