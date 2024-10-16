from selenium import webdriver
import pytest
import allure


@allure.title("Verify the title of the webpage https://katalon-demo-cura.herokuapp.com/")
def test_open_katalon():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    return driver.title
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"
    assert driver.title == "CURA Healthcare Service"
