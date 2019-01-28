clc
clear
close all

x = [-2:0.1:10]
y = x*pi
y = y/4
y = sin(y)
y = 2*y

plot(x,y)
grid on 