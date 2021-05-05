import matplotlib.pyplot as plt

numAtom_M1k = [5,10,20,40,70,100]
czestoscZderzen_M1k = [1.159,1.067,2.286,4.681,10.811,8.662]
sredniaDroga_M1k = [0.14739,0.31980,0.17847,0.12349,0.06761,0.03404]
czestoscZderzen_M3k = [0.548,0.777,1.592, 2.982,5.736,12.768]
sredniaDroga_M3k = [0.87786,0.36533,0.06108,0.16913,0.04472,0.04258]
czestoscZderzen_M500 = [1.111,1.081,0.930,6.222,3.448,11.954]
sredniaDroga_M500 = [0.30156,0.26798,0.28194,0.08782,0.16298,0.06013]
czestoscZderzen_M5k = [0.235,1.229,3.310,4.835,7.968,8.142]
sredniaDroga_M5k = [1.01633,0.34318,0.18602,0.04873,0.04767,0.04115]
plt.plot(numAtom_M1k, czestoscZderzen_M1k)
plt.xlabel("Ilość atomów")
plt.ylabel("Czestosc Zderzeń 1/s")
plt.grid(True)
plt.title("Cześtość Zderzeń-M=1k")
plt.legend()
plt.show()

plt.plot(numAtom_M1k, sredniaDroga_M1k)
plt.xlabel("Ilość atomów")
plt.ylabel("Średnia droga między zderzeniami")
plt.grid(True)
plt.title("Średnia droga między zderzeniami-M=1k")
plt.legend()
plt.show()

plt.plot(numAtom_M1k, czestoscZderzen_M3k)
plt.xlabel("Ilość atomów")
plt.ylabel("Czestosc Zderzeń 1/s")
plt.grid(True)
plt.title("Cześtość Zderzeń-M=3k")
plt.legend()
plt.show()

plt.plot(numAtom_M1k, sredniaDroga_M3k)
plt.xlabel("Ilość atomów")
plt.ylabel("Średnia droga między zderzeniami")
plt.grid(True)
plt.title("Średnia droga między zderzeniami-M=3k")
plt.legend()
plt.show()

plt.plot(numAtom_M1k, czestoscZderzen_M500)
plt.xlabel("Ilość atomów")
plt.ylabel("Czestosc Zderzeń 1/s")
plt.grid(True)
plt.title("Cześtość Zderzeń-M=500")
plt.legend()
plt.show()

plt.plot(numAtom_M1k, sredniaDroga_M500)
plt.xlabel("Ilość atomów")
plt.ylabel("Średnia droga między zderzeniami")
plt.grid(True)
plt.title("Średnia droga między zderzeniami-M=500")
plt.legend()
plt.show()

plt.plot(numAtom_M1k, czestoscZderzen_M5k)
plt.xlabel("Ilość atomów")
plt.ylabel("Czestosc Zderzeń 1/s")
plt.grid(True)
plt.title("Cześtość Zderzeń-M=5k")
plt.legend()
plt.show()

plt.plot(numAtom_M1k, sredniaDroga_M5k)
plt.xlabel("Ilość atomów")
plt.ylabel("Średnia droga między zderzeniami")
plt.grid(True)
plt.title("Średnia droga między zderzeniami-M=5k")
plt.legend()
plt.show()


