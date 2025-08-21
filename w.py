import whisper
path=r"C:\Users\DELL\Desktop\open_notebook\audiotwo.mp3"
model = whisper.load_model("tiny")
result = model.transcribe(path)
print(result["text"])