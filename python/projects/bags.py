from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    sites = ['twitter', 'facebook', 'instagram', 'whatsapp']
    return render_template("about.html", sites=sites)


@app.route("/welcome")
def welcome():
    return render_template("welcome.html")

words = ['ability', 'able', 'about', 'above', 'accept', 'according', 'account']


@app.route('/english', methods=['GET', 'POST'])
def english():
    if request.method == 'POST':
        button_pressed = request.form.get('button_pressed')
        if button_pressed == 'start':
            messages = "מעולה! אנחנו נתחיל מההתחלה"
            hide_button = True
        elif button_pressed == 'continue':
            messages = "מעולה! אנחנו נמשיך מאותה הנקודה"
            hide_button = False
        else:
            messages = ""  # טיפול במצבים אחרים
            hide_button = False
        return render_template("english.html", messages=messages, hide_buttons=True, hide_button=hide_button)
    return render_template("english.html")


@app.route('/choose_list', methods=['GET', 'POST'])
def choose_list():
    if request.method == 'POST':
        button = request.form.get('button')
        if button == '1000_words':
            options = "welcome"
        elif button == '2000_words':
            options = "welcome!!!"
        elif button == 'hitec':
            options = "welcome!!!!!!"
        else:
            options = ""  # טיפול במצבים אחרים
        return render_template("english.html", options=options)
    return render_template("english.html")




@app.route("/<name>")
def welco(name):
    return render_template("welcome.html", name=name)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        msg = request.form.get('msg')
        return "Message received successfully!"
    return render_template("welcome.html")


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        age = int(request.form['age'])
        if age >= 18:
            message = "You're welcome!"
        else:
            message = "Your age is too low!"
        return render_template('index.html', message=message)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)