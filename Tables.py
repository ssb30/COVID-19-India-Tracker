import pandas as pd

link = "https://api.covid19india.org/csv/latest/state_wise.csv"
df = pd.read_csv(link)
india_df = df.copy().drop(
    ['Last_Updated_Time', 'Migrated_Other', 'State_code', 'Delta_Confirmed', 'Delta_Recovered', 'Delta_Deaths',
     'State_Notes'], axis=1)
india_df1 = india_df.drop([0])
india_df1['Confirmed'] = india_df1['Confirmed'].astype('int64').apply(lambda x: "{:,}".format(x))
india_df1['Recovered'] = india_df1['Recovered'].astype('int64').apply(lambda x: "{:,}".format(x))
india_df1['Deaths'] = india_df1['Deaths'].astype('int64').apply(lambda x: "{:,}".format(x))
india_df1['Active'] = india_df1['Active'].astype('int64').apply(lambda x: "{:,}".format(x))
final_frame = india_df1
new_df = pd.read_csv(link)
india_new = df.copy().drop(
    ['Last_Updated_Time', 'Migrated_Other', 'State_code', 'Delta_Confirmed', 'Delta_Recovered', 'Delta_Deaths',
     'State_Notes'], axis=1)
india_new1 = india_new.drop([0])
confirmed = india_new1['Confirmed'].sum()
active = india_new1['Active'].sum()
recovered = india_new1['Recovered'].sum()
deaths= india_new1['Deaths'].sum()
confirmed_table = '{:,.0f}'.format(confirmed)
active_table = '{:,.0f}'.format(active)
recovered_table = '{:,.0f}'.format(recovered)
deaths_table = '{:,.0f}'.format(deaths)
print(confirmed_table)