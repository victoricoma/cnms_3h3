from flask import Flask, render_template_string, request
import random

app = Flask(__name__)

def numerosLoteria(qtd_jogo=6, lmt_max=60):
    if qtd_jogo > lmt_max:
        raise ValueError("O jogo não pode ser maior que o limite dos numeros da loteria.")
    numeros = random.sample(range(1, lmt_max + 1) , qtd_jogo)
    return sorted(numeros)

executa_jogo = numerosLoteria(6, 60)
print("Seus números da sorte são: ", executa_jogo)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gerador de Loteria</title>
    <style>
        body{
            font-family: Arial, Helvetica, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f0f2f5;
            margin: 0;
        }
        .card{
            background-color: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 8px 10px rgb(0, 0, 0, 0, 0.1);
            text-align: center;
            max-width: 400px;
            width: 100%;
        }
        .ball-container{
            display: flex;
            justify-content: center;
            gap: 10px;
            margin: 20px 0;
            flex-wrap: wrap;
        }
        .ball{
            background-color: #2e7d32;
            color: white;
            width: 45px;
            height: 45px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            font-size: 1.1rem;
        }
        .button{
            background-color: #2e7d32;
            color: white;
            border: none;
            padding: 12px 20px;
            font-size: 1rem;
            border-radius: 6px; 
            cursor: pointer;
            transition: 0.2;
        }
        .button:hover{
            background-color: #1b5e20;
        }
    </style>
</head>
<body>
    <div class="card">
        <div class="ball-container">
            {% for num in numeros %}
                <div class="ball">{{ "%02d" % num }}</div>
            {% endfor %}
        </div>
        <form action="POST">
            <button type="submit">🍀Gerar Numeros🍀</button>
        </form>
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET','POST'])
def home():
    numeros = numerosLoteria(6, 60)
    return render_template_string(HTML_TEMPLATE, numeros=numeros)

if __name__ =='__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)