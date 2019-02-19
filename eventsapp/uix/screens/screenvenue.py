'''ScreenSponsor:
Display all the information about venue.
'''

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.garden.mapview import MapView, MapMarker


class ScreenVenue(Screen):

    Builder.load_string('''
<ScreenVenue>
    name: 'ScreenVenue'
    BoxLayout
        spacing: dp(13)
        orientation: 'vertical'
        padding: dp(4)
        BoxLayout
            orientation: 'vertical'
            Label:
                color: 0, 0, 0, 1
                text: app.venue_name
                halign: 'center'
                size_hint_y: None
                height: dp(25)
            Image:
                id: img_venue
                source: app.screenschedule.event['venue_partners'][0]['photo']
                allow_stretch: True
                keep_ratio: True
        Splitter
            sizable_from: 'top'
            MapView:
                zoom: 11
                on_parent:
                    coords = app.screenschedule.event['venue_partners'][0]['coords'].split(',')
                    self.lat = map.lat = float(coords[0]) 
                    self.lon = map.lon = float(coords[1])
                MapMarker
                    id: map
        BoxLayout:
            size_hint: 1, None
            height: dp(45)
            spacing: dp(13)
            padding: dp(4)
            ActiveButton:
                text: 'Directions 23rd Feb'
                on_release:
                    import webbrowser
                    webbrowser.open(app.screenschedule.event['venue_partners'][0]['directions'])
            ActiveButton:
                text: 'Directions 24th Feb'
                on_release:
                    import webbrowser
                    webbrowser.open(app.screenschedule.event['venue_partners'][0]['directions1']) 
''')

