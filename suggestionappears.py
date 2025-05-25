from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Firefox()
driver.get("https://mart-uat.hamrostack.com/")

wait = WebDriverWait(driver, 10)

search_field = wait.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, "input[placeholder='Search products here...']")))

search_field.click()
search_field.send_keys("Dr")
time.sleep(2)

suggestions = driver.find_elements(By.XPATH, '//*[@id="searchDropdown"]/ul')
assert len(suggestions) > 0
print("Suggestion functionality passed")