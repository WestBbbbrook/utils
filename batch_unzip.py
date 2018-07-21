# -*- coding:utf-
import os
import shutil
import sys
from zipfile import ZipFile
#root=sys.argv[1] #
#root1=sys.argv[2]#
root='/home/ct/myfile/data/THUMOS14/val_frame'
save_root='/home/ct/myfile/data/THUMOS14/val_frame_unzip/'
#root='C:\\Users\\chenteng\\Desktop\\thumos\\annotation'
#root2="C:\\Users\\chenteng\\Desktop\\thumos\\TH14_Temporal_Annotations_Test\\annotations\\annotation"
fs=os.listdir(root)
#print(fs)
for fi in fs:
	path=os.path.join(root,fi)
	#print(path)
	fs1=os.listdir(path)
	for fj in fs1:
		f=os.path.join(path+"/"+fj)
		print(f)
		print("path",path)
		with ZipFile(f,'r')as zip:
			#zip.printdir()
			save_dir=os.path.join(save_root+path.split("/")[-1])
			print("save dir: ",save_dir)
                        if not os.path.exists(save_dir):
				os.mkdir(save_dir)
                        os.chdir(save_dir)
			#os.chdir("E:\\test_frame\\aa")
			print('Extracting all the files now...')
			zip.extractall()
			print(f+" Done!")
