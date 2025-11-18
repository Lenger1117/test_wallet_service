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
Приложение можно проверить по ссылке: 
```
http://localhost:8000/docs
```
Для ручных тестов рекомендуются следующие UUID:
```
f47ac10b-58cc-4372-a567-0e02b2c3d479
```
```
550e8400-e29b-41d4-a716-446655440000
```
```
6ba7b810-9dad-4b1e-80b1-d2c3d4e5f6a7
```
```
a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d
```
```
123e4567-e89b-42d3-a456-426614174000
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
