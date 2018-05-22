#include <iostream>
#include <cstdio>
#include <opencv2/opencv.hpp>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <unordered_map>
//Ïû³ýÉî¶ÈÍ¼±³¾°
//深度图像背景消除
using namespace std;
using namespace cv;
int main(){
	const int a = 105;
	//IplImage *src = cvLoadImage("E:\\1.jpg", 0);
	Mat Img = imread("E:\\1.jpg");
	Mat grayImg; //   
	cvtColor(Img, grayImg, CV_BGR2GRAY);
	int lmax = 0, lmin = 255, ldelta;
	for (int col = 0; col < grayImg.cols; col++){
		for (int row = 0; row < grayImg.rows; row++){
			int pixel = (int)(*(grayImg.data + grayImg.step[0] * row + grayImg.step[1] * col));
			if (pixel >= lmax){
				lmax = pixel;
			}
			if (pixel <= lmin){
				lmin = pixel;
			}

		}
	}
	ldelta = lmin + a*(lmax - lmin);
	cout << lmin << "  " << lmax << endl;
	cout << "ldelta" << ldelta << endl;
	for (int col = 0; col < grayImg.cols; col++){
		for (int row = 0; row < grayImg.rows; row++){
			int pixel = (int)(*(grayImg.data + grayImg.step[0] * row + grayImg.step[1] * col));
			//if (pixel>0 && pixel<255)cout << pixel << endl;
			if (pixel<=100){
				*(grayImg.data + grayImg.step[0] * row + grayImg.step[1] * col) = 0;
			}
		}
	}
	imshow("....", grayImg);
	cout << "end" << endl;
	waitKey(15);
	system("pause");
}