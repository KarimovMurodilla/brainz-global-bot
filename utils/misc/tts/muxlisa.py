import aiohttp
from pathlib import Path

from loader import db


class Muxlisa:
    def __init__(self):
        self.__api = "https://api.muxlisa.uz/v1/tts/?text="
        self.__dir = Path(__file__).resolve().parent / 'audio_results'

    async def generate_file_name(self, message):
        audio = await db.get_audio(message.chat.id)
        audio_len = len(audio)
        file_name = f"{message.chat.title}_{audio_len}"

        return file_name
    
    async def text_to_speech(self, text, message):
        url = self.__api + text
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                audio_file_bytes = await resp.content.read()

            file_name = await self.generate_file_name(message)
            dist = self.__dir / f'{file_name}.mp3'
            with open(dist, 'wb') as f:
                f.write(audio_file_bytes)
        
        return dist