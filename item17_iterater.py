

def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100*value/total
        result.append(percent)
    return result


visits = [15, 35, 80]
percentage = normalize(visits)
print(percentage)


# Enable to read data throgh a data path
class ReadVists():
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)


def normalize_defensive(numbers):
    if iter(numbers) is iter(numbers):   # numbersがイテレータでない場合、新たなイテレータオブジェクトが返されるため、is構文でTrueとならない
        raise TypeError('Must suply a container')

    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result
