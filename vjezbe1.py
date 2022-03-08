from xml.sax.xmlreader import InputSource
import matplotlib.pyplot as plt

def pravac(A, B):
    a=(B[1]-A[1])/(B[0]-A[0])
    b=A[1]-a*A[0]
    
    C=[A[0], B[0]]
    D=[A[1], B[1]]
    plt.plot(C, D, marker='D')
    
    if a==int(a):
        a=int(a)
    if b==int(b):
        b=int(b)
    if a==1:
        a=""
    if b<0:
        print ('y = '+str(a)+'x - '+str(abs(b)))
    elif b==0:
        print('y = '+str(a)+'x')
    else:
        print('y = '+str(a)+'x + '+str(b))
    if input("Ako graf želite prikazati na ekranu, unesite y: ")=='y':
        plt.show()
    elif input("Ako graf želite spremiti u pdf formatu, unesite y: ")=='y':
        plt.savefig(input("Odaberite ime datoteke: "), format="pdf", bbox_inches="tight")


while True:
    try:
        T1=[float(input('Unesite x1: ')), float(input('Unesite y1: '))]
        T2=[float(input('Unesite x2: ')), float(input('Unesite y2: '))]
        pravac(T1, T2)
        break;
    except ValueError:
        print ('Pokušajte ponovno')