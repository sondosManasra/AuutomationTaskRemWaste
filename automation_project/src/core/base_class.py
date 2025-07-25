from core.main_functions import MainFunctions
from selenium.webdriver.support.ui import WebDriverWait
from page_objects.home_page import HomePage
import time


class BaseClass:

    def __init__(self, driver):
        self.driver = driver
        self.main_functions = MainFunctions()
        self.home_page = HomePage(self.driver)
        self.config_path = '../config_files/project.properties'

    def get_config_value(self, key):
        config_value = self.main_functions.read_config(self.config_path, key)
        return config_value

    def general_do_login(self):
        local_host = self.get_config_value('local_host_frontend')
        self.driver.get(local_host)
        welcome_message = self.home_page.do_valid_login(self.get_config_value("username"),
                                                        self.get_config_value("password"))
        return welcome_message

    def general_do_invalid_login(self):
        local_host = self.get_config_value('local_host_frontend')
        self.driver.get(local_host)
        self.home_page.do_login(self.get_config_value("invalid_username"), self.get_config_value("invalid_password"))
        time.sleep(1)
        # Alert box expected
        alert_present = False
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            alert.accept()
            alert_present = "Invalid login" in alert_text
        except:
            alert_present = False

        return alert_present

    def general_add_todos(self):
        self.home_page.add_todo("Learn Selenium")
        self.home_page.add_todo("Write Pytest tests")
        self.WebDriverWait(self.driver, 5).until(lambda d: "Learn Selenium" in self.home_page.get_all_todo_texts(d))
        todos = self.home_page.get_all_todo_texts()
        return todos

    def general_uodate_todos(self):
        self.home_page.update_todo("Learn Selenium", "Master Selenium")
        WebDriverWait(self.driver, 5).until(lambda d: "Master Selenium" in self.home_page.get_all_todo_texts(d))
        todos_after_update = self.home_page.get_all_todo_texts()
        return todos_after_update

    def general_delete_todos(self):
        self.home_page.delete_todo("Write Pytest tests")
        WebDriverWait(self.driver, 5).until(lambda d: "Write Pytest tests" not in self.home_page.get_all_todo_texts(d))
        todos_after_delete = self.home_page.get_all_todo_texts()
        return todos_after_delete


