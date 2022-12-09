import whisper
model = whisper.load_model("base")
result = model.transcribe("Kayıt.m4a")
print(result('text'))