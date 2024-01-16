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
sehirlist = []
for i in range(220):

    driver.get(
        f"{i + 1}")

    ad = driver.find_elements(By.XPATH, "//td[@data-title='Firma Adı']")
    telefon = driver.find_elements(By.XPATH, "//td[@data-title='Telefon']")
    #website = driver.find_elements(By.XPATH, "//td[@data-title='Website']")
    #email = driver.find_elements(By.XPATH, "//td[@data-title='Email']")
    sehir = driver.find_elements(By.XPATH, "//td[@data-title='İl']")

    for name, tel, il in zip(ad, telefon, sehir):

        sehirlist.append(il.text)
        companylist.append(name.text)
        numberlist.append(tel.text)

df = pd.DataFrame({"Şehir": sehirlist, "FIRMA ADI": companylist, "TELEFON": numberlist})
df.to_excel("lojistikWSehirler.xlsx")

driver.close()
