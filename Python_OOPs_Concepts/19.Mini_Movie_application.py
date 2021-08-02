class Movie:
    '''Movie class developed by Durga for python Demo Purpose'''
    def __init__(self, title, hero,heroine):
        self.title = title
        self.hero = hero
        self.heroine = heroine
    def info(self):
        print('Movie name:', self.title)
        print('hero name:',self.hero)
        print('heroine name:', self.heroine)

list_of_movies = []
while True:
    title = input('Enter the Movie name:')
    hero = input('Enter the hero name:')
    heroine = input('Enter the heroine name:')
    m = Movie(title, hero, heroine)
    list_of_movies.append(m)
    print('Movie added to the ;ist successfully')
    option = input('Do you want to add one more movie [yes|No]:')
    if option.lower() == 'no':
        break

print('All Moovie Information....')
print('#'*40)
for movie in list_of_movies:
    movie.info()

# sir all object are using same reference variable, then how can i difference among them selves
# can we call method of the class without calling of the class
