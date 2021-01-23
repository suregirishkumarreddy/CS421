class Tollywood:

    def __init__(self, list_of_movies):
        self.list_of_movies = list_of_movies

    def __repr__(self):
        return 'Tollywood(list_of_movies=%s)' % (self.list_of_movies)

    def __str__(self):
        return 'Tollywood(list_of_movies=%s)' % (self.list_of_movies)

class Movie:

    def __init__(self, name, list_of_songs):
        self.name = name
        self.list_of_songs = list_of_songs

    def __repr__(self):
        return 'Movie(name=%s, songs=%s)' % (self.name, self.list_of_songs)

    def __str__(self):
        return 'Movie(name=%s, songs=%s)' % (self.name, self.list_of_songs)

class Song:

    def __init__(self, name, list_of_artists):
        self.name = name
        self.list_of_artists = list_of_artists

    def __repr__(self):
        return 'Song(name=%s, artists=%s)' % (self.name, self.list_of_artists)

    def __str__(self):
        return 'Song(name=%s, artists=%s)' % (self.name, self.list_of_artists)

class Singer:

    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def __repr__(self):
        return 'Singer(name=%s, sex=%s)' % (self.name, self.sex)

    def __str__(self):
        return 'Singer(name=%s, sex=%s)' % (self.name, self.sex)

class Lyricist:

    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def __repr__(self):
        return 'Lyricist(name=%s, sex=%s)' % (self.name, self.sex)

    def __str__(self):
        return 'Lyricist(name=%s, sex=%s)' % (self.name, self.sex)

class Music_Director:

    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def __repr__(self):
        return 'Music Director(name=%s, sex=%s)' % (self.name, self.sex)

    def __str__(self):
        return 'Music Director(name=%s, sex=%s)' % (self.name, self.sex)
    
# Creating an instance for each Singer
singer_1 = Singer("S.P. Balasubramaniam", "Male")
singer_2 = Singer("S. Janaki", "Female")
singer_3 = Singer("Chitra", "Female")
singer_4 = Singer("Mano", "Male")


# Creating an instance for each Lyricist
lyricist_1 = Lyricist("Veturi", "Male")
lyricist_2 = Lyricist("C. Narayana Reddy", "Male")
lyricist_3 = Lyricist("Sirivennala Seetharama Sastry", "Male")


# Creating an instance for each Music Director
music_director_1 = Music_Director("Illayaraja", "Male")
music_director_2 = Music_Director("Chakravarthy", "Male")


# Creating an instance for each Song
song_1 = Song("Priya Priyatama", [singer_4, singer_3, lyricist_1, music_director_1])
song_2 = Song("Suvvi Suvvi", [singer_1, singer_2, lyricist_2, music_director_1])
song_3 = Song("Subhalekha Rasukunna", [singer_1, singer_3, lyricist_1, music_director_1])
song_4 = Song("Sirimalle Puvva", [singer_2, lyricist_1, music_director_2])
song_5 = Song("Chamaku Chamaku Cham", [singer_1, singer_3, lyricist_3, music_director_1])


# Creating an instance for each Movie with song details
movie_1 = Movie("Killer", [song_1])
movie_2 = Movie("Swathi Muthyam", [song_2])
movie_3 = Movie("Kondaveeti Donga", [song_3, song_5])
movie_4 = Movie("Padaharella Vayasu", [song_4])


# Creating an instance Tolloywood Movies with my list of Movies
my_tollywood_movie_list = [movie_1, movie_2, movie_3, movie_4]


# Print the list of Movies in Tollywood
print("List of Movies in Tollywood : ", Tollywood(my_tollywood_movie_list))

