import json, os
DB="data/ctr_memory.json"
if not os.path.exists(DB): open(DB,"w").write("{}")

def save(txt, good=True):
    d=json.load(open(DB))
    s=d.get(txt,{"w":0,"l":0})
    s["w"]+=1 if good else 0
    s["l"]+=0 if good else 1
    d[txt]=s
    json.dump(d,open(DB,"w"))
