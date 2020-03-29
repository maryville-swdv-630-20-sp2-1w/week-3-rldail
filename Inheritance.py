# Week 3 submission
# Inheritance.py
# Application containing a generic superclass and three subclasses of that superclass
# each subclass has 2 attributes and 2 methods
# includes test method that shows the classes in operation.

class Media:
    # Initialize the instance
    def __init__(self, title, year, type):
        self.title = title
        self.year = year
        self.type = type
        self.tags = []

    # Get the title
    def getTitle(self):
        return self.title
    
    # Get the year
    def getYear(self):
        return self.year
    
    # Get the type
    def getType(self):
        return self.type

    # Update the year
    def updateYear(self, year):
        self.year = year
    
    # Get the tags
    def getTags(self):
        return self.tags

    # Update the tags        
    def updateTags(self, tag):
        self.tags.append(tag)


class Movie(Media):
    # Initialize the instance
    def __init__(self, genre, length, director, *args, **kwargs):
        self.genre = genre
        self.length = length
        self.director = director
        super(Movie, self).__init__(*args, **kwargs)

    # Get the genre
    def getGenre(self):
        return self.genre

    # Update the genre
    def updateGenre(self, genre):
        self.genre = genre

    # Get the length
    def getLength(self):
        return self.length

    # Update the length
    def updateLength(self, length):
        self.length = length

    # Get the director
    def getDirector(self):
        return self.director

    # Update the director
    def updateDirector(self, director):
        self.director = director

class Music(Media):
    # Initialize the instance
    def __init__(self, artist, length, *args, **kwargs):
        self.artist = artist
        self.length = length
        super(Music, self).__init__(*args, **kwargs)

    # Get the artist
    def getArtist(self):
        return self.artist

    # Update the artist
    def updateArtist(self, artist):
        self.artist = artist

    # Get the length
    def getLength(self):
        return self.length

    # Update the length
    def updateLength(self, length):
        self.length = length

class Image(Media):
    # Initialize the instance
    def __init__(self, artist, size, *args, **kwargs):
        self.artist = artist
        self.size = size
        super(Image, self).__init__(*args, **kwargs)

    # Get the artist
    def getArtist(self):
        return self.artist

    # Update the artist
    def updateArtist(self, artist):
        self.artist = artist

    # Get the size
    def getSize(self):
        return self.size

    # Update the size
    def updateSize(self, size):
        self.size = size
        

def main():
    movie1 = Movie('Comedy', '93 minutes', 'Terry Jones', 'Monty Python''s Life of Brian', 1979, 'Movie')
    movie2 = Movie('Horror', '91 minutes', 'Mike Flanagan', 'Hush', 2016, 'Movie')

    song1 = Music('Metallica', '7:39', 'Enter Sandman', 1991, 'Music')
    song2 = Music('Depeche Mode', '6:22', 'Blasphemous Rumours', 1984, 'Music')

    image1 = Image('Leonardo Da Vinci', '3024x4164', 'The Mona Lisa', 1503, 'Image')
    image2 = Image('Vincent van Gogh', '1200x1557', 'Vase with Twelve Sunflowers', 1888, 'Image')

    print(movie1.getTitle() + ' is a ' + movie1.getType() + '. It was made in ' + str(movie1.getYear()) + ' and is ' + movie1.getLength() + ' long.\nIt was directed by ' + movie1.getDirector() + '.\n')
    print(movie2.getTitle() + ' is a ' + movie2.getType() + '. It was made in ' + str(movie2.getYear()) + ' and is ' + movie2.getLength() + ' long.\nIt was directed by ' + movie2.getDirector() + '.\n')

    print(song1.getTitle() + ' is a ' + song1.getType() + ' type file. It was recorded in ' + str(song1.getYear()) + ' and is ' + song1.getLength() + ' long.\n' + song1.getArtist() + ' is the artist.\n')
    print(song2.getTitle() + ' is a ' + song2.getType() + ' type file. It was recorded in ' + str(song2.getYear()) + ' and is ' + song2.getLength() + ' long.\n' + song2.getArtist() + ' is the artist.\n')

    print(image1.getTitle() + ' is an ' + image1.getType() + ' type file. It was created in ' + str(image1.getYear()) + ' and has dimensions of ' + image1.getSize() + '.\n' + image1.getArtist() + ' is the artist.\n')
    print(image2.getTitle() + ' is an ' + image2.getType() + ' type file. It was created in ' + str(image2.getYear()) + ' and has dimensions of ' + image2.getSize() + '.\n' + image2.getArtist() + ' is the artist.\n')

main()

