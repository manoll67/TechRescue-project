import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from openai import OpenAI

# Зареждане на конфигурацията
load_dotenv()

app = Flask(__name__)

# Инициализиране на клиента (Новият стандарт)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    # 1. Получаване на данни от Frontend-а
    data = request.get_json()
    if not data:
        return jsonify({"response": "Грешка: Не са изпратени данни."}), 400

    user_query = data.get('message', '')
    os_context = data.get('os', 'Linux') # По подразбиране Linux

    try:
        # 2. Изпращане на заявка към OpenAI
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system", 
                    "content": f"Ти си експерт по техническа поддръжка за {os_context}. "
                               "Давай конкретни стъпки и команди. Използвай професионален тон."
                },
                {"role": "user", "content": user_query}
            ],
            temperature=0.7
        )

        # 3. Извличане на отговора
        ai_response = completion.choices[0].message.content
        return jsonify({"response": ai_response})

    except Exception as e:
        # Логване на грешката в терминала за теб
        print(f"DEBUG ERROR: {str(e)}")
        return jsonify({"response": "Сървърна грешка при връзка с AI. Провери .env файла."}), 500

if __name__ == '__main__':
    # Включен debug режим за лесно проследяване на грешки в Linux терминала
    app.run(host='127.0.0.1', port=5000, debug=True)

