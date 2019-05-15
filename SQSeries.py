class SQSeries:
    #   Predicative
    def __init__(self, name):
        self._value = None
        self._index = None
        self._meta = {}

        self._meta["index_type"] = "simple"
        self._meta["value_type"] = "float"

        self._name = name
        self._length = 0

    @property
    def value(self):
        return self._value

    @property
    def index(self):
        return self._index

    @property
    def index_type(self):
        return self._meta["index_type"]

    @property
    def value_type(self):
        return self._meta["value_type"]

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        self._name = None

    @property
    def length(self):
        return self._length

    def _update_len(self):
        self._length = len(self._value)

    def from_list(self, value, value_type="float"):
        # TODO: allow different value_type
        # TODO: allow different index_type
        self._index = range(len(value))
        self._value = value

        self._meta["value_type"] = "float"
        self._meta["index_type"] = "simple"
        
        self._update_len()

    def from_file(self, fname):
        #   made for files with 1 column : value
        self._index = []
        self._value = []
        self._length = 0

        with open(fname, "r") as f_read:
            all_lines = f_read.readlines()
            ind = 0
            for each_line in all_lines:
                self._index.append(ind)
                self._value.append(float(each_line))
                ind += 1

        self._update_len()

    def fetch(self, index):
        # TODO: labels
        return self._value[self._index.index(index)]

    def fetch_tuple(self, index):
        for (ind, val) in zip(self._index, self._value):
            if ind == index:
                return (ind, val)

        return None

    def to_file(self, fname):
        with open(fname, "w") as fopen:
            fopen.write("Index,Value\n")
            for i in range(self.length):
                fopen.write(str(self._index[i]) + "," + str(self._value[i]) + "\n")

    def __dir__(self):
        return ["index", "value", "index_type", "value_type", "name", "length"]

    def __str__(self):
        return self.name
