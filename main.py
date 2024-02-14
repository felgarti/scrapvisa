# prompt: write me code to scrap a certain div from a modal from a website and return text with selenium 

from selenium import webdriver
from selenium.webdriver.common.by import By
import regex as re
from time import sleep
# Initialize the web driver
while True:
    driver = webdriver.Chrome()

    # Open the desired webpage
    driver.get("https://www.blsspainmorocco.net/MAR/home/index")



    # Wait for the modal to load
    driver.implicitly_wait(5)

    # Locate the desired div within the modal
    target_div = driver.find_element(By.XPATH, '/html/body/main/section[4]/div[2]/div/div/div[2]/div[1]')

    # Extract the text from the div
    text = target_div.text

    # Close the web driver
    driver.quit()

    pattern= "(?<=Nous vous informons que le ).*(?=les rendez-vous pour le visa Schengen et National pour Casablanca seront disponibles sur notre site internet)"
    result= re.findall( pattern, text)

    print("##Current dates : ",result)

    old_dates=['22 Janvier à 16h, ',
    '28 janvier à 10h, ',
    '04 Février à 10h, ',
    '11 Février à 10h, ']


    for date in result : 
        if date not in old_dates:
            print("##New date : ", date)

    #sleep 1 hour 
    sleep(3600)
