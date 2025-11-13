from dataclasses import dataclass, field


@dataclass
class PolyLine:
    width: float = field(compare=False)
    color: int = field(compare=False, default=0)
    points: list = field(default_factory=list)

    def __post_init__(self):
        self.points = [(0, 0)]


pl1 = PolyLine(width=0.5, color=0)
pl2 = PolyLine(width=1.5, color=2)

pl1.points.extend([(10, -5), (12, 1)])
pl2.points.extend([(10, -5), (12, 1)])

res = pl1 == pl2
