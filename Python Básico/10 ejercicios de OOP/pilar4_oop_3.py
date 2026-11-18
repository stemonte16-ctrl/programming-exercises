"""
INVESTIGACION DE LA HERENCIA MULTIPLE

¿Qué es la herencia multiple?
Permite que una clase hija herede atributos y métodos de más de una clase padre.
Esto es útil para reutilizar código y establecer relaciones entre clases de manera más eficiente.

USOS:
1.Reutilización de código: permite aprovechar atributos y métodos de varias clases padre sin tener que volvera
escribirlos.
2.Combinación de funcionalidades: permite reunir comportamientos de diferentes clases en una sola clase hija.
3.Modelado de objetos con múltiples capacidades: permite representar objetos que poseen caracteristicas de 
diferentes categorías.
4.Incorporación de funcionalidades transversales: permite integrar caracteristicas como registro de actividades(logging),
validación de datos y serialización.
5.Combinación de responsabilidades: permite crear clases que reúnen diferentes capacidades, como administración, programación
o gestión de permisos.
6.Extensión de clases existentes: permite ampliar las capacidades de una clase aprovechando funcionalidades de otras clases sin 
modificar directamente su código.
7.Implementación de Mixins: permite agregar funcionalidades específicas y reutilizables a diferentes clases.

Ventajas (Pros)
1. Reutilización de código: permite aprovechar atributos y métodos de varias clases padre sin tener que volver a escribirlos.
2. Flexibilidad: permite combinar diferentes funcionalidades para crear clases que tengan capacidades más completas.
3. Menor duplicación de código: evita repetir métodos y funcionalidades que ya están implementados en otras clases.
4. Modularidad: permite separar funcionalidades en clases independientes y reutilizarlas cuando sean necesarias.
5. Extensibilidad: facilita agregar nuevas capacidades a una clase mediante la herencia de otras clases existentes.

Desventajas (Contras)
1. Mayor complejidad: cuando una clase hereda de muchas clases padre, puede resultar más difícil comprender su funcionamiento.
2. Conflictos entre métodos: dos o más clases padre pueden tener métodos con el mismo nombre, lo que puede generar ambigüedad.
3. Orden de resolución de métodos (MRO): Python debe determinar qué método utilizar cuando varias clases tienen métodos 
con el mismo nombre.Es necesario comprender cómo funciona este mecanismo.
4. Dificultad de mantenimiento: los cambios realizados en las clases padre pueden afectar
a las clases hijas que heredan de ellas.
5. Problemas con los constructores: cuando varias clases padre tienen sus propios constructores, 
puede ser más complicado inicializar correctamente todos los atributos heredados.
"""
class Camera:
    def take_photo(self):
        print("Taking a photo")

class Phone:
    def Make_call(self):
        print("Making a call")

class Smartphone(Camera, Phone):
    pass

samsumg_galaxy = Smartphone()
samsumg_galaxy.take_photo()
samsumg_galaxy.Make_call()
