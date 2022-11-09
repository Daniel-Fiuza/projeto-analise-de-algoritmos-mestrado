from src.InsertionSort import InsertionSort
from src.MergeSort import MergeSort
from src.MergeSortAdapted import MergeSortAdapted
from src.Plot import Plot
from src.Utils import Utils
import copy


def main():
    utils = Utils()
    insertion_sort = InsertionSort()
    merge_sort = MergeSort()
    merge_sort_adapted = MergeSortAdapted(limit_size=100)

    print('SIZE OF INPUT ARRAYS: ', utils.size_of_arrays)
    print('NUMBER OF EXECUTIONS: ', utils.number_of_executions)

    for size in utils.size_of_arrays:
        for _ in range(utils.number_of_executions):
            input_arrays = utils.generate_array(size)

            input_insert = input_arrays.copy()
            insertion_sort.run(input_insert)
            
            input_merge = input_arrays.copy()
            merge_sort.run(input_merge)

            input_merge_adpt = input_arrays.copy()
            merge_sort_adapted.run(input_merge_adpt)

        insertion_sort.calculate_mean_times()
        merge_sort.calculate_mean_times()
        merge_sort_adapted.calculate_mean_times()


    print('INSERTION TIMES: ', insertion_sort.mean_times)
    print('MERGE TIMES: ', merge_sort.mean_times)
    print('MERGE ADAPTED TIMES: ', merge_sort_adapted.mean_times)

    plot = Plot([insertion_sort, merge_sort, merge_sort_adapted], utils.size_of_arrays)
    plot.compare_algorithms()


if __name__ == '__main__':
    main()    
