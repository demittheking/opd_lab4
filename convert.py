from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/') #Отслеживаем маршрутизацию
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    currency_from = request.form['currency_from']
    currency_to = request.form['currency_to']
    amount = float(request.form['amount'])

    # данная API используется для получения акутальных данных о курсах валют
    url = f"https://api.frankfurter.app/latest?from={currency_from}&to={currency_to}&amount={amount}"

    # Получаем данные и записываем их в переменную response
    response = requests.get(url).json()

    # Извлекаем конвертированную сумму (c 2-vz цифрами после запятой)
    converted_amount = round(response['rates'][currency_to],2)

    # Возвращаем результат пользователю
    return render_template('result.html', currency_from=currency_from, currency_to=currency_to, amount=amount, converted_amount=converted_amount)

def zapusk():
    app.run(debug=True)