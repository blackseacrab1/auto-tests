import time
from selenium.webdriver.common.by import By

def test_add_and_count_elements(driver):
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

    add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")

    print("Начинаем добавлять элементы...")
    for i in range(1, 6):
        add_button.click()
        time.sleep(0.5)  # маленькая пауза, чтобы увидеть в браузере и консоли
        delete_buttons = driver.find_elements(By.CSS_SELECTOR, ".added-manually")
        print(f"Добавлен элемент №{i}, теперь их: {len(delete_buttons)}")

    assert len(delete_buttons) == 5
    print("Успех: добавлено ровно 5 элементов!\n")


def test_add_and_remove_elements(driver):
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

    add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")

    print("Добавляем 3 элемента...")
    for i in range(1, 4):
        add_button.click()
        time.sleep(0.5)
        print(f"Добавлен элемент №{i}")

    delete_buttons = driver.find_elements(By.CSS_SELECTOR, ".added-manually")
    print(f"Сейчас элементов: {len(delete_buttons)}. Удаляем первый...")
    delete_buttons[0].click()
    time.sleep(0.5)

    delete_buttons = driver.find_elements(By.CSS_SELECTOR, ".added-manually")
    print(f"Теперь элементов: {len(delete_buttons)}. Удаляем последний...")
    delete_buttons[-1].click()
    time.sleep(0.5)

    remaining = driver.find_elements(By.CSS_SELECTOR, ".added-manually")
    assert len(remaining) == 1
    print("Успех: остался ровно 1 элемент!")