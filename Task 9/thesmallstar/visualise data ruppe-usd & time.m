
t = readtable('./EXINUS.csv');
plot(t.DATE,t.EXINUS);
ylabel("value of INR per USD");
xlabel("time");
