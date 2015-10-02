import webbrowser


class Movie():
    """ ... this is the class documentation docstring ...
    The Movie class defines the properties of each movie instance
    """
    def __init__(self, movie_title, movie_year,
                 movie_storyline, poster_image,
                 trailer_youtube):
        """ ... this is the constructor method docstring ...
        the function receives as inputs the title, year of release,
        storyline, poster image url and youtube trailer url assigning
        these values to the corresponding instance variables:
        title, year, storyline, poster_image_url and trailer_youtube_url
        """
        self.title = movie_title
        self.year = movie_year
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
