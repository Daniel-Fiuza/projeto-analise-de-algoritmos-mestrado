from random import randint, uniform

class Utils():

    def __init__(self) -> None:
        self.number_of_executions = randint(10, 20)
        self.num_of_arrays = None
        self.size_of_input_arrays = None

    def generate_random_arrays(self, num_of_arrays=10):
        # size_of_arrays = [randint(10, 10000) for _ in range(num_of_arrays)]
        size_of_arrays = [randint(10, 100) for _ in range(num_of_arrays)]
        self.size_of_input_arrays = [ size * self.number_of_executions for size in size_of_arrays]
        self.matrix_of_arrays = []

        print('TAMANHO DE ARRAYS ESCOLHIDOS INICIALMENTE: ', size_of_arrays)
        print('FATOR M GERADO ALEATORIAMENTE TAL QUE 10 ≤ m ≤ 20: ', self.number_of_executions)
        print('TAMANHO DE CADA VETOR DE ENTRADA: ', self.size_of_input_arrays)


        for size in self.size_of_input_arrays:
            list_arrays = [uniform(-1,1)*2*size for _ in range(size)]
            self.matrix_of_arrays.append(list_arrays)

        return self.matrix_of_arrays