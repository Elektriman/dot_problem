# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 10:09:55 2021

@author: Julien
"""

import numpy as np

class path_tree :
    """
    a static class that will help construct the path
    It has no purpose other than having a standard OOP-style tree construction
    """
    pass
    

class path_tree_filled(path_tree):
    """
    a class to contruct a non-binary tree to seek paths
    each instance will be either a node or a leaf of the tree
    """
    
    N = 0 #number of dots
    paths = [] #list of paths, valid or not
    
    def __init__(self, val, path):
        """
        creates a filled tree node carrying the value 'val'
        this is where the recursion of the 'build_tree' method occurs

        Parameters
        ----------
        val : int
            the value of the node
        path : list
            the path that lead to this point

        """
        self.v = val
        self.path = path + [val]
        self.branches = self.build_tree()
    
    #tree specific methods
    def is_empty():
        return False
    
    def is_leaf(self):
        return isinstance(self.branches, path_tree_empt)
    
    def build_tree(self):
        """
        a recursive method that builds the tree and fills the list of paths

        Returns
        -------
        path_tree_empt object or a tuple of path_tree_filled objects
            this represents the branches attached to the node. 
            A path_tree_empt object represents the end of a path
            A tuple of path_tree_filled objects represents all the sub-branches attached
        """
        #this is a mask that accounts for all the values already visited in the previous nodes
        mask = np.array([not val in self.path for val in np.arange(self.N)])
        
        #from that mask we can retrieve the remaining values that we can visit
        remaining_values = np.arange(self.N)[mask]
        
        #initiating an empty branch list that will be completed
        branches = []
        
        for j in remaining_values :
            if abs(self.path[-1]-j)>1 : #checking if the dots are not next to each other
                """this is where the recursion occurs (the constructor and the build_tree methods call each other)"""
                branches.append(path_tree_filled(j, self.path)) #if found, adding a new way to our path
        
        if len(branches)==0 : #no branches found means its the end of the path
            self.paths.append(self.path) #adding the path to the list
            return path_tree_empt() #setting an empty tree object at the end of the path
        else :
            return tuple(branches) #returning the branches
    
    @classmethod
    def set_N(cls, N):
        """
        a setter for the static sttribute N that is often used in the program

        Parameters
        ----------
        cls : class
            this is a class method so we can access the class attributes using this shortcut
        N : int
            the number of dots
        """
        cls.N = N
    
    @classmethod
    def sort_paths(cls):
        """
        this static method will retrieve only the paths that correspond to the following criterias :
            - a path has to go throught all the points
            - two paths are considered the same if they go throught the same points when the order of the dots is reversed (so only one will be kept)
        
        Parameters
        ----------
        cls : class
            this is a class method so we can access the class attributes using this shortcut
            in this case, we need to access the 'paths' list
        """
        result = [] #storing the paths that got filtered throught
        for p in cls.paths :
            if len(p)==cls.N : #checking the length first
                """
                the reverse path is the direct reverse of one path, but we also have to change the numbers to make the reverse path comparable to the others
                example :
                    [1, 3, 0, 2, 4] is a valid path
                    [4, 2, 0, 3, 1] is the direct reverse
                    but because we only compute paths that start at indexes under N//2, the correct inverse path is
                    [0, 2, 4, 1, 3]
                    (this is why we have to compute N-i-1 instead of just reversing the path)
                """
                reverse_path = [cls.N-p[i]-1 for i in range(len(p)-1, -1, -1)]
                if not reverse_path in result : #checking if the reverse path has already been added to the final list
                    result.append(p)
        return result

class path_tree_empt(path_tree):
    """
    this class has no purpose other than having clean OOP tree code
    """
    
    def __init__(self):
        """
        this is an empty node so every attribute is set to None
        """
        self.v = None
        self.path = None
        self.branches = None
    
    #tree specific methods
    def is_empty():
        return True
    
    def is_leaf():
        return False

def show(N, show_list=False):
    """
    this function shows the number of different paths that can be made with N points
    
    Parameters
    ----------
    N : int
        the number of dots
    show_list : boolean
        whether or not you want the function to print all the different paths it found
    
    Returns
    -------
    None.
    """
    path_tree_filled.set_N(N) #setting N
    
    trees = [] #each starting point has its own tree of possible paths
    for i in range(N//2): #going untill N//2 to avoid computing the same paths
        trees.append(path_tree_filled(i, []))
        
    final_list = path_tree_filled.sort_paths()
    if show_list :
        for p in final_list :
            print(p)
    
    print(len(final_list))

if __name__ == "__main__" :
    N = 6
    for i in range(4,N+1):
        show(i)