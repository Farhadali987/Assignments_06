class A:
    def show(self):
        print("show of A")

class B(A):
    def show(self):
        print("show of B")

class C(A):
    def show(self):
        print("show of C")

class D(B,C):
    pass

print(D.__mro__)

d = D()
d.show()