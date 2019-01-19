#include<iostream>
#include<string.h>

using namespace std;

int main(){
 string a,b;
 cout<<"Enter username :"<<endl;
 cin>>a;
 cout<<"Enter password :"<<endl;
 cin>>b;
 int l=b.length();
 int l2=a.length();
 string m="@gmail.com";
 int f=1,c=0;
 for(int i=0;i<l2;i++){
  if(a[i]=='@'){
    c+=1;
   for(int j=i;j<l2;j++){
    if(a[j]!=m[j-i]){
      f=0;
      break;
     }
   }
}
}
 if(f && c)
   cout<<"Valid username"<<endl;
 else
   cout<<"Invalid username"<<endl;
    
if(l<9)
  cout<<"Invalid password"<<endl;
 else
   cout<<"Valid password"<<endl;
}
