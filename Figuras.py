import  math

##------------------------------------------------------------------------------------------------------

class Punto:
    def __init__(self,x=0,y=0):
        self.x = x;
        self.y = y;

##-------------------------------------------------------------------------------------------------------
class Figura:

    def distancePoint(self, puntoA, puntoB):
        return (math.sqrt((puntoB.x - puntoA.x) ** 2 + (puntoB.y - puntoA.y) ** 2));

##-------------------------------------------------------------------------------------------------------
class Circulo(Figura):
    punto_origen  = None;
    def __init__(self, x,y):
        self.punto_origen = Punto(x,y);
        self.radio = self.getRadio();


    def getRadio(self):
        return  (self.punto_origen.x**2 + self.punto_origen.y**2);

    def isInPosition(self, puntoC):
        if(puntoC.x <= self.radio and puntoC.y<=self.radio ):
            if(puntoC.x>=self.punto_origen.x and puntoC.y >= self.punto_origen.y):
                return True;
            else:
                return False;
        else:
            return False

##----------------------------------------------------------------------------------------------------


class Triangulo(Figura):


    def __init__(self,  medidaLados = [],angulosEsquinas = []):
        self.medidasLados = medidaLados;
        self.angulosEsquinas = angulosEsquinas;

    def determinateTriangule(self):
        return ;
