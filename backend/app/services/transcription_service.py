import whisper

model = whisper.load_model("base")


def transcribe_audio(audio_path: str) -> str:
    return model.transcribe(audio_path)["text"]
