from cmath import sqrt
import matplotlib.pyplot as plt
import numpy as np

def kruznica(t, o, r):
    d= (t[0] - o[0])**2 + (t[1] - o[1])**2
    D=abs(sqrt(d) - r)

    if d==r**2:
        print ('Točka se nalazi na kružnici')
    elif d<r**2:
        print ('Točka se nalazi unutar kružnice, na udaljenosti %f' % (D))
    elif d>r**2:
        print ('Točka se nalazi izvan kružnice, na udaljenosti %f' % (D))
    
    x=max(abs(o[0]), abs(o[1]))
    plt.axis([o[0]-r-x, o[0]+r+x, o[1]-r-x, o[1]+r+x])
    plt.axis("equal")
    q=plt.Circle((o[0], o[1]), r, fill=False)
    w=plt.Circle((t[0], t[1]), r*0.02)
    plt.gca().add_artist(q)
    plt.gca().add_artist(w)
    
    if input("Ako graf želite prikazati na ekranu, unesite y: ")=='y':
        plt.show()
    elif input("Ako graf želite spremiti u pdf formatu, unesite y: ")=='y':
        plt.savefig(input("Odaberite ime datoteke: "), format="pdf", bbox_inches="tight")

while True:
    try:
        print ('Točka')
        T=[float(input('Unesite x1: ')), float(input('Unesite y1: '))]
        print ('Središte kružnice')
        O=[float(input('Unesite x2: ')), float(input('Unesite y2: '))]
        R=abs(float(input('Unesite polumjer kružnice:')))
        kruznica(T, O, R)
        break;
    except ValueError:
        print ('Pokušajte ponovno')