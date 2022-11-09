import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import copy

class Plot():

    def __init__(self, list_of_algorithms, x_index):
        self.organize_data(list_of_algorithms, x_index)
        self.data = self.prepare_data(list_of_algorithms, x_index)


    def compare_algorithms(self):
        plt.plot(self.data['index'], self.data['InsertionSort'], label = 'InsertionSort')
        plt.plot(self.data['index'], self.data['MergeSort'], label = 'MergeSort')
        plt.plot(self.data['index'], self.data['MergeSortAdapted'], label = 'MergeSortAdapted')
        plt.legend()
        plt.show()

        # fig = go.Figure()
        # fig.add_trace(go.Scatter(x=data['index'],y=data['InsertionSort'], mode='lines',name='lines'))
        # fig.add_trace(go.Scatter(x=data['index'],y=data['MergeSort'], mode='lines+markers',name='lines+markers'))
        # fig.add_trace(go.Scatter(x=data['index'],y=data['MergeSortAdapted'], mode='markers',name='markers'))

        # fig.show()

    def prepare_data(self, list_of_algorithms, x_index):
        data = {}

        for algorithm in list_of_algorithms:
            data[algorithm.class_name] = algorithm.list_times

        data['index'] = x_index
        return data


    def organize_data(self, list_of_algorithms, x_index):        
        x_index.sort()
        for algorithm in list_of_algorithms:
            algorithm.list_times.sort()