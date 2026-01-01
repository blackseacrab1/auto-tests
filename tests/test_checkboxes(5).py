import time
from selenium.webdriver.common.by import By

def test_checkboxes_toggle(driver):
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    time.sleep(0.5)  # увидеть загрузку

    # Находим оба чекбокса (они в форме, input type=checkbox)
    cb1 = driver.find_element(By.XPATH, "(//form[@id='checkboxes']//input)[1]")
    cb2 = driver.find_element(By.XPATH, "(//form[@id='checkboxes']//input)[2]")

    print("Состояние до кликов:")
    print(f"Чекбокс 1: {'выбран' if cb1.is_selected() else 'не выбран'}")
    print(f"Чекбокс 2: {'выбран' if cb2.is_selected() else 'не выбран'}")

    # Кликаем по обоим
    cb1.click()
    cb2.click()
    time.sleep(0.5)

    print("\nПосле кликов:")
    print(f"Чекбокс 1: {'выбран' if cb1.is_selected() else 'не выбран'}")
    print(f"Чекбокс 2: {'выбран' if cb2.is_selected() else 'не выбран'}")

    # Проверки: первый стал выбран, второй стал не выбран
    assert cb1.is_selected(), "Первый чекбокс должен стать выбранным"
    assert not cb2.is_selected(), "Второй чекбокс должен стать не выбранным"

    print("\nВсё ок: чекбоксы переключаются как надо!")