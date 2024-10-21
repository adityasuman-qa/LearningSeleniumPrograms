import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By

@pytest.mark.positive
@allure.title("Positive testcase-App.vwo.com Sing up button verification. ")
@allure.description("Verify that Start a free trial link is clicked and navigate to next page")
def test_start_free_trial_link_project3():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    anchor_tag_element = driver.find_element(By.LINK_TEXT, "Start a free trial")
    anchor_tag_element.click()
    assert driver.current_url == "https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"

    time.sleep(3)
    driver.back()
