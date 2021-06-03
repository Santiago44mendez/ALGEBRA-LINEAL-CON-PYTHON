Descripción general
-------

Este módulo contiene algunas herramientas para la representación gráfica de vectores en el plano y en el espacio, diseñado para un curso de álgebra lineal con aplicaciones, contiene funciones para graficar vectores libres o anclados en el origen, para su realización se utilizó la librería de graficación interactiva **Plotly** y de arreglos multidimensionales **NumPy**, es compatible con vectores construidos en la librería **SymPy**. Puede servir como herramienta de visualización, para la validación del conocimiento por parte de los estudiantes y la resolución de problemas relacionados con conceptos vectoriales.

Instalación
-------

Para utilizar el módulo de graficación **plotvectors** debe importarlo de la siguiente manera:



*    ``pip install PlotLinearAlgebra``
*   ``from PlotLinearAlgebra.plotvectors import *``

Funciones
-------

El módulo **plotvectors** contiene las funciones **plotvectors2D** para graficación de vectores en el plano y **plotvectors3D** para la graficación de vectores en el espacio tridimensional.

plotvectors2D
~~~~~~~~~~
permite graficar multiples vectores libres y anclados en el origen del plano cartesiano, además de vectores equipolentes que inicien en un punto dado y vectores en forma polar  anclados o libres, acepta como argumentos vectores definidos en la librería SymPy.

*   ``plotvectors2D ([x,y])`` permite graficar un vector con punto inicial ``(0,0)`` y punto final ``(x,y)``.
*   ``plotvectors2D (A)`` permite graficar un vector ``A = [x,y]`` o definido en la librería **sympy** como ``A = Matrix([x,y])`` o ``A = Matrix([x])``.
*   ``plotvectors2D ([P,Q])`` permite graficar un vector con punto inicial ``P = (x1,y1)`` y punto final ``Q = (x2,y2)``.
*   ``plotvectors2D ([P,B])`` permite graficar un vector equipolente al vector  definido como ``B = [x,y]`` o  ``B = Matrix([x,y])`` con punto inicial en ``P = (x0,y0)``.
*   ``plotvectors2D ([a,"b"])`` permite graficar un vector con magnitud ``a`` y ángulo en grados respecto al eje x positivo ``b``.
*   ``plotvectors2D ([P,a,"b"])`` permite graficar un vector con punto inicial en ``P = (x0,y0)``, magnitud ``a`` y ángulo en grados respecto al eje x positivo ``b``.
*   ``plotvectors2D ([v1],[v2],...,[v3])`` permite graficar multiples vectores como los definidos anteriormente en el plano.

plotvectors3D
~~~~~~~~~~
permite graficar multiples vectores libres y fijados en el origen del espacio tridimensional, ademas de vectores equipolentes que inicien en un punto dado y vectores definidos desde su magnitud y con vector director unitario dado, acepta como argumentos vectores de la librería SymPy.

*   ``plotvectors2D ([x,y])`` permite graficar un vector con punto inicial ``(0,0)`` y punto final ``(x,y)``.
*   ``plotvectors2D (A)`` permite graficar un vector ``A = [x,y]`` o definido en la librería **sympy** como ``A = Matrix([x,y])`` o ``A = Matrix([x])``.
*   ``plotvectors2D ([P,Q])`` permite graficar un vector con punto inicial ``P = (x1,y1)`` y punto final ``Q = (x2,y2)``.
*   ``plotvectors2D ([P,B])`` permite graficar un vector equipolente al vector  definido como ``B = [x,y]`` o  ``B = Matrix([x,y])`` con punto inicial en ``P = (x0,y0)``.
*   ``plotvectors2D ([a,"b"])`` permite graficar un vector con magnitud ``a`` y ángulo en grados respecto al eje x positivo ``b``.
*   ``plotvectors2D ([P,a,"b"])`` permite graficar un vector con punto inicial en ``P = (x0,y0)``, magnitud ``a`` y ángulo en grados respecto al eje x positivo ``b``.
*   ``plotvectors2D ([v1],[v2],...,[v3])`` permite graficar multiples vectores como los definidos anteriormente en el plano



