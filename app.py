from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    bmi = 0
    if request.method == 'POST' and 'height' in request.form:
        try:
            height = float(request.form.get('height'))
            weight = float(request.form.get('weight'))
            bmi = weight/pow(height, 2)
            bmi = round(bmi, 1)
        except:
            bmi = "ERROR"
    return render_template("index.html", bmi = bmi)


if __name__ == '__main__':
    app.run()
