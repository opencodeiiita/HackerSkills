filename='gold.csv';
x=readtable(filename);
plot(x.Date,x.Price);
xlabel("Year");
ylabel("Price of Gold");
