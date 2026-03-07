# test_add_to_cart.py

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    d = webdriver.Chrome()
    yield d
    d.quit()


def test_search_and_add_to_cart(driver):
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

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "summary[aria-label='Search']"))).click()

    search_box = wait.until(EC.visibility_of_element_located((By.NAME, "q")))
    search_box.send_keys("The Collection Snowboard: Liquid")
    search_box.send_keys(Keys.ENTER)

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.full-unstyled-link[href*='/products/']")))

    for p in driver.find_elements(By.CSS_SELECTOR, "a.full-unstyled-link[href*='/products/']"):
        if p.text.strip():
            driver.get(p.get_attribute("href"))
            break

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "form[action*='/cart/add']")))

    if driver.find_elements(By.CSS_SELECTOR, "button[name='add'][disabled]"):
        pytest.skip("Product is sold out.")

    wait.until(EC.element_to_be_clickable((By.NAME, "add"))).click()

    assert "/products/" in driver.current_url