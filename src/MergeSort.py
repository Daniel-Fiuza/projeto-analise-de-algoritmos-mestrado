from time import time
import sys
sys.setrecursionlimit(2000)

class MergeSort():
    
    def __init__(self, input_arrays):
        '''
        Algoritmo Merge Sort, baseado no pseudo-código do livro seção 2.3.1 A abordagem de divisão e conquista
        '''
        self.class_name = self.__class__.__name__
        self.steps = 0
        self.input_arrays = input_arrays
        self.list_times = []

    
    def run(self):
        for array in self.input_arrays:
            length_of_array = len(array)
            init_time = time()
            # print(f'[{self.class_name}]: INITIAL ARRAY: {array}')
            self.merge_sort(array, 0, length_of_array-1)
            # print(f'[{self.class_name}]: FINAL ARRAY: {array}')
            time_elapsed = time() - init_time
            self.list_times.append(time_elapsed)
            self.steps += 1
            print(f'[{self.class_name}]: STEP {self.steps} OF {len(self.input_arrays)} - TIME ELAPSED: {time_elapsed}')


    def merge(self, array, p, q, r):
        n1 = q - p + 1 
        n2 = r - q     
        left_array = [0 for _ in range(n1)]
        right_array = [0 for _ in range(n2)]
        
        for i in range(0, n1):
            # left_array[i] = array[p +i -1]
            left_array[i] = array[p +i]
        for j in range(0, n2):
            right_array[j] = array[q +1 +j]

        i = j = 0
        k = p

        while i < n1 and j < n2:

            if left_array[i] <= right_array[j]:
                array[k] = left_array[i]
                i += 1
            else:
                array[k] = right_array[j]
                j += 1
            k +=1

        while i < n1:
            array[k] = left_array[i]
            i += 1
            k += 1

        while j < n2:
            array[k] = right_array[j]
            j += 1
            k += 1


    def merge_sort(self, array, p, r):
        if p < r:
            q = (p+(r-1))//2
            self.merge_sort(array, p, q)
            self.merge_sort(array, q+1, r)
            self.merge(array, p, q, r)
        # print('FINAL ARRAY: ', array)
