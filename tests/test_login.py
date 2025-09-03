# tests/test_login.py
import pytest
from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from config import USERNAME, PASSWORD

class TestLogin:
    def setup_method(self):
        self.driver = get_driver()
        self.login_page = LoginPage(self.driver)

    def test_valid_login(self):
        # Алхам 2: Хуудсыг нээх
        self.login_page.open()

        # Нэвтрэх үйлдэл
        self.login_page.enter_username(USERNAME)
        self.login_page.enter_password(PASSWORD)
        self.login_page.click_login()

        # Алхам 3: Үр дүн шалгах
        if self.login_page.is_login_successful():
            assert True, " Амжилттай нэвтэрлээ: 'Оюутны гарын авлага' харагдаж байна."
        elif self.login_page.is_error_displayed():
            assert False, "Нэвтрэхэд алдаа гарлаа: Буруу нэр эсвэл нууц үг."
        else:
            assert False, "Төлөв тодорхойгүй: Амжилт эсвэл алдаа илэрсэнгүй."

    def teardown_method(self):
        self.driver.quit()
