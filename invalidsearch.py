from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Firefox()
driver.get("https://mart-uat.hamrostack.com/")

wait = WebDriverWait(driver, 10)

try:
    search_field = wait.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, "input[placeholder='Search products here...']")))
    search_field.click()
    search_field.send_keys("XYZ doesn't exist")
    search_field.send_keys(Keys.ENTER)
    time.sleep(5)

    products = driver.find_elements(By.CLASS_NAME,'py-4')
    assert len(products) > 0
    print("Invalid product search passed")
except Exception as e:
    print("Invalid product search failed",e)
