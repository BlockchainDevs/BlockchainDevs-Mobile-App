Blockchaincon.io 2019 Application
=======
> Mobile App for Blockchain Devs

## Requirements:
### Kivy Installation:
-   https://kivy.org/docs/installation/installation.html
### Dependencies-
Install from pip
-  ` pip install -r requirements.txt`

WIP
====

### To test install kivy and run the following::

    $ python eventsapp/main.py -m screen:droid2,portrait -m inspector
    $ python3 eventsapp/main.py -m screen:droid2,portrait -m inspector

### Help on screens
- https://kivy.org/docs/api-kivy.modules.screen.html

## To change images in app
   - Paste/change the image in BlockchainDevs/tools/theming
   - Change your directory to BlockchainDevs-Mobile-App
   - Run command ``make theming``

This command will aggregate all the png images in your file to one atlas
from which the images are loaded.

## to make apk **prefer linux**

1. Install buildozer: pip install buildozer
2. Edit the buildozer.spec to specify if you have android ndk and sdk,
   if not they will be automatically be downloaded by the next step.
3. Connect your mobile, enable usb debugging, Then goto BlockchainDevs