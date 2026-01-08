import replicate, os, uuid, requests
from config import REPLICATE_API_TOKEN

os.environ["REPLICATE_API_TOKEN"]=REPLICATE_API_TOKEN

def generate(prompt):
    out=replicate.run("stability-ai/sdxl",
        input={"prompt":prompt,"num_outputs":3,"width":1280,"height":720})
    files=[]
    for u in out:
        f=f"sdxl_{uuid.uuid4()}.jpg"
        open(f,"wb").write(requests.get(u).content)
        files.append(f)
    return files
