import logging

from googlesearch import search
from pyrogram import filters

from SONALI import app
from SafoneAPI import SafoneAPI
from search_engine_parser.core.engines.stackoverflow import \
    Search as StackSearch
from search_engine_parser.core.exceptions import NoResultsFound, NoResultsOrTrafficError


@app.on_message(filters.command(["google", "gle"]))
async def google(bot, message):
    if len(message.command) < 2 and not message.reply_to_message:
        await message.reply_text("Example:\n\n/google lord ram")
        return

    if message.reply_to_message and message.reply_to_message.text:
        user_input = message.reply_to_message.text
    else:
        user_input = " ".join(message.command[1:])
    b = await message.reply_text("Sᴇᴀʀᴄʜɪɴɢ ᴏɴ Gᴏᴏɢʟᴇ....")
    try:
        result = await gsearch.async_search(query)
        keyboard = ikb(
            [
                [
                    (
                        f"{result[0]['titles']}",
                        f"{result[0]['links']}",
                        "url",
                    ),
                ],
                [
                    (
                        f"{result[1]['titles']}",
                        f"{result[1]['links']}",
                        "url",
                    ),
                ],
                [
                    (
                        f"{result[2]['titles']}",
                        f"{result[2]['links']}",
                        "url",
                    ),
                ],
                [
                    (
                        f"{result[3]['titles']}",
                        f"{result[3]['links']}",
                        "url",
                    ),
                ],
                [
                    (
                        f"{result[4]['titles']}",
                        f"{result[4]['links']}",
                        "url",
                    ),
                ],
            ]
        )

        txt = f"ʜᴇʀᴇ ᴀʀᴇ ᴛʜᴇ ʀᴇsᴜʟᴛs ᴏғ ʀǫᴜᴇsᴛᴇᴅ : {query.title()}"
        await to_del.delete()
        await msg.reply_text(txt, reply_markup=keyboard)
        return
    except NoResultsFound:
        await to_del.delete()
        await msg.reply_text("ɴᴏ ʀᴇsᴜʟᴛ ғᴏᴜɴᴅ ᴄᴏʀʀᴇsᴘᴏɴᴅɪɴɢ ᴛᴏ ʏᴏᴜʀ ǫᴜᴇʀʏ")
        return
    except NoResultsOrTrafficError:
        await to_del.delete()
        await msg.reply_text("**ɴᴏ ʀᴇsᴜʟᴛ ғᴏᴜɴᴅ ᴅᴜᴇ ᴛᴏ ᴛᴏᴏ ᴍᴀɴʏ ᴛʀᴀғғɪᴄ")
        return
    except Exception as e:
        await to_del.delete()
        await msg.reply_text(f"sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ :\nʀᴇᴘᴏʀᴛ ᴀᴛ ɪᴛ @PURVI_SUPPORT")
        print(f"error : {e}")
        return


@app.on_message(filters.command(["app", "apps"]))
async def app(bot, message):
    if len(message.command) < 2 and not message.reply_to_message:
        await message.reply_text("Example:\n\n`/app Free Fire`")
        return

    if message.reply_to_message and message.reply_to_message.text:
        user_input = message.reply_to_message.text
    else:
        user_input = " ".join(message.command[1:])
    cbb = await message.reply_text("**Sᴇᴀʀᴄʜɪɴɢ ᴏɴ Pʟᴀʏ Sᴛᴏʀᴇ....**")
    a = await SafoneAPI().apps(user_input, 1)
    b = a["results"][0]
    icon = b["icon"]
    id = b["id"]
    link = b["link"]
    ca = b["description"]
    title = b["title"]
    dev = b["developer"]
    info = f"<b>[ᴛɪᴛʟᴇ : {title}]({link})</b>\n<b>ɪᴅ</b>: <code>{id}</code>\n<b>ᴅᴇᴠᴇʟᴏᴘᴇʀ</b> : {dev}\n<b>ᴅᴇsᴄʀɪᴘᴛɪᴏɴ </b>: {ca}"
    try:
        await message.reply_photo(icon, caption=info)
        await cbb.delete()
    except Exception as e:
        await message.reply_text(e)


__MODULE__ = "Gᴏᴏɢʟᴇ"
__HELP__ = """/google [ǫᴜᴇʀʏ] - ᴛᴏ sᴇᴀʀᴄʜ ᴏɴ ɢᴏᴏɢʟᴇ ᴀɴᴅ ɢᴇᴛ ʀᴇsᴜʟᴛs
/app | /apps [ᴀᴘᴘ ɴᴀᴍᴇ] - ᴛᴏ ɢᴇᴛ ᴀᴘᴘ ɪɴғᴏ ᴛʜᴀᴛ ᴀᴠᴀɪʟᴀʙʟᴇ ᴏɴ ᴘʟᴀʏsᴛᴏʀᴇ"""


