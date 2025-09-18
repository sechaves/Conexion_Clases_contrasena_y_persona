import random
import string

class Contraseña:
    def __init__(self, longitud=8):
        self.longitud = longitud
        self.contraseña = self.generar_contraseña()
        
    def generar_contraseña(self):
        caracteres = string.ascii_letters + string.digits
        contraseña = ''.join(random.choice(caracteres) for _ in range(self.longitud))
        return contraseña
    
    def verificar_seguridad_contraseña(self):
        tiene_mayus = any(c.isupper() for c in self.contraseña)
        tiene_minus = any(c.islower() for c in self.contraseña)
        tiene_num = any(c.isdigit() for c in self.contraseña)

        if len(self.contraseña) >= 8 and tiene_mayus and tiene_minus and tiene_num:
            return True
        else:
            return False 