from src.InsertionSort import InsertionSort
from src.MergeSort import MergeSort
from src.Utils import Utils


def main():
    input_arrays = Utils.generate_random_arrays(num_of_arrays=10)
    # input_arrays = [[9, 8, 7, 6, 4, 3, 2, 5],[6,3,8,4,7,4]]
    
    insertion_sort = InsertionSort(input_arrays)
    insertion_sort.run()
    
    merge_sort = MergeSort(input_arrays)
    merge_sort.run()
    
    print('INSERTION TIMES: ', insertion_sort.list_times)
    print('MERGE TIMES: ', merge_sort.list_times)


if __name__ == '__main__':
    main()    
