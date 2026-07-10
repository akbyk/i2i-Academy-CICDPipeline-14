from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_homepage_title():
    options = Options()
    options.add_argument("--headless=new")   # run Chrome with no visible window
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://www.example.com")
        assert "Example Domain" in driver.title
    finally:
        driver.quit()