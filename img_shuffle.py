import os
import shutil

target_path = r'D:\Play\Pictures\漫画'
img_path = r'.\data'
# manga_dict = {28386:'cae2883a%2C1660312044%2Ca1bb4%2A21'}
manga_dict = {28386:'更衣人偶坠入爱河'}
def shuffle(path, target_path):
    dirname,name = os.path.split(target_path)
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    shutil.copy(path,target_path)


comicID = 28386
manga_name = manga_dict.get(comicID)
for root,dirs,files in os.walk(img_path):
    for file in files:
        cha,ind = file.split('_')
        fn = os.path.join(root,file)
        new_fn = os.path.join(target_path,manga_name,cha.zfill(4),ind.zfill(7))
        shuffle(fn,new_fn)


