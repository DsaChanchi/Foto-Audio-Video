from moviepy.editor import *

# Keyboard Audio
print("Give Audio:")
audio = input()

# Keyboard Image
print("Give image:")
image = input()

# Import the audio
background = AudioFileClip(audio+".mp3")

# Import the image, create the video and set its duration same as the audio
video = ImageClip(image+".jpg").set_duration(background.duration)

# Set the audio of the video
video = video.set_audio(background)

# Export the video
video.write_videofile(audio+".mp4", fps=24)
