# TRON Wallet Info API

### Микросервис для работы с кошельками сети TRON

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=FastAPI&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

## 📋 Описание

### Сервис предоставляет REST API для:
- Получения информации о кошельке TRON (баланс, bandwidth, energy)
- Логирования запросов в базу данных
- Просмотра истории запросов с пагинацией

## 🚀 Быстрый старт

### Требования
- Docker 20.10+
- Docker Compose 2.4+

### Запуск через Docker
```bash
git clone https://github.com/nicola1223/TronTestTask
cd TronTestTask
docker compose up --build
```

Сервис будет доступен:
http://localhost:8000

Документация API:
http://localhost:8000/docs

## 🛠 Ручная установка

1. Установите зависимости:
```bash
pip install -r requirements.txt
```

2. Настройте окружение .env:
```ini
DATABASE_URL='sqlite:///./<YOUR DB NAME>.sqlite3'
```

3. Запустите сервер:
```bash
uvicorn main:app --reload
```

## 🌐 API Endpoints

### Получить информацию о кошельке

```http
POST /api/v1/wallet/
Content-Type: application/json

{
  "address": "test_address"
}
```

### Получить информацию о кошельке

```http
GET /api/v1/wallet/queries?skip=0&limit=10
```

## 🧪 Тестирование

```bash
# Запуск всех тестов
pytest tests/

# Запуск интеграционных тестов
pytest tests/ -m integration

# Запуск юнит-тестов 
pytest tests/ -m unit
```

## 📁 Структура проекта
```
tron-wallet-api/
├── api/               # Эндпоинты API
├── core/              # Базовые настройки
├── models/            # Модели базы данных
├── schemas/           # Pydantic схемы
├── services/          # Бизнес-логика
├── tests/             # Тесты
└── utils/             # Вспомогательные утилиты
```

## ⚙️ Конфигурация

### Основные параметры в .env:
```ini
DATABASE_URL='sqlite:///./<YOUR DB NAME>.sqlite3'
```
