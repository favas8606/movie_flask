from flask import Flask
demo = Flask(__name__)


# for string
# ---------
# @demo.route('/profile/<username>')
# def profile(username):
#     return '<h1>This page for %s</h1>' % username



# for integer
# ---------

@demo.route('/profile/<int:id>')

def profile(id):
    return '<h1>This page for %id</h1>' % id

demo.run()