from bruteforce import startProgrammeBrute
import time


def main():
    """ Fonction get starting"""

    starTime = time.time()
    startProgrammeBrute()
    endTime = time.time()
    elapsed = (endTime - starTime)
    print(f"Temps d'exécution : {elapsed:.3} s")


if __name__ == "__main__":
    main()
