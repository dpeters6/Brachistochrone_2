from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''
    <html>
    <img src="/static/images/map.png" alt="Test Image" />
    </html>
    '''
    return render_template('Menu.html')

@app.route('/hello/<user>/')
def hello_name(user):
   return render_template('hello.html', name = user)


if __name__ == '__main__':
    app.run()
