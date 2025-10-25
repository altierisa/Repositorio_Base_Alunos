import flask,requests,url_for, render_template

app= Flask(__name__)
if __name == '__main__':

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def portal_matematico():
    resultado = None
    erro = None

    if request.method == 'POST':
        operacao = request.form.get('operacao')
        num1 = request.form.get('num1')
        num2 = request.form.get('num2')

        # Validação simples para garantir que os números sejam convertidos
        try:
            num1 = float(num1)
            num2 = float(num2)

            if operacao == 'multiplicacao':
                resultado = num1 * num2
            elif operacao == 'potencia':
                resultado = num1 ** num2
            else:
                erro = 'Operação inválida.'
        except ValueError:
            erro = 'Por favor, insira números válidos.'

    return render_template('portal.html', resultado=resultado, erro=erro)

if __name__ == '__main__':
    app.run(debug=True)

