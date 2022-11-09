from time import time

class InsertionSort():
    
    def __init__(self, input_arrays):
        '''
        Algoritmo Insertion Sort, baseado no pseudo-código do livro seção 2.1 Ordenação por Inserção
        '''
        self.class_name = self.__class__.__name__
        self.steps = 0
        self.input_arrays = input_arrays
        self.list_times = []


    def run(self):
        for array in self.input_arrays:
            init_time = time()
            self.sort(array)
            time_elapsed = time() - init_time
            self.list_times.append(time_elapsed)
            self.steps += 1
            print(f'[{self.class_name}]: STEP {self.steps} OF {len(self.input_arrays)} - TIME ELAPSED: {time_elapsed}')


    @classmethod
    def sort(self, array):
        for j in range(1, len(array)):
            # print('j: ',j,' len: ',len(array)+ 1,' val:',array[j])
            key = array[j]
            i = j - 1
            while i >= 0 and array[i] > key:
                array[i + 1] = array[i]
                i -= 1
            array[i + 1] = key