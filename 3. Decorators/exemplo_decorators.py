import time

def meu_decorator(func):
    def wrapper(*args, **kwargs):
        print(f'[LOG] Args: {args}')
        print(f'[LOG] Kwargs: {kwargs}')
        inicio = time.time()
        response = func(*args, **kwargs)
        print(f'[LOG] A duração foi de: {time.time() - inicio}')
        return response
    return wrapper

@meu_decorator
def funcao_1(a, b):
    time.sleep(5)

@meu_decorator
def funcao_2():
    time.sleep(5)

@meu_decorator
def funcao_3():
    time.sleep(5)

@meu_decorator
def funcao_4():
    time.sleep(5)

@meu_decorator
def funcao_5():
    time.sleep(5)


funcao_1(a=1, b=2)