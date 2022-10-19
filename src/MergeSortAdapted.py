from src.MergeSort import MergeSort
from src.InsertionSort import InsertionSort


class MergeSortAdapted(MergeSort):
    
    def __init__(self, input_arrays, limit_size):
        '''
        Algoritmo Merge Sort Adaptado para utilizar o Insertion Sort em entradas Pequenas.
        Neste caso, como é apenas uma variação da Merge Sort, será aproveitada a sua implementação herdando sua classe e
        sobrescrevendo apenas o método do caso base para incorporar o InsertionSort.
        Nota-se que há um atributo a mais na construção da classe denominado limit_size que define o valor do
        tamanho limite de um array para o qual será utilizado o algoritmo InsertionSort.
        '''
        self.limit_size = limit_size
        super().__init__(input_arrays)


    def merge_sort(self, array, p, r):
        if (r - p) < self.limit_size:
            InsertionSort.sort(array)
        else:
            if p < r:
                q = (p+(r-1))//2
                self.merge_sort(array, p, q)
                self.merge_sort(array, q+1, r)
                self.merge(array, p, q, r)