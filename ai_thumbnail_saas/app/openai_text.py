from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def gen_texts(topic, lang):
    p=f"Generate 5 viral thumbnail texts (max 4 words) in {lang} for {topic}"
    r=client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role":"user","content":p}],
        temperature=0.9
    )
    return [x.strip().upper() for x in r.choices[0].message.content.split("\n") if x.strip()]
