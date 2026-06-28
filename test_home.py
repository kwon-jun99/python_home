'''
print("hello")

a=10
print(a)

c=19
print(a+c)

# 1. 정수(int)

a=10
print(a)
print(type(a))
print(3>5)

# 2. 문자열(str)
e= "python"
print(e)
print(type(e))
print(e[1])

# 3. 리스트(list) / list는 가변객체
f=[1,2,3]
print(f)
print(type(f))
print(f[1])
f[1]= "abc"
print(f)

# 4. 튜플(tuple) / tuple은 불변객체

g=(1,2,3)
print(g)
print(type(g))
print(g[1])

# 5. 딕셔너리(dict)

h = {"a": 1}
print(h)
print(type(h))
h["id"] = "rnjswns"
h["pw"] = "0000" # 가변객체
print(h)

# 6. 범위(range)

j= range(5)
print(j)
print(type(j))
'''
# 7. 함수(function)

def hello():
    print("Hy")

print(hello)
print(type(hello))

