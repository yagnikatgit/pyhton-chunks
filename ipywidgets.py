'''

Runs only in Jupyter Notebook.

'''
from ipywidgets import interactive
import ipywidgets as widgets
from IPython.display import display

def func(a,b):
	display(a**b)
	return a**b

out = interactive(func,a=10,b=15)
display(out) 
