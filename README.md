# REST API для управления балансом кошельков с поддержкой конкурентных операций.

## Запуск приложения
### 1. Клонируйте проект:
```
git clone https://github.com/Lenger1117/test_wallet_service.git
```
### 2. Запустите приложение (Docker должен быть запущен):
```
docker-compose up --build
```

## Запуск тестов(локально, без Docker)
### 1. Клонируйте проект:
```
git clone https://github.com/Lenger1117/test_wallet_service.git
```
### 2. Установите и активируйте виртуальное окружение:
```
python3 -m venv venv или python -m venv venv
```
```
source venv/bin/activate или source venv/Scripts/activate
```
### 3. Установите зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
### 4. Запуск тестов:
```
pytest tests/ -v
```
