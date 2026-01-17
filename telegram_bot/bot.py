import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "8545631557:AAFgkX0XB_A6o7spK__7Y_NuGgsnwnGGamE"

bot = Bot(token=TOKEN)
dp = Dispatcher()

menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="⭐ Купить звёзды", callback_data="stars")],
        [InlineKeyboardButton(text="🌟 Telegram Premium",
                              callback_data="premium")]
    ]
)


@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(
        "⭐️ **Donyaa Pay — Stars** ⭐️\n\n"
        "🌟 Добро пожаловать!\n"
        "Быстро, безопасно и по приятным ценам 🔝\n\n"
        "💱 Валюта: **сумы / рубли**\n"
        "Выберите раздел 👇",
        reply_markup=menu,
        parse_mode="Markdown"
    )


@dp.callback_query()
async def callbacks(callback: types.CallbackQuery):

    if callback.data == "stars":
        await callback.message.edit_text(
            "⭐ **Звёзды Telegram** ⭐️\n\n"
            "📌 **Актуальные цены:**\n"
            "• 50 ⭐️ — 14 000 сум / ~100 ₽\n"
            "• 75 ⭐️ — 20 000 сум / ~145 ₽\n"
            "• 100 ⭐️ — 24 000 сум / ~170 ₽\n"
            "• 150 ⭐️ — 35 000 сум / ~250 ₽\n"
            "• 175 ⭐️ — 41 000 сум / ~295 ₽\n"
            "• 200 ⭐️ — 46 000 сум / ~330 ₽\n"
            "• 250 ⭐️ — 58 000 сум / ~415 ₽\n"
            "• 350 ⭐️ — 80 000 сум / ~570 ₽\n"
            "• 450 ⭐️ — 102 000 сум / ~730 ₽\n"
            "• 500 ⭐️ — 115 000 сум / ~820 ₽\n"
            "• 750 ⭐️ — 170 000 сум / ~1215 ₽\n"
            "• 1000 ⭐️ — 225 000 сум / ~1600 ₽\n\n"
            "🛍 Оплата: **UZS / RUB**\n"
            "✉️ Покупка: @Nyx1011\n"
            "👍 Отзывы: @Donyaa_Otzivi\n\n"
            "↩️ /start — назад",
            parse_mode="Markdown"
        )

    elif callback.data == "premium":
        await callback.message.edit_text(
            "🌟 **Telegram Premium** 🌟\n\n"
            "📥 **С входом на аккаунт:**\n"
            "• 1 месяц — 45 000 сум / ~320 ₽\n"
            "• 1 год — 320 000 сум / ~2285 ₽\n\n"
            "🛡 **Без входа на аккаунт:**\n"
            "• 3 месяца — 170 000 сум / ~1215 ₽\n"
            "• 6 месяцев — 225 000 сум / ~1600 ₽\n"
            "• 12 месяцев — 430 000 сум / ~3070 ₽\n\n"
            "🚀 Для покупки: @Nyx1011\n"
            "🌃 Отзывы: @Donyaa_Otzivi\n\n"
            "↩️ /start — назад",
            parse_mode="Markdown"
        )

    await callback.answer()


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
