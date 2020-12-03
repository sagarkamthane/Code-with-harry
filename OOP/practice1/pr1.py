class C2DVector:
    def __init__(self, i, j):
        self.icap = i
        self.jcap = j

    def __str__(self):
        return f'{self.icap}i + {self.jcap}j'

class C3DVector(C2DVector):
    def __init__(self, i, j, k):
        super().__init__(i,j)
        self.kcap = k

    def __str__(self):
        return f'{self.icap}i + {self.jcap}j + {self.kcap}k'


v2d = C2DVector(1,2)
v3d = C3DVector(1,2,3)

print(v2d,v3d)
