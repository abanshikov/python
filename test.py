class BookStudy:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.yeat = year

    def __eq__(self, other):
        return self.name.lower() == other.name.lower() and self.author.lower() == other.author.lower()

    def __hash__(self):
        return hash((self.name.lower(), self.author.lower()))

    def __str__(self):
        return f"{self.name}: {self.author}"

    def __repr__(self):
        return f"{self.name}: {self.author}"


lst_bs = []
for _ in lst_in:
    name, author, year = _.split(";")
    book = BookStudy(name.strip(), author.strip(), int(year))
    lst_bs.append(book)

unique_books = len(set(lst_bs))
#print(unique_books)
