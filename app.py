from flask import Flask, render_template, request

app = Flask(__name__)
# Пътят към началната страница
@app.route('/')
def home():

    return render_template('index.html')
# Мястото,където ще приемаме въпросите от чата
@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    user_massage = data.get('message')
    os_type = data.get("os")

    # Тук ще се добави логиката за обработка на въпроса и генериране на отговор
    # За сега ще връщаме фиктивен отговор
    if os_type == "windows":
        ai_response = f"Виждам,че имаш проблем с Windows.Опитвам се да намеря решение за този проблем: {user_massage}"
    else:
        ai_response = f"Linux експертът е тук! Анализиран твоя проблем: {user_massage}"


    return jsonify({"response": ai_response})

if __name__ == '__main__':
    app.run(debug=True)
    

