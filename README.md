# Live Installer

A live installer for the Debian edition

## Slideshow
The Slideshow is located at usr/share/live-installer/slideshow/

We have 7 pages in the slideshow with 7 Screenshots needed:

- welcome
- about
- appcenter
- documentation
- web
- community
- donations

The order these pages are displayed is set by the file: usr/share/live-installer/slideshow/index.html

The Screenshots of the current pages in the test-slideshow.py app can be found in the screenshots folder.

## Dependencies

To test the slideshow on a standard BL7 default install:

```
sudo apt update
sudo apt install python3 python3-gi gir1.2-webkit2-4.0 xapp
```
## Preview Slideshow

 clone this repo and cd into it.
 
 ```
 cd scripts/
 ./test-slideshow.py
 
 ```
## Languages

To preview in another language, edit line 42 in scripts/slideshow.py to reflect the language you wish to preview.
