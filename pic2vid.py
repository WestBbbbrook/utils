import cv2

img_dir="no_gt_1.15.realsort/"
img_dir="3D_1.07_easy_base_sem_indiv_pred_warp_nose_mask_new_loss.color.alldata.realsort/"
img_dir="demo_nomask_gt1/"
img_dir="rs_e1_data123456789.color_flip_no_crop.easy_base_sem_indiv_pred_warp.demo.115.allsize/"
save_path="allsize_nir_fps10.avi"
#fps = 24   #视频帧率
#fourcc = cv2.cv.CV_FOURCC('M','J','P','G')  
videoWriter = cv2.VideoWriter(save_path,cv2.VideoWriter_fourcc(*'MJPG'), 10, (480,640))   #(1360,480)为视频大小
for i in range(51):

    # img = cv2.imread(img_dir+"NIR_"+str(i)+'.png')
    img = cv2.imread(img_dir+"nir_"+str(i)+'.png')
    #img = cv2.imread(img_dir+"rgb_"+str(i)+'.png')
    print("img shape:",img.shape)
#    cv2.imshow('img', img12)
#    cv2.waitKey(1000/int(fps))
    videoWriter.write(img)
videoWriter.release()