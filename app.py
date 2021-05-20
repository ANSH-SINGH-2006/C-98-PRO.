def fileswap():
    x=input("Enter first file's name: ")
    y=input("Enter second file's name: ")

    xx=open(x, 'r')
    yy=open(y, 'r')
    f=xx.read()
    g=yy.read()
    
    ddd=open(x, 'w')
    fff=open(y, 'w')
    ddd.write(g)
    fff.write(f)


fileswap()