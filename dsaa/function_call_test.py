def test(t):
    t = 20
    print("In Function:",t)

x=10
print("Before:",x)
test(x)
print("After:",x)

def test_global():
    global y
    y = 20
    print(y)

y=10
print("Before:",y)
test_global()
print("After:",y)