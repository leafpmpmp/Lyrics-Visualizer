# Lyrics Visualizer(Prototype)
### This is a prototype, and may not work well.

## Pre Requirements
1. Python 3 (**Python 2 may not work**)

To check your python version
```
python
```
2. simpleaudio

To install
```
pip install simpleaudio
```

## Usage
1. Variables

Open the python script with any IDE, and you should see these at the top of the file
```
###Things should be changed across different songs###
sound = "sound.wav"
beats_per_bar = 4
bpm = 130.5
audio_offset = 0 #(second)
bar_line = '!'
wait = '$' #(second)
#####################################################
```
2. Lyrics

Replace the example lyrics with yours, and follow the guide line:

1. Add a `bar_line` between every bar segment, e.g:
```
Fill in my data
!Parameters INITIALISATION
```
2. For long breaks, specify it with `wait`, followed by `number of bar segments`, and **at least 1 character**, otherwise the break won't work. e.g
```
!$8Test lyrics
```
3. Add a `bar_line` at the end of your lyrics(**and so should you in actual music composing**), or it may cause an error.
4. Of course you can use colorama to decorate your lyrics
## Credits and notes
1. The example lyrics are from [Mili - world.execute(me);](https://www.youtube.com/watch?v=ESx_hy1n7HA), they do not belong to me. For the same reason, I shall not provide the sound file for this example, prepare yours.
2. The idea of this came from this video [world.execute(me); but in python3](https://www.youtube.com/watch?v=OnWktOJHrjQ), but there should be plenty of other videos doing similiar things.
