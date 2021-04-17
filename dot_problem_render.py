# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 15:25:50 2021

@author: Julien
"""

#imports
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import dot_problem

def draw_link(a, b, lvl, ax):
    #patches.Arc(xy, width, height, angle=0.0, theta1=0.0, theta2=360.0)
    center = (a+b)/2,0
    width = abs(a-b)
    height = 2*abs(lvl)
    angle = 0
    if lvl>0 :
        theta1 = 0
        theta2 = 180
    else :
        theta1 = 180
        theta2 = 360
    
    arc = Arc(center, width, height, angle, theta1, theta2)
    ax.add_patch(arc)

def draw_dots(N, ax):
    ax.scatter(np.arange(N), np.zeros(N), c='k', s=5)

def draw_path(path, ax):
    up = 1
    for i in range(len(path)-1):
        a,b = path[i],path[i+1]
        lvl = abs(a-b)*0.5*up
        draw_link(a, b, lvl, ax)
        up*=-1

def draw_one(path):
    N = len(path)
    fig, ax = plt.subplots()
    ax.set_xlim(-0.5,N-0.5)
    draw_dots(N, ax)
    draw_path(path, ax)
    plt.show()

def draw_all(paths):
    N = len(paths[0])
    n_rows, n_cols = display_arr(len(paths))
    fig, ax = plt.subplots(n_rows, n_cols, sharex=True)
    for i in range(n_rows) :
        for j in range(n_cols):
            ax[i,j].axis('off')
            if i*n_cols+j < len(paths) :
                ax[i,j].set_xlim(-0.5,N-0.5)
                draw_dots(N, ax[i,j])
                draw_path(paths[i*n_cols+j], ax[i,j])
    plt.show()

def display_arr(M):
    a = int(np.sqrt(M))
    b = a
    while a*b <= M :
        b+=1
    return (b,a)

if __name__ == '__main__' :
    paths = dot_problem.get_paths(5)
    draw_all(paths)
    # draw_one(paths[0])