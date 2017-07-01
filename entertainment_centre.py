# import modules needed
import media
import fresh_tomatoes

# create an object for each movie to be displayed on webpage
frozen = media.Movie("Frozen",
                     "A princess saves sister with magical powers",
                     "https://static.posters.cz/image/1300/"
                     "posters/frost-group-i20838.jpg",
                     "https://www.youtube.com/watch?v=FLzfXQSPBOg")

findingNemo = media.Movie("Finding Nemo",
                          "Father looks for son",
                          "https://fiu-assets-2-syitaetz61hl2sa."
                          "stackpathdns.com/static/use-media-"
                          "items/17/16316/full-900x1300/"
                          "56702cc2/pva6ds.jpeg?resolution=0",
                          "https://www.youtube.com/watch?v=wZdpNglLbt8")

lego = media.Movie("Lego Movie",
                   "A Child plays with legos",
                   "https://img.csfd.cz/files/images/user/profile"
                   "/159/110/159110092_d8e43f.jpg",
                   "https://www.youtube.com/watch?v=fZ_JOBCLF-I")

beforeSunrise = media.Movie("Before Sunrise",
                            "A man and woman meet on a train",
                            "http://img.moviepostershop.com/before-sunrise-"
                            "movie-poster-1995-1020190611.jpg",
                            "https://www.youtube.com/watch?v=jGvcbSabADM")

Summer = media.Movie("500 Days of Summer",
                     "A man recounts memories of his relationship",
                     "http://www.impawards.com/2009/posters/"
                     "five_hundred_days_of_summer_xlg.jpg",
                     "https://www.youtube.com/watch?v=PsD0NpFSADM")

# create a list of the movies
movies = [frozen, findingNemo, lego, beforeSunrise, Summer]

# display webpage
fresh_tomatoes.open_movies_page(movies)

