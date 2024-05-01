for i in range(1, 101):
    if(i%15==0):
        print(f"{i} tic-toc")
    elif(i%3==0):
        print(f"{i} tic")
    elif(i%5==0):
        print(f"{i} toc")
    else:
        print(f"{i} ")