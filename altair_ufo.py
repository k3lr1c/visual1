# -*- coding: utf-8 -*-
"""Copia de Proyecto Visualizacion de informacion.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Im3D8_fFdOl1EPR1nnMy3hTC1he34Lwa

**Alumnos:**
- Roberto Araya
- Felipe Aguirre
- Tomas Vega
"""

import altair as alt
import pandas as pd
import numpy as np
import streamlit as st
from vega_datasets import data

df1 = pd.read_csv('https://raw.githubusercontent.com/Alpha-ari1/visual1/main/UFO_scrubbed.csv')

alt.data_transformers.disable_max_rows()

st.title("UFO Report")

st.text('Este reporte contiene más de 80.000 informes de avistamientos de ovnis durante el último siglo.')
st.text('Fuente: https://www.kaggle.com/datasets/NUFORC/ufo-sightings')


url = 'https://raw.githubusercontent.com/vega/datalib/master/test/data/world-110m.json'
#data.world_110m.url
countries = alt.topo_feature(url, 'countries')

input_dropdown = alt.binding_select(options=['cylinder', 'light', 'circle', 'sphere', 'disk', 'fireball',
       'unknown', 'oval', 'other', 'cigar', 'rectangle', 'chevron',
       'triangle', 'formation', 'delta', 'changing', 'egg',
       'diamond', 'flash', 'teardrop', 'cone', 'cross', 'pyramid',
       'round', 'crescent', 'flare', 'hexagon', 'dome', 'changed'], name='shape')
selection = alt.selection_single(fields=['shape'], bind=input_dropdown)

color_scale = alt.Scale(domain=['M', 'F'],
                        range=['#1FC3AA', '#8624F5'])

background = alt.Chart(countries).mark_geoshape(
    fill='lightgray',
    stroke='white'
).project(
    "equirectangular"
).properties(
    width=600,
    height=400
)

base = alt.Chart(df1).properties(
    width=250,
    height=250
).add_selection(selection)

points = base.mark_circle().encode(
    longitude='longitude :Q',
    latitude='latitude:Q',
    size=alt.value(10),
    tooltip='shape'
).add_selection(
    selection
).transform_filter(
    selection
)


hists = base.mark_bar().encode(
    x='datetime:T',
    y='count(datetime)'
).transform_filter(
    selection
).properties(
    width=600,
    height=400
)
#background + points | hists
st.altair_chart(background + points | hists, use_container_width=True)
