#include<iostream>
#include<string>
using namespace std;
string caesar_encrypt(string str,int n)
{
	string caesar=str;
	for(int i=0;i<str.length();i++)
	{
		if(islower(str[i]))
		{
			if(isalpha(str[i]+n))
				caesar[i]=str[i]+n;
			else
				caesar[i]=(str[i]+n)-26;
		}
		if(isupper(str[i]))
		{
			if(isalpha(str[i]+n))
				caesar[i]=str[i]+n;
			else
				caesar[i]=(str[i]+n)-26;
		}
	}
	return caesar;
}
int main()
{
	cout<<caesar_encrypt("abc",1);
	return 0;
}
