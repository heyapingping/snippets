# Telegram file copying using pyrogram
# pip3 install pyrogram
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import asyncio


FROM = -1482836524
TO = -1428358122
PYRO_SESSION = "BQAVqzFiPAyqnwgkoZsKB9yhIrpBw1kiik3nCVBvVh2gbN5aXhfKJLft5pIeM0xLgyxpZHeSna3WV1_y6shLES8GkYEs45F1dhB6ntu6AKi_GwplLPi0WN5A-vfFOQ3nSvGoyMCHRq4vJsmHAQvlM8-2z5Px1E_6QHlijJ_0kHRWpmXlub9ASQjbBknXvib8gCaQFK-t0ZoovEbsur2XhEtlxpKXGch8LTEJsGG70eGq01xs6bAUBoUi9IyVs9kPinwZi6P11D8cKQRMy3QntpTTci6ZyI33iayBn4RDW_593s5qt4ORzinwtbEBKJk6YcCzCBbc4dSn929AleAKm0qONdr9jAA"
API_ID = 3994297
API_HASH = "8273eb7b5b2dcf60a6ecb9eba727c473"

user = Client(
    PYRO_SESSION,
    api_id=API_ID,
    api_hash=API_HASH,
)

@user.on_message(filters.command('copy') & filters.me)
async def copy_files(c, m):
    async for msg in c.iter_history(FROM):
        try:
            if msg.document:
                await msg.copy(TO)
        except FloodWait as sec:
            await asyncio.sleep(sec)
  
user.run()
