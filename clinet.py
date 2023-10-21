import discord
import asyncio
from typing import Any
from crawler import start_crawler
import logging

logger = logging.getLogger(__name__)
class Client(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.chennel_id = 1164808092135985193 # update here to change chennel id

    async def on_ready(self):
        logger.info(f'Logged on as {self.user}!')

    async def on_error(self, event_method: str, /, *args: Any, **kwargs: Any) -> None:
        return await super().on_error(event_method, *args, **kwargs)

    async def setup_hook(self) -> None:
        self.bg_task = self.loop.create_task(self.send_scheduled_message())

    async def send_scheduled_message(self):
        await self.wait_until_ready()
        channel = self.get_channel(self.chennel_id)  # 替換為您希望發送消息的頻道的 ID
        logger.info('取得頻道訊息...')
        logger.info(f'頻道名稱: {channel.name}')
        while not self.is_closed():            
            for news in start_crawler():
                logger.info('正在發送訊息...')
                logger.info(news)
                await channel.send(news)  # 替換為您想要發送的消息
            await asyncio.sleep(3600)  # 這個示例每隔一小時發送一次消息