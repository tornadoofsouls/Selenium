import selenium.webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = selenium.webdriver.Chrome(executable_path=r"C:\Users\T1091565\chromedriver.exe")

driver.get("https://www.amazon.com/")

driver.implicitly_wait(5)


driver.maximize_window()

sleep(2)

driver.find_element(By.ID, "icp-nav-flyout").click()

sleep(2)

driver.find_element(By.CSS_SELECTOR, "#icp-language-settings > div:nth-child(11) > div > label > i").click()

sleep(2)

driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/form/div[3]/div/p/span/span/span/span").click()

sleep(2)

driver.find_element(By.ID, "icp-currency-dropdown_15").click()

sleep(2)

driver.refresh()

driver.implicitly_wait(5) # seconds

driver.find_element(By.NAME, "field-keywords").send_keys("desktops")

sleep(2)

driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div[2]/div/div[2]/div[6]/div").click()

sleep(2)