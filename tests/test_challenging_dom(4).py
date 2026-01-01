import time
from selenium.webdriver.common.by import By

def test_challenging_dom(driver):
    driver.get("https://the-internet.herokuapp.com/challenging_dom")
    time.sleep(1)

    print("Страница загружена, кнопки с динамическими классами видны")

    # Просто кликаем по всем трём — если локаторы нашли, тест зелёный
    driver.find_element(By.XPATH, "//a[contains(@class, 'button') and not(contains(@class, 'alert')) and not(contains(@class, 'success'))]").click()
    print("Синяя кликнута")

    driver.find_element(By.XPATH, "//a[contains(@class, 'button alert')]").click()
    print("Красная кликнута")

    driver.find_element(By.XPATH, "//a[contains(@class, 'button success')]").click()
    print("Зелёная кликнута")

    # edit и delete в таблице
    driver.find_element(By.XPATH, "//a[text()='edit']").click()  # любой edit
    time.sleep(0.5)
    assert "#edit" in driver.current_url
    print("Edit работает")

    driver.get("https://the-internet.herokuapp.com/challenging_dom")  # перезагрузка для чистоты
    time.sleep(1)
    driver.find_element(By.XPATH, "//a[text()='delete']").click()
    assert "#delete" in driver.current_url
    print("Delete работает")

    print("Успех: устойчивые локаторы на динамических элементах!")