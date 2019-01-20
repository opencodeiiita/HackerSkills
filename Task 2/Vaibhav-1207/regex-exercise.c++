#include<iostream>
#include<regex>

using namespace std;
int main(){
 string a,b;
 cout<<"Enter username :"<<endl;
 cin>>a;
 cout<<"Enter password :"<<endl;
 cin>>b;
 regex c("(.*)(@gmail.com)");
 regex d("(.*){9}");
 if(regex_match(a,c))
  cout<<"Valid username"<<endl;
 else
  cout<<"Invalid username"<<endl;
 if(regex_match(b,d)&&b.length()>8)
  cout<<"Valid password"<<endl;
 else
  cout<<"Invalid password"<<endl;
 }

