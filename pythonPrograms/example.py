'''durga='Durga Prasad is a good boy'
print((durga+' ')*3)
print('nice' not in 'Prasad is a nice person')
print(9^8)'''

a,b=input('Enter x,y values').split(',')
x=int(a)
y=int(b)
if x>=y:
    print('{} is greater than {}'.format(x,y))
else:
    print('{} is lesser than {}'.format(x,y))