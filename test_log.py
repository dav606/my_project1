import logging
from telnetlib import EC

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait

from pytest1.locators.page_locators import baseURL, search_input_locator, contact_us_locator, contactUsURL, goodURL, \
    add_to_cart_locator, cart_counter_locator
from pytest1.pages.homepage import HomePage




@pytest.fixture
def driver():
    from selenium import webdriver
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.mark.test
def test_find_text(driver, session, function):
    driver.get(baseURL)
    title = "Laptop screens for all brands from $39"
    element = driver.find_element(By.XPATH, f"//*[text()='{title}']")
    assert element.text.strip() == title

def test_home_button(driver):
    homepage = HomePage(driver)
    homepage.open_url(baseURL)

    home_button_locator = (By.XPATH, "//a[@href='/English/']")

    homepage.click_element(home_button_locator)
    time.sleep(3)

    assert driver.current_url == baseURL


def test_search_functionality(driver):
    homepage = HomePage(driver)
    homepage.open_url(baseURL)
    homepage.find_element(search_input_locator)

    homepage.enter_text(search_input_locator, "HP 1000-1100 SERIES")
    search_input = homepage.find_element(search_input_locator)
    search_input.send_keys(Keys.RETURN)


    time.sleep(3)
    assert "HP 1000-1100 SERIES" in driver.page_source

def test_contact_us_link(driver):
    homepage = HomePage(driver)
    homepage.open_url(baseURL)
    # click
    homepage.click_element(contact_us_locator)
    time.sleep(3)

    print(driver.current_url)
    print(f"{baseURL}" + f"{contactUsURL}")
    assert driver.current_url == f"{baseURL}" + f"{contactUsURL}"




