import clipboard as c
x = "Data to be copied to clipboard"
c.copy(x)
a = c.paste()
print(a)
print(type(a))