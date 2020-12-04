# import math
# from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.common.by import By
#
# browser = webdriver.Chrome()
# link = "http://suninjuly.github.io/explicit_wait2.html"
# browser.get(link)
# browser.implicitly_wait(5)
#
#
# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
#
#
# button = browser.find_element_by_id("book")
# count = WebDriverWait(browser, 15).until(
#     ec.text_to_be_present_in_element((By.ID, "price"), "$100")
# )
# button.click()
#
# x = browser.find_element_by_id("input_value").text
# y = calc(x)
# browser.find_element_by_id("answer").send_keys(y)
# browser.find_element_by_id("solve").click()
#
# alert = browser.switch_to.alert
# alert_text = alert.text
# print(alert_text)
#
# browser.quit()
