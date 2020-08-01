from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)
browser.get(link)

try:
	text = WebDriverWait(browser, 15).until(
			EC.text_to_be_present_in_element((By.ID, "price"), "$100")
		)
	
	button = browser.find_element(By.ID, "book")
	button.click()

	x = browser.find_element(By.CSS_SELECTOR, "#input_value")
	x = int(x.text)

	result = str(math.log(abs(12*math.sin(x))))

	text_area = browser.find_element(By.CSS_SELECTOR, "#answer")
	text_area.send_keys(result)

	button = browser.find_element(By.ID, "solve")
	button.click()
	
	alert = browser.switch_to.alert
	alert_text = alert.text
	my_split = alert_text.split(': ')[-1]
	print("Ответ: ", my_split)

finally:
	time.sleep(5)
	browser.quit()

