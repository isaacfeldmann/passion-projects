import whisper
import os

os.environ["FFMPEG_BINARY"] = r"C:\ffmpeg\bin\ffmpeg.exe"

model = whisper.load_model("medium")  # medium or large preferred, small for testing purposes

print('model loaded!')

result = model.transcribe(
    r'harvard.wav',
    language='en',
    task='transcribe',
    condition_on_previous_text=False,
    fp16=False
)

print(result['text'])
