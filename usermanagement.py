# import unittest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.ui import Select
# import time

# class TestLogin(unittest.TestCase): #TEST SCENARIO

#     def setUp(self):
#         self.browser = webdriver.Chrome(ChromeDriverManager().install()) #deklarasi library chrome

#     def test_ORANGEHRM10(self):
#         #Steps
#         browser = self.browser 
#         browser.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login') #url web yang dituju
#         time.sleep(1) #delay 5 detik
#         browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys("Admin")
#         time.sleep(1)
#         browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys("admin123")
#         time.sleep(1)
#         browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
#         time.sleep(2)
#         browser.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a').click()
#         time.sleep(1)
#         browser.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/a').click()   # isi nama employee untuk search  
#         time.sleep(1)
#         browser.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input').send_keys("Paula")
#         time.sleep(1)
#         browser.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input').send_keys("Adam")
#         time.sleep(1)
#         browser.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input').send_keys("Rix")
#         time.sleep(1)
#         browser.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]').click() # klik Save
#         time.sleep(2)

#     def test_ORANGEHRM11(self):
#         #Steps
#         browser = self.browser 
#         browser.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login') #url web yang dituju
#         time.sleep(1) #delay 5 detik
#         browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys("Admin")
#         time.sleep(1)
#         browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys("admin123")
#         time.sleep(1)
#         browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
#         time.sleep(2)
#         browser.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/a').click()   # isi nama employee untuk search  
#         time.sleep(1)
#         browser.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input').send_keys("")
#         time.sleep(1)
#         browser.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input').send_keys("Adam")
#         time.sleep(1)
#         browser.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input').send_keys("Rix")
#         time.sleep(1)
#         browser.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]').click() # klik Save
#         time.sleep(2)
#         # validasi
#         response_data = browser.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/span').text
#         self.assertIn('',response_data)

#     def tearDown(self):
#         self.browser.close 

# if __name__ == "__main__":
#     unittest.main()
