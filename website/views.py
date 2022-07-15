import pandas as pd
from flask import Flask, render_template, redirect, request, url_for, session, flash, Blueprint
import json
import pandas

views = Blueprint("views", __name__)

def stack_index(index):
    for keys, values in relations.items():
      for value in values:
          if index in values:
            if value == index:
                twink = value
                del values[values.index(index)]
                values.append(twink)

with open('./data/shall_pass.json') as file:
   shall_pass = json.load(file)
   print(shall_pass)

with open('./data/relations.json') as file:
   relations = json.load(file)
   print(relations)

df = pd.read_csv("./data/selection.csv")
@views.route('/')
def home():
    return render_template('first.html', df=df, shall_pass=shall_pass, relations=relations)

@views.route('/article/<index>')
def second(index):

    index = int(index)
    str_index = str(index)
    stack_index(index)
    return render_template('second.html', df=df, shall_pass=shall_pass, relations=relations,
                           index=index, str_index=str_index)
