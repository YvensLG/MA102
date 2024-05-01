def mes(n):
    assert n<=12 and n>=1
    m=''
    if(n==1):
        m='janeiro'
        return m
    if(n==2):
        m='fevereiro'
        return m
    if(n==3):
        m='março'
        return m
    if(n==4):
        m='abril'
        return m
    if(n==5):
        m='maio'
        return m
    if(n==6):
        m='junho'
        return m
    if(n==7):
        m='julho'
        return m
    if(n==8):
        m='agosto'
        return m
    if(n==9):
        m='setembro'
        return m
    if(n==10):
        m='outubro'
        return m
    if(n==11):
        m='novembro'
        return m
    if(n==12):
        m='dezembro'
        return m

def main():
    n = int(input())
    print(mes(n))

main()