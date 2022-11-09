from time import time

class InsertionSort():
    
    def __init__(self):
        '''
        Algoritmo Insertion Sort, baseado no pseudo-código do livro seção 2.1 Ordenação por Inserção
        '''
        self.class_name = self.__class__.__name__
        self.steps = 0
        self.list_times = []
        self.mean_times = []


    def run(self, input_arrays):
        init_time = time()

        self.sort(input_arrays)
        
        time_elapsed = time() - init_time
        self.list_times.append(time_elapsed)
        self.steps += 1
        print(f'[{self.class_name}]: STEP {self.steps} - TIME ELAPSED: {time_elapsed}')


    def calculate_mean_times(self):
        self.mean_times.append((sum(self.list_times) / len(self.list_times)))
        self.list_times = []


    @classmethod
    def sort(self, array):
        for j in range(1, len(array)):
            key = array[j]
            i = j - 1
            while i >= 0 and array[i] > key:
                array[i + 1] = array[i]
                i -= 1
            array[i + 1] = key