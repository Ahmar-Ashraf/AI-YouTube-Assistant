from moviepy.editor import *

audio = AudioFileClip("voiceover.mp3")
image = ImageClip("thumbnail.jpg").set_duration(audio.duration)
video = image.set_audio(audio)

video.write_videofile("final_video.mp4", fps=24)