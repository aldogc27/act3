import unittest
import os
import shutil

def copiar_archivo(origen, destino):
    shutil.copy(origen, destino)
    return os.path.exists(destino)

class TestCopiaArchivo(unittest.TestCase):
    def test_copiar_archivo(self):
        resultado = copiar_archivo("archivo.txt", "archivo_copia.txt")
        self.assertTrue(resultado)

    def tearDown(self):
        if os.path.exists("archivo_copia.txt"):
            os.remove("archivo_copia.txt")

if __name__ == "__main__":
    unittest.main()
