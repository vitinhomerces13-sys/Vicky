from PIL import Image
import numpy as np

def score(p):
    a=np.array(Image.open(p).convert("L"))
    return (a.mean()/255*20)+(a.std()/128*25)

def best(imgs):
    return max(imgs, key=score), score(max(imgs,key=score))
