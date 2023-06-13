from bruteforce import startProgrammBrute
from optimized import startProgrammOptimized
import time


def main():
    """ Fonction get starting"""

    starTime = time.time()
    
    #startProgrammBrute()
    startProgrammOptimized()

    endTime = time.time()
    theTime = (endTime - starTime)
    print(f"Temps d'exécution : {theTime:.3} s")


if __name__ == "__main__":
    main()
