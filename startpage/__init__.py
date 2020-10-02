print('startpage')
from core import app

import controller

import model

import os, jinja2

my_loader = jinja2.ChoiceLoader(
    [app.jinja_loader,
     jinja2.FileSystemLoader([os.path.abspath(os.path.dirname(__file__))+'/templates'])]
)
app.jinja_loader = my_loader
