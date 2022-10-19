from random import randint, uniform

class Utils():

    @staticmethod
    def generate_random_arrays(num_of_arrays=10):
        size_of_arrays = [randint(10, 10000) for _ in range(num_of_arrays)]
        multiplier = randint(10, 20)
        size_of_input_arrays = [ size * multiplier for size in size_of_arrays]
        matrix_of_arrays = []

        print('TAMANHO DE ARRAYS ESCOLHIDOS INICIALMENTE: ', size_of_arrays)
        print('FATOR M GERADO ALEATORIAMENTE TAL QUE 10 ≤ m ≤ 20: ', multiplier)
        print('TAMANHO DE CADA VETOR DE ENTRADA: ', size_of_input_arrays)


        for size in size_of_input_arrays:
            list_arrays = [uniform(-1,1)*2*size for _ in range(size)]
            matrix_of_arrays.append(list_arrays)

        return matrix_of_arrays