from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus, ParseMode

import config

from ..logging import LOGGER


class VIP(Client):
    def __init__(self):
        LOGGER(__name__).info(f"بدء تشغيل البوت بنجاح... ")
        super().__init__(
            name="VIPMUSIC",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            max_concurrent_transmissions=7,
        )

    async def start(self):
        await super().start()
        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.username = self.me.username
        self.mention = self.me.mention

        try:
            await self.send_message(
                chat_id=config.LOGGER_ID,
                text=f"<u><b>» {self.mention} تم تشغيل بوت :</b><u>\n\nايدي البوت : <code>{self.id}</code>\nاسم البوت : {self.name}\nيوزر البوت : @{self.username}",
            )
        except (errors.ChannelInvalid, errors.PeerIdInvalid):
            LOGGER(__name__).error(
                "قم برفع البوت مشرف في الكروب او القناة، وقم بتشغيل مكالمه صوتيه. "
            )
            
        except Exception as ex:
            LOGGER(__name__).error(
                f"لا يستطيع البوت من الوصول للمجموعه او القناة.\n  بسبب : {type(ex).__name__}."
            )
            

        a = await self.get_chat_member(config.LOGGER_ID, self.id)
        if a.status != ChatMemberStatus.ADMINISTRATOR:
            LOGGER(__name__).error(
                "من فضلك قم برفع البوت مشرف في الكروب والقناة وتأكد من تشغيل المكالمه الصوتيه."
            )
            
        LOGGER(__name__).info(f"بدء تشغيل البوت {self.name}")

    async def stop(self):
        await super().stop()
