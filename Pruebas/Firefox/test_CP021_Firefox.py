import csv
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestRegistroalsistema():
  def setup_method(self):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self):
    self.driver.quit()
  
  def test_registroalsistema(self): 
    self.driver.get("https://tucan.toolsincloud.net/index.php")
    self.driver.maximize_window()
    success_count = 0
    failure_count = 0
    with open('Archivos csv/registros_cp02_1.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for fila in reader:
            name = fila['name']
            username = fila['username']
            email = fila['email']
            password = fila['password']
            self.driver.find_element(By.ID, "auto").click()
            WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.ID, "exampleInputEmail1")))
            self.driver.find_element(By.ID, "exampleInputEmail1").click()
            self.driver.find_element(By.ID, "exampleInputEmail1").send_keys(name)
            self.driver.find_element(By.NAME, "username").click()
            self.driver.find_element(By.NAME, "username").send_keys(username)
            self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(4) > #exampleInputEmail1").click()
            self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(4) > #exampleInputEmail1").click()
            self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(4) > #exampleInputEmail1").click()
            self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(4) > #exampleInputEmail1").send_keys(email)
            self.driver.find_element(By.ID, "exampleInputPassword1").click()
            self.driver.find_element(By.ID, "exampleInputPassword1").send_keys(password)
            self.driver.find_element(By.NAME, "signup").click()
            self.driver.refresh()
            if self.driver.current_url == "https://tucan.toolsincloud.net/home.php":
              success_count += 1
              print(f"La prueba {success_count} fue exitosa")
              self.driver.find_element(By.CSS_SELECTOR, ".grid-sidebar:nth-child(11) strong").click()
            else:
              failure_count += 1
              print(f"La prueba {failure_count} fue fallida")

test = TestRegistroalsistema()
test.setup_method()
test.test_registroalsistema()
test.teardown_method()