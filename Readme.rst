Descripción general
-------

Este módulo contiene algunas herramientas para la representación gráfica de vectores en el plano y en el espacio, diseñado para un curso de álgebra lineal con aplicaciones, contiene funciones para graficar vectores con punto inicial y punto final dado, o anclados en el origen, para su realización se utilizó la librería de graficación interactiva **Plotly** y la librería de arreglos multidimensionales **NumPy**, es compatible con vectores construidos como matriz columna en la librería **SymPy**. Puede servir como herramienta de visualización, para validar el conocimiento por parte de los estudiantes y para la resolución de problemas relacionados con conceptos vectoriales.

Instalación
-------

Para utilizar el módulo de graficación **plotvectors** debe importarlo de la siguiente manera:



*    ``pip install PlotLinearAlgebra``
*   ``from PlotLinearAlgebra.plotvectors import *``

Funciones
-------

El submódulo **plotvectors** contiene las funciones **plotvectors2D** que permite realizar la visualización de vectores en el plano cartesiano y **plotvectors3D** que permite la visualización de vectores en el espacio tridimensional, para definir puntos en estos módulos se usarán los objetos tipo tupla, por ejemplo el punto ``P =(x,y)`` o ``P =(x,y,z)`` y para definir vectores se usarán listas, por ejemplo el vector unidimensional ``V =[x]``, bidimensional ``V =[x,y]`` o tridimensional ``V =[x,y,z]``,  tambien podemos definir vectores como una matriz columna, haciendo uso de la librería sympy, de la forma ``V =Matrix([x])``, ``V =Matrix([x,y])`` o ``V =Matrix([x,y,z])`` dependiendo de la dimensión del vector.

plotvectors2D
~~~~~~~~~~
Permite visualizar multiples vectores en el plano cartesiano, que pueden tener un punto inicial y un punto final dado, estar anclados en el origen del plano, o vectores equipolentes a otro que inicie en un punto dado (traslación de vectores), y vectores en forma polar anclados en el origen o con un punto inicial dado, acepta como argumentos vectores definidos como matriz columna en la librería SymPy.

A continuación  se presenta la sintaxis adecuada para el manejo de esta función:

*   ``plotvectors2D ([x,y])`` permite graficar un vector con punto inicial ``(0,0)`` y punto final ``(x,y)``.
*   ``plotvectors2D ([x])`` permite graficar un vector unidimensional en la recta numérica con punto inicial  en el origen y punto final ``(x)``.
*   ``plotvectors2D (A)`` permite graficar un vector definido como ``A = [x,y]`` o en la librería **sympy** como ``A = Matrix([x,y])`` o ``A = Matrix([x])``.
*   ``plotvectors2D ([P,Q])`` permite graficar un vector con punto inicial ``P = (x1,y1)`` y punto final ``Q = (x2,y2)``.
*   ``plotvectors2D ([P,B])`` permite graficar un vector equipolente al vector  definido como ``B = [x,y]`` o  ``B = Matrix([x,y])`` con punto inicial en ``P = (x0,y0)``.
*   ``plotvectors2D ([a,"b"])`` permite graficar un vector con magnitud ``a`` y ángulo en grados respecto al eje x positivo ``b``.
*   ``plotvectors2D ([P,a,"b"])`` permite graficar un vector con punto inicial en ``P = (x0,y0)``, magnitud ``a`` y ángulo en grados respecto al eje x positivo ``b``.
*   ``plotvectors2D ([v1],[v2],...,[v3])`` permite graficar multiples vectores como los definidos anteriormente en el plano.

Como ejemplo, podemos presentar el siguiente código::
   
   
   from sympy import Matrix 
   A = Matrix([2,4])
   B = Matrix([-2])
   plotvectors2D([(1,2),[5,3]],[3],B,[2,1], [(7,5),(2,8)],A,[(2,2),A],[5,"300"],[(2.5,-4.33),[4,"90"]])
.. code-block:: rst


plotvectors3D
~~~~~~~~~~
permite graficar multiples vectores libres y fijados en el origen del espacio tridimensional, ademas de vectores equipolentes que inicien en un punto dado y vectores definidos desde su magnitud y con vector director unitario dado, acepta como argumentos vectores de la librería SymPy.

*   ``plotvectors3D ([x,y])`` permite graficar un vector con punto inicial ``(0,0,0)`` y punto final ``(x,y,z)``.
*   ``plotvectors3D (A)`` permite graficar un vector definido como ``A = [x,y,z]`` o en la librería **sympy** como ``A = Matrix([x,y,z])``.
*   ``plotvectors3D ([P,Q])`` permite graficar un vector con punto inicial ``P = (x1,y1,z1)`` y punto final ``Q = (x2,y2,z2)``.
*   ``plotvectors3D ([P,B])`` permite graficar un vector equipolente al vector  definido como ``B = [x,y,z]`` o  ``B = Matrix([x,y,z])`` con punto inicial en ``P = (x0,y0,z0)``.
*   ``plotvectors3D ([a,U])`` permite graficar un vector con magnitud ``a`` y vector director unitario definido como ``U = [x,y,z]`` o ``U = Matrix([x,y,z])``.
*   ``plotvectors3D ([P,a,U])`` permite graficar un vector con punto inicial en ``P = (x0,y0,z0)``, magnitud ``a`` y vector director unitario definido como ``U = [x,y,z]`` o ``U = Matrix([x,y,z])``.
*   ``plotvectors3D ([v1],[v2],...,[v3])`` permite graficar multiples vectores como los definidos anteriormente en el plano

Como ejemplo, podemos presentar el siguiente código::
   
   
   from sympy import Matrix 
   A = Matrix([2,4])
   B = Matrix([-2])
   plotvectors2D([(1,2),[5,3]],[3],B,[2,1], [(7,5),(2,8)],A,[(2,2),A],[5,"300"],[(2.5,-4.33),[4,"90"]])
.. code-block:: rst
   
   

 



