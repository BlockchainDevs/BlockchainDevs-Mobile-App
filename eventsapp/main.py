# -*- coding: utf8 -*-
'''App for PyConIndia 2018:

Github Repo: http://github.com/pythonindia/PyCon-Mobile-App
'''

__version__ = '0.4.0'

# setup error reporting
# import sentry_sdk
# sentry_sdk.init(
#     "https://0002ee03a88d419a886333ab69f01df5@sentry.io/1284618",
#     debug=True)
# That's all for error reporting

import os
import sys
from os.path import abspath, dirname
# This allows you to use a custom data dir for kivy allowing you to
# load only the images that you set here in this dir.
# This way you avoid first loading kivy default images and .kv then
# loading your data files on top.
os.environ['KIVY_DATA_DIR'] = abspath(dirname(__file__)) + '/data'
#os.environ["PYCONF_OFFLINE_MODE"] = "1"

# import App this is the main Class that manages UI's event loop
from kivy.app import App
# Kivy's properties are based on a observer pattern
# :ref: https://en.wikipedia.org/wiki/Observer_pattern
from kivy.properties import ListProperty, StringProperty

script_path = os.path.dirname(os.path.realpath(__file__))

# add module path for screen so they can be dynamically be imported
module_path = script_path + '/uix/screens/'
sys.path.insert(0, module_path)

# patch the browser to open webview on mobile
#from utils import patch_browser
import webbrowser
from utils import load_screen


class PyConApp(App):
    '''
    Our main app class:
    '''

    base_active_bright = ListProperty((216/255., 34/255., 118/255., 1))
    '''
    '''

    base_active_color = ListProperty([62./256., 30./256., 101./255, 1])
    '''This is the base Color in the app that is used to denote the currently
    active widgets, active buttons and highlited areas. Format
    is RGBA.

    :attr:`base_active_color` is a :class:`~kivy.properties.ListProperty`

    defaults to Red(217, 52, 47)
    '''

    base_inactive_color = ListProperty([202./256., 202./256., 202./255, 1])
    '''This is the base Color in the app that is used to denote the currently
    inactive items, inactive buttons and highlited areas. Format
    is RGBA.

    :attr:`base_inactive_color` is a :class:`~kivy.properties.ListProperty`

    defaults to Red(217, 52, 47)
    '''

    base_inactive_light = ListProperty([99./255., 34./255., 105./255., 1])
    '''This is the base Color in the app that is used to denote the currently
    active color used to display active buttons and highlited areas. Format
    is RGBA.

    :attr:`base_active_color` is a :class:`~kivy.properties.ListProperty`

    defaults to Red(225p, 224, 224)
    '''

    base_color = ListProperty([1, 1, 1, 1])
    '''This is the base Color in the app that is used to for bakgrounds.

    :attr:`base_color` is a :class:`~kivy.properties.ListProperty`

    defaults to Red(250, 250, 250, 1)
    '''

    event_name = StringProperty('')
    '''
    This is the name of the event.

    :attr:`event_name` is a :class:`~kivy.properties.StringProperty`

    defaults to ''
    '''

    venue_name = StringProperty('')
    '''
    This is the name of the venue.

    :attr:`venue_name` is a :class:`~kivy.properties.StringProperty`

    defaults to ''
    '''

    def build(self):
        self.script_path = script_path
        self.icon = 'data/icon.png'
        # Here we build our own navigation higherarchy.
        # So we can decide what to do when the back
        # button is pressed.
        self._navigation_higherarchy = []
        # this is the main entry point of our app
        from uix.pyconf import PyConfScreenManager
        sm = PyConfScreenManager()
        # This `sm` is the root widget of our app refered by app.root
        return sm

    def on_pause(self):
        # return True to allow for the app to pause
        return True

    def on_start(self):
        # bind to the keyboard to listen to
        # specific key codes
        from utils.keyboard import hook_keyboard
        hook_keyboard()
        # let's load our first screen
        load_screen('StartupScreen')

# Check if app is started as main and only then insitantiate the App class.
if __name__ == '__main__':
    PyConApp().run()
