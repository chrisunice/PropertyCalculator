import dash_player
import dash_html_components as html
import dash_core_components as dcc


def app_layout():
    layout = html.Div(
        className='row',
        children=[
            html.Div(
                className='left-side',
                children=[
                    html.Div(
                        className='video-container',
                        children=[
                            dash_player.DashPlayer(
                                id='video-player',
                                url='/static/flying_spirit.mp4',    # local file
                                controls=False,                     # no controls
                            )
                        ]
                    ),
                    html.Div(
                        className='control-container',
                        children=[
                            dcc.Slider(
                                id='scrubber-slider',
                                value=0,            # starting time
                                min=0,              # minimum is zero seconds
                                step=0.1,           # step every 1/10 of a second
                                updatemode='drag'   # most responsive
                            ),
                            dcc.Input(
                                id='scrubber-position'
                            )
                        ]
                    )
                ]
            ),
            html.Div(
                className='right-side',
                children=[]
            )
            # html.Video(
            #     # src='/static/flying_spirit.mp4#t=10,20',
            #     src='/static/flying_spirit.mp4',
            #     controls=True,
            #     autoPlay=False,
            #     preload='auto'
            # )
        ]
    )
    return layout
# end file
