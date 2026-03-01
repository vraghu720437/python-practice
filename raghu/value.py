

#to find the compound inrest
# ci=compound interest
#p=principle ammount(total ammount)
#r=anneal interest
#t=time of revenue
p=int(input('enter the total barrowed ammount:'))
r=float(input('enter the rate of interest per hundred(100):'))
t=float(input('enter the time for revenue:'))
ci=p((1+(r/100))**t)-p
print('compound interest:',ci)