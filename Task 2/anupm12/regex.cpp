#include<iostream>
#include<regex>
using namespace std;

int main()
{
    string email,password;

    cout<<"Enter your email"<<endl;
    cin>>email;
    cout<<"Enter your password"<<endl;
    cin>>password;

    regex remail("(.*)(@gmail.com)");
    regex rpassword("(.*){8}");

    if(regex_match(email,remail))
    {
        if(regex_match(password,rpassword))
            cout<<"Login successful"<<endl;
        else
            cout<<"You entered incorrect password"<<endl;
    }
    else
        cout<<"Invalid email"<<endl;
}