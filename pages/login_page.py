# pages/login_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ЗӨВ локаторууд
    USERNAME_FIELD = (By.NAME, "username")
    PASSWORD_FIELD = (By.NAME, "password")
    
    # input type="submit" ба value="Нэвтрэх"
    LOGIN_BUTTON = (By.XPATH, "//input[@type='submit' and @value='Нэвтрэх']")

    WELCOME_TEXT = (By.XPATH, "//*[contains(text(), 'Оюутны гарын авлага')]")
    ERROR_MESSAGE = (By.XPATH, "//*[contains(text(), 'Нэвтрэх боломжгүй') or contains(text(), 'алдаа')]")

    def open(self):
        self.driver.get("https://student.must.edu.mn")

    def enter_username(self, username):
        self.wait.until(EC.presence_of_element_located(self.USERNAME_FIELD)).send_keys(username)

    def enter_password(self, password):
        self.wait.until(EC.presence_of_element_located(self.PASSWORD_FIELD)).send_keys(password)

    def click_login(self):
        login_button = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
        login_button.click()

    def is_login_successful(self):
        try:
            return self.wait.until(EC.presence_of_element_located(self.WELCOME_TEXT)).is_displayed()
        except:
            return False

    def is_error_displayed(self):
        try:
            return self.driver.find_element(*self.ERROR_MESSAGE).is_displayed()
        except:
            return False