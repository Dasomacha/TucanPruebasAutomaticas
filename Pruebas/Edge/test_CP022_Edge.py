import csv
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException

class TestRegistroalsistemaerroneo():
  def setup_method(self):
    self.driver = webdriver.Edge()
    self.vars = {}
  
  def teardown_method(self):
    self.driver.quit()
  
  def test_registroalsistemaerroneo(self):
    self.driver.get("https://tucan.toolsincloud.net/index.php")
    self.driver.maximize_window()
    success_count = 0
    failure_count = 0
    with open('Archivos csv/registros_cp02_2.csv', newline='',encoding="utf8") as csvfile:
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
            self.driver.find_element(By.NAME, "username").click()
            self.driver.find_element(By.NAME, "username").send_keys(username)
            self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(4) > #exampleInputEmail1").click()
            self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(4) > #exampleInputEmail1").send_keys(email)
            self.driver.find_element(By.ID, "exampleInputPassword1").click()
            self.driver.find_element(By.ID, "exampleInputPassword1").send_keys(password)
            self.driver.find_element(By.NAME, "signup").click()
            WebDriverWait(self.driver, 30).until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".alert:nth-child(2) > .text-center"), "email is not valid email"))
            if not self.driver.current_url == "https://tucan.toolsincloud.net/home.php":
              success_count += 1
              print(f"La prueba {success_count} fue exitosa")
            else:
              failure_count += 1
              print(f"La prueba {failure_count} fue fallida")
            try:
              assert self.driver.find_element(By.CSS_SELECTOR, ".alert:nth-child(2) > .text-center").text == "email is not valid email"
            except NoSuchElementException:
              print(f"En la prueba no se encontró el mensaje 'email is not valid email'")
            try:
              assert self.driver.find_element(By.CSS_SELECTOR, ".alert:nth-child(3) > .text-center").text == "password must between 5 and 20 length"
            except NoSuchElementException:
              print(f"En la prueba no se encontró el mensaje 'password must between 5 and 20 length'")
            try:
              assert self.driver.find_element(By.CSS_SELECTOR, ".text-center:nth-child(1)").text == "Only Chars and Numbers allowed in username"
            except AssertionError:
              print(f"En la prueba no se encontró el mensaje 'Only Chars and Numbers allowed in username'")
            self.driver.refresh()
  
test = TestRegistroalsistemaerroneo()
test.setup_method()
test.test_registroalsistemaerroneo()
test.teardown_method()