import re

from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import BaseFilter, Command
from aiogram.enums import ChatMemberStatus
from datetime import datetime, time


router = Router()
night_mode_status = {} # Dictionary to store night mode status for each chat


class LinkFilter(BaseFilter):
    """Custom filter to check if a message contains a link."""
    async def __call__(self, message: Message) -> bool:
        return bool(re.search(r"(https?://|t\.me|telegram\.me)", message.text or ""))


async def is_admin(bot, chat_id: int, user_id: int) -> bool:
    """Helper function to check if a user is an admin in the chat."""
    member = await bot.get_chat_member(chat_id, user_id)
    return member.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.CREATOR]

def is_night_time() -> bool:
    """Check if the current time is within the night hours."""
    NIGHT_START = time(0, 0)  # 00:00
    NIGHT_END = time(6, 0)    # 06:00

    now = datetime.now().time()
    return NIGHT_START <= now < NIGHT_END


@router.message(Command("night_mode"))
async def toggle_night_mode(message: Message) -> None:
    """Handler to toggle night mode on/off."""
    if not await is_admin(message.bot, message.chat.id, message.from_user.id):
        await message.reply("Only admins can toggle night mode.")
        return
    
    args = message.text.split()
    if len(args) < 2 or args[1] not in ["on", "off"]:
        await message.reply("Usage: /night_mode on|off")
        return

    if args[1] == "on":
        night_mode_status[message.chat.id] = True
        await message.reply("Night mode enabled. Messages will be deleted during night hours.")
    else:
        night_mode_status[message.chat.id] = False
        await message.reply("Night mode disabled. Messages will not be deleted during night hours.")


@router.message(F.chat.type.in_(["group", "supergroup"]), LinkFilter())
async def links_handler(message: Message) -> None:
    """Handler to delete messages containing links."""
    await message.delete()


@router.message(F.chat.type.in_(["group", "supergroup"]), F.content_type.in_(
    ["photo", "video", "document", "animation"]
))
async def mederate_admin(message: Message, bot) -> None:
    """Handler to delete media from regular users (not admins/owner)."""
    if await is_admin(bot, message.chat.id, message.from_user.id):
        return
    
    await message.delete()


@router.message(F.chat.type.in_(["group", "supergroup"]))
async def night_handler(message: Message) -> None:
    """Handler to delete messages during night hours."""
    chat_id = message.chat.id
    enabled = night_mode_status.get(chat_id, False) # Get night mode status for the chat, default to False

    if not enabled:
        return

    if not is_night_time():
        return
    
    if await is_admin(message.bot, message.chat.id, message.from_user.id):
        return

    await message.delete()