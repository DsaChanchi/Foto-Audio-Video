from moviepy.editor import *
import pathlib

#JPG+MP3=Video
directorionuevo = pathlib.Path()

#Elección de imagen
image = "cover.jpg"

for inverso in directorionuevo.iterdir():
    if inverso.is_file() and inverso.name.endswith('backwards.mp3'):
        background = AudioFileClip(inverso.name) # Import the audio
        video = ImageClip(image).set_duration(background.duration) # Import the image, create the video and set its duration same as the audio
        video = video.set_audio(background) # Set the audio of the video
        video.write_videofile(inverso.name[:-4]+".mp4", fps=24) # Export the video