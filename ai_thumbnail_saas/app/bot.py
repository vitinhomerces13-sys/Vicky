from aiogram import Bot,Dispatcher,types
from config import BOT_TOKEN
from database import get_user,add_credits,deduct_credit
from language_detect import detect_language
from openai_text import gen_texts
from nano_prompt import nano_prompt
from sdxl_generate import generate
from ctr_score import best
from image_utils import text_overlay
from yt_meta import yt_meta
import asyncio,uuid,os

bot=Bot(BOT_TOKEN)
dp=Dispatcher()
state={}

@dp.message(commands=["start"])
async def s(m):
    c=get_user(m.from_user.id)
    await m.answer(f"Credits: {c}\nSend topic")

@dp.message()
async def f(m):
    u=m.from_user.id
    s=state.setdefault(u,{})
    if "topic" not in s:
        s["topic"]=m.text
        s["lang"]=detect_language(m.text)
        s["texts"]=gen_texts(s["topic"],s["lang"])
        await m.answer("\n".join([f"{i+1}. {t}" for i,t in enumerate(s["texts"])]))
        return
    if "text" not in s:
        s["text"]=s["texts"][int(m.text)-1]
        await m.answer("Type PAID")
        return
    if m.text=="PAID":
        deduct_credit(u)
        imgs=generate(nano_prompt(s["topic"],"Gen"))
        b,sc=best(imgs)
        out=f"final_{uuid.uuid4()}.jpg"
        text_overlay(b,s["text"],out)
        await bot.send_photo(u,types.FSInputFile(out))
        await m.answer(yt_meta(s["topic"],s["lang"]))
        for i in imgs+[out]: os.remove(i)
        state.pop(u)

asyncio.run(dp.start_polling(bot))
