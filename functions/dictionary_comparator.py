import matplotlib.pyplot as plt

class DictionaryComparator:
    def __init__(self, dict1, dict2, name1="Dictionary 1", name2="Dictionary 2"):
        self.dict1 = dict1
        self.dict2 = dict2
        self.name1 = name1
        self.name2 = name2

    def compare_dictionaries(self):
        if self.dict1 is None or self.dict2 is None:
            raise ValueError(f"One of the dictionaries ({self.name1} or {self.name2}) is None")

        # Size Comparison
        size_dict1 = len(self.dict1)
        size_dict2 = len(self.dict2)
        print(f"Size of {self.name1}: {size_dict1}")
        print(f"Size of {self.name2}: {size_dict2}")

        # Common and Unique Elements
        common_keys = set(self.dict1.keys()).intersection(set(self.dict2.keys()))
        unique_to_dict1 = set(self.dict1.keys()).difference(set(self.dict2.keys()))
        unique_to_dict2 = set(self.dict2.keys()).difference(set(self.dict1.keys()))

        print(f"Number of common elements: {len(common_keys)}")
        print(f"Number of unique elements in {self.name1}: {len(unique_to_dict1)}")
        print(f"Number of unique elements in {self.name2}: {len(unique_to_dict2)}")

        # Frequency Distribution
        common_counts = {key: (self.dict1[key], self.dict2[key]) for key in common_keys}

        return common_keys, unique_to_dict1, unique_to_dict2, common_counts

    def plot_bar_chart(self, common_counts):
        keys = list(common_counts.keys())
        values_dict1 = [common_counts[key][0] for key in keys]
        values_dict2 = [common_counts[key][1] for key in keys]

        x = range(len(keys))
        plt.bar(x, values_dict1, width=0.4, label=self.name1, align='center')
        plt.bar(x, values_dict2, width=0.4, label=self.name2, align='edge')

        plt.xlabel('StudCuts')
        plt.ylabel('Counts')
        plt.title('Frequency Comparison of Common StudCuts')
        plt.legend()
        plt.show()
