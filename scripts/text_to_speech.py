from gtts import gTTS

text = "This is a sample AI-generated voiceover."
tts = gTTS(text)
tts.save("voiceover.mp3")

print("Voiceover saved as voiceover.mp3")