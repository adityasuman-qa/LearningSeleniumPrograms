import allure
import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

@pytest.mark.positive
@allure.title("Create an account on opencart")
@allure.description("Verify that an account is created on opencart")
def test_task1():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")
    first_name_input_tag = driver.find_element(By.XPATH, "//input[@placeholder='First Name']")
    first_name_input_tag.send_keys("Ram Kumar")
    last_name_input_tag = driver.find_element(By.XPATH,"//input[@placeholder='Last Name']")
    last_name_input_tag.send_keys("Sharma")
    email_name_input_tag = driver.find_element(By.XPATH, "//input[@placeholder='E-Mail']")
    email_name_input_tag.send_keys("12tytrest1234@gmail.com")
    telephone_name_input_tag = driver.find_element(By.XPATH, "//input[@placeholder='Telephone']")
    telephone_name_input_tag.send_keys("1234567890")
    password_name_input_tag = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
    password_name_input_tag.send_keys("Password1$")
    password_name_input_tag = driver.find_element(By.XPATH, "//input[@placeholder='Password Confirm']")
    password_name_input_tag.send_keys("Password1$")
    newsletter_name_input_tag = driver.find_element(By.XPATH,"//input[@value='0']")
    newsletter_name_input_tag.click()
    privacy_policy_checkbox = driver.find_element(By.NAME, "agree")
    privacy_policy_checkbox.click()
    continue_button = driver.find_element(By.XPATH, "//input[@type='submit' and @value='Continue']")
    continue_button.click()
    assert driver.current_url == 'https://awesomeqa.com/ui/index.php?route=account/success'
    time.sleep(5)
    driver.quit()

