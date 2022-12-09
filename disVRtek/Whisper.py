


import whisper

model = whisper.load_model("base")

# Sesi yükleyin ve Pad/30 saniyeye uyacak şekilde kırpın
audio = whisper.load_audio("disleksi.mp3")
audio = whisper.pad_or_trim(audio)

# log-mel spektrogramı yapın ve modelle aynı cihaza geçin
mel = whisper.log_mel_spectrogram(audio).to(model.device)

# Sözlü dilini tespit edin
_, probs = model.detect_language(mel)
print(f"Detected language: {max(probs, key=probs.get)}")

# Sesi çözün
options = whisper.DecodingOptions()
result = whisper.decode(model, mel, options)
# Tanınan metni yazdırın
print(result.text)
