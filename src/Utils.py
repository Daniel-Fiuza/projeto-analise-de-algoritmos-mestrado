from random import randint, uniform

class Utils():

    def __init__(self) -> None:
        self.number_of_executions = randint(10, 20)
        self.size_of_arrays = self._generate_size_of_random_arrays()


    def _generate_size_of_random_arrays(self):
        return [randint(10, 10000) for _ in range(10)]


    def generate_array(self, size_of_array):
        array = []
        for _ in range(size_of_array):
            array.append(uniform(-1,1)*2*size_of_array)
        return array