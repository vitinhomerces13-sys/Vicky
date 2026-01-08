import re
def detect_language(t):
    if re.search(r'[\u0900-\u097F]', t): return "Hindi"
    if any(w in t.lower() for w in ["kya","kyu","kaise","hai"]): return "Hinglish"
    return "English"
