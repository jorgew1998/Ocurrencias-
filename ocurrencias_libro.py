ocurrencias = {}

def ocurrencia():
    
    archivo=open('La cámara secreta.txt',encoding='utf8')
    linea = archivo.readline()
    
    while linea:
        lista=[]
        lista=linea.split()
        for w in lista:
            if w in ocurrencias:
                ocurrencias[w] += 1
            else:
                ocurrencias[w] = 1
                
        linea = archivo.readline()
        
    for palabras in ocurrencias:
          print('({},{})'.format(palabras,ocurrencias[palabras]))

    archivo.close()
    
ocurrencia()
