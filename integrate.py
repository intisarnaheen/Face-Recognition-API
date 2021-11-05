import cv2
import glob
import pickle
from main.RECOGNITION import RECOG
from maim.embed_save import SAVE_EMBDED

emb =SAVE_EMBDED()
recg=RECOG()

path = "./crop/"

process = input(" What do you want to do recognition or register:")

if process == "recognition":
    image = glob.glob(path+"*")
    for file in image:
        file = cv2.imread(file)
        result=recg.recognition(file)
        print(result)
        if result == 'Unknown':
            process = input(" What do you want to do register if Yes then press y or Y")
            if process  == "Y" or "y":
                ID = input(" Please give a register ID:")
                emb.single_image(file, ID)
            else:
                continue
        else:
            continue


if process == "register":
    train =emb.save_multiple_embed(path)
