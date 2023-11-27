from  flask import Flask, render_template
index = Flask(__name__)

@index.route('/')
def indexPage():
    return render_template('index.html')

@index.route('/profile/<users>')
def profile(users):
    return render_template('profile.html', users = users , isActive = False)

@index.route('/movies')
def movie():
    movies = [{'movie':'Iron Man ', 'year':'2008','img':'https://media.wired.com/photos/5955ceabcbd9b77a41915cf6/master/w_1600,c_limit/marvel-characters.jpg'}, {'movie': 'The Incredible Hulk ', 'year':'2008','img':'https://media.wired.com/photos/5955ceabcbd9b77a41915cf6/master/w_1600,c_limit/marvel-characters.jpg'},{'movie':'Iron Man 2 (2010)', 'year':'2010','img':'https://media.wired.com/photos/5955ceabcbd9b77a41915cf6/master/w_1600,c_limit/marvel-characters.jpg'} , {'movie':'Thor (2011)','year':'2011','img':'https://media.wired.com/photos/5955ceabcbd9b77a41915cf6/master/w_1600,c_limit/marvel-characters.jpg'}, {'movie':'Captain America: The First Avenger (2011)','year':'2011','img':'https://media.wired.com/photos/5955ceabcbd9b77a41915cf6/master/w_1600,c_limit/marvel-characters.jpg'}]
    return render_template('movies.html', movies = movies)
index.run(debug = True)


