from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.keys import Keys
import time

options = Options()
driver = webdriver.Edge(options=options)

driver.get("https://mart-uat.hamrostack.com/")
wait = WebDriverWait(driver, 10)

try:
    user_login = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div/main/div[1]/div[1]/div[1]/div[3]/button")))
    user_login.click()

    google_button = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button.w-full:nth-child(2)")))
    google_button.click()

    wait.until(lambda d: len(d.window_handles) > 1)
    driver.switch_to.window(driver.window_handles[1])

    email_input = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "input[type='email']")))
    email_input.send_keys("test986349@gmail.com")
    email_input.send_keys(Keys.ENTER)

    password_input = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "input[type='password']")))

    time.sleep(1)

    password_input.click()
    password_input.clear()
    password_input.send_keys("986349test")
    password_input.send_keys(Keys.ENTER)

    print("Login passed")

except Exception as e:
    print(f"Login Failed: {e}")

finally:
    pass
