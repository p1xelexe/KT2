import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

def test_product_images():
    driver.get("https://demo-opencart.ru/")
    product_link = driver.find_element(By.CSS_SELECTOR, ".product-layout:nth-child(1) .caption a")
    product_link.click()
    time.sleep(2)  # Даем странице немного времени для загрузки

    thumbnails = driver.find_elements(By.CSS_SELECTOR, ".thumbnail")
    if len(thumbnails) > 1:
        thumbnails[1].click()
        time.sleep(2)

def test_korzina():
    driver.get("https://demo-opencart.ru/")
    korzina_link = driver.find_element(By.CSS_SELECTOR, "#content > div.row > div:nth-child(1) > div > div.button-group > button:nth-child(1)")
    time.sleep(2)
    korzina_link.click()
    time.sleep(2)

    korzina_catalog_lik = driver.find_element(By.CSS_SELECTOR, "#top-links > ul > li:nth-child(4) > a > i")
    korzina_catalog_lik.click()
    time.sleep(2)
    summ = driver.find_element(By.CSS_SELECTOR, "#content > div.row > div > table > tbody > tr:nth-child(2) > td:nth-child(2)")
    if summ == 0:
        print("Корзина пуста")
    else:
        print("Товар в корзине")

def test_empty_category():

    driver.get("https://demo-opencart.ru/index.php")

    search = driver.find_element(By.CSS_SELECTOR,
                                 "div.container:nth-child(3) nav.navbar div.collapse.navbar-collapse.navbar-ex1-collapse ul.nav.navbar-nav li.dropdown:nth-child(1) > a.dropdown-toggle")

    search.click()

    time.sleep(2)

    search = driver.find_element(By.CSS_SELECTOR,
                                 "div.container:nth-child(3) nav.navbar div.collapse.navbar-collapse.navbar-ex1-collapse ul.nav.navbar-nav li.dropdown:nth-child(1) div.dropdown-menu div.dropdown-inner ul.list-unstyled li:nth-child(1) > a:nth-child(1)")

    search.click()

    time.sleep(2)

    products=driver.find_elements(By.CSS_SELECTOR, ".product-layout")
    if not products:
        print("Страница категории PC пуста.")
    else:
        print("Страница категории PC не пуста.")


def test_registration():
    search = driver.find_element(By.CSS_SELECTOR,
                                 "div.container div.nav.pull-right ul.list-inline li.dropdown:nth-child(2) > "
                                 "a.dropdown-toggle")
    search.click()
    time.sleep(2)
    search = driver.find_element(By.CSS_SELECTOR,
                                 "div.container div.nav.pull-right ul.list-inline li.dropdown.open:nth-child(2) "
                                 "ul.dropdown-menu.dropdown-menu-right li:nth-child(1) > a:nth-child(1)")
    search.click()
    time.sleep(2)
    search = driver.find_element(By.CSS_SELECTOR, "#input-firstname")
    words = "Здраствуйте"
    search.click()
    for letter in words:
        search.send_keys(letter)
    time.sleep(2)
    search = driver.find_element(By.CSS_SELECTOR, "#input-lastname")
    words = "Сэнпай"
    search.click()
    for letter in words:
        search.send_keys(letter)
    time.sleep(2)
    search = driver.find_element(By.CSS_SELECTOR, "#input-email")
    words = "gaga@gmail.com"
    search.click()
    for letter in words:
        search.send_keys(letter)
    time.sleep(2)
    search = driver.find_element(By.CSS_SELECTOR, "#input-telephone")
    words = "77777"
    search.click()
    for letter in words:
        search.send_keys(letter)
    time.sleep(2)
    search = driver.find_element(By.CSS_SELECTOR, "#input-password")
    words = "77777"
    search.click()
    for letter in words:
        search.send_keys(letter)
    time.sleep(2)
    search = driver.find_element(By.CSS_SELECTOR, "#input-confirm")
    words = "77777"
    search.click()
    for letter in words:
        search.send_keys(letter)
    time.sleep(2)
    search = driver.find_element(By.CSS_SELECTOR,
                                 "div.container:nth-child(4) div.row div.col-sm-9 form.form-horizontal:nth-child(3) div.buttons:nth-child(4) div.pull-right > input:nth-child(3)")
    search.click()
    time.sleep(2)
    search = driver.find_element(By.CSS_SELECTOR,
                             "div.container:nth-child(4) div.row div.col-sm-9 form.form-horizontal:nth-child(3) div.buttons:nth-child(4) div.pull-right > input.btn.btn-primary:nth-child(4)")
    search.click()
    time.sleep(2)


def test_search():
    driver.get("https://demo-opencart.ru/")
    search_input = driver.find_element(By.NAME, "search")
    search_input.send_keys("phone")
    search_button = driver.find_element(By.CSS_SELECTOR, ".input-group-btn button")
    search_button.click()
    time.sleep(2)



test_product_images()
test_korzina()
test_empty_category()
test_registration()
test_search()


driver.quit()