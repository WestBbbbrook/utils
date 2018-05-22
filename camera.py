#-*- coding: utf-8 -*-

import cv2
import sys
import os
#from PIL import Image

#fourcc = cv2.VideoWriter_fourcc(*"CVID")
#fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
fourcc = cv2.cv.CV_FOURCC('m', 'p', '4', 'v')
angle = 'middle'

def CatchUsbVideo(window_name, menu, video_idx):
    arg1 = os.getcwd()+'//'+'Head//' + str(angle) + '//' + str(menu) + '//'
    out = cv2.VideoWriter(arg1+ str(video_idx) + '.avi', fourcc, 7, (1280, 720))

    cv2.namedWindow(window_name)
    
    #视频来源,来自USB摄像头camera_idx:如0,1,2
    cap = cv2.VideoCapture(1) 
    cap.set(3,1280) # 视频每一帧的宽 CV_CAP_PROP_FRAME_WIDTH = 3
    cap.set(4,720) # 视频每一帧的高 CV_CAP_PROP_FRAME_HEIGHT = 4
    cap.set(7,30) # 视频的帧数 CV_CAP_PROP_FRAME_COUNT = 7   
    while cap.isOpened(): # 循环读取每一帧
        ok, frame = cap.read() #读取一帧数据
        if not ok:            
            break                    
                        
        #显示图像并等待10毫秒按键输入，输入‘q’退出程序
        cv2.imshow(window_name, frame)
        # 保存视频
        frame = cv2.flip(frame, 1)  # 在帧上进行操作1
        
        out.write(frame)  # 保存视频1  

        c = cv2.waitKey(10)
        if c & 0xFF == ord('q'):
            break        
    
    #释放摄像头并销毁所有窗口
    cap.release()
    out.release()
    cv2.destroyAllWindows() 


def Load_path(menu):
    if not os.path.exists(os.getcwd()+'//'+'Head//'):
        os.makedirs(os.getcwd()+'//'+'Head//')
    if not os.path.exists(os.getcwd()+'//'+'Head//' + str(angle) + '//'):
        os.makedirs(os.getcwd()+'//'+'Head//' + str(angle) + '//')
    if not os.path.exists(os.getcwd()+'//'+'Head//' + str(angle) + '//' + str(menu) + '//'):
        os.makedirs(os.getcwd()+'//'+'Head//' + str(angle) + '//' + str(menu) + '//')


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage:%s camera_id\r\n" % (sys.argv[0]))
    else:
        Load_path(int(sys.argv[1]))
        CatchUsbVideo("Camera 1", int(sys.argv[1]), sys.argv[2])