Descripción general
-------

Este módulo contiene algunas herramientas para la representación gráfica de vectores en el plano y en el espacio, diseñado para un curso de álgebra lineal con aplicaciones, contiene funciones para graficar vectores libres o anclados en el origen, para su realización se utilizó la librería de graficación interactiva **Plotly** y de arreglos multidimensionales **NumPy**, es compatrible con vectores construidos en la librería **SymPy**. Puede servir como herramienta de visualización, para la validación del conocimiento por parte de los estudiantes y la resolución de problemas relacionados con conceptos vectoriales.

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
permite graficar multiples vectores libres y fijados en el origen del plano cartesiano, ademas de vectores equipolentes que inicien en un punto dado y vectores en forma polar, acepta como argumentos vectores definidos en la librería SymPy.

*   ``plotvectors2D ([x,y])`` permite graficar el vector con punto inicial ``(0,0)`` y punto final ``(x,y)``.
*   ``plotvectors2D (A)`` permite graficar el vector definido en la librería **sympy**  ``A = Matrix([x,y])`` o ``A = Matrix([x])``.
*   ``plotvectors2D ([A,B])`` permite graficar el vector con punto inicial ``A = (x1,y1)`` y punto final ``B = (x2,y2)``.
*   ``plotvectors2D ([A,B])`` permite graficar un vector equipolente al vector ``B = [x,y]`` o  ``B = Matrix([x,y])`` con punto inicial ``A = (x0,y0)``.

plotvectors3D
~~~~~~~~~~
permite graficar multiples vectores libres y fijados en el origen del espacio tridimensional, ademas de vectores equipolentes que inicien en un punto dado y vectores definidos desde su magnitud y con vector director unitario dado, acepta como argumentos vectores de la librería SymPy.



