# -*- coding: utf-8 -*-
import pandas as pd
import plotly.graph_objects as go


india = "https://api.covid19india.org/csv/latest/case_time_series.csv"
india_daily = pd.read_csv(india)
india_daily['Daily Active'] = india_daily['Daily Confirmed'] - india_daily['Daily Deceased'] - india_daily[
    'Daily Recovered']
india_daily['Total Active'] = india_daily['Total Confirmed'] - india_daily['Total Recovered'] - india_daily[
    'Total Deceased']
test = "https://api.covid19india.org/csv/latest/tested_numbers_icmr_data.csv"
test_df = pd.read_csv(test)
conf_cummulative = india_daily.copy().drop(
    ['Daily Confirmed', 'Daily Recovered', 'Total Recovered', 'Daily Deceased', 'Total Deceased', 'Daily Active'],
    axis=1)
conf_cumm = go.Figure(data=[
    go.Scatter(x=conf_cummulative['Date'], y=conf_cummulative['Total Confirmed'], mode='lines+markers',
               line=dict(color='crimson'), marker=dict(color='crimson'))], )
conf_cumm.update_layout(xaxis=dict(showline=True,
                                   showgrid=True,
                                   showticklabels=True,
                                   linecolor='rgb(204,204,204)',
                                   linewidth=2,
                                   ticks='outside',
                                   tickfont=dict(family='Arial', size=12, color='rgb(82,82,82)', )),
                        yaxis=dict(showline=True,
                                   showgrid=True,
                                   showticklabels=True,
                                   linecolor='rgb(204,204,204)',
                                   linewidth=2, ),
                        autosize=True,
                        margin=dict(autoexpand=True, l=100, r=20, t=110, )
                        )
conf_cumm.layout.width = 650
conf_cumm.layout.height = 400
conf_cumm.layout.plot_bgcolor = "rgba(255, 0, 0, 0.4)"
active_cum = india_daily.copy().drop(
    ['Daily Confirmed', 'Total Confirmed', 'Daily Recovered', 'Total Recovered', 'Daily Deceased', 'Total Deceased',
     'Daily Active'], axis=1)
active_cumm = go.Figure(data=[
    go.Scatter(x=active_cum['Date'], y=active_cum['Total Active'], mode='lines+markers', line=dict(color='blue'),
               marker=dict(color='blue'))])
active_cumm.update_layout(xaxis=dict(showline=True,
                                     showgrid=True,
                                     showticklabels=True,
                                     linecolor='rgb(204,204,204)',
                                     linewidth=2,
                                     ticks='outside',
                                     tickfont=dict(family='Arial', size=12, color='rgb(82,82,82)', )),
                          yaxis=dict(showline=True,
                                     showgrid=True,
                                     showticklabels=True,
                                     linecolor='rgb(204,204,204)',
                                     linewidth=2, ),
                          autosize=True,
                          margin=dict(autoexpand=True, l=100, r=20, t=110, ),
                          )
active_cumm.layout.width = 650
active_cumm.layout.height = 400
active_cumm.layout.plot_bgcolor = "rgba(0,0,128,0.4)"

rec_cum = india_daily.copy().drop(
    ['Daily Confirmed', 'Daily Recovered', 'Total Confirmed', 'Daily Deceased', 'Total Deceased', 'Daily Active'],
    axis=1)
rec_cumm = go.Figure(data=[
    go.Scatter(x=rec_cum['Date'], y=rec_cum['Total Recovered'], mode='lines+markers', line=dict(color='green'),
               marker=dict(color='green'))])
rec_cumm.update_layout(xaxis=dict(showline=True,
                                  showgrid=True,
                                  showticklabels=True,
                                  linecolor='rgb(204,204,204)',
                                  linewidth=2,
                                  ticks='outside',
                                  tickfont=dict(family='Arial', size=12, color='rgb(82,82,82)', )),
                       yaxis=dict(showline=True,
                                  showgrid=True,
                                  showticklabels=True,
                                  linecolor='rgb(204,204,204)',
                                  linewidth=2, ),
                       autosize=True,
                       margin=dict(autoexpand=True, l=100, r=20, t=110, )
                       )
rec_cumm.layout.width = 650
rec_cumm.layout.height = 400
rec_cumm.layout.plot_bgcolor = "rgba(0,128,0,0.4)"

test_df_clean1 = test_df.copy().drop(
    ['Update Time Stamp', 'Sample Reported today', 'Total Individuals Tested', 'Total Positive Cases',
     'Tests conducted by Private Labs', 'Positive cases from samples reported', 'Source', 'Source 1',
     'Test positivity rate', 'Individuals Tested Per Confirmed Case', 'Tests Per Confirmed Case', 'Tests per million'],
    axis=1)
tested_cumm = go.Figure(data=[
    go.Scatter(x=test_df_clean1['Tested As Of'], y=test_df_clean1['Total Samples Tested'], mode='lines+markers',
               line=dict(color='purple'), marker=dict(color='purple'))])
tested_cumm.update_layout(xaxis=dict(showline=True,
                                     showgrid=True,
                                     showticklabels=True,
                                     linecolor='rgb(204,204,204)',
                                     linewidth=2,
                                     ticks='outside',
                                     tickfont=dict(family='Arial', size=12, color='rgb(82,82,82)', )),
                          yaxis=dict(showline=True,
                                     showgrid=True,
                                     showticklabels=True,
                                     linecolor='rgb(204,204,204)',
                                     linewidth=2, ),
                          autosize=True,
                          margin=dict(autoexpand=True, l=100, r=20, t=110, ),
                          )
tested_cumm.layout.width = 650
tested_cumm.layout.height = 400
tested_cumm.layout.plot_bgcolor = "rgba(128,0,128,0.4)"
dec_cum = india_daily.copy().drop(
    ['Daily Confirmed', 'Daily Recovered', 'Total Confirmed', 'Daily Deceased', 'Total Recovered', 'Daily Active'],
    axis=1)
dec_cummm = dec_cum.drop([138], axis=0)
dec_cumm = go.Figure(data=[
    go.Scatter(x=dec_cummm['Date'], y=dec_cummm['Total Deceased'], mode='lines+markers', line=dict(color='black'),
               marker=dict(color='black'))], )
dec_cumm.update_layout(xaxis=dict(showline=True,
                                  showgrid=True,
                                  showticklabels=True,
                                  linecolor='rgb(204,204,204)',
                                  linewidth=2,
                                  ticks='outside',
                                  tickfont=dict(family='Arial', size=12, color='rgb(82,82,82)', )),
                       yaxis=dict(showline=True,
                                  showgrid=True,
                                  showticklabels=True,
                                  linecolor='rgb(204,204,204)',
                                  linewidth=2, ),
                       autosize=True,
                       margin=dict(autoexpand=True, l=100, r=20, t=110, ))
dec_cumm.layout.width=650
dec_cumm.layout.height=400
dec_cumm.layout.plot_bgcolor="rgba(0,0,0,0.4)"


test_df_clean = test_df.copy().drop(
    ['Update Time Stamp', 'Total Samples Tested', 'Total Individuals Tested', 'Total Positive Cases',
     'Tests conducted by Private Labs', 'Positive cases from samples reported', 'Source', 'Source 1',
     'Test positivity rate', 'Individuals Tested Per Confirmed Case', 'Tests Per Confirmed Case', 'Tests per million'],
    axis=1)
tested_daily = go.Figure(data=[
    go.Bar(x=test_df_clean['Tested As Of'], y=test_df_clean['Sample Reported today'], marker=dict(color='purple'))])
tested_daily.update_layout(xaxis=dict(showline=True,
                                      showgrid=True,
                                      showticklabels=True,
                                      linecolor='rgb(204,204,204)',
                                      linewidth=2,
                                      ticks='outside',
                                      tickfont=dict(family='Arial', size=12, color='rgb(82,82,82)', )),
                           yaxis=dict(showline=True,
                                      showgrid=True,
                                      showticklabels=True,
                                      linecolor='rgb(204,204,204)',
                                      linewidth=2, ),
                           autosize=True,
                           margin=dict(autoexpand=True, l=100, r=20, t=110, ),
                           )
tested_daily.layout.width = 650
tested_daily.layout.height = 400
tested_daily.layout.plot_bgcolor = "rgba(128, 0, 128, 0.4)"

conf = india_daily.copy().drop(
    ['Total Confirmed', 'Daily Recovered', 'Total Recovered', 'Daily Deceased', 'Total Deceased'], axis=1)
confirmed = go.Figure(data=[go.Bar(x=conf['Date'], y=conf['Daily Confirmed'], marker=dict(color='crimson'))])
confirmed.update_layout(xaxis=dict(showline=True,
                                   showgrid=True,
                                   showticklabels=True,
                                   linecolor='rgb(204,204,204)',
                                   linewidth=2,
                                   ticks='outside',
                                   tickfont=dict(family='Arial', size=12, color='rgb(82,82,82)', )),
                        yaxis=dict(showline=True,
                                   showgrid=True,
                                   showticklabels=True,
                                   linecolor='rgb(204,204,204)',
                                   linewidth=2, ),
                        autosize=True,
                        margin=dict(autoexpand=True, l=100, r=20, t=110, ),
                        )
confirmed.layout.width = 650
confirmed.layout.height = 400
confirmed.layout.plot_bgcolor = "rgba(255, 0, 0, 0.4)"

rec = india_daily.copy().drop(
    ['Total Confirmed', 'Daily Confirmed', 'Total Recovered', 'Daily Deceased', 'Total Deceased'], axis=1)
recovered = go.Figure(data=[go.Bar(x=rec['Date'], y=rec['Daily Recovered'], marker=dict(color='green'))])
recovered.update_layout(xaxis=dict(showline=True,
                                   showgrid=True,
                                   showticklabels=True,
                                   linecolor='rgb(204,204,204)',
                                   linewidth=2,
                                   ticks='outside',
                                   tickfont=dict(family='Arial', size=12, color='rgb(82,82,82)', )),
                        yaxis=dict(showline=True,
                                   showgrid=True,
                                   showticklabels=True,
                                   linecolor='rgb(204,204,204)',
                                   linewidth=2, ),
                        autosize=True,
                        margin=dict(autoexpand=True, l=100, r=20, t=110, ),
                        )
recovered.layout.width = 650
recovered.layout.height = 400
recovered.layout.plot_bgcolor = "rgba(0,128,0,0.4)"

active = india_daily.copy().drop(
    ['Total Confirmed', 'Daily Confirmed', 'Total Recovered', 'Daily Deceased', 'Total Deceased', 'Daily Recovered'],
    axis=1)
actived = go.Figure(data=[go.Bar(x=active['Date'], y=active['Daily Active'], marker=dict(color='blue'))])
actived.update_layout(xaxis=dict(showline=True,
                                 showgrid=True,
                                 showticklabels=True,
                                 linecolor='rgb(204,204,204)',
                                 linewidth=2,
                                 ticks='outside',
                                 tickfont=dict(family='Arial', size=12, color='rgb(82,82,82)', )),
                      yaxis=dict(showline=True,
                                 showgrid=True,
                                 showticklabels=True,
                                 linecolor='rgb(204,204,204)',
                                 linewidth=2, ),
                      autosize=True,
                      margin=dict(autoexpand=True, l=100, r=20, t=110, ),
                      )
actived.layout.width = 650
actived.layout.height = 400
actived.layout.plot_bgcolor = "rgba(0,0,128,0.4)"

death = india_daily.copy().drop(
    ['Daily Confirmed', 'Daily Recovered', 'Total Confirmed', 'Total Deceased', 'Total Recovered'], axis=1)
deaded = death.drop([138], axis=0)
dead = go.Figure(data=[go.Bar(x=deaded['Date'], y=deaded['Daily Deceased'], marker=dict(color='black'))])
dead.update_layout(xaxis=dict(showline=True,
                              showgrid=True,
                              showticklabels=True,
                              linecolor='rgb(204,204,204)',
                              linewidth=2,
                              ticks='outside',
                              tickfont=dict(family='Arial', size=12, color='rgb(82,82,82)', )),
                   yaxis=dict(showline=True,
                              showgrid=True,
                              showticklabels=True,
                              linecolor='rgb(204,204,204)',
                              linewidth=2, ),
                   autosize=True,
                   margin=dict(autoexpand=True, l=100, r=20, t=110, ),
                   )
dead.layout.width = 650
dead.layout.height = 400
dead.layout.plot_bgcolor = "rgba(0,0,0,0.4)"


# final graphs

# CUMMULATIVE GRAPHS
graph_conf_final_cumm = conf_cumm
graph_act_final_cumm = active_cumm
graph_rec_final_cumm = rec_cumm
graph_dead_final_cumm = dec_cumm
graph_tests_final_cumm = tested_cumm
# DAILY GRAPHS
graph_conf_final_daily = confirmed
graph_act_final_daily = actived
graph_rec_final_daily = recovered
graph_dead_final_daily = dead
graph_test_final_daily = tested_daily

