import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Giulio's Favourite Movie Trailers</title>
    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        /* Modified margin and padding */
        .movie-tile {
            margin-top: 10px;
            padding-top: 10px;
            margin-bottom: 5px;
            padding-bottom: 5px;
        }
        /* Modified h2 font size to display the movie title */
        .movie-tile h2 {
            font-size: 1.3em;
            font-weight: bold;
        }
        /* Additional class to style the movie's year of release */
        .movie-year {
            background-color: #282828;
            font-weight: bold;
        }
        /* Additional class to style the storyline of the movie*/
        .movie-storyline {
            margin-left: 5px;
            font-weight: bold;
            text-align: justify;
        }
        /* Styling the storyline content displayed by the popover */
        .popover-content {
            font-size: .7em;
            font-weight: normal;
            display: -webkit-flex; /* Safari */
            -webkit-justify-content: space-around; /* Safari 6.1+ */
            display: flex;
            justify-content: space-around;
            text-justify: justify;
            text-align: justify;
        }
        /* Styling the storyline title displayed by the popover */
        .popover-title {
            font-weight: bold;
        }
        .movie-tile:hover {
            background-color: #EEE;
            border: none;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
        // Additional function to initialise all the popovers containing each
        // movie's storyline. When the user hovers the pointer over the
        // "storyline" button the storyline for that movie is displayed
        $(function () {
          $('[data-toggle="popover"]').popover()
        })
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Giulio's Favourite Movie Trailers</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
        <div class="row">
            {movie_tiles}
        </div>
    </div>
  </body>
</html>
'''


# A single movie entry html template

# The div now contains an additional h4 element containing a span element
# to display the year of release of the movie and another link styled as a
# button which displays the movie's storyline in a popover, whenever the user
# hovers the mouse over that button

movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="342">
    <h4>
        <span class="label label-default movie-year">
            <span class="glyphicon glyphicon-film" aria-hidden="true"></span> {movie_year}
        </span>
        <a href="#" tabindex="0" class="btn btn-sm btn-default movie-storyline" role="button" data-toggle="popover" data-trigger="hover" data-placement="top" data-content="{movie_storyline}" title="{movie_title}">
            <span class="glyphicon glyphicon-comment" aria-hidden="true"></span> Storyline
        </a>
    </h4>
    <h2>{movie_title}</h2>
</div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match else None)

        # Append the tile for the movie with its content filled in

        # In addition the year of release and the storyline are also appended

        content += movie_tile_content.format(
            movie_title=movie.title,
            movie_year=movie.year,
            movie_storyline=movie.storyline,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies)
        )

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
