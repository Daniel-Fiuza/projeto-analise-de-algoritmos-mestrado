from src.MergeSort import MergeSort
from src.InsertionSort import InsertionSort
from time import time

class MergeSortAdapted(MergeSort, InsertionSort):
    
    def __init__(self, limit_size):
        '''
        Algoritmo Merge Sort Adaptado para utilizar o Insertion Sort em entradas Pequenas.
        Neste caso, como é apenas uma variação da Merge Sort, será aproveitada a sua implementação herdando sua classe e
        sobrescrevendo apenas o método do caso base para incorporar o InsertionSort.
        Nota-se que há um atributo a mais na construção da classe denominado limit_size que define o valor do
        tamanho limite de um array para o qual será utilizado o algoritmo InsertionSort.
        '''
        self.limit_size = limit_size
        super().__init__()

    
    def run(self, input_arrays):
        length_of_array = len(input_arrays)
        init_time = 0

        if length_of_array < self.limit_size:
            init_time = time()
            self.sort(input_arrays)
        else:
            init_time = time()
            self.merge_sort(input_arrays, 0, length_of_array-1)
        
        time_elapsed = time() - init_time
        self.list_times.append(time_elapsed)
        self.steps += 1
        print(f'[{self.class_name}]: STEP {self.steps} - TIME ELAPSED: {time_elapsed}')