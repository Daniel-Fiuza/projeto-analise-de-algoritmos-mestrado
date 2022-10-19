from src.InsertionSort import InsertionSort
from src.MergeSort import MergeSort
from src.Utils import Utils


def main():
    input_arrays = Utils.generate_random_arrays(num_of_arrays=10)
    insertion_sort = InsertionSort(input_arrays)
    insertion_sort.run()


if __name__ == '__main__':
    main()    
