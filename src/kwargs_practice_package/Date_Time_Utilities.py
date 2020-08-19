from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://seamlessly.net/')
driver.find_element_by_xpath("//a[text()='Login']").click()
driver.find_element_by_css_selector("#user").send_keys('User1')
driver.find_element_by_css_selector("#password").send_keys('Userpass123', Keys.ENTER)
driver.implicitly_wait(5)
driver.quit()