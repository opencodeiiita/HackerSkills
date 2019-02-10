clc
clear
close all

x = [-5:0.01:5]
y = x*pi
y = y/4
y = sin(y)
y = 2*y

plot(x,y)
grid on