#!/usr/bin/python

bacteria = 2
time = 0
death = False
print '> Starting bacteria count:',bacteria
while death != True:
    bacteria = pow(bacteria, 2)
    time += 23
    print '>bacteria count',bacteria,'after',time,'minutes'
    if bacteria >= 7300000:
        death = True
print '> The bacteria count in your body is', bacteria, 'You are now dead :( after', time, 'minutes'
print '> A cure takes 150 minutes and the bacteria will kill you before it is effective'
