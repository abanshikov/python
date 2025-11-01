class Player:
    def __init__(self, name, old, score):
        self.name = name
        self.old = old
        self.score = score

    def __bool__(self):
        return self.score > 0

    def __repr__(self):
        return f"{self.name} ({self.old}): {self.score}"

players = []
for item in lst_in:
    name, old, score = item.split(";")
    players.append(Player(name, int(old), int(score)))

players_filtered = list(filter(bool, players))
