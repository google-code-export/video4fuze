Based on ewelot's findings on sansa forums, I've done a little GUI app. which will let you convert your videos to a format readable by our beloved fuze.

[Video explaining how to use video4fuze](http://www.youtube.com/watch?v=m4-jt3B3Bag)

New: for those who wanted it, now there's a zip compiled archive for download.



It has support for a wide range of video formats (the same as mencoder, as it uses mencoder as a backend) and should work on all **nix  systems and windows.**


The universal tar.bz2 archive requires python, mencoder, ffmpeg, PyQt4 and PIL



Please, let me know if it works on any non-Debian sid non-Windows XP SP3 system (the only ones i've tested so far).



Features



**.pla playlist creation and edition for MSC mode! ATM it's a basic implementantion, but I might polish it a bit. These playlists can have files from both the internal memory and the µSD. Thanks to Dunny for providing me with all the information I needed about the .pla/.pla.refs file format :smileywink:**



**Video batch conversion capability, with advanced customizable options, and video thumbnail generation (.thm file) and huge input format support**



**Image batch conversion & resizing, in order to be displayable and fit the fuze's screen size, with huge input format support**



**Fully translated into 3 languages (english, spanish, catalan). If you would like your language supported, read the end of the post**



**Crossplatform: works on all major platforms, taking native look and feel ( I don't have a mac, so it's not tested on macosx, but it should work. Also, it won't take macosx's look and feel if you use qt4-x11(fink, darwinports) instead of qt4-mac)**



**It's free as in free beer and as in free speech.**



Changelog:



--0.5--
**Fixed launch of v4f in OSX** UI enhancements
**Mencoder invoquing code almost rewritten: now it should load just fine mencoder binaries in paths containing whitespace. (Me and my personal war against whitespaces in windows...)** Now v4f remembers last used paths for videos, songs and images
**AMG backend dropped in favour of fuzemux. Code for this based on Struct's fuze.py modification** LOTS of code cleanup.
**Settings in INI files in windows and OSX too**

> --0.4.1--
**Updated copyright and license information in main script** Bugfix: mencoder changing path work-arounded by creating a windows installer (Yes! I finally did it)
**Bugfix: Now unicode paths work on all platforms!** Bugfix: Video thumbnails are now generatod for files with whitespace in its name
**Bugfix: Strange selection behaviour in playlist mode** Bugfix: Now it displays thumbnails correctly
--v0.4--
**Added playlist creation and edition capibilities. The playlists creted with v4f can have files from both internal memory and µSD card. Only tested in MSC.** Added image preview in image conversion
**Some UI redesign.
--v0.3--** Now it makes .thm thumbnails of videos while converting (which adds a dependency on ffmpeg)
**Bugfix: working directory permissions, fix adapted from the one supplied by srtuct in the sansa forums. Only affects the .deb package (and converted packages).** Updated .deb depencies in order to make it installable with the relatively new "wine-unstable" sid package.
**Some little changes in unicode string handling, hoping they would solve some problems, but without any effect so far.** This version won't load settings from previous versions.
--v0.2.1--
**Bugfix: Now supports utf-8 paths in**nix (not on windows for some weird reason)
**Bugfix: Now it refreshes correctly the output path.** Bugfix: Fixed whitespace basename error (you couldn't convert files with whitespace in their name)
--v0.2--
**mencoder command line no more hard-coded: you can now set it in advanced>preferences** Major restructuration of code in fuze.py
**Changed default mencoder options, using the last suggested by ewelot** Now it also supports image conversion!
--v0.1--
**First public release**



-Known issues:



**On OSX unicode filenames and image converting won't work. Don't ask me why, blame apple for shipping a broken custom python.**



> You can convert images while converting videos, as the video conversion will only gray out the "Video" tab. I comment this because it may not be obvious if you don't know it...



Planned features:



- Concurrent video conversion, maybe detecting the number of cores of the cpu?

- More advanced playlist editing. Maybe ordering by tags and so on. It will add dependencies, though.



Every feedback is also welcomed



If you want it translated into your language and would like to help translate it, just tell me, it's a very very easy process!