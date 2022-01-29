from re import M
from turtle import color
from matplotlib import markers
import matplotlib.pyplot as plt
import numpy as np

def line():
        xs=input("Enter the X-label: ")
        ys=input("Enter the Y-label: ")
        ts=input("Enter the title of the graph : ")
        c=input("Enter the color of the line : ")
        li=input("Enter the line style you want : ")
        m=input("Enter the marker you want to apply : ")
        a=list(map(int,input("Enter x-axis values: ").split()))
        b=list(map(int,input("Enter y-axis values: ").split()))
        plt.xlabel(xs)
        plt.ylabel(ys)
        plt.title(ts)
        x=np.array(a)
        y=np.array(b)
        plt.plot(x,y,color=c,ls=li,marker=m)
        plt.show()
def bar():
        xs=input("Enter the X-label: ")
        ys=input("Enter the Y-label: ")
        ts=input("Enter the title of the graph : ")
        a=list(input("Enter x-axis values: \n").split())
        b=list(map(int,input("Enter y-axis values: ").split()))
        x=np.array(a)
        y=np.array(b)
        plt.xlabel(xs)
        plt.ylabel(ys)
        plt.title(ts)
        plt.bar(x,y)
        plt.show()
def pie():
        ts=input("Please enter a title for your pie chart :\n")
        a=list(map(int,input("Enter the values : ").split()))
        b=list(input("Enter the lebels to corresponding values : \n").split())
        c=np.array(a)
        plt.pie(c,labels=b)
        plt.title(ts)
        e=input("Do you want legend on pie chart?(y/n) : ")
        if e=='y':
                plt.legend()
        plt.show()