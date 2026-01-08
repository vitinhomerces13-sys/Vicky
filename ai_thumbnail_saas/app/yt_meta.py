from openai import OpenAI
from config import OPENAI_API_KEY
client = OpenAI(api_key=OPENAI_API_KEY)

def yt_meta(topic, lang):
    p=f"Create YouTube title + description in {lang} for {topic}"
    r=client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role":"user","content":p}],
        temperature=0.7
    )
    return r.choices[0].message.content
