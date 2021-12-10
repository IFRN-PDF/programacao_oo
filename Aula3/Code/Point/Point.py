import math

"Observe que ao usar a classe, o docstring fica disponível para o usuário da classe"
class Point:
    "Representa coordenadas geométricas de um ponto no espaço bidimensional"
    def __init__(self, x=0, y=0):
        """Inicializa a posição de um novo ponto. x e y podem
           ser especificados. Se eles não forem, as coordenadas
           serão inicializadas na origem."""
        self.move(x, y)
        
    def move(self, x, y):
        "Move um ponto para uma nova coordenada no espaço 2D." 
        self.x = x
        self.y = y
    
    def reset(self):
        "Reposiciona um ponto na origem geométrica: (0, 0)" 
        self.move(0, 0)

    def calculate_distance(self, other_point):
        """Calcula a distância entre esse ponto e um segundo
        ponto passado como parâmetro. Depois, a distância é 
        retorna como um float."""
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2 )
    
    def __add__(self, other):
        '''soma x e y de dois pontos distintos'''
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return "Point: x %d, y, %d" % (self.x , self.y)

p1 = Point(1,1)
p2 = Point(2,2)

print(p1.calculate_distance(p2))

p3 = p1+p2

print(p3)