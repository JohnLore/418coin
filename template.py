""" Our large test data is currently procedurally generated. However, in actual use. It would be ported over from the app using the server server.py in RestTest. """



""" High Level Overview: Traditionally in template matching, parallelism is used in the multiscaling step. Each scale is done in parallel. However, 
due to our Octree implementation, we will be splitting the octree spatially into sections, and running those in parallel. In traditional 
template matching, a sliding window of the template is convolved around the image, and the highest matching metric is returned as a match. Using Octrees, 
we are able to simplify the scaling up process. We have come up with a method of combining metrics at scale X to calculate the metric at scale X+1 
without having to recalculate. This provides massive speedup as we are able to reduce drastically the amount of work which needs to be done. Template
matching usually only works if the template image is in the same orientation as it is in the search image. However, when we spin up a new instance
of the app, our direction is arbitrary. Whichever direction we are facing when the app opens up is the x-axis, and the position we are at at that moment
is determined as the origin. Thus, our algorithm must be position and direction agnostic. To do this, our algorithm samples a set of all the points within
a radius r. It then compares this set of points to the template, and produces a metric. The breakthrough reduction in work required is due to the
fact that by using this method with an octree implementation instead of with a matrix implementation, we can determine the metrics for all the
larger scales after having calculated it for the lowest scale, as mentioned earlier. """


"""Note** Since python passes by reference, we are able to pass in the large data structures which is our octree. We are really only
passing a pointer to that potentially very large data structure. A 64x64x64 octree is over 1/4 million data entry points"""

#from pyoctree import pyoctree as ot
from octree import Octree
import numpy as np
import multiprocessing as mp
from multiprocessing import Pool
import time
import sys
import math
from functools import partial
#import cv2


def test_parallel(x):
    return x*x


def parallel_metric(tree, template):
    return 5
    

def calc_metric(entries, template):
    """ this is the function which is used to calculate the metric. Finding the optimal metric is beyond the scope of this project, but some common 
    metrics used generally in template matching are squared difference, normalized square difference, ccorr, normalized ccorr, ccoeff, and normalized
    ccoeff. All of these have the same complexity during calculation, so for the purposes of analyzing the parallelism, they are the same, and 
    are equivalent to just counting and comparing the number of points within, which is what we do here, to analyze performance"""
    #print("faffer")
    entriesValue = len(entries)
    #print(template)
    #print(template.root)
    #print(template.root.value)
    try:
        templateValue = len(template.root.value)
    except TypeError:
        templateValue = 0

    return abs(entriesValue - templateValue)


def naive(tree, template, n):
    """ In actual template matching, there would be a threshold under which we would return 'no match'. For our implementation, this threshold
    we have chosen to be infinite, because we want there to always be a matching, but it is implemented such that a threshold can exist"""
    """ This most naive version recalculates the metric for each zoom level"""
    counter = 4
    x = -n
    y = -n
    z = -n
    minMetric = sys.maxint
    minX = 0
    minY = 0
    minZ = 0
    threshold = sys.maxint 
    minZoom = 0
    while(counter <= n):
        x = -n + counter/2
        while( x <= n - counter/2):
            y = -n + counter/2
            while(y <= n):
                z = -n + counter/2
                while(z <= n - counter/2):
                    entries = tree.find_within_range((x,y,z), counter, "cube")
                    tempMetric = calc_metric(entries, template)
                    if (tempMetric < minMetric):
                        minMetric = tempMetric
                        minX = x
                        minY = y
                        minZ = z
                        minZoom = counter
                    z += counter
                y += counter
            x += counter
        counter *= 2
    if (minMetric < threshold):
        return (minX, minY, minZ, minZoom)
    else:
        return None

def reduce(matrix):
    """ This function takes an NxNxN matrix and returns an N/2xN/2xN/2 matrix in which every element is the sum of 8 of the elements from 
    the original matrix"""
    #print(matrix)
    n = len(matrix[0][0])
    newMetric = [[[0 for a in range(n/2)] for b in range(n/2)] for c in range(n/2)]
    for x in range(n/2):
        for y in range(n/2):
            for z in range(n/2):
                newMetric[x][y][z] = matrix[2*x][2*y][2*z] +matrix[2*x][2*y][2*z+1] +matrix[2*x][2*y+1][2*z] +matrix[2*x][2*y+1][2*z+1] +matrix[2*x+1][2*y][2*z] +matrix[2*x+1][2*y][2*z+1] +matrix[2*x+1][2*y+1][2*z] +matrix[2*x+1][2*y+1][2*z+1] 
    return newMetric


def single(tree, template, n):
    """This version of the matching should be better than the naive, but not as good as the parallel"""
    counter = 4
    x = -n
    y = -n
    z = -n
    x = -n + counter/2
    metric = [[[0 for a in range(n/2)] for b in range(n/2)] for c in range(n/2)]
    a = 0
    b = 0
    c = 0
    minMetric = sys.maxint
    threshold = sys.maxint
    while (x <= n - counter/2):
        y = -n + counter/2
        while(y <= n - counter/2):
            z = -n + counter/2
            while(z <= n - counter/2):
                entries = tree.find_within_range((x,y,z), counter, "cube")
                metric[a][b][c] = calc_metric(entries, template)
                if (metric[a][b][c] < minMetric):
                    minMetric = metric[a][b][c]
                    minX = x
                    minY = y
                    minZ = z
                    minZoom = counter
                z+= counter
            y += counter
        x += counter
    while(counter <= 16):
        metric = reduce(metric)
        n = len(metric)
        for a in range(n):
            for b in range(n):
                for c in range(n):
                    if (metric[a][b][c] < minMetric):
                        minMetric = tempMetric  
                        minX = x
                        minY = y
                        minZ = z
                        minZoom = 2*counter
        counter*=2
    if (minMetric < threshold):
        return (minX, minY, minZ, minZoom)
    else:
        return None


def reduceMulti(matrix):
    """ This function takes an MxNxN matrix and returns an M/2xN/2xN/2 matrix in which every element is the sum of 8 of the elements from 
    the original matrix"""
    m = len(matrix)
    n = len(matrix[0][0])
    if (m > 1):
        newMetric = [[[0 for a in range(m/2)] for b in range(n/2)] for c in range(n/2)]
        for x in range(m/2):
            for y in range(n/2):
                for z in range(n/2):
                    newMetric[x][y][z] = matrix[2*x][2*y][2*z] +matrix[2*x][2*y][2*z+1] +matrix[2*x][2*y+1][2*z] +matrix[2*x][2*y+1][2*z+1] +matrix[2*x+1][2*y][2*z] +matrix[2*x+1][2*y][2*z+1] +matrix[2*x+1][2*y+1][2*z] +matrix[2*x+1][2*y+1][2*z+1] 
    else: 
        newMetric = [[[0 for a in range(m)] for b in range(n/2)] for c in range(n/2)]
        for y in range(n/2):
                for z in range(n/2):
                    newMetric[x][y][z] = matrix[0][2*y][2*z] +matrix[0][2*y][2*z+1] +matrix[0][2*y+1][2*z] +matrix[0][2*y+1][2*z+1] +matrix[0][2*y][2*z] +matrix[0][2*y][2*z+1] +matrix[0][2*y+1][2*z] +matrix[0][2*y+1][2*z+1] 
    
    return newMetric


def multi(tree, template, n, core):
    """This version of the matching should be better than the naive, but not as good as the parallel"""
    counter = 4
    x = -32
    y = -32
    z = -32
    x = -32 + counter/2 + core * 64/n
    metric = [[[0 for a in range(16/n)] for b in range(16)] for c in range(16)]
    a = 0
    b = 0
    c = 0
    minMetric = sys.maxint
    threshold = sys.maxint
    while (x <= 32 - counter/2 + (core + 1)*64/n):
        y = -32 + counter/2
        while(y <= 32 - counter/2):
            z = -32 + counter/2
            while(z <= 32 - counter/2):
                entries = tree.find_within_range((x,y,z), counter, "cube")
                metric[a][b][c] = calc_metric(entries, template)
                if (metric[a][b][c] < minMetric):
                    minMetric = metric[a][b][c]
                    minX = x
                    minY = y
                    minZ = z
                    minZoom = counter
                z+= counter
            y += counter
        x += counter
    while(counter <= 16):
        metric = reduceMulti(metric)
        for a in range(len(metric)):
            for b in range(len(metric[0])):
                for c in range(len(metric[0][0])):
                    if (metric[a][b][c] < minMetric):
                        minMetric = tempMetric
                        minX = x
                        minY = y
                        minZ = z
                        minZoom = 2*counter
        counter *= 2
    if (minMetric < threshold):
        return (minX, minY, minZ, minZoom)
    else:
        return None


if __name__ == "__main__":
    #print(sys.argv[1])
    n = int(sys.argv[1])
    pool = Pool(processes=n)
    #inputs = [(tree, template, x, n) for x in range(n)]
    #pool.map(multi, inputs)
    #print(pool.map(test_parallel, range(10)))

    #x = np.array([2,3,1])
    #y = np.array([5,7,10])
    #tree = ot.PyOctree(x, y)


    print "Creating octree"
    treeSize = 64
    templateSize = 4
    tree = Octree(treeSize, treeSize, treeSize, -treeSize, -treeSize, -treeSize)
    template = Octree(templateSize, templateSize, templateSize, -templateSize, -templateSize, -templateSize)
    counter = 0 

    start_time = time.time()

    for x in range(-treeSize,treeSize):
        for y in range(-treeSize,treeSize):
            for z in range(-treeSize,treeSize):
                tree.add_item(counter, (x,y,z))
                counter+=1
                #print(counter)


    counter = 0
    for x in range(-templateSize, templateSize):
        for y in range (-templateSize, templateSize):
            for z in range(-templateSize, templateSize):
                template.add_item(counter, (x,y,z))
                counter+= 1



    print("Intialization: --- %s seconds ---" % (time.time() - start_time))

    func = partial(multi, [tree, template, n])

    start_time = time.time()
    naive(tree, template, treeSize)
    print("Naive: --- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    single(tree, template, treeSize)
    print("Single: --- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    #print(inputs)
    pool.map(func, range(n))
    print("Parallel: --- %s seconds ---" % (time.time() - start_time))






