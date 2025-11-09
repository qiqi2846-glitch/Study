#%% - Import Lib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import json

#%% - Config
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

#%% - Crawl data
url ="https://www.dienmayxanh.com/may-lanh/midea-inverter-1-hp-mafa-09cdn8"
driver = webdriver.Chrome(options=chrome_option)
driver.get(url)

time_out = 20
try:
    WebDriverWait(driver, time_out).until(ec.visibility_of_element_located((By.CLASS_NAME, "cmt-txt")))
except TimeoutException:
    print("Timeout")
    driver.quit()

#%% - Display data
#comments = driver.find_elements(By.CLASS_NAME, "cmt-txt")
#cmt_list = []
#for comment in comments:
    #print(comment.text)
    #cmt_list.append({"comment": comment.text})

#comment_list_element = driver.find_element(By.CLASS_NAME, "comment-list")
#comment_list_element = driver.find_element(By.CSS_SELECTOR, ".comment-list")
#comment_list_element = driver.find_element(By.CSS_SELECTOR, "ul.comment-list")
comment_list_element = driver.find_element(By.CSS_SELECTOR, "ul[class='comment-list']")

li_elements = comment_list_element.find_elements(By.TAG_NAME, "li")
print(li_elements[1].find_element(By.CSS_SELECTOR, "p.cmt-top-name").text)

cmt_list = []
for li in li_elements:
    user = li.find_element(By.CSS_SELECTOR, "p.cmt-top-name").text
    cmt = li.find_element(By.CSS_SELECTOR, "p.cmt-txt").text
    cmt_list.append({"user": user, "comment": cmt})
print(cmt_list)

#%% - Save data
with open("data/cmts.json", "w", encoding="utf-8") as f:
    json.dump(cmt_list, f, indent=3, ensure_ascii=False)

#%% -
btn = driver.find_element(By.XPATH, "/html/body/section/div[2]/div[1]/div[8]/div[2]/div/div/div[6]/div/a")
btn.click()

#%% -
btn_next = driver.find_element(By.XPATH, "/html/body/div[8]/div/div[2]/div/div/div[7]/div/div[2]/div/a[6]")
btn_next.click()