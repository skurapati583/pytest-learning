import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.fixture(scope='class')
def browser():
    driver = webdriver.Safari()
    yield driver
    driver.quit()


def test_run_google(browser):
    browser.get('http://www.yahoo.com')
    assert 'Yahoo' in browser.title
    elem = browser.find_element(By.NAME, 'p')  # Find the search box
    elem.send_keys('seleniumhq' + Keys.RETURN)


def test_run_bing(browser):
    browser.get('https://www.bing.com')
    assert 'Bing' in browser.title
    elem = browser.find_element(By.ID, 'sb_form_q')
    elem.send_keys('seleniumhq' + Keys.RETURN)
