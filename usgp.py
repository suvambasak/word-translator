import matplotlib.pyplot as plt
x = "x = "
y = "y = "
temp=raw_input('Name for X axis  : ')
x=x+temp
temp=raw_input('Name for Y axis : ')
y=y+temp

plt.xlabel(x)
plt.ylabel(y)

size=input('How many point : ')
ax=[0]*size
print "\t<<ENTER VALUE FOR X AXIS>>"
for i in range(size):
            ax[i]=input('Value : ')

ay=[0]*size
print "\t<<ENTER VALUE FOR Y AXIS>>"
for i in range(size):
            ay[i]=input('Value : ')

#print ay
#print '\n\n'
print "processing..."
plt.plot(ax,ay,'ro')
print 'ploting...'
plt.plot(ax,ay)
#print '\n\n'
print '\t<<YOUR GRAPH IS PLOTED ! :D>>'
print '\n'
plt.show()
