# import modules needed
import webbrowser

# create Movie clas
class Movie():
    
    # function to initialize movie object
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
    # function to display movie trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube)
        
