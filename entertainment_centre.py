# import modules needed
import media
import fresh_tomatoes

# create an object for each movie to be displayed on webpage
# includes title, storyline, image, and youtube URL
frozen = media.Movie("Frozen",
                     "A princess saves sister with magical powers",
                     "https://en.wikipedia.org/wiki/Frozen_(2013_film)#/media/File:Frozen_(2013_film)_poster.jpg",
                     "https://www.youtube.com/watch?v=FLzfXQSPBOg")

findingNemo = media.Movie("Finding Nemo",
                   "A father looks for his son",
                   "https://en.wikipedia.org/wiki/Finding_Nemo#/media/File:Finding_Nemo.jpg",
                   "https://www.youtube.com/watch?v=wZdpNglLbt8")

lego = media.Movie("Lego Movie",
                   "A Child plays with legos",
                   "https://en.wikipedia.org/wiki/The_Lego_Movie#/media/File:The_Lego_Movie_poster.jpg",
                   "https://www.youtube.com/watch?v=fZ_JOBCLF-I")

beforeSunrise = media.Movie("Before Sunrise",
                        "A man and woman meet on a train",
                        "https://en.wikipedia.org/wiki/Before_Sunrise#/media/File:Before_Sunrise_poster.jpg",
                        "https://www.youtube.com/watch?v=jGvcbSabADM")

Summer = media.Movie("500 Days of Summer",
                        "A man recounts memories of his relationship",
                        "https://en.wikipedia.org/wiki/500_Days_of_Summer#/media/File:Five_hundred_days_of_summer.jpg",
                        "https://www.youtube.com/watch?v=PsD0NpFSADM")

# create a list of the movies
movies = [frozen, findingNemo, lego, beforeSunrise, Summer]

# display webpage
fresh_tomatoes.open_movies_page(movies)

