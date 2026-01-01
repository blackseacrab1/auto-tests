import time
import requests
from selenium.webdriver.common.by import By

def test_broken_images(driver):
    driver.get("https://the-internet.herokuapp.com/broken_images")
    time.sleep(1)  # страница загрузится, картинки попробуют подгрузиться

    images = driver.find_elements(By.TAG_NAME, "img")
    print(f"Всего картинок на странице: {len(images)}\n")

    broken_count = 0
    good_count = 0

    for img in images:
        src = img.get_attribute("src")
        if not src:
            continue

        try:
            r = requests.head(src, timeout=5, allow_redirects=True)
            if r.status_code == 200:
                print(f"✓ Работает: {src}")
                good_count += 1
            else:
                print(f"✗ Сломана (статус {r.status_code}): {src}")
                broken_count += 1
        except requests.RequestException:
            print(f"✗ Сломана (не удалось подключиться): {src}")
            broken_count += 1

    print(f"\nРезультат: нормальных — {good_count}, битых — {broken_count}")
    assert broken_count > 0, "На этой странице должны быть битые картинки!"

    print("Тест пройден: найдены битые изображения")