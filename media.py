# !/usr/bin/python2
# media.py

class Movie(object):
    """ Base Class which inherits from Object.
    Atrributes will be the specific values for a movie.
    
    Attributes:
        title: A string containing the videos' title text.
        run_time: An integer of run time in whole minutes.
        rating: A string containing the MPAA or FCC approved rating text.
        author: A string containing the primary or preferred authors'name.
        year_of_release: An integer of the 4-digit year of release.
        plot_synopsis: A string with a single sentence plot summary.
        poster_image_url: A string with an Internet URL to an offical
            promotional poster image.
        trailer_youtube_url: A string with an Internet URL to the offical
            video promotional trailer hosted on youbute.com.
    """
    
    def __init__(self, title, run_time, author, year_of_release,
            plot_synopsis, rating_image_url, poster_image_url, trailer_youtube_url):
        """ Default Constructor with default values

        Args:
            title: Movie title.
            run_time: Duration of the video in minutes
            author: Name of lead screenplay author.
            year_of_release: Year released.
            plot_synopsis: Single sentence plot summary.
            rating_image_url: Url for MPAA rating image badge.
            poster_image_url: Url to poster image.
            trailer_youtube_url: Url to offical youtube movie trailer.
        """

        self.title = title
        self.run_time = run_time
        self.author = author
        self.year_of_release = year_of_release
        self.plot_synopsis = plot_synopsis
        self.rating_image_url = rating_image_url
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url