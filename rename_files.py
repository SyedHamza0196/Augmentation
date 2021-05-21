import os

path = './images/train' #set path
i = 1
for filename in os.listdir(path):
    os.rename(os.path.join(path,filename), os.path.join(path,'000'+str(i)+'.jpg'))
    i = i +1