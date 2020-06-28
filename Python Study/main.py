import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import string, os, time
ascii_chars = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'.")
def loadImg(path):
	img = Image.open(path)
	img = np.array(img)
	return img
def genPics(vName):
	picDirPath = './pictures/'+vName+'/'
	charDirPath = './chars/'+vName+'/'
	if not os.path.exists(charDirPath):
		os.makedirs(charDirPath)
	pics = os.listdir(picDirPath)
	pics.sort(key= lambda x:int(x[3:-4]))
	index=0
	for pic in pics:
		print(pic)
		img = loadImg(picDirPath+pic)[:,:,0]
		with open(charDirPath+str(index)+'.txt','w') as f:
			for i in range(img.shape[0]):
				for j in range(img.shape[1]):
					code = img[i][j]
					f.write(ascii_chars[int(code/50)])
					f.write(ascii_chars[int(code/50)])
					f.write(ascii_chars[int(code/50)])

				f.write('\n')
		index = index+1

def show(vName):
	dirPath = './chars/'+vName+'/'
	txts = os.listdir(dirPath)
	txts.sort(key= lambda x:int(x[:-4]))
	first=True
	for txt in txts:
		os.system('cat '+dirPath+txt)
		if first:
			input('')
			first = False
		time.sleep(0.01)
def videoToImgs(vName,revolution='320*180'):
	if not os.path.exists('./pictures/'+vName):
		os.makedirs('./pictures/'+vName)
	os.system('ffmpeg -i original_videos/'+vName+'.mp4 -s '+revolution+' pictures/'+vName+'/out%d.png')
# videoToImgs('ggcfcmd','320*180')
# genPics('ggcfcmd')
show('jntm')



