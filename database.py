import unittest

def buscar_datos(*args, **kwargs):
    for key , value in kwargs.items():
        existe = True
        for i, n in value.items():
            if n not in args:
                existe = False
        if existe:
            return key
    return "Los datos no estan en la base de datos"
     
database = {
    "persona1":{
        "primer_nombre":"Pablo",
        "segundo_nombre": "Diego",
        "primer_apellido": "Ruiz",
        "segundo_apellido": "Picasso", 
     },
    "persona2": {
        "primer_nombre": "Manuel",
        "segundo_nombre": "Daniel",
        "primer_apellido": "Videla",
     },
    "persona3": {
        "primer_nombre": "Santiago",
        "segundo_nombre": "Damian",
        "primer_apellido": "Garcia",
        "segundo_apellido": "Correa",
       
    },
    "persona4": {
        "primer_nombre": "Franco",
        "segundo_nombre": "José",
        "primer_apellido": "Pagotto",
       
    }

}
   


buscar_datos("Pablo", "Diego","Ruiz", "Picasso",**database)

class TestKwargs(unittest.TestCase):

    def test1(self):
        resultado = buscar_datos("Pablo", "Diego","Ruiz", "Picasso",**database)
        self.assertEqual(resultado,"persona1")

    def test_datos_inexistentes(self):
        resultado = buscar_datos("messi", "cristiano","mendoza", "",**database)
        self.assertEqual(resultado,"Los datos no estan en la base de datos")
    
    def test2(self):
        resultado = buscar_datos("Manuel", "Daniel","Videla",**database)
        self.assertEqual(resultado,"persona2")

    def test3(self):
        resultado = buscar_datos("Santiago", "Damian","Garcia","Correa",**database)
        self.assertEqual(resultado,"persona3")


    def test4(self):
        resultado = buscar_datos("Franco", "José","Pagotto",**database)
        self.assertEqual(resultado,"persona4")

    


unittest.main()