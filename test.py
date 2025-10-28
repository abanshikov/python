class WordString:
    def __init__(self, string=""):
        self.__string = string

    def __call__(self, *args, **kwargs):
        return self.string.split()[args[0]]

    def __len__(self):
        return len(self.string.split())

    @property
    def string(self):
        return self.__string

    @string.setter
    def string(self, string):
        self.__string = string
