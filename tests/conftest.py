import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def driver():
    # Создаём браузер
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
  

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    
    driver.maximize_window()
    
    # Отдаём готовый драйвер тесту
    yield driver
    
    # После теста закрываем браузер
    driver.quit()