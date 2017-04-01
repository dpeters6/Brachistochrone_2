from flask import Flask, request, render_template
import map

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('Menu.html')

@app.route('/', methods=['POST'])
def my_for_post():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text

@app.route('/map/')
def map():
    return '''
    <html>
    <img src="/static/images/map.png" alt="Test Image" />
    </html>
    '''

@app.route('/hello/<user>/')
def hello_name(user):
   return render_template('hello.html', name = user)


if __name__ == '__main__':
    app.run()
