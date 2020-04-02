import datetime
from os.path import dirname, abspath
from moviepy.editor import VideoFileClip
from dash.dependencies import Input, Output, State


def run(app):
    @app.callback([Output('scrubber-slider', 'max'),
                   Output('scrubber-slider', 'marks')],
                  [Input('video-player', 'url')])
    def update_scrubber(url):
        # Load the video
        project_directory = dirname(dirname(abspath(__file__)))
        full_video_path = abspath(project_directory + url)
        video = VideoFileClip(full_video_path)

        # Get duration in seconds
        duration = datetime.timedelta(seconds=video.duration)   # timedelta object
        end_time = str(duration)                                # str in HH:MM:SS.ms format
        end_time = end_time[:end_time.find('.')]                # str in HH:MM:SS format

        # Start time formatting
        start_time = datetime.timedelta(seconds=0)
        start_time = str(start_time)

        mark_style = {'font-size': '1.5em', 'color': 'white'}
        marks = {
            0: {'label': start_time, 'style': mark_style},
            video.duration: {'label': end_time, 'style': mark_style}
        }
        return video.duration, marks

    @app.callback(Output('video-player', 'seekTo'),
                  [Input('scrubber-slider', 'value')])
    def update_seek_to(value):
        return value

    return None
#     #end file


