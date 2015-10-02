import media
import fresh_tomatoes

# Instances of the Movie class

jfk = media.Movie("JFK",
                  "1991",
                  "A New Orleans DA discovers there's more to the Kennedy \
                   assassination than the official story.",
                  "http://ia.media-imdb.com/images/M/MV5BMTY4ODI3Njg5N15BMl5BanBnXkFtZTgwODgyMDUxMDE@._V1__SX1196_SY578_.jpg",  # noqa
                  "https://youtu.be/w16bYZ-4nmE")
star_trek = media.Movie("Star Trek: The Motion Picture",
                        "1979",
                        "When an alien spacecraft of enormous power is spotted \
                         approaching Earth, Admiral Kirk resumes command of \
                         the Starship Enterprise in order to intercept, \
                         examine and hopefully stop the intruder.",
                        "http://ia.media-imdb.com/images/M/MV5BNzE4MTY1MTMyN15BMl5BanBnXkFtZTcwMzk5MzI4OA@@._V1__SX1196_SY578_.jpg",  # noqa
                        "https://youtu.be/ZLlV_JVtO5c")
the_pelican_brief = media.Movie("The Pelican Brief",
                                "1993",
                                "A law student uncovers a conspiracy, putting \
                                 herself and others in danger.",
                                "http://ia.media-imdb.com/images/M/MV5BMTQwNTc1MDEyMF5BMl5BanBnXkFtZTcwMjUzNjMyMQ@@._V1__SX1196_SY578_.jpg",  # noqa
                                "https://youtu.be/N7seUNbY1_w")
the_matrix = media.Movie("The Matrix",
                         "1999",
                         "A computer hacker learns from mysterious rebels about \
                          the true nature of his reality and his role in the \
                          war against its controllers.",
                         "http://ia.media-imdb.com/images/M/MV5BMTkxNDYxOTA4M15BMl5BanBnXkFtZTgwNTk0NzQxMTE@._V1__SX1196_SY578_.jpg",  # noqa
                         "https://youtu.be/vKQi3bBA1y8")
star_wars = media.Movie("Star Wars: Episode VI - Return of the Jedi",
                        "1983",
                        "After rescuing Han Solo from the palace of Jabba the Hutt, \
                         the rebels attempt to destroy the second Death Star, \
                         while Luke struggles to make Vader return from the \
                         dark side of the Force.",
                        "http://ia.media-imdb.com/images/M/MV5BMTQ0MzI1NjYwOF5BMl5BanBnXkFtZTgwODU3NDU2MTE@._V1._CR93,97,1209,1861__SX1196_SY578_.jpg",  # noqa
                        "https://youtu.be/CsDwpF3uiZI")
apollo_13 = media.Movie("Apollo 13",
                        "1995",
                        "NASA must devise a strategy to return Apollo 13 to Earth \
                         safely after the spacecraft undergoes massive \
                         internal damage putting the lives of the three \
                         astronauts on board in jeopardy.",
                        "http://ia.media-imdb.com/images/M/MV5BMTI3MTgzODk4Nl5BMl5BanBnXkFtZTYwODQ0NzQ5._V1__SX1196_SY578_.jpg",  # noqa
                        "https://youtu.be/KtEIMC58sZo")
die_hard = media.Movie("Die Hard",
                        "1988",
                        "John McClane, officer of the NYPD, tries to save wife Holly \
                         Gennaro and several others, taken hostage by German \
                         terrorist Hans Gruber during a Christmas party at \
                         the Nakatomi Plaza in Los Angeles.",
                        "http://ia.media-imdb.com/images/M/MV5BMTY4ODM0OTc2M15BMl5BanBnXkFtZTcwNzE0MTk3OA@@._V1__SX1196_SY578_.jpg",  # noqa
                        "https://youtu.be/2TQ-pOvI6Xo")
a_space_odissy = media.Movie("2001: A Space Odyssey",
                             "1968",
                             "Humanity finds a mysterious, obviously artificial, object \
                              buried beneath the Lunar surface and, with the \
                              intelligent computer H.A.L. 9000, sets off on \
                              a quest.",
                             "http://ia.media-imdb.com/images/M/MV5BNDYyMDgxNDQ5Nl5BMl5BanBnXkFtZTcwMjc1ODg3OA@@._V1__SX1196_SY578_.jpg",  # noqa
                             "https://youtu.be/e-QFj59PON4")
war_games = media.Movie("War Games",
                        "1983",
                        "A young man finds a back door into a military central \
                         computer in which reality is confused with \
                         game-playing, possibly starting World \
                         War III.",
                        "http://ia.media-imdb.com/images/M/MV5BMTMyMTE3OTk3NF5BMl5BanBnXkFtZTcwOTkwNDc3NA@@._V1__SX1196_SY578_.jpg",  # noqa
                        "https://youtu.be/hbqMuvnx5MU")
erin_brockovich = media.Movie("Erin Brockovich",
                              "2000",
                              "An unemployed single mother becomes a legal \
                               assistant and almost single-handedly brings \
                               down a California power company accused of \
                               polluting a city's water supply.",
                              "http://ia.media-imdb.com/images/M/MV5BMjMyMDMzMDg4M15BMl5BanBnXkFtZTgwNDc3ODYxMTE@._V1__SX1196_SY578_.jpg",  # noqa
                              "https://youtu.be/_2GvrAQMNoU")
indiana_johnes = media.Movie("Indiana Jones and the Last Crusade",
                              "1989",
                              "When Dr. Henry Jones Sr. suddenly goes missing \
                               while pursuing the Holy Grail, eminent \
                               archaeologist Indiana Jones must follow \
                               in his father's footsteps and stop \
                               the Nazis.",
                              "http://ia.media-imdb.com/images/M/MV5BMTQxMTUyODg2OF5BMl5BanBnXkFtZTcwNDM2MjAxNA@@._V1__SX1196_SY578_.jpg",  # noqa
                              "https://youtu.be/a6JB2suJYHM")
hunt_for_red_october = media.Movie("The Hunt for Red October",
                              "1990",
                              "In 1984, the USSR's best submarine captain in \
                              their newest sub violates orders and heads for \
                              the USA. Is he trying to defect, or to start \
                              a war?",
                              "http://ia.media-imdb.com/images/M/MV5BNzk3OTE2NjQ0OV5BMl5BanBnXkFtZTgwMDg3ODYxMTE@._V1__SX1196_SY578_.jpg",  # noqa
                              "https://youtu.be/iGfk_IU3Wlo")

# Array containing the instances

movies = [jfk, star_trek, the_pelican_brief, the_matrix, star_wars,
          apollo_13, die_hard, a_space_odissy, war_games, erin_brockovich,
          indiana_johnes, hunt_for_red_october]

# Calling the open_movies_page function passing the array containing the movies
fresh_tomatoes.open_movies_page(movies)
