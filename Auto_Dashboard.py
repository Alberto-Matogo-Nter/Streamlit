import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(layout='wide')
path='clean_auto_mpg.csv'
df=pd.read_csv(path,sep=',')

#function
def metric_calculatio(df_metric,unique_origin):

    df_tab=df_metric
    avg_mpg=round(df_tab['mpg'].mean(),1)
    avg_mpg=round(df_tab['displacement'].mean(),1)
    avg_mpg=round(df_tab['horsepower'].mean(),1)
    avg_mpg=round(df_tab['weight'].mean(),1)

    col1,col2,col3,col4=st.columns([1,1,1,1])
    col1.metric(label='Avg MPG', value=avg_mpg)
    col2.metric(label='Avg Displacement', value=avg_mpg)
    col3.metric(label='Avg Horsepower', value=avg_mpg)
    col4.metric(label='Avg Weight', value=avg_mpg)
    col5,col6=st.columns([4,2])
    scatter=px.scatter(data_frame=df_tab,
                       x='weight',
                       y='horsepower',
                       size='displacement',
                       hover_name='car name',
                       color='cylinders',
                       title='Weight vs HP for cars from {}'.format(unique_origin))
    
    histrogram=px.histogram(data_frame=df_tab,
                            x='mpg',
                            title='MPG Distribution')
    col5.plotly_chart(scatter)
    col6.plotly_chart(histrogram)


unique_origin=list(df['origin'].unique())
unique_origin.sort()
unique_origin_str=['Origin: ' + str(origin) for origin in unique_origin]

#add tabs
tab1,tab2,tab3=st.tabs([unique_origin_str[0],
                        unique_origin_str[1],
                        unique_origin_str[2]
])

with tab1:
    st.subheader(unique_origin_str[0])
    df_tab=df[df['origin']==unique_origin[0]]
    metric_calculatio(df_tab, unique_origin[0])

with tab2:
    st.subheader(unique_origin_str[1])
    df_tab=df[df['origin']==unique_origin[1]]
    metric_calculatio(df_tab, unique_origin[1])


with tab3:
    st.subheader(unique_origin_str[2])
    df_tab=df[df['origin']==unique_origin[2]]
    metric_calculatio(df_tab, unique_origin[2])

