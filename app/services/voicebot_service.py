import numpy as np
import re
import soundfile as sf
from kokoro import KPipeline


def _process_text(text: str) -> str:
    """Prepare LLM output for text-to-speech"""
    # Replace "#[##] text" with "**text...**"
    text = re.sub(r"#+ (.*?)\n", r"**\1...**", text)

    # Replace "**text**" with "[text](+2)"
    text = re.sub(r"\*\*(.*?)\*\*", r"[\1](+2)", text)
    # Replace "*text*"" with "[text](+1)"
    text = re.sub(r"\*(.*?)\*", r"[\1](+1)", text)

    text = text.replace("\n", " ")
    return text


def _lang_code(kokoro_voice: str) -> str:
    return kokoro_voice[0]


class VoiceBotService:
    def __init__(self, kokoro_voice: str, output_file: str):
        self._kokoro_voice = kokoro_voice
        self._output_file = output_file

    def generate_audio(self, text: str) -> None:
        """Generate lecture audio from text using Kokoro"""
        text = _process_text(text)

        pipeline = KPipeline(lang_code=_lang_code(self._kokoro_voice))
        generator = pipeline(text, voice=self._kokoro_voice)

        all_audio = []
        for i, (gs, ps, audio) in enumerate(generator):
            all_audio.append(audio)  # Collect all audio chunks
        final_audio = np.concatenate(all_audio, axis=0)

        sf.write(self._output_file, final_audio, 24000)
