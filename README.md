# TechRescue | AI Техническа Поддръжка

Уеб приложение за техническа поддръжка, задвижвано от AI. Потребителят избира операционна система (Windows/Linux), описва проблема си и получава конкретни стъпки и команди от AI асистент.

## Технологии

- **Backend:** Python + Flask
- **AI:** OpenAI API (`gpt-3.5-turbo`)
- **Frontend:** HTML, CSS, Bootstrap 5, Font Awesome

## Изисквания

- Python 3.10+
- OpenAI API ключ

## Инсталация

```bash
# Клониране на хранилището
git clone https://github.com/manoll67/TechRescue-project.git
cd TechRescue-project

# Създаване и активиране на виртуална среда
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Инсталиране на зависимостите
pip install -r requirements.txt

# Конфигурация — копирай шаблона и попълни своя API ключ
cp .env.example .env
# редактирай .env и сложи OPENAI_API_KEY=sk-...
```

## Стартиране

```bash
python app.py
```

Отвори `http://127.0.0.1:5000` в браузъра.

## Как работи

1. Избираш ОС — Windows или Linux
2. Пишеш въпроса си в полето в дъното (или натискаш **Enter**)
3. Frontend-ът праща `POST /ask` към Flask сървъра със съобщението и избраната ОС
4. Сървърът пита OpenAI със system prompt, настроен за съответната ОС
5. Отговорът се показва в чат кутията

## Структура на проекта

```
TechRescue-project/
├── app.py              # Flask сървър + /ask endpoint
├── requirements.txt    # Python зависимости
├── .env.example        # Шаблон за конфигурация (копирай като .env)
├── .env                # Реалният API ключ (НЕ се комитва)
├── templates/
│   └── index.html      # Единствената страница + JS за чата
└── static/
    └── styles.css      # Тъмна тема
```

## Забележки

- `debug=True` е включен в `app.py` — само за разработка, не за продукция
- `.env`, `venv/`, `__pycache__/` са в `.gitignore` — не се качват в GitHub
