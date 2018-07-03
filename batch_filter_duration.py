import os
import shutil
import sys
#root=print("all video num: ",len(res))
#root=sys.argv[1]
#root1=sys.argv[2]
#root2=sys.argv[3]
root='C:/Users/66401/Desktop/thumos_14/temporal_annotations_test'
root2="C:/Users/66401/Desktop/thumos_14/test_durations.txt"
root3="C:/Users/66401/Desktop/thumos_14/filter_test_durations.txt"
fs=os.listdir(root)
res=[]
print(fs)
for f1 in fs:
	path=os.path.join(root,f1)
	print(path)
	if os.path.isfile(path):
		f=open(path,'r')
		while 1:
			lines=f.readlines(5)
			if not lines:
				break
			for line in lines:
				s=line.split()
				res.append(s[0]+'.mp4')
print("all video num: ",len(res))
video_set=set(res)
print("video_set:",video_set)
print("video2copy num",len(video_set))

f=open(root2,'r')
video_duration=f.read()
video_duration_list=video_duration.split()
print("len video_duration:",len(video_duration_list))

new_duration_list=[]
for i in range(len(video_duration_list)):
	if i%2==0 and video_duration_list[i] in video_set:
		new_duration_list.append(video_duration_list[i])
		new_duration_list.append(video_duration_list[i+1])
print("len new_duration_list:",len(new_duration_list))
print(new_duration_list)
with open(root3,'w')as f:
	for i in new_duration_list:
		f.writelines(i)
		#f.write('\n')  
#print(video_duration)
#print("video name: ",video_set)
#for f in video_set:
#	print(root2+f)
#	shutil.copy(root1+f,root2+f)
"""
fl=os.listdir(root)
print(fl)
for fi in fs:
	path=os.path.join(root,fi)
	print(path)
	if os.path.isfile(path):
		f=open(path,encoding='utf-8')
		if f in video_set:
			shutil.copy("C:\\Users\\chenteng\\Desktop\\thumos\\TH14_Temporal_Annotations_Test\\annotations\\annotation\\Ambiguous_test.txt","C:\\Users\\chenteng\\Desktop\\thumos\\TH14_Temporal_Annotations_Test\\annotations\\annotation\\Ambiguous_test1.txt")
"""
