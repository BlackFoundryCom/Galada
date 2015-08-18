from robofab.interface.all.dialogs import GetFile

filePath = GetFile("Open Translation Rules")

myFile = open(filePath, 'r')
glyphOrderDev = []
glyphOrderProd = []
devToProd = {}
prodToDev = {}

for l in myFile.readlines():
    prodName = l.split(';')[0]
    if l.split(';')[1][-1:] == '\n':
        devName = l.split(';')[1][:-1]
    else:
        devName = l.split(';')[1]
    glyphOrderDev.append(devName)
    glyphOrderProd.append(prodName)
    devToProd[devName] = prodName
    prodToDev[prodName] = devName
    
f = CurrentFont()

# for g in f:
#     try:
#         g.name = prodToDev[g.name]
#     except:
#         print g.name, 'not in translation rules'

f.glyphOrder = glyphOrderDev