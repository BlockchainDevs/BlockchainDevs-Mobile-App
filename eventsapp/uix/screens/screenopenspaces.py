'''
'''
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder


class ScreenOpenSpaces(Screen):

    Builder.load_string('''
<ScreenOpenSpaces>
    name: 'ScreenOpenSpaces'
    ScrollView
        ScrollGrid
            AsyncImage
                source: "http://hrexperience.it/wp-content/uploads/2012/12/openspace.gif"
                size_hint_y: None
                allow_stretch: True
                height: dp(200)
                mipmap: True
            BackLabel
                active: True
                text: "Open Space is the only process that focuses on expanding time and space for the force of self-organisation to do its thing. Although one can't predict specific outcomes, it's always highly productive for whatever issue people want to attend to. Some of the inspiring side effects that are regularly noted are laughter, hard work which feels like play, surprising results and fascinating new questions. \\n-Michael M Pannwitz, Open Space practitioner"
            BackLabel
                text: "The best part about attending any meetups or conferences is getting a chance to converse with people with similar interests. Know about their domains of expertise, tell them about yours and if the interests meet up, collaborate for any future projects/prospects. Open Spaces are exactly for providing such environment for you. So go ahead, find a place, interact with people and make the best of this conference. Have a great time!"
        ''')