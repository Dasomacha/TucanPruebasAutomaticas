# Generated by Selenium IDE
import pytest
import time
import json
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestCP042():
  def setup_method(self):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self):
    self.driver.quit()
  
  def test_cP042(self):
    print("Nombre de la prueba: Publicar un Squawk fallido")
    print("Navegador: Chrome")
    success_count = 0
    failure_count = 0
    
    # Test name: CP04-2
    # Step # | name | target | value
    # 1 | open | /home.php | 
    self.driver.get("https://tucan.toolsincloud.net/home.php")
    # 2 | setWindowSize | 1382x744 | 
    self.driver.set_window_size(1382, 744)
    
    self.driver.find_element(By.NAME, "email").click()
            # 4 | type | name=email | predeterminado.username@gmail.com
    self.driver.find_element(By.NAME, "email").send_keys("predeterminado.username@gmail.com")
            # 5 | click | name=password |
    self.driver.find_element(By.NAME, "password").click()
            # 6 | type | name=password | clave123
    self.driver.find_element(By.NAME, "password").send_keys("clave123")
            # 7 | sendKeys | name=password | ${KEY_ENTER}
    self.driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)

    with open('CP04-2.csv', 'r') as file:
      csv_reader = csv.reader(file)
      next(csv_reader) #skip header
      for row in csv_reader:
    # 3 | click | name=status | 
       self.driver.find_element(By.NAME, "status").click()
    # 4 | runScript | window.scrollTo(0,0) | 
       self.driver.execute_script("window.scrollTo(0,0)")
       message = row[0]
    # 5 | type | name=status | a ingeniería de software abarca un amplio abanico de campos de la informática y la ciencia de la computación. Esta tecnología cumple ahora dos funciones: es el producto, pero también sirve como vehículo que a su vez lo transporta. Sirve de base de control para el producto como motor, como un sistema operativo o un sistema de gestión de redes.
       self.driver.find_element(By.NAME, "status").send_keys(message)
    # 6 | click | css=.fa-image | 
       self.driver.find_element(By.CSS_SELECTOR, ".fa-image").click()
    # 7 | runScript | window.scrollTo(0,0) | 
       self.driver.execute_script("window.scrollTo(0,0)")
    # 8 | type | id=tweet_img | C:\fakepath\videoprueba.mp4
       image_path = row[1]
       self.driver.find_element(By.ID, "tweet_img").send_keys(image_path)
    # 9 | click | id=tweet-input | 
       self.driver.find_element(By.ID, "tweet-input").click()
       try:
                self.driver.find_element(By.ID, "tweet-input").click()
       except:
                print("Se encontró una alerta. No se puede continuar")
                break
       if self.driver.current_url == "https://tucan.toolsincloud.net/home.php":
                    success_count += 1
                    print(f"La prueba {success_count} fue exitosa")
       else:
                    failure_count += 1
                    print(f"La prueba {failure_count} fue fallida")
    # 11 | close |  | 
    self.driver.close()
test = TestCP042()
test.setup_method()
test.test_cP042()
  
