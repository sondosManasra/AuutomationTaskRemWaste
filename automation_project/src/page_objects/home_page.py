from selenium.webdriver.support.ui import WebDriverWait
from page_objects.locators import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def do_login(self, user_name, password):
        """
        Method to do the basic login and to make sure that it'd done by find the xpath
        elements for the inputs for username and password and then click on the login button

        Args:
            user_name (str): user name for the credentials
            password (str): password for the credentials

        Returns:
            None
        """
        self.driver.find_element(By.XPATH, Locators.user_name_xpath).send_keys(user_name)
        self.driver.find_element(By.XPATH, Locators.password_xpath).send_keys(password)
        self.driver.find_element(By.XPATH, Locators.login_button_xpath).click()

    def do_valid_login(self, user_name, password):
        """
        Method to verify the login by checking the welcome text after being logged in
        Args:
            user_name (str): user name for the credentials
            password (str): password for the credentials

        Returns:
            welcome_message: xpath elements for the welcome text
        """
        self.do_login(user_name, password)
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Locators.welcome_xpath))
        )
        welcome_message = self.driver.find_element(By.XPATH, Locators.welcome_xpath).text
        return welcome_message

    def add_todo(self, text):
        """
        add new "todo" based on the passed argument
        Args:
            text (str): new todo to be added
        Returns:
            None
        """
        input_box = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, Locators.new_todo_xpath))
        )
        input_box.clear()
        input_box.send_keys(text)
        self.driver.find_element(By.XPATH, Locators.add_button_xpath).click()

    def get_all_todo_texts(self):
        """
        get all todos was created
        Args:
            None
        Returns:
            all todos(list): list elements for all todos
        """
        # Remove user tag if included
        return [item.text.split(' (')[0] for item in self.driver.find_elements(By.XPATH, Locators.all_elements_xpath)]

    def delete_todo(self, text):
        """
       delete specific todo
        Args:
            text(str): todo to be added
        Returns:
            None
        """
        todo_items = WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, Locators.all_elements_xpath))
        )
        for item in todo_items:
            if text in item.text:
                item.find_element(By.XPATH, Locators.delete_button_xpath).click()
                break

    def update_todo(self, old_text, new_text):
        """
       update specific todo
        Args:
            old_text(str): todo to be updated
            new_text(str): new todo
        Returns:
            None
        """
        todo_items = WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, Locators.all_elements_xpath))
        )
        for item in todo_items:
            if old_text in item.text:
                item.find_element(By.XPATH, Locators.edit_button_xpath).click()
                input_box = self.driver.find_element(By.XPATH, Locators.new_todo_xpath)
                input_box.clear()
                input_box.send_keys(new_text)
                self.driver.find_element(By.XPATH, Locators.update_button_xpath).click()
                break
