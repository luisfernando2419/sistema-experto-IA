from experta import *
class Sintoma(Fact):
    """Clase que representa un síntoma que tiene el paciente"""
    pass
class DiagnosticoEnfermedad(KnowledgeEngine):
    
    @Rule(Sintoma(tos='si', fiebre='si', dolor_cabeza='si', fatiga='si'))
    def gripe(self):
        print("El diagnóstico es: Gripe")
    
    @Rule(Sintoma(tos='si', fiebre='no', dolor_cabeza='si', fatiga='no'))
    def resfriado(self):
        print("El diagnóstico es: Resfriado común")
    
    @Rule(Sintoma(estornudos='si', ojos_llorosos='si', picazon_nariz='si', fiebre='no'))
    def alergia(self):
        print("El diagnóstico es: Alergia")
if __name__ == "__main__":
    engine = DiagnosticoEnfermedad()

   
    engine.reset()

   
    engine.declare(Sintoma(tos='si', fiebre='si', dolor_cabeza='si', fatiga='si'))

    # Ejecutar el sistema experto
    engine.run()
