    import numpy as np
    import time

    array = []
    print("> Lembre-se que a matriz deve ser quadrada para realizarmos a potenciação <")
    dim = int(input("Insira a dimensão da sua matriz: "))

    array = np.random.randint(10, size=(dim, dim))
    print("Matriz gerada:\n", array)

    m = int(input("Escolha um valor para M [2, 3 ou 4]: "))
    start_time = time.time()
    M = np.linalg.matrix_power(array, m)                            
            
    print(f"Matriz elevada à potência{m}:\n", M)
            
    end_time = time.time()
    execution_time = end_time - start_time
    print("\nO tempo de execução foi: ", execution_time)
