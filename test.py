from pathlib import Path


filenames = ["boat.jpg", "ans.web.png", "text.txt", "www.python.doc", "my.ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.xls"]


class FileAcceptor:
    def __init__(self, *args):
        self.acceptors = set(args)

    def __call__(self, filename):
        return Path(filename).suffix.replace('.', '') in self.acceptors

    def __add__(self, other):
        if not isinstance(other, FileAcceptor):
            raise ArithmeticError("Правый операнд должен быть типом FileAcceptor")

        tmp = self.acceptors | other.acceptors
        return FileAcceptor(*tmp)


acceptor1 = FileAcceptor("jpg", "jpeg", "png")
acceptor2 = FileAcceptor("png", "bmp")
acceptor12 = acceptor1 + acceptor2    # ("jpg", "jpeg", "png", "bmp")
# print(acceptor12.acceptors)

acceptor_images = FileAcceptor("jpg", "jpeg", "png")
acceptor_docs = FileAcceptor("txt", "doc", "xls")
filenames = list(filter(acceptor_images + acceptor_docs, filenames))
