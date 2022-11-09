from src.InsertionSort import InsertionSort
from src.MergeSort import MergeSort
from src.MergeSortAdapted import MergeSortAdapted
from src.Plot import Plot
from src.Utils import Utils
import copy


def main():
    utils = Utils()
    input_arrays = utils.generate_random_arrays(num_of_arrays=10)

    input_insert = copy.deepcopy(input_arrays)
    insertion_sort = InsertionSort(input_insert)
    insertion_sort.run()
    
    input_merge = copy.deepcopy(input_arrays)
    merge_sort = MergeSort(input_merge)
    merge_sort.run()

    input_merge_adpt = copy.deepcopy(input_arrays)
    merge_sort_adapted = MergeSortAdapted(input_merge_adpt, limit_size=100)
    merge_sort_adapted.run()
    

    print('INSERTION TIMES: ', insertion_sort.list_times)
    print('MERGE TIMES: ', merge_sort.list_times)
    print('MERGE ADAPTED TIMES: ', merge_sort_adapted.list_times)

    print('SIZE OF INPUT ARRAYS: ', utils.size_of_input_arrays)
    # print('LIST OF ARRAYS> ', [insertion_sort, merge_sort, merge_sort_adapted])
    # print('INSERTION SORT LIST TIME: ', insertion_sort.list_times)
    plot = Plot([insertion_sort, merge_sort, merge_sort_adapted], utils.size_of_input_arrays)
    plot.compare_algorithms()


if __name__ == '__main__':
    main()    
