from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import os
import time

pdfConverUrl = "http://pdf2html.tabesugi.net:8080"
pwdPath = str(os.getcwd()) + "/"
fileToConvert = str(sys.argv[1])

browser = webdriver.Chrome()

browser.get(pdfConverUrl)

fileInput = browser.find_element_by_name("f")
fileInput.send_keys(pwdPath + fileToConvert)

convertBtn = browser.find_element_by_xpath("//input[@name='c' and @value='Convert to TEXT']")
convertBtn.click()

time.sleep(2)

result = browser.find_element_by_tag_name("pre")
result = result.text
result = result.split("\n")[2]

print result

browser.close()
