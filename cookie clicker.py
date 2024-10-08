import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie_button = driver.find_element(By.ID, "cookie")


store = ["Cursor", "Factory", "Grandma", "Shipment", "Mine", "Alchemy lab", "Portal", "Time machine"]

items = driver.find_elements(By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]




timeout = time.time() + 5
five_min = time.time() + 60*5

while True:
    cookie_button.click()
    if time.time() > timeout:
        all_prices = driver.find_elements(By.CSS_SELECTOR, value="#store b")
        item_prices = []
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                amount = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(amount)

        bonus_button = {}
        for n in range(len(item_prices)):
            bonus_button[item_prices[n]] = item_ids[n]

        current_money = driver.find_element(By.ID, "money").text
        if "," in current_money:
            current_money = current_money.replace(",", "")
            current_money = int(current_money.replace(",", ""))
        else:
            current_money = int(current_money)

        affordable_upgrade = {}
        for amount, id in bonus_button.items():
            if current_money > amount:
                affordable_upgrade[amount] = id
        
        highest_price_affordable_upgrade = max(affordable_upgrade)
        to_purchase_id = affordable_upgrade[highest_price_affordable_upgrade]

        driver.find_element(by=By.ID, value=to_purchase_id).click()

        timeout = time.time() + 5

    if time.time() > five_min:
        cookie_per_s = driver.find_element(by=By.ID, value="cps").text
        print(cookie_per_s)
        break













