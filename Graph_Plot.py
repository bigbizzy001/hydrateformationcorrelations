import math
import matplotlib.pyplot as plt
import numpy as np


from Correlations import HFCorrelations

models = HFCorrelations()


def get_xy(model):
    x, y = [], []
    for i in range(len(model)):
        x.append(model[i][0])
        y.append(model[i][1])
    return x, y


def hammerschmidt_correlation():
    hammer = models.hammerschmidt(1, 200)
    x, y = get_xy(hammer)

    plt.plot(x, y, color='c')
    plt.title('Hammerschmidt Correlation')
    plt.xlabel('Temperature 0F')
    plt.ylabel('Pressure, psia')
    plt.grid(True, lw=0.5, c='k')
    plt.show()


def bahadori_and_vuthaluru():
    hammer = models.bahadori_and_vuthaluru(1, 200, 0.8)
    x, y = get_xy(hammer)

    plt.plot(x, y, color='c')
    plt.title('Bahadori and Vuthaluru Correlation')
    plt.xlabel('Temperature 0F')
    plt.ylabel('Pressure, psia')
    plt.grid(True, lw=0.5, c='k')
    plt.show()


def towler_and_mokhatab():
    hammer = models.towler_and_mokhatab(1, 200, 0.8)
    x, y = get_xy(hammer)

    plt.plot(x, y, color='c')
    plt.title('Towler and Mokhatab Correlation')
    plt.xlabel('Temperature 0F')
    plt.ylabel('Pressure, psia')
    plt.grid(True, lw=0.5, c='k')
    plt.show()


def berge():
    hammer = models.berge(1, 200, 0.8)
    x, y = get_xy(hammer)

    plt.plot(x, y, color='c')
    plt.title('Berge Correlation')
    plt.xlabel('Temperature, 0F')
    plt.ylabel('Pressure, psia')
    plt.grid(True, lw=0.5, c='k')
    plt.show()


def holder_et_al():
    hammer = models.holder_et_al(1, 200)
    x, y = get_xy(hammer)

    plt.plot(x, y, color='c')
    plt.title('Holder et al. Correlation')
    plt.xlabel('Temperature, 0F')
    plt.ylabel('Pressure, psia')
    plt.grid(True, lw=0.5, c='k')
    plt.show()


def motiee():
    hammer = models.motiee(1, 200, 0.8)
    x, y = get_xy(hammer)

    plt.plot(x, y, color='c')
    plt.title('Motiee Correlation')
    plt.xlabel('Temperature, 0F')
    plt.ylabel('Pressure, psia')
    plt.grid(True, lw=0.5, c='k')
    plt.show()


def aut():
    hammer = models.aut(1, 200, 0.8)
    x, y = get_xy(hammer)

    plt.plot(x, y, color='c')
    plt.title('Aut Correlation')
    plt.xlabel('Temperature, 0F')
    plt.ylabel('Pressure, psia')
    plt.grid(True, lw=0.5, c='k')
    plt.show()


def kobayashi_et_al():
    hammer = models.kobayashi_et_al(1, 200, 0.8)
    x, y = get_xy(hammer)

    plt.plot(x, y, color='c')
    plt.title('Kobayashi et al. Correlation')
    plt.xlabel('Temperature, 0F')
    plt.ylabel('Pressure, psia')
    plt.grid(True, lw=0.5, c='k')
    plt.show()



def combined_plots():
    hammer = models.hammerschmidt(1, 200)
    koba = models.kobayashi_et_al(1, 200, 0.8)
    aut = models.aut(1, 200, 0.8)
    mot = models.motiee(1, 200, 0.8)
    hold = models.holder_et_al(1, 200)
    berg = models.berge(1, 200, 0.8)
    tow = models.towler_and_mokhatab(1, 200, 0.8)
    bv = models.bahadori_and_vuthaluru(1, 200, 0.8)

    xha, yha = get_xy(hammer)
    xk, yk = get_xy(koba)
    xa, ya = get_xy(aut)
    xm, ym = get_xy(mot)
    xh, yh = get_xy(hold)
    xb, yb = get_xy(berg)
    xw, yw = get_xy(tow)
    xv, yv = get_xy(bv)

    plt.plot(xha, yha, color='b', label='hammer')
    plt.plot(xk, yk, color='g', label='Koba')
    plt.plot(xa, ya, color='r', label='Aut')
    plt.plot(xm, ym, color='c', label='Mot')
    plt.plot(xh, yh, color='m', label='Holders')
    plt.plot(xb, yb, color='k', label='Berge')
    plt.plot(xw, yw, color='#D4FF00', label='Tow')
    plt.plot(xv, yv, color='#6B3E3E', label='Bahadori')
    plt.title('Combined Correlation')
    plt.xlabel('Temperature, 0F')
    plt.ylabel('Pressure, psia')
    plt.grid(True, lw=0.5, c='k')
    plt.legend()
    plt.show()


# hammerschmidt_correlation()
# bahadori_and_vuthaluru()
# towler_and_mokhatab()
# berge()
# holder_et_al()
# motiee()
# aut()
# kobayashi_et_al()
combined_plots()