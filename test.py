class ImageFileAcceptor:
    def __init__(self, extensions):
        self.__extensions = extensions

    def __call__(self, filenames):
        result = []
        for ext in self.__extensions:
            if ext in filenames:
                result.append(filenames)

        return result
