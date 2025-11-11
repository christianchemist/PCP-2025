while True:
    delta_t = float(input("Was ist Delta T? "))
    peaks = int(input("Anzahl peaks? "))
    wavelength = 0.000000532
    length = 0.09
    beta = (peaks * wavelength)/(2 * length * delta_t)
    print(f"Beta is {beta} \n")
