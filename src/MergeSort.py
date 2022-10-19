from time import time

class MergeSort():
    
    def __init__(self, input_arrays):
        '''
        Algoritmo Merge Sort, baseado no pseudo-código do livro seção 2.3.1 A abordagem de divisão e conquista
        '''
        self.input_arrays = input_arrays
        self.list_times = []

    
    def run(self):
        for array in self.input_arrays:
            init_time = time()
            self.sort(array)
            time_elapsed = time() - init_time
            self.list_times.append(time_elapsed)
            print('TIME: ', time_elapsed)


    def merge_sort(self, array, p, q, r):
        pass

    def merge(self):
        pass

    
    def merge(self):
        pass
