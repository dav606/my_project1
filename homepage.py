from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def enter_text(self, locator, text, timeout=5):
        element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        element.clear()  # Clears any existing text
        element.send_keys(text)

    def click_element(self, locator, timeout=5):
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator)).click()
