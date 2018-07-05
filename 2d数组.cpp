#include <iostream>
using namespace std;
int main() {
	int n2Arr[][5]={{1,2},{3,4}};
	int n2Arr2[3][5]={{1,2},{3,4}};
    int m,n;
    cin>>m>>n;
    int **ary=new int*[m];
    for(int i=0;i<m;++i){
    	ary[i]=new int[n];
	}
	for(int i=0;i<m;++i){
		for(int j=0;j<n;++j){
			ary[i][j]=i*n+j;
		}
	}
	for(int i=0;i<m;++i){
		for(int j=0;j<n;++j){
			cout<<ary[i][j]<<" ";
		}
		cout<<endl;
	}
	for(int i=0;i<m;++i){
		delete[]ary[i];
	}
	delete[]ary;
    return 0;
}
