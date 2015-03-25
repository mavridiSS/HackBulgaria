#include<iostream>
#include<vector>
#include<iomanip>
#include<math.h>
using namespace std;
float fill_tetrahedron(int num)
{
	
	float cubicToLiter=0.001;
	float liters=((pow(num,3)*sqrt(2))/12)*cubicToLiter;
	return liters;
}
int main()
{
	cout<<fill_tetrahedron(100);
	return 0;
}
