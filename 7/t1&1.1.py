
class vec():
    def __init__(self,x,y,z):
        assert isinstance(x, (int,float))
        assert isinstance(y, (int,float))
        assert isinstance(z, (int,float))
        self.x=x
        self.y=y
        self.z=z
    def f(self):
        return self.x, self.y, self.z
    def __radd__(self, o):
        return'这是什么？'
    def __add__(self, other):
        return vec(self.x + other, self.y + other, self.z + other)
    def __sub__(self, o):
        return vec(self.x - o, self.y - o, self.z - o)
    def __rsub__(self, o):
        return '不好人'
    def __mul__(self, o):
        #return self.x * o, self.y * o, self.z * o
        return vec(self.x * o, self.y * o, self.z * o)
    def __truediv__(self, o):
        return vec(self.x / o, self.y / o, self.z / o)
    def __rmul__(self, other):
        return'太不好'
    def sk(self, vec):
        return self.x * vec.x + self.y * vec.y + self.z * vec.z
    def __abs__(self):
        return (self.x**2 + self.y ** 2 + self.z**2)**(1/2)
    def avec (self, k):
        return vec((self.x + k.x), (self.y + k.y), (self.z + k.z))
    def svec (self, k):
        return vec(self.x - k.x, self.y - k.y, self.z - k.z)

k=vec(3,3,3)
l=vec(1,1,1)
print(l.f())
print('l + x = ',(l+2).f())
print(2+l)
print('l - x = ',(l-1).f())
print(2*k)
print('l * 2 = ',(l*2).f())
print('k / 2 = ', (k/2).f())
print(2*l)
print('|l| = ',abs(l))
print('l + k = ', (l.avec(k)).f())
print('l - k = ', (l.svec(k)).f())
print(l.sk(k))
#l=map(vec, list(map(float,input().split())))
m1 = 1
m2 = 1
print((((l*m1).avec(k*m2))/(m1+m2)).f())
