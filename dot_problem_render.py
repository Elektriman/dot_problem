# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 15:25:50 2021

@author: Julien
"""
"""
Thanks ! Also, I was able to make a renderer that just plots every path possible for a number of dots. It may be usefull if you wanna compare your man
"""

#imports
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import dot_problem

def draw_link(a, b, lvl, ax):
    """
    a functions that will draw the arc between two points a and b on the object ax

    Parameters
    ----------
    a,b : int, int
        the two points to link
    lvl : float
        the way the line goes over :
            • 0.5 means the farthest point from the line made b the dots will be at distance 0.5
            • -0.5 means the same but the line will go under the set of points
    ax : matplotlib.axes
        the axis object on which to plot the ellipsis
        also, the matplitlib.patches.Arc function needs to be plotted on an axis object as specified on the documentation
    """
    center = (a+b)/2,0 #the center of the ellipsis
    width = abs(a-b) #the width of the ellipsis
    height = 2*abs(lvl) #the height of the ellipsis
    angle = 0 #the ellipsis is not rotated
    
    #because the function traces the ellipsis in the trigonometric order
    #we need to adjust starting and anding angles to trace the correct portion of the ellipsis
    
    if lvl>0 : #if the curve goes over
        theta1 = 0
        theta2 = 180
    else : #if the curve goes under
        theta1 = 180
        theta2 = 360
    
    arc = Arc(center, width, height, angle, theta1, theta2) #create the ellipsis object
    ax.add_patch(arc) #tracing the ellipsis

def draw_dots(N, ax):
    """
    draw the dots for the problem

    Parameters
    ----------
    N : int
        the number of dots we need to display.
    ax : matplotlib.axis
        the axis object on which to plot the points.
    """
    ax.scatter(np.arange(N), np.zeros(N), c='k', s=5)

def draw_path(path, ax):
    """
    the function that draws the entire path

    Parameters
    ----------
    path : list
        the list of integers that represent the path we want to display.
    ax : matplotlib.axis
        the axis object on which to plot the path.
    """
    up = 1 #this variable will alternate between 1 and -1 to make the lines loop around
    for i in range(len(path)-1):
        a,b = path[i],path[i+1] #recovering the abscisses
        lvl = abs(a-b)*0.5*up #computing a level following how far the two points are appart
        draw_link(a, b, lvl, ax) #draw the link
        up*=-1 #reverse the side

def draw_one(path):
    """
    draw one path on the figure

    Parameters
    ----------
    path : list
        the list of integers that represent the path to display.
    """
    N = len(path)
    
    fig, ax = plt.subplots() #new figure
    ax.set_xlim(-0.5,N-0.5) #custom x limits for a beter view
    #y limits are not customised because its hard to manually get a nice view for each path
    draw_dots(N, ax)
    draw_path(path, ax)
    plt.show()

def draw_all(paths):
    """
    draw all the paths from a list of paths

    Parameters
    ----------
    paths : nested list
        a list of paths to display.
    """
    N = len(paths[0]) #number of dots
    n_rows, n_cols = display_arr(len(paths)) #compute the shape of the subplots
    fig, ax = plt.subplots(n_rows, n_cols, sharex=True) #create a subplotted figure
    
    for i in range(n_rows) :
        for j in range(n_cols):
            ax[i,j].axis('off') #disable the axis for a clean view
            
            if i*n_cols+j < len(paths) : #avoiding indexOutOfRange error
                ax[i,j].set_xlim(-0.5,N-0.5) #custom x limits for a beter view
                #y limits are not customised because its hard to manually get a nice view for each path
                draw_dots(N, ax[i,j])
                draw_path(paths[i*n_cols+j], ax[i,j])
    plt.show()

def display_arr(M):
    """
    computes the best way to display M figures on a screen in a grid that is as close to a square as possible

    Parameters
    ----------
    M : int
        the number of subplots to display.

    Returns
    -------
    a,b : (int,int)
        the tuple of (rows,columns) that are optimised to display M plots close to a square shape

    """
    a = int(np.sqrt(M)) #takin the floor of the square root
    #a² must be just below M, or equal if M is a perfect square number
    b = a
    while a*b <= M : #incrementing the number of rows untill we can fit everything
        b+=1 
    return (b,a)

if __name__ == '__main__' :
    paths = dot_problem.get_paths(5)
    draw_all(paths)
    # draw_one(paths[0])