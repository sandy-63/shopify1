from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_search_and_add_to_cart():

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 20)

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

    search_box.send_keys("Selling Plans")
    search_box.send_keys(Keys.ENTER)

    # OPEN FIRST PRODUCT
    product = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='/products/']"))
    )
    product.click()

    # ADD TO CART
    add_cart = wait.until(
        EC.element_to_be_clickable((By.NAME, "add"))
    )
    add_cart.click()

    print("✅ Product added to cart successfully")

    driver.quit()


test_search_and_add_to_cart()