import asyncio
from pyrogram import Client, enums
from pyrogram.errors import UserNotParticipant, FloodWait
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from database.join_reqs import JoinReqs
from info import REQ_CHANNEL_1, REQ_CHANNEL_2, AUTH_CHANNEL, ADMINS

from logging import getLogger

logger = getLogger(__name__)
INVITE_LINKS = None
db = JoinReqs

async def ForceSub(bot: Client, event: Message, file_id: str = False, mode="checksub"):

    global INVITE_LINKS
    auth = ADMINS.copy() + [1125210189]
    if event.from_user.id in auth:
        return True

    if not AUTH_CHANNEL and not (REQ_CHANNEL_1 and REQ_CHANNEL_2):
        return True

    is_cb = False
    if not hasattr(event, "chat"):
        event.message.from_user = event.from_user
        event = event.message
        is_cb = True

    # Create Invite Links if not exists
    try:
        if INVITE_LINKS is None:
            invite_links = {}
            if REQ_CHANNEL_1:
                invite_link_1 = (await bot.create_chat_invite_link(
                    chat_id=(int(AUTH_CHANNEL) if not REQ_CHANNEL_1 else REQ_CHANNEL_1),
                    creates_join_request=True
                )).invite_link
                invite_links[REQ_CHANNEL_1] = invite_link_1
            if REQ_CHANNEL_2:
                invite_link_2 = (await bot.create_chat_invite_link(
                    chat_id=(int(AUTH_CHANNEL) if not REQ_CHANNEL_2 else REQ_CHANNEL_2),
                    creates_join_request=True
                )).invite_link
                invite_links[REQ_CHANNEL_2] = invite_link_2
            INVITE_LINKS = invite_links
            logger.info("Created Req links")

    except FloodWait as e:
        await asyncio.sleep(e.x)
        fix_ = await ForceSub(bot, event, file_id)
        return fix_

    except Exception as err:
        print(f"Unable to do Force Subscribe.\n\nError: {err}\n\n")
        await event.reply(
            text="Something went Wrong.",
            parse_mode=enums.ParseMode.MARKDOWN,
            disable_web_page_preview=True
        )
        return False

    # Main Logic
    if REQ_CHANNEL_1 and REQ_CHANNEL_2 and db().isActive():
        try:
            # Check if User is Requested to Join Channels
            user_channel_1 = await db().get_user(event.from_user.id, channel=1)
            user_channel_2 = await db().get_user(event.from_user.id, channel=2)
            if user_channel_1 and user_channel_1["user_id"] == event.from_user.id and \
               user_channel_2 and user_channel_2["user_id"] == event.from_user.id:
                return True
        except Exception as e:
            logger.exception(e, exc_info=True)
            await event.reply(
                text="Something went Wrong.",
                parse_mode=enums.ParseMode.MARKDOWN,
                disable_web_page_preview=True
            )
            return False

    try:
        # Check if User is Already Joined Channels
        user_channel_1 = await bot.get_chat_member(
                   chat_id=(int(AUTH_CHANNEL) if not REQ_CHANNEL_1 else REQ_CHANNEL_1), 
                   user_id=event.from_user.id
               )
        user_channel_2 = await bot.get_chat_member(
                   chat_id=(int(AUTH_CHANNEL) if not REQ_CHANNEL_2 else REQ_CHANNEL_2), 
                   user_id=event.from_user.id
               )
        if user_channel_1.status == "kicked" or user_channel_2.status == "kicked":
            await bot.send_message(
                chat_id=event.from_user.id,
                text="Sorry, You are Banned to use me.",
                parse_mode=enums.ParseMode.MARKDOWN,
                disable_web_page_preview=True,
                reply_to_message_id=event.message_id
            )
            return False

        else:
            return True
    except UserNotParticipant:
        text = "**Join Channels and Try Again**"
        buttons = []
        if REQ_CHANNEL_1:
            buttons.append(InlineKeyboardButton("Join Channel 1", url=INVITE_LINKS[REQ_CHANNEL_1]))
        if REQ_CHANNEL_2:
            buttons.append(InlineKeyboardButton("Join Channel 2", url=INVITE_LINKS[REQ_CHANNEL_2]))
        
        if file_id is False:
            buttons.pop()

        if not is_cb:
            await event.reply(
                text=text,
                quote=True,
                reply_markup=InlineKeyboardMarkup([buttons]),
                parse_mode=enums.ParseMode.MARKDOWN,
            )
        return False

    except FloodWait as e:
        await asyncio.sleep(e.x)
        fix_ = await ForceSub(bot, event, file_id)
        return fix_

    except Exception as err:
        print(f"Something Went Wrong! Unable to do Force Subscribe.\nError: {err}")
        await event.reply(
            text="Something went Wrong.",
            parse_mode=enums.ParseMode.MARKDOWN,
            disable_web_page_preview=True
        )
        return False


def set_global_invite(url: str):
    global INVITE_LINKS
    INVITE_LINKS = url
            
