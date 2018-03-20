WRLD Coding Exercise - the Most Isolated Feature 
=============================================

Solution
--------
The *most isolated* feature can be obtained by searching for a point, representing it in the Euclidian space, with the highest isolation among the other points that surround it. Isolation criteria can be reformulated as the distance to another _nearest_ point from the set, i.e. the smallest distance among its neighbours. We establish the neighbourhood relationships by using the Delaunay graph, which is the dual of the Voronoi graph, which avoids considering points that are not in the proximity. 

Complexity
----------
The [complexity of Delaunay computation](http://www.qhull.org/html/qh-code.htm#performance) is limited by O(n*log n) in the *worst* case. The isolation search is limited by O(n*k), where k is the largest number of neighbours in the Voronoi diagram, and, since it can be considered a constant for a large and evenly distributed point set in space,  the complexity is instead O(n). Taking into account both operations, we stay within the O(n*log n) limits. 
An improvement to the constant factor in the isolation search could have been made by caching the distance between any two neighbours, improving the performance roughly twice-fold.

Implementation
--------------
Python (version 3) language was used for the implementation. It was tempting to use C++, but the overhead of the build setup and the dependencies like the Boost Polygon library was not worth it in the end. We use the [Delauney](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.Delaunay.html#scipy.spatial.Delaunay) module of the SciPy python library that is in turn based on the [Qhull](http://www.qhull.org) library. [NumPy](http://www.numpy.org) library was used for the algebraic operations and as a dependency. For Python 3 SciPy can be installed by executing:

```bash
pip3 install scipy
```


