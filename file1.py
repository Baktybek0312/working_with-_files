f = open("ww.txt", 'r')
# f.write("""sadasdsadasdadcassca
#         asdasadasd
#         sczxscascascas""")
for r in f:

    print(f.readline())
f.close()

with open("ww.txt",'r') as f:
    print(f.read())


