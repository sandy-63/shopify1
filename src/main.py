from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def search_and_add_to_cart():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    driver.get("https://adnabu-store-assignment1.myshopify.com")

    # ENTER PASSWORD
    password = wait.until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    password.send_keys("AdNabuQA")

    submit = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    submit.click()

    # CLICK SEARCH ICON
    search_icon = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "summary[aria-label='Search']"))
    )
    search_icon.click()

    # SEARCH PRODUCT
    search_box = wait.until(
        EC.visibility_of_element_located((By.NAME, "q"))
    )
    search_box.send_keys("The Collection Snowboard: Liquid")
    search_box.send_keys(Keys.ENTER)

    # OPEN FIRST PRODUCT
    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a.full-unstyled-link[href*='/products/']"))
    )
    all_products = driver.find_elements(By.CSS_SELECTOR, "a.full-unstyled-link[href*='/products/']")
    for p in all_products:
        if p.text.strip():
            driver.get(p.get_attribute("href"))
            break

    # ADD TO CART
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "form[action*='/cart/add']")))

    sold_out = driver.find_elements(By.CSS_SELECTOR, "button[name='add'][disabled]")
    if sold_out:
        print("Product is sold out.")
    else:
        wait.until(EC.element_to_be_clickable((By.NAME, "add"))).click()
        print("Product added to cart successfully")

    driver.quit()


search_and_add_to_cart()