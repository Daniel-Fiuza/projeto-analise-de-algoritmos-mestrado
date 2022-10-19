import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt

class Plot():

    def __init__(self, list_of_algorithms):
        self.data = self.prepare_data(list_of_algorithms)


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

    def prepare_data(self, list_of_algorithms):
        data = {}
        length_of_array = -1

        for algorithm in list_of_algorithms:
            data[algorithm.class_name] = algorithm.list_times
            length_of_array = len(algorithm.list_times)

        data['index'] = [index for index in range(1,length_of_array+1)]

        return data