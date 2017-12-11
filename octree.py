



class node():
    """
    Class to be a node in my octree
    """

    def __init__(self,parent, Xupperlimit, Yupperlimit, Zupperlimit, Xlowerlimit, Ylowerlimit, Zlowerlimit):
        self.parent = parent
        self.Xupperlimit = Xupperlimit
        self.Yupperlimit = Yupperlimit
        self.Zupperlimit = Zupperlimit
        self.Xlowerlimit = Xlowerlimit
        self.Ylowerlimit = Ylowerlimit
        self.Zlowerlimit = Zlowerlimit
        self.Xcenter = (self.Xupperlimit + self.Xlowerlimit)/2.
        self.Ycenter = (self.Yupperlimit + self.Ylowerlimit)/2.
        self.Zcenter = (self.Zupperlimit + self.Xlowerlimit)/2.

    parent = None
    value = None
    
    #children
    posXposYposZ = None
    posXposYnegZ = None
    posXnegYposZ = None
    posXnegYnegZ = None
    negXposYposZ = None
    negXposYnegZ = None
    negXnegYposZ = None
    negXnegYnegZ = None

    #array of children
    chidren = [posXposYposZ,posXposYnegZ,posXnegYposZ,posXnegYnegZ,negXposYposZ,negXposYnegZ,negXnegYposZ,negXnegYnegZ]

    #position in space
    Xupperlimit = None
    Yupperlimit = None
    Zupperlimit = None
    
    Xlowerlimit = None
    Ylowerlimit = None
    Zlowerlimit = None
    def get_array_of_children(self):
        """
        helper function to return array of children
        because there is some weird issue where just setting an 
        array variable isn't cutting it
        """
        children = [self.posXposYposZ,self.posXposYnegZ,self.posXnegYposZ,self.posXposYnegZ,self.negXposYposZ,self.negXposYnegZ,self.negXnegYposZ,self.negXnegYnegZ ]        
        return children

    def print_types(self):
        """
        helper function to printout types of children
        """
        print type(self.posXposYposZ)
        print type(self.posXposYnegZ)
        print type(self.posXnegYposZ)
        print type(self.posXnegYnegZ)
        print type(self.negXposYposZ)
        print type(self.negXposYnegZ)
        print type(self.negXnegYposZ)
        print type(self.negXnegYnegZ)
    def print_info(self):
        """
        helper function to dump node paramaters
        """

        print "parent:\t {0}".format(self.parent)
        print "value:\t {0}".format(self.value)
        
        #children
        print "posXposYposZ: \t {0}".format(self.posXposYposZ)
        print "posXposYnegz: \t {0}".format(self.posXposYnegZ)
        print "posXnegYposZ: \t {0}".format(self.posXnegYposZ)
        print "posXnegYnegZ: \t {0}".format(self.posXnegYnegZ)
        print "negXposYposZ: \t {0}".format(self.negXposYposZ)
        print "negXposYnegZ: \t {0}".format(self.negXposYnegZ)
        print "negXnegYposZ: \t {0}".format(self.negXnegYposZ)
        print "negXnegYnegZ: \t {0}".format(self.negXnegYnegZ) 

        #position in space
        print "Xupperlimit: \t {0}".format(self.Xupperlimit)
        print "Yupperlimit: \t {0}".format(self.Yupperlimit)
        print "Zupperlimit: \t {0}".format(self.Zupperlimit)
        
        print "Xlowerlimit: \t {0}".format(self.Xlowerlimit)
        print "Ylowerlimit: \t {0}".format(self.Ylowerlimit)
        print "Zlowerlimit: \t {0}".format(self.Zlowerlimit)

        print "Xcenter: \t {0}".format(self.Xcenter)
        print "Ycenter: \t {0}".format(self.Ycenter)
        print "Zcenter: \t {0}".format(self.Zcenter)

            
    def add(self, payload, coord, level):
        
        """
        Create a subnode
        """

        if level == 0:
            try:
                self.value.append((coord,payload))
            except AttributeError:
                self.value = []
                self.value.append((coord,payload))

        else:
            level -= 1
            #Determine quadrant
            if coord[0] <= self.Xcenter:
                #negX
                if coord[1] <= self.Ycenter:
                    #negY
                    if coord[2] <= self.Zcenter:
                        #negZ
                        Xupperlimit = self.Xcenter
                        Yupperlimit = self.Ycenter
                        Zupperlimit = self.Zcenter
                        Xlowerlimit = self.Xlowerlimit
                        Ylowerlimit = self.Ylowerlimit
                        Zlowerlimit = self.Zlowerlimit
                        self.negXnegYnegZ = node(self.negXnegYnegZ, Xupperlimit, Yupperlimit, Zupperlimit, Xlowerlimit, Ylowerlimit, Zlowerlimit)
                        self.negXnegYnegZ.add(payload, coord, level)
                    else:
                        #posZ
                        Xupperlimit = self.Xcenter
                        Yupperlimit = self.Ycenter
                        Zupperlimit = self.Zupperlimit
                        Xlowerlimit = self.Xlowerlimit
                        Ylowerlimit = self.Ylowerlimit
                        Zlowerlimit = self.Zcenter
                        self.negXnegYposZ = node(self.negXnegYnegZ, Xupperlimit, Yupperlimit, Zupperlimit, Xlowerlimit, Ylowerlimit, Zlowerlimit)
                        self.negXnegYposZ.add(payload, coord, level)
                else:
                    #posY
                    if coord[2] <= self.Zcenter:
                        #negZ
                        Xupperlimit = self.Xcenter
                        Yupperlimit = self.Yupperlimit
                        Zupperlimit = self.Zcenter
                        Xlowerlimit = self.Xlowerlimit
                        Ylowerlimit = self.Ycenter
                        Zlowerlimit = self.Zlowerlimit
                        self.negXposYnegZ = node(self.negXnegYnegZ, Xupperlimit, Yupperlimit, Zupperlimit, Xlowerlimit, Ylowerlimit, Zlowerlimit)
                        self.negXposYnegZ.add(payload, coord, level)

                    else:
                        #posZ
                        Xupperlimit = self.Xcenter
                        Yupperlimit = self.Yupperlimit
                        Zupperlimit = self.Zupperlimit
                        Xlowerlimit = self.Xlowerlimit
                        Ylowerlimit = self.Ycenter
                        Zlowerlimit = self.Zcenter
                        self.negXposYposZ = node(self.negXnegYnegZ, Xupperlimit, Yupperlimit, Zupperlimit, Xlowerlimit, Ylowerlimit, Zlowerlimit)
                        self.negXposYposZ.add(payload, coord, level)


            else:
                #posX
                if coord[1] <= self.Ycenter:
                    #negY
                    if coord[2] <= self.Zcenter:
                        #negZ
                        Xupperlimit = self.Xupperlimit
                        Yupperlimit = self.Ycenter
                        Zupperlimit = self.Zcenter
                        Xlowerlimit = self.Xcenter
                        Ylowerlimit = self.Ylowerlimit
                        Zlowerlimit = self.Zlowerlimit
                        self.posXnegYnegZ = node(self.negXnegYnegZ, Xupperlimit, Yupperlimit, Zupperlimit, Xlowerlimit, Ylowerlimit, Zlowerlimit)
                        self.posXnegYnegZ.add(payload, coord, level)

                    else:
                        #posZ
                        Xupperlimit = self.Xupperlimit
                        Yupperlimit = self.Ycenter
                        Zupperlimit = self.Zupperlimit
                        Xlowerlimit = self.Xcenter
                        Ylowerlimit = self.Ylowerlimit
                        Zlowerlimit = self.Zcenter
                        self.posXnegYposZ = node(self.negXnegYnegZ, Xupperlimit, Yupperlimit, Zupperlimit, Xlowerlimit, Ylowerlimit, Zlowerlimit)
                        self.posXnegYposZ.add(payload, coord, level)

                else:
                    #posY
                    if coord[2] <= self.Zcenter:
                        #negZ
                        Xupperlimit = self.Xupperlimit
                        Yupperlimit = self.Yupperlimit
                        Zupperlimit = self.Zcenter
                        Xlowerlimit = self.Zcenter
                        Ylowerlimit = self.Ycenter
                        Zlowerlimit = self.Zlowerlimit
                        self.posXposYnegZ = node(self.negXnegYnegZ, Xupperlimit, Yupperlimit, Zupperlimit, Xlowerlimit, Ylowerlimit, Zlowerlimit)
                        self.posXposYnegZ.add(payload, coord, level)

                    else:
                        #posZ
                        Xupperlimit = self.Xupperlimit
                        Yupperlimit = self.Yupperlimit
                        Zupperlimit = self.Zupperlimit
                        Xlowerlimit = self.Xcenter
                        Ylowerlimit = self.Ycenter
                        Zlowerlimit = self.Zcenter
                        self.posXposYposZ = node(self.negXnegYnegZ, Xupperlimit, Yupperlimit, Zupperlimit, Xlowerlimit, Ylowerlimit, Zlowerlimit)
                        self.posXposYposZ.add(payload, coord, level)


        

            
            


class Octree():
    """
    class to hold the whole tree
    We decided on using maxiter = 6 so that we would have each of the smallest subnodes be 1x1x1. 
    """
    
    def __init__(self, Xmax, Ymax, Zmax, Xmin, Ymin, Zmin, root_coords=(0,0,0), maxiter=6):
        self.Xmax = Xmax
        self.Ymax = Ymax
        self.Zmax = Xmax
        self.Xmin = Xmin
        self.Ymin = Ymin
        self.Zmin = Zmin
        self.root_coords = root_coords
        self.maxiter = maxiter
        
        self.root = node('root', Xmax, Ymax, Zmax, Xmin, Ymin, Zmin)

    def add_item(self, payload, coord):
        """
        Create recursively create subnodes until maxiter is reached
        then deposit payload in that node
        """

        self.root.add(payload, coord, self.maxiter)

    def find_within_range(self, center, size, shape):
        """
        Return payloads and coordinates of every payload within
        a specified area
        """

        if shape == "cube":
            
            payloads = []
            templist = [self.root]
            list_list = []
            list_list.append([self.root])
            for level in range(self.maxiter):
                list_list.append([])

            #print list_list
            for level in range(self.maxiter):
                for node in list_list[level]:
                    Xedge_max = center[0] + size
                    Xedge_min = center[0] - size
                    Yedge_max = center[1] + size
                    Yedge_min = center[1] - size
                    Zedge_max = center[2] + size
                    Zedge_min = center[2] - size

                    corner0 = (Xedge_max, Yedge_max, Zedge_max)
                    corner1 = (Xedge_max, Yedge_max, Zedge_min)
                    corner2 = (Xedge_max, Yedge_min, Zedge_max)
                    corner3 = (Xedge_max, Yedge_min, Zedge_min)
                    corner4 = (Xedge_min, Yedge_max, Zedge_max)
                    corner5 = (Xedge_min, Yedge_max, Zedge_min)
                    corner6 = (Xedge_min, Yedge_min, Zedge_max)
                    corner7 = (Xedge_min, Yedge_min, Zedge_min)
                    corners = [corner0, corner1, corner2, corner3, corner4, corner5, corner6, corner7]
                    table = ((corner0[0] > node.Xcenter),(corner0[1] > node.Ycenter) ,(corner0[2] > node.Zcenter))
                    if not False in table:
                        list_list[level+1].append(node.posXposYposZ)
                    table = ((corner1[0] > node.Xcenter),(corner1[1] > node.Ycenter) ,(corner1[2] < node.Zcenter))
                    if not False in table:
                        list_list[level+1].append(node.posXposYnegZ)
                    table = ((corner2[0] > node.Xcenter),(corner2[1] < node.Ycenter) ,(corner2[2] > node.Zcenter))
                    if not False in table:
                        list_list[level+1].append(node.posXnegYposZ)
                    table = ((corner3[0] > node.Xcenter),(corner3[1] < node.Ycenter) ,(corner3[2] < node.Zcenter))
                    if not False in table:
                        list_list[level+1].append(node.posXnegYnegZ)
                    table = ((corner4[0] < node.Xcenter),(corner4[1] > node.Ycenter) ,(corner4[2] > node.Zcenter))
                    if not False in table:
                        list_list[level+1].append(node.negXposYposZ)
                    table = ((corner5[0] < node.Xcenter),(corner5[1] > node.Ycenter) ,(corner5[2] < node.Zcenter))
                    if not False in table:
                        list_list[level+1].append(node.negXposYnegZ)
                    table = ((corner6[0] < node.Xcenter),(corner6[1] < node.Ycenter) ,(corner6[2] > node.Zcenter))
                    if not False in table:
                        list_list[level+1].append(node.negXnegYposZ)
                    table = ((corner7[0] < node.Xcenter),(corner7[1] < node.Ycenter) ,(corner7[2] < node.Zcenter))
                    if not False in table:
                        list_list[level+1].append(node.negXnegYnegZ)


                    #must remove children that aren't real yet
                    temp_templist = []
                    for node in list_list[level+1]:
                        try:
                           node.Xcenter  
                           temp_templist.append(node)
                        except AttributeError:
                            pass
                    list_list[level+1] = temp_templist
             

            payloads = [i.value for i in list_list[-1]]
            return payloads

                


    

