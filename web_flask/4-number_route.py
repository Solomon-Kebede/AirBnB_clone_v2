#!/usr/bin/python3

'''
Write a script that starts a Flask web application:
    -Your web application must be listening on `0.0.0.0`, port `5000`
    -Routes:
        -`/`: display "Hello HBNB!"
        -`/hbnb`: display "HBNB"
        -`/c/<text>`: display "C " followed by the value of the `text`
        variable (replace underscore `_` symbols with a space ` `)
        -`/python/(<text>)`: display "Python ", followed by the value of
        the `text` variable (replace underscore _ symbols with a space ` `)
            -The default value of text is "is cool"
        -`/number/<n>`: display "`n` is a number" **only** if `n` is an integer
    -You must use the option `strict_slashes=False` in your route definition
'''


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    '''Returns the home page'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''Returns the hbnb page'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def ctext(text):
    '''Returns a subdirectory page of C'''
    if '_' in text:
        result = text.replace('_', ' ')
    else:
        result = text
    return 'C {}'.format(result)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pytext(text=''):
    '''Returns a subdirectory page of Python'''
    if text == '':
        result = 'is cool'
    elif '_' in text:
        result = text.replace('_', ' ')
    else:
        result = text
    return 'Python {}'.format(result)


@app.route('/number/<int:n>', strict_slashes=False)
def isint(n):
    return '{:d} is a number'.format(n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
