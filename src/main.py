# coding:utf-8
from selenium import webdriver
driver = webdriver.Chrome(driver_path)
driver.get(URL)
driver.close()
driver.quit()