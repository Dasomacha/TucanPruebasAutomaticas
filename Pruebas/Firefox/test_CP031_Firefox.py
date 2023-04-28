import csv
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import InvalidSessionIdException

class TestBusquedadeusuarios():
  def setup_method(self):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self):
    self.driver.quit()
  
  def test_busquedadeusuarios(self):
    self.driver.get("https://tucan.toolsincloud.net/index.php")
    self.driver.maximize_window()
    self.driver.find_element(By.NAME, "email").click()
    self.driver.find_element(By.NAME, "email").send_keys("predeterminado.username@gmail.com")
    self.driver.find_element(By.NAME, "password").click()
    self.driver.find_element(By.NAME, "password").send_keys("clave123")
    self.driver.find_element(By.NAME, "login").click()
    with open('Archivos csv/registros_cp03_1.csv', newline='', encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['name']
            username = row['username']
            self.driver.find_element(By.CSS_SELECTOR, ".form-control").click()
            self.driver.find_element(By.CSS_SELECTOR, ".form-control").send_keys(name)
            WebDriverWait(self.driver, 30).until(expected_conditions.text_to_be_present_in_element((By.LINK_TEXT, name), name))
            self.driver.find_element(By.LINK_TEXT, name).click()
            if self.driver.current_url == f'https://tucan.toolsincloud.net/{username[1:]}':
              assert self.driver.find_element(By.CSS_SELECTOR, ".user-handle").text == username
            else:
              self.driver.close()
              print("Error: La página localhost ha rechazado la conexión")
  
test = TestBusquedadeusuarios()
test.setup_method()
test.test_busquedadeusuarios()
test.teardown_method()
