#include<iostream>
#include<algorithm>
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
int tetrahedron_filled(vector<int> tetrahedrons,int water)
{
	int maxNumberToFill=0;
	float filledWater=0;
	sort(tetrahedrons.begin(),tetrahedrons.end());
	for(int i=0;i<tetrahedrons.size();i++)
	{
		if((int)filledWater<water && fill_tetrahedron(tetrahedrons[i])<=(int)(water-filledWater))
		{
			filledWater+=fill_tetrahedron(tetrahedrons[i]);
			maxNumberToFill++;
		}
	}
	return maxNumberToFill;
}
int main()
{
	vector<int> tetrahedrons;
	tetrahedrons.push_back(100);
	tetrahedrons.push_back(20);
	tetrahedrons.push_back(30);
	cout<<tetrahedron_filled(tetrahedrons,10);
	return 0;
}
