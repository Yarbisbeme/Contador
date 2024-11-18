from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver
import time

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("file:///C:/Users/mercedes/Desktop/tareaProgramacion/PIII/Contador/index.html")
    yield driver
    driver.quit()

def test_increment(setup):
    driver = setup
    increment_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "increment"))
    )
    count_display = driver.find_element(By.ID, "count")
    
    increment_button.click()
    time.sleep(1)
    driver.save_screenshot("increment_test.png")  # Captura de pantalla
    assert count_display.text == "1", "El contador no incrementó correctamente"

def test_decrement(setup):
    driver = setup
    
    increment_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "increment"))
    )
    decrement_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "decrement"))
    )
    count_display = driver.find_element(By.ID, "count")
    
    increment_button.click()
    time.sleep(1) 
    
    decrement_button.click()
    time.sleep(1)
    
    driver.save_screenshot("decrement_after_increment_test.png")
    
    assert count_display.text == "0", "El contador no decrementó correctamente después de incrementarlo"
