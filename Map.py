import pandas as pd
import plotly.graph_objects as go
link = "https://api.covid19india.org/csv/latest/state_wise.csv"
df = pd.read_csv(link)
df1 =df.replace(['Jammu and Kashmir'], ['Jammu & Kashmir'])

fig = go.Figure(data=go.Choropleth(
    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
    featureidkey='properties.ST_NM',
    locationmode='geojson-id',
    locations=df1['State'],
    z=df1['Active'],

    autocolorscale=False,
    colorscale='Reds',
    marker_line_color='peachpuff',


))
colorbar = dict(
    title={'text': "Active Cases"},

    thickness=15,
    len=0.35,
    bgcolor='rgba(255,255,255,0.6)',

    tick0=0,
    dtick=20000,

    xanchor='left',
    x=0.01,
    yanchor='bottom',
    y=0.05)

fig.update_geos(
    visible=False,
    projection=dict(
        type='conic conformal',
        parallels=[12.472944444, 35.172805555556],
        rotation={'lat': 24, 'lon': 80}
    ),
    lonaxis={'range': [68, 98]},
    lataxis={'range': [6, 38]}
)

fig.update_layout(
    title=dict(
        text="Active COVID-19 Cases in India by State",
        xanchor='center',
        x=0.5,
        yref='paper',
        yanchor='bottom',
        y=1,
        pad={'b': 10}
    ),
    margin={'r': 0, 't': 30, 'l': 0, 'b': 0},

)

fig.layout.xaxis.fixedrange=True
fig.layout.yaxis.fixedrange=True
Map=fig
