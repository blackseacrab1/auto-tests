# Автотесты для the-internet.herokuapp.com

UI-тесты на Python с Selenium и pytest.  
Практика автоматизации на классической "песочнице" для тестировщиков.

## Реализовано
- Add/Remove Elements — добавление и удаление элементов с визуальными паузами и логами (файл test_add_remove_elements(1).py)

## Как запустить локально
`bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
pytest -v -s               # -s чтобы видеть print'ы в консоли