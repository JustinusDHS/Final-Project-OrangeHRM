import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

class TestLogin(unittest.TestCase): #TEST SCENARIO

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install()) #deklarasi library chrome

    def test_ORANGEHRM7(self):
        #Steps
        browser = self.browser 
        browser.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login') #url web yang dituju
        time.sleep(1) #delay 5 detik
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys("Admin")
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys("admin123")
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
        time.sleep(2)
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input').send_keys("Aaliyah Haq")    # isi nama employee untuk search  
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]').click() # klik tombol search
        time.sleep(1)
        # validasi
        response_data = browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]').text
        self.assertIn('Aaliyah Haq',response_data)

    # def test_ORANGEHRM8(self):
    #     #Steps
    #     browser = self.browser 
    #     browser.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login') #url web yang dituju
    #     time.sleep(1) #delay 5 detik
    #     browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys("Admin")
    #     time.sleep(1)
    #     browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys("admin123")
    #     time.sleep(1)
    #     browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
    #     time.sleep(2)
    #     Hover = Select(browser.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div/div[1]'))
    #     Hover.select_by_index('0')
    #     time.sleep(1) 
    #     browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]').click() # klik tombol search
    #     time.sleep(1)
    #     # validasi
    #     response_data = browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]').text
    #     self.assertIn('Full',response_data)

    def tearDown(self):
        self.browser.close 

if __name__ == "__main__":
    unittest.main()

