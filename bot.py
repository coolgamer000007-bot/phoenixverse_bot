import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.environ.get("8482871094:AAHx8sR3QW5YE6VsxgqH1dg7cDOTD1Vb4og")
CHANNEL_USERNAME = "@phoenixverse_07"

APPS = {
    "blurr": {
        "file_id": "BQACAgUAAxkBAAIBB2me8LGx_9e2yAFgp6Pd8vFIF1UjAAIVIQACx0b5VDFnVS4nU3yvOgQ",
        "caption": "🔥 Blurr Premium Version\n\n✅ All Features Unlocked\n🚀 Enjoy Editing!"
    },
    "capcut": {
        "file_id": "BQACAgUAAxkBAAIBCWme8T2-J-TMBQABD5yjGEAaUkiJowACFyEAAsdG-VTRz_0NypDWyDoE",
        "caption": "🔥 CapCut Pro Version\n\n✅ No Watermark\n🚀 Premium Features Unlocked!"
    },
    "alight": {
        "file_id": "BQACAgUAAxkBAAIBC2me8YYfqhKQMd1qxfInERJsBC_UAAIZIQACx0b5VGnFeqHvG5VFOgQ",
        "caption": "🔥 Alight Motion Premium\n\n✅ All Features Enabled\n🚀 No Watermark!"
    },
    "node": {
        "file_id": "BQACAgUAAxkBAAIBJGmfDAABbYE1FCeFazVC5DRpLgxSJAACsCEAAsdG-VStR7WTMGatdzoE",
        "caption": "🔥 Node App Premium\n\n✅ All Features Unlocked\n🚀 Enjoy Editing!"
    },
    "vmake": {
        "file_id": "BQACAgUAAxkBAAIBJmmfDLVSwF-RmSKzGk6ZBwABaCu34QACsiEAAsdG-VRr4ZQtw2q_8DoE",
        "caption": "🔥 Vmake App Premium\n\n✅ All Features Unlocked\n🚀 Enjoy Editing!"
    }
}

async def is_joined(user_id, context):
    try:
        member = await context.bot.get_chat_member(CHANNEL_USERNAME, user_id)
        return member.status in ["member", "administrator", "creator"]
    except:
        return False

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    args = context.args

    if not args:
        await update.message.reply_text("Use proper link like:\n/start blurr")
        return

    app_name = args[0].lower()

    if app_name not in APPS:
        await update.message.reply_text("App not found.")
        return

    if not await is_joined(user.id, context):
        await update.message.reply_text(
            f"Join our channel first:\nhttps://t.me/{CHANNEL_USERNAME.replace('@','')}"
        )
        return

    app_data = APPS[app_name]

    await context.bot.send_document(
        chat_id=update.effective_chat.id,
        document=app_data["file_id"],
        caption=app_data["caption"]
    )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

PORT = int(os.environ.get("PORT", 10000))

app.run_webhook(
    listen="0.0.0.0",
    port=PORT,
    webhook_url=os.environ.get("RENDER_EXTERNAL_URL")
)