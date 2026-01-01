import time
from selenium.webdriver.common.by import By

def test_successful_basic_auth(driver):
    # Передаём логин/пароль в URL — попап не появится вообще
    auth_url = "https://admin:admin@the-internet.herokuapp.com/basic_auth"
    
    print("Заходим с правильными кредсами...")
    driver.get(auth_url)
    time.sleep(1)  # пауза, чтобы увидеть страницу

    # Ищем заголовок успеха
    heading = driver.find_element(By.TAG_NAME, "h3")
    assert heading.text == "Basic Auth"
    
    # Ищем основной текст поздравления
    content = driver.find_element(By.CSS_SELECTOR, "div.example p")
    assert "Congratulations" in content.text
    
    print("Успех: вошли с admin/admin!")
    print(content.text)  # выведет весь текст для лога


def test_failed_basic_auth(driver):
    # Пробуем с неправильными кредсами — браузер покажет попап, но Selenium получит 401
    wrong_url = "https://wrong:wrong@the-internet.herokuapp.com/basic_auth"
    
    print("Пробуем с неверными кредсами...")
    driver.get(wrong_url)
    time.sleep(1)
    
    # Страница не загрузится нормально — получим 401, но в title или source будет намёк
    # Проверяем по title (он остаётся "The Internet" или пустой, но content пустой)
    page_source = driver.page_source
    
    # В случае ошибки источник содержит "401 Unauthorized" или минимальный HTML
    assert "Congratulations" not in page_source
    assert "Unauthorized" in page_source or driver.title != "Basic Auth"
    
    print("Как и ожидалось: доступ запрещён с неверными кредсами")