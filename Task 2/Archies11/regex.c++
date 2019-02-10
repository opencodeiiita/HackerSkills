#include<iostream>
#include<regex>
using namespace std;
int main()
{
  string username,password;
  cout<<"USERNAME:";
  cin>>username;
  cout<<endl<<"PASSWORD:";
  cin>>password;
  regex x("(.*)(@gmail.com)");
  if ( regex_match(username, x) )
        cout << "Valid username"<<endl;
  else
        cout<< "Invalid username"<<endl;
  if ( password.length()>8 )
        cout<< "Valid password"<<endl;
  else
        cout<< "Invalid password"<<endl;
  return 0; 
}
