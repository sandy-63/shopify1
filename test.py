from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def test_search_and_add_to_cart():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    wait = WebDriverWait(driver, 15)

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

    # Open search
    search_icon = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "summary[aria-label='Search']"))
    )
    search_icon.click()

    # Search product
    search_box = wait.until(
        EC.visibility_of_element_located((By.NAME, "q"))
    )
    search_box.send_keys("Selling Plans")
    search_box.submit()

    # Wait for search results and click first product
    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a[href*='/products/']"))
    )

    product = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='/products/']"))
    )
    product.click()

    # Add to cart
    add_to_cart = wait.until(
        EC.element_to_be_clickable((By.NAME, "add"))
    )
    add_to_cart.click()

    # Verify cart page
    wait.until(EC.url_contains("/cart"))

    print("Test Passed: Product added to cart successfully")

    driver.quit()


test_search_and_add_to_cart()