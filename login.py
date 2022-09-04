import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestLogin(unittest.TestCase): #TEST SCENARIO

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install()) #deklarasi library chrome

    def test_a_success_login(self):
        #Steps
        browser = self.browser 
        browser.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login') #url web yang dituju
        time.sleep(1) #delay 5 detik
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys("Admin")
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys("admin123")
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
        time.sleep(1)

    def test_b_unsuccessful_login(self):
        #Steps
        browser = self.browser 
        browser.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login') #url web yang dituju
        time.sleep(1) #delay 5 detik
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys("Adminnn")
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys("admin123")
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
        time.sleep(2)

        #Validation
        response_message = browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]').text

        self.assertIn('Invalid', response_message)

def tearDown(self):
        self.browser.close 

if __name__ == "__main__":
    unittest.main()
