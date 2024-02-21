from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input="Appu mama Gappu mama enna panringo, Appu mama Gappu mama enna panra head. Appu mama Gappu mama enna panringo, Appu mama Gappu mama enna panra head. Appu mama Gappu mama enna panringo, Appu mama Gappu mama enna panra head.  "
    #input="Pith siks, Pith siks, Pith siks, Pith siks, Pith siks, Pith siks, Pith siks, Pith siks, Pith siks, Pith siks, Pith siks, Pith siks, Pith siks"
    #input="ishika mika dika, ishika mika dika, ishika mika dika, ishika mika dika, ishika mika dika, ishika mika dika, ishika mika dika, ishika mika dika, ishana "
)

response.stream_to_file(speech_file_path)
