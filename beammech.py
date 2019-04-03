
#librerias importadas necesarias para los calculos
import math
import numpy as np

__version__ = '0.12'

def simplebeam():
    #se define un diccionario en el cual se ira agregando los datos en campos separados
    beam={}
    leng=input("\nIngrese el largo de la viga que sera en metros: ")
    #se especifican los valores para el largo y las posiciones de los soportes en una tupla
    beam["length"]=int(float(leng)*1000)
    beam["supports"]=(0,int(float(leng)*1000))
    wnum=input("\nIngrese el numero de cargas: ")
    loads=[]
    #se agregan las cargas con cada uno de sus valores en una lista
    for i in range(0,int(wnum)):
        load=input("\nIngrese el valor de la carga # "+str(i+1)+", si es una carga puntual su posición, si es distribuida o lineal agregar ademas su inicio y fin\nEjemplo:\n1. Carga puntual: '1|20|100' (carga puntual, fuerza (N) ,posicion (m))\n2. Carga distribuida: '2|50|10|25' (carga distribuida, Kg/m, posicion inicial, posicion final)\n3. Carga lineal: '3|100|0|20' (carga lineal, fuerza (N), posicion inicial (m), posicion final (m))\n")
        load=load.split("|")
        if load[0]=="1":
            loads.append(Load(force=-float(load[1]), pos=int(float(load[2])*1000)))
        elif load[0]=="2":
            loads.append(DistLoad(kg=float(load[1])*(float(load[3])-float(load[2]))/9.81, pos=(int(float(load[2])*1000),int(float(load[3])*1000))))
        elif load[0]=="3":
            loads.append(TriangleLoad(force=-float(load[1]),pos=(int(float(load[2])*1000),int(float(load[3])*1000))))

    #de la misma manera, en la lista loads, se agrega todos los momentos que se desee
    mnum=input("\nIngrese el numero de momentos: ")
    for i in range(0,int(mnum)):
        mload=input("\nIngrese el valor del momento # "+str(i+1)+", de la siguiente manera:\nEjemplo: 2000|100 (valor de momento, posicion en viga.\n")
        mload=mload.split("|")
        loads.append(MomentLoad(moment=int(float(mload[0]))*1000,pos=int(float(mload[1])*1000)))
    #se agrega la lista loads y se envia el diccionario al metodo solve(), el cual retorna el mismo diccionario con los resultados en distintos campos.
    beam['loads'] = loads
    return solve(beam)

#para el resto de opciones que se presenta, se usa la misa logica, sin embargo en ciertos de estos ya se pide las posiciones de los soportes de manera
#explicita y de alguna otra carga

def overhangbeam():
    beam={}
    leng=input("\nIngrese el largo de la viga que sera en metros: ")
    beam["length"]=int(float(leng)*1000)
    suppa=input("\nIngrese la posición del primer soporte: ")
    suppb=input("\nIngrese la posición del segundo soporte: ")
    beam["supports"]=(int(float(suppa)*1000),int(float(suppb)*1000))
    wnum=input("\nIngrese el numero de cargas: ")
    loads=[]
    for i in range(0,int(wnum)):
        load=input("\nIngrese el valor de la carga # "+str(i+1)+", si es una carga puntual su posición, si es distribuida o lineal agregar ademas su inicio y fin\nEjemplo:\n1. Carga puntual: '1|20|100' (carga puntual, fuerza (N) ,posicion (m))\n2. Carga distribuida: '2|50|10|25' (carga distribuida, Kg/m, posicion inicial, posicion final)\n3. Carga lineal: '3|100|0|20' (carga lineal, fuerza (N), posicion inicial (m), posicion final (m))\n")
        load=load.split("|")
        if load[0]=="1":
            loads.append(Load(force=-float(load[1]), pos=int(float(load[2])*1000)))
        elif load[0]=="2":
            loads.append(DistLoad(kg=float(load[1])*(float(load[3])-float(load[2]))/9.81, pos=(int(float(load[2])*1000),int(float(load[3])*1000))))
        elif load[0]=="3":
            loads.append(TriangleLoad(force=-float(load[1]), start=int(float(load[2])*1000), end=int(float(load[3])*1000)))
    
    mnum=input("\nIngrese el numero de momentos: ")
    for i in range(0,int(mnum)):
        mload=input("\nIngrese el valor del momento # "+str(i+1)+", de la siguiente manera:\nEjemplo: 2000|100 (valor de momento, posicion en viga.\n")
        mload=mload.split("|")
        loads.append(MomentLoad(moment=int(float(mload[0]))*1000,pos=int(float(mload[1])*1000)))
    beam['loads'] = loads
    return (solve(beam),suppa,suppb)

def cantilevbeam():
    beam={}
    leng=input("\nIngrese el largo de la viga que sera en metros: ")
    beam["length"]=int(float(leng)*1000)
    beam["supports"]=None
    wnum=input("\nIngrese el numero de cargas: ")
    loads=[]
    for i in range(0,int(wnum)):
        load=input("\nIngrese el valor de la carga #"+str(i)+", si es una carga puntual su posición, si es distribuida o lineal agregar ademas su inicio y fin\nEjemplo:\n1. Carga puntual: '1|20|100' (carga puntual, fuerza (N) ,posicion (m))\n2. Carga distribuida: '2|50|10|25' (carga distribuida, Kg/m, posicion inicial, posicion final)\n3. Carga lineal: '3|100|0|20' (carga lineal, fuerza (N), posicion inicial (m), posicion final (m))\n")
        load=load.split("|")
        if load[0]=="1":
            loads.append(Load(force=-float(load[1]), pos=int(float(load[2])*1000)))
        elif load[0]=="2":
            loads.append(DistLoad(kg=float(load[1])*(float(load[3])-float(load[2]))/9.81, pos=(int(float(load[2])*1000),int(float(load[3])*1000))))
        elif load[0]=="3":
            loads.append(TriangleLoad(force=-float(load[1]),pos=(int(float(load[2])*1000),int(float(load[3])*1000))))

    mnum=input("\nIngrese el numero de momentos: ")
    for i in range(0,int(mnum)):
        mload=input("\nIngrese el valor del momento #"+str(i)+", de la siguiente manera:\nEjemplo: 2000|100 (valor de momento, posicion en viga.\n")
        mload=mload.split("|")
        loads.append(MomentLoad(moment=-int(float(mload[0]))*1000,pos=int(float(mload[1])*1000)))

    beam['loads'] = loads
    return solve(beam)

#metodo solve, el cual dado un diccionario retorna el mismo con la soluciones de las cargas.
def solve(problem):
    #primero se checkea con el metodo de _check_length_supports, la posicion de los soportes.
    length, (s1, s2) = _check_length_supports(problem)
    #con el metodo de check_loads se mira que las cargas esten correctas, como que su posicion no sea fuera de la viga
    loads = _check_loads(problem)
    #se crea una copia de las cargas ya que estas son modificadas
    loads = [ld for ld in loads]
    #se valida si es que el problema tendra corte
    shear = _check_shear(problem)
    #se hace una suma de todos los arrays hechos por las cargas con sus valores
    moment = sum([ld.moment(s1) for ld in loads])
    #se obtiene el valor del soporte, en el caso de que este empotrado, el de s2 se define como el momento que da en el lado que se encuentra empotrado.
    if s2:
        R2 = Load(force=-moment / (s2 - s1), pos=s2)
        loads.append(R2)
    else:
        R2 = -moment
    #se obtiene el valor del primer soporte
    R1 = Load(force=-sum([ld.size for ld in loads]), pos=s1)
    loads.append(R1)
    #se define los valores de corte en un array que corre por milmetros haciendo la suma de todas las fuerzas sometidas.
    D = np.sum(np.array([ld.shear(length) for ld in loads]), axis=0)
    #se define la suma para el momento flector
    M = np.cumsum(D)
    Mstep = np.sum(
        np.array([ld.moment_array(length) for ld in loads if isinstance(ld, MomentLoad)]), axis=0
    )
    M += Mstep
    if s2 is None:
        M -= M[-1]
    #se guarda lo necesario en las distintas variables, y se retorna el nuevo diccionario
    problem['D'], problem['M'] = D, M/1000
    problem['R'] = (R1, R2)
    return problem

class Load(object):  # {{{
    """Point load."""

    def __init__(self, **kwargs):
        """
        Create a point load.

        Named arguments:
            force: Force in Newtons. N.B: downwards force should be a
                *negative* number.
            kg: Weight of a mass in kg, alternative for force. N.B: a weight
                of 1 kg will translate into a force of -9.81 N.
            pos: Distance from the origin to the location of the force in mm.

        Examples:
            >>> str(Load(kg=150, pos=100))
            'point load of -1471.5 N @ 100 mm.'
        """
        self.size = _force(**kwargs)
        self.pos = round(float(kwargs['pos']))

    def __str__(self):
        return f"point load of {self.size} N @ {self.pos} mm."

    def moment(self, pos):
        """
        Returns the bending moment that the load exerts at pos.
        """
        return (self.pos - pos) * self.size

    def shear(self, length):
        """
        Return the contribution of the load to the shear.

        Arguments:
            length: length of the array to return.

        Returns:
            An array that contains the contribution of this load.
        """
        rv = np.zeros(length + 1)
        rv[self.pos:] = self.size
        return rv  # }}}


class MomentLoad(Load):  # {{{

    def __init__(self, moment, pos):
        """Create a local bending moment load.

        Arguments:
            moment: bending moment in Nmm
            pos: position of the bending moment.
        """
        self.m = float(moment)
        Load.__init__(self, force=0, pos=pos)

    def __str__(self):
        return f'moment of {self.m} Nmm @ {self.pos}'

    def moment(self, pos):
        """
        Returns the bending moment that the load exerts at pos.
        """
        return self.m

    def shear(self, length):
        """
        Return the contribution of the load to the shear.

        Arguments:
            length: length of the array to return.

        Returns:
            An array that contains the contribution of this load.
        """
        return np.zeros(length + 1)

    def moment_array(self, length):
        """
        Return the contribution of the load to the bending moment.

        Arguments:
            length: length of the array to return.

        Returns:
            An array that contains the contribution of this load.
        """
        rv = np.zeros(length + 1)
        rv[self.pos:] = -self.m
        return rv  # }}}


class DistLoad(Load):  # {{{
    """Evenly distributed load."""

    def __init__(self, **kwargs):
        """
        Create an evenly distributed load.

        Named arguments:
            force: Force in Newtons. N.B: downwards force should be a
                *negative* number.
            kg: Weight of a mass in kg, alternative for force. N.B: a weight
                of 1 kg will translate into a force of -9.81 N.
            start: Begin of the distributed load. Must be used in combination
                with the 'end' argument.
            end: End of the distributed load.
            pos: 2-tuple containing the borders of the distributed load.
                You can use this instead of start and end.
        """
        size = _force(**kwargs)
        self.start, self.end = _start_end(**kwargs)
        if self.start > self.end:
            self.start, self.end = self.end, self.start
        Load.__init__(self, force=size, pos=float(self.start + self.end) / 2)

    def __str__(self):
        return f"constant distributed load of {self.size} N @ {self.start}--{self.end} mm."

    def shear(self, length):
        rem = length + 1 - self.end
        d = self.end - self.start
        q = self.size
        parts = (np.zeros(self.start), np.linspace(0, q, d), np.ones(rem) * q)
        return np.concatenate(parts)  # }}}


class TriangleLoad(DistLoad):  # {{{
    """Linearly rising distributed load."""

    def __init__(self, **kwargs):
        """
        Create an linearly rising distributed load.

        Named arguments:
            force: Force in Newtons. N.B: downwards force should be a
                *negative* number.
            kg: Weight of a mass in kg, alternative for force. N.B: a weight
                of 1 kg will translate into a force of -9.81 N.
            start: Begin of the distributed load. Must be used in combination
                with the 'end' argument.
            end: End of the distributed load.
        """
        DistLoad.__init__(self, **kwargs)
        length = abs(self.start - self.end)
        pos = (self.start, self.end)
        self.pos = round(min(pos)) + 2.0 * length / 3.0
        self.q = 2 * self.size / length

    def __str__(self):
        if self.start < self.end:
            d = 'ascending'
        else:
            d = 'descending'
        return f"linearly {d} distributed load of {self.size} N @ {self.start}--{self.end} mm."

    def shear(self, length):
        rem = length + 1 - self.end
        parts = (
            np.zeros(self.start), np.linspace(0, self.q, self.end - self.start),
            np.ones(rem) * self.q
        )
        dv = np.concatenate(parts)
        return np.cumsum(dv)  # }}}

#funcion para obtener la fuerza de cada una de las cargas
def _force(**kwargs):  # {{{
  
    if 'force' in kwargs:
        force = float(kwargs['force'])
    elif 'kg' in kwargs:
        force = -9.81 * float(kwargs['kg'])
    else:
        raise KeyError("No 'force' or 'kg' present")
    return force  # }}}

#dedicado para los objetos DistLoad() y TriangleLoad(), su posicion inicial y final
def _start_end(**kwargs):  # {{{
    
    if 'pos' in kwargs:
        p = kwargs['pos']
        if not isinstance(p, tuple) and len(p) != 2:
            raise ValueError("'pos' should be a 2-tuple")
        pos = (round(float(kwargs['pos'][0])), round(float(kwargs['pos'][1])))
    elif 'start' in kwargs and 'end' in kwargs:
        pos = (round(float(kwargs['start'])), round(float(kwargs['end'])))
    else:
        raise KeyError("Neither 'pos' or 'start' and 'end' present")
    return pos  # }}}

#se revisa el estado de los soportes
def _check_length_supports(problem):  # {{{
    #se valida si es que los soportes se encuentran antes de la viga
    problem['length'] = round(problem['length'])
    if problem['length'] < 1:
        raise ValueError('length must be ≥1')
    s = problem['supports']
    if s is not None:
        #validacion para saber si hay dos soportes
        if len(s) != 2:
            t = 'The problem definition must contain exactly two supports.'
            raise ValueError(t)
        s = (round(s[0]), round(s[1]))
        #validacion para ver si los soportes no estan en la misma posicion
        if s[0] == s[1]:
            raise ValueError('Two identical supports found!')
        #validacion para saber si no esta fuera de la viga el soporte
        elif s[0] > s[1]:
            s = (s[1], s[0])
        if s[0] < 0 or s[1] > problem['length']:
            raise ValueError('Support(s) outside of the beam!')
    else:
        s = (0, None)
    problem['supports'] = s
    return (problem['length'], s)  # }}}

#funcion encarga de revisar que esten bien las cargas en el diccionario ingresado
def _check_loads(problem):  # {{{
    #se valida que los objetos ingresados sean del tipo load
    loads = problem['loads']
    if isinstance(loads, Load):
        loads = [loads]
        problem['loads'] = loads
    #se valida que hayan loads dentro del diccionario, ya que no tendria sentido de lo contrario
    if loads is None or len(loads) == 0:
        raise ValueError('No loads specified')
    #finalmente se avisa si es que uno de los objetos ingresados no es del tipo load
    for ld in loads:
        if not isinstance(ld, Load):
            raise ValueError('Loads must be Load instances')
    return list(loads)  # }}}

#funcion para revisar que va a haber corte en el diccionario
def _check_shear(problem):  # {{{
    
    if 'shear' not in problem:
        problem['shear'] = True
    elif not isinstance(problem['shear'], bool):
        raise ValueError("'shear' should be a boolean.")
    return problem['shear']  # }}}
