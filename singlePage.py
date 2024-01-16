from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl
import pandas as pd

workbook = openpyxl.Workbook()
sheet = workbook.active
driver = webdriver.Chrome()
companylist = []
numberlist = []
maillist = []
websitelist = []

driver.get(
    f"{websiteNameHere}")
for i in range(60):

    names = driver.find_elements(By.XPATH, f"{xPathValueHere}")
    email = driver.find_elements(By.XPATH, f"{PathValueHere}")
    website = driver.find_elements(By.XPATH, f"{PathValueHere}")
    phone = driver.find_elements(By.XPATH, f"{PathValueHere}")

    for name, pho, wbs, eml in zip(names, phone, website, email):
        companylist.append(name.text)
        numberlist.append(pho.text)
        websitelist.append(wbs.text)
        maillist.append(eml.text)

df = pd.DataFrame({"COMPANY NAME": companylist, "WEB ": websitelist, "EMAIL": maillist, "PHONE NUMBER": numberlist})
df.to_excel(f"{documentName}.xlsx")

driver.close()
