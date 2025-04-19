import pytest
import time
from selenium import webdriver

chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = chrome_path
driver = webdriver.Chrome(options=chrome_options)

url = "http://127.0.0.1:8080"

#Teste da página inicial
driver.get(url)
time.sleep(10)
assert "Dash" in driver.title
assert "pagina inicial" in driver.page_source
print("Teste da pagina inicial feito com sucesso!")

#Teste da pagina do formulario
driver.get(url+"/formulario")
time.sleep(10)
assert "Dashboard - Formulario" in driver.title
assert "Formulario" in driver.page_source
print("Teste da pagina formulado feito com sucesso!")

# Teste da pagina de graficos
driver.get(url+"/gaficos")
time.sleep(10)
assert "Dashboard - Graficos" in driver.title
assert "Graficos" in driver.page_source
print("Teste da pagina de graficos feito com sucesso!")

driver.quit()