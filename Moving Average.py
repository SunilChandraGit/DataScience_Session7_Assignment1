#initilaize list of numbers
li=[3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150]

#variable for storing average for each moving average
avg=0;

#initialize window, number of numbers whose average should be taken at a time
window=3

#print the header
print('Sr.No.'+'\t'+'Participating Numbers'+ '\t'*(window-2) +'Average')
print('-'*8*(window+2))

#loop till n-k+1 element
for i in range(len(li)-window+1):
    #print the moving average serial number
    print(' '+str(i+1), end='\t')
    
    #initialize average to 0
    avg=0
    
    #loop and add next window number of items
    for j in range(window):
        avg=avg+li[j+i]
        print(li[j+i], end='\t')
        
    #print the average over each iteration
    print("{:3.2f}".format(avg/window))