from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
counter =0

def test_findHeading():
    driver.get('https://blockstream.info/block/000000000000000000076c036ff5119e5a5a74df77abf64203473364509f7732')
    heading_element = WebDriverWait(driver,25).until(EC.presence_of_element_located((By.XPATH,"//h3")))
    heading = heading_element.text
    assert heading == "25 of 2875 Transactions"

def findHash(value):
   driver.get('https://blockstream.info/block/000000000000000000076c036ff5119e5a5a74df77abf64203473364509f7732')
   driver.implicitly_wait(30) 
   transaction_header = driver.find_element(By.XPATH, f"//div[@class='transactions']/div[{value}]/div[1]/div/a").text
   input_tokens = driver.find_elements(By.XPATH,f"//div[@class='transactions']/div[{value}]/div[2]/div[1]/*")
   output_tokens = driver.find_elements(By.XPATH,f"//div[@class='transactions']/div[{value}]/div[2]/div[3]/*")
   if len(input_tokens)==1 and len(output_tokens) == 2:
      print (transaction_header)
      counter = counter + 1

def test_txnHashFinder():
   for i in range(1,26):
      try: 
        findHash(i)
        assert counter == 7
      except: 
       print(f"Error ocurred at {i}")
       continue

