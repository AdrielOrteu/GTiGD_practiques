import networkx
import random
import typing
import matplotlib


def timer(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print(f"Execution time: {t2 - t1:.6f} seconds")
        return result
    return wrapper


def task_1():
    
    def simulate_coincidence(average, deviation):
        pass
    
    def how_many_cliques(n, average, deviation):
        pass
    


def task_2():
    n = int(input("Introduce cantidad de números a elegir (n): "))
    m = int(input("Introduce cantidad de números posibles (m): "))

    combinacion = input("Introduce el código: ")
    combinacion = list(map(int, combinacion.split()))
    combinacion.sort()

    intentos = 0
    ganador = []

    while combinacion != ganador:
        ganador = random.sample(range(1, m + 1), n)
        ganador.sort()
        intentos += 1

    print("Has ganado tras {intentos} intentos.")






def task_3():
    pass
task_2()