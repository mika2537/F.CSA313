# utils/driver_setup.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os
import logging

def get_driver():
    """Apple Silicon (M1/M2) дээр ажиллах ChromeDriver-ийг зөв ачааллах."""
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-web-security")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    try:
        # Унших: webdriver-manager-ийн суулгасан зам
        downloaded_path = ChromeDriverManager().install()

        # Чухал: Хэрэв downloaded_path нь файл бол, түүний эцэг директорыг авна
        if os.path.isfile(downloaded_path):
            # Жишээ: .../THIRD_PARTY_NOTICES.chromedriver → .../chromedriver-mac-arm64/
            driver_dir = os.path.dirname(downloaded_path)
        else:
            driver_dir = downloaded_path  # Хэрэв директор бол шууд ашигла

        # Бодит chromedriver файлын зам
        driver_path = os.path.join(driver_dir, "chromedriver")

        # Шалгах: файл оршин байх эсэх
        if not os.path.isfile(driver_path):
            raise FileNotFoundError(f"ChromeDriver файл олдсонгүй: {driver_path}")

        # Зөв эрхтэй эсэхийг шалгах (нэмэлт аюулгүй байдал)
        if not os.access(driver_path, os.X_OK):
            logging.warning(f" Биелэх эрхгүй байна, chmod +x хийж байна: {driver_path}")
            os.chmod(driver_path, 0o755)

        # WebDriver эхлүүлэх
        service = Service(executable_path=driver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)

        logging.info("✅ Chrome хөтчийг амжилттай нээлээ.")
        return driver

    except Exception as e:
        logging.error(f"❌ Chrome драйверийг эхлүүлэхэд алдаа гарлаа: {e}")
        raise
