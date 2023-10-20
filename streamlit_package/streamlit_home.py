import mysql.connector
import pandas as pd
import plotly.express as px
import streamlit as st

# st.image(Image.open(r"PhonePe-Logo.png"), width=100)
st.title("PhonePe Pulse Data Visualization")

conn = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    password='root',
    database='phonepe_visual'
)

cursor = conn.cursor()


def aggregated_transaction_state_wise(data):
    y = st.selectbox("select  :", ["State Wise", "Year Wise"])
    fig = px.choropleth(data,
                        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                        featureidkey='properties.ST_NM',
                        locations='alter_state',
                        color=y,
                        color_continuous_scale='Reds'
                        )

    fig.update_geos(fitbounds="locations", visible=False)
    return fig


def state_list(cursor, key):
    query = "SELECT * FROM States"
    cursor.execute(query)
    result = cursor.fetchall()
    state_names = [state[2] for state in result]
    option = st.selectbox('Select the state', state_names, key=key)
    return option


def transaction_list(cursor, key):
    query = "SELECT * FROM TransactionTypes"
    cursor.execute(query)
    result = cursor.fetchall()
    transaction_names = [transaction[1] for transaction in result]
    option = st.selectbox('Select the Transaction', transaction_names, key=key)
    return option


def brand_list(cursor, key):
    query = "SELECT * FROM DeviceBrands"
    cursor.execute(query)
    result = cursor.fetchall()
    device_names = [device[1] for device in result]
    option = st.selectbox('Select the Device', device_names, key=key)
    return option


def district_list(cursor, state_name, key):
    query = "select district_value from Districts d left join States s on d.state_id = s.id where s.state_value = %s"
    cursor.execute(query, (state_name,))
    result = cursor.fetchall()
    district_name = [district[0] for district in result]
    option = st.selectbox('Select the District', district_name, key=key)
    return option


def aggregated_transaction_state_and_transaction_wise(cursor, state_selected, transaction_selected):
    query = """SELECT
            DISTINCT ASD.COUNT, ASD.AMOUNT, ASD.YEAR_WITH_QUARTER, TT.TYPES AS TRANSACTION_TYPE, S.STATE_VALUE
            FROM PHONEPE_VISUAL.AggregatedTransactionDetails ASD
            INNER JOIN PHONEPE_VISUAL.STATES S ON ASD.STATE_ID = S.ID 
            INNER JOIN PHONEPE_VISUAL.TransactionTypes TT ON ASD.TRANSACTION_TYPE_ID = TT.ID
            WHERE S.STATE_VALUE = %s AND TT.TYPES = %s
            ORDER BY ASD.YEAR_WITH_QUARTER ASC"""
    cursor.execute(query, (state_selected, transaction_selected,))
    result = cursor.fetchall()
    return result


def display_aggregated_transaction_data(data):
    df = pd.DataFrame(data, columns=['Count', 'Amount', 'Year_Quarter', 'Transaction_Types', 'State'])
    df['Amount'] = df['Amount'].apply(float)
    print(df)
    fig = px.choropleth(
        df,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='State',
        color='Amount',
        hover_name='State',
        hover_data=['Transaction_Types', 'Count', 'Amount', 'Year_Quarter'],
        animation_frame='Year_Quarter',
        title='Aggregated Transaction by Each Quarter for Each State',
        color_continuous_scale='Sunsetdark',
        range_color=(0, 9999999999)
    )
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(width=900, height=800)
    fig.update_layout(title_font=dict(size=25), title_font_color='#801D70')
    return fig


def aggregated_transaction_state_and_user_wise(cursor, state_selected, brand_selected):
    query = """SELECT
           DISTINCT ASD.COUNT, ASD.PERCENTAGE , ASD.REGISTERED_USER , ASD.YEAR_WITH_QUARTER, DB.BRAND_NAME  AS BRAND_NAME, S.STATE_VALUE
            FROM PHONEPE_VISUAL.AGGREGATEDUSERDETAILS ASD
            INNER JOIN PHONEPE_VISUAL.STATES S ON ASD.STATE_ID = S.ID 
            INNER JOIN PHONEPE_VISUAL.DEVICEBRANDS DB ON ASD.BRAND_NAMES_ID  = DB.ID
            WHERE S.STATE_VALUE = %s AND DB.BRAND_NAME = %s
            ORDER BY ASD.YEAR_WITH_QUARTER ASC"""
    cursor.execute(query, (state_selected, brand_selected,))
    result = cursor.fetchall()
    return result


def display_aggregated_user_data(data):
    df = pd.DataFrame(data, columns=['Count', 'Percentage', 'Registered User', 'Year_Quarter', 'Brand Name', 'State'])
    print(df)
    fig = px.choropleth(
        df,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='State',
        color='Registered User',
        hover_name='State',
        hover_data=['Count', 'Percentage', 'Registered User', 'Year_Quarter', 'Brand Name', 'State'],
        animation_frame='Year_Quarter',
        title='Aggregated User by Each Quarter for Each State',
        color_continuous_scale='Sunsetdark',
        range_color=(0, 9999999999)
    )
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(width=900, height=800)
    fig.update_layout(title_font=dict(size=25), title_font_color='#801D70')
    return fig


def map_transaction_state_and_transaction_wise(cursor, state_selected, district_selected):
    query = """SELECT
            DISTINCT ASD.COUNT, ASD.AMOUNT, ASD.YEAR_WITH_QUARTER, D.DISTRICT_VALUE, S.STATE_VALUE
            FROM PHONEPE_VISUAL.MAPTRANSACTIONDETAILS ASD
            INNER JOIN PHONEPE_VISUAL.STATES S ON ASD.STATE_ID = S.ID 
            INNER JOIN PHONEPE_VISUAL.DISTRICTS D ON ASD.DISTRICT_ID  = D.ID
            WHERE S.STATE_VALUE = %s AND D.DISTRICT_VALUE = %s
            ORDER BY ASD.YEAR_WITH_QUARTER ASC"""
    cursor.execute(query, (state_selected, district_selected,))
    result = cursor.fetchall()
    return result


def display_map_transaction_data(data):
    df = pd.DataFrame(data, columns=['Count', 'Amount', 'Year_Quarter', 'District', 'State'])
    df['Amount'] = df['Amount'].apply(float)
    print(df)
    fig = px.choropleth(
        df,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='State',
        color='Amount',
        hover_name='State',
        hover_data=['Count', 'Amount', 'Year_Quarter', 'District', 'State'],
        animation_frame='Year_Quarter',
        title='Map Transaction by Each Quarter for Each State',
        color_continuous_scale='Sunsetdark',
        range_color=(0, 9999999999)
    )
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(width=900, height=800)
    fig.update_layout(title_font=dict(size=25), title_font_color='#801D70')
    return fig


def map_transaction_state_and_user_wise(cursor, state_selected, district_selected):
    query = """SELECT DISTINCT asd.registered_user, asd.app_opens, asd.year_with_quarter, s.state_value
                FROM PHONEPE_VISUAL.MapUserDetails ASD INNER JOIN PHONEPE_VISUAL.STATES S ON ASD.STATE_ID = S.ID
                INNER JOIN PHONEPE_VISUAL.DISTRICTS D ON ASD.DISTRICT_ID = D.ID
                WHERE S.STATE_VALUE = %s AND D.DISTRICT_VALUE = %s
                ORDER BY ASD.YEAR_WITH_QUARTER ASC"""
    cursor.execute(query, (state_selected, district_selected,))
    result = cursor.fetchall()
    return result


def display_map_user_data(data):
    df = pd.DataFrame(data, columns=['Registered_User', 'App_Opens', 'Year_Quarter', 'State'])
    print(df)
    fig = px.choropleth(
        df,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='State',
        color='App_Opens',
        hover_name='State',
        hover_data=['Registered_User', 'App_Opens', 'Year_Quarter', 'State'],
        animation_frame='Year_Quarter',
        title='Map User by Each Quarter for Each State',
        color_continuous_scale='Sunsetdark',
        range_color=(0, 9999999999)
    )
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(width=900, height=800)
    fig.update_layout(title_font=dict(size=25), title_font_color='#801D70')
    return fig


def top_transaction_state_and_transaction_wise(cursor, state_selected, district_selected):
    query = """SELECT
            DISTINCT ASD.COUNT, ASD.AMOUNT, ASD.YEAR_WITH_QUARTER, D.DISTRICT_VALUE, S.STATE_VALUE
            FROM PHONEPE_VISUAL.TOPDISTRICTTRANSACTIONDETAILS ASD
            INNER JOIN PHONEPE_VISUAL.STATES S ON ASD.STATE_ID = S.ID 
            INNER JOIN PHONEPE_VISUAL.DISTRICTS D ON ASD.DISTRICT_ID  = D.ID
            WHERE S.STATE_VALUE = %s AND D.DISTRICT_VALUE = %s
            ORDER BY ASD.YEAR_WITH_QUARTER ASC"""
    cursor.execute(query, (state_selected, district_selected,))
    result = cursor.fetchall()
    return result


def display_top_transaction_data(data):
    df = pd.DataFrame(data, columns=['Count', 'Amount', 'Year_Quarter', 'District', 'State'])
    df['Amount'] = df['Amount'].apply(float)
    print(df)
    fig = px.choropleth(
        df,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='State',
        color='Amount',
        hover_name='State',
        hover_data=['Count', 'Amount', 'Year_Quarter', 'District', 'State'],
        animation_frame='Year_Quarter',
        title='Top Transaction by Each Quarter for Each State',
        color_continuous_scale='Sunsetdark',
        range_color=(0, 9999999999)
    )
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(width=900, height=800)
    fig.update_layout(title_font=dict(size=25), title_font_color='#801D70')
    return fig


def top_transaction_state_and_user_wise(cursor, state_selected, district_selected):
    query = """SELECT DISTINCT asd.registered_user, asd.year_with_quarter, s.state_value
                FROM PHONEPE_VISUAL.TopDistrictUserDetails ASD INNER JOIN PHONEPE_VISUAL.STATES S ON ASD.STATE_ID = S.ID
                INNER JOIN PHONEPE_VISUAL.DISTRICTS D ON ASD.DISTRICT_ID = D.ID
                WHERE S.STATE_VALUE = %s AND D.DISTRICT_VALUE = %s
                ORDER BY ASD.YEAR_WITH_QUARTER ASC"""
    cursor.execute(query, (state_selected, district_selected,))
    result = cursor.fetchall()
    return result


def display_top_user_data(data):
    df = pd.DataFrame(data, columns=['Registered_User', 'Year_Quarter', 'State'])
    print(df)
    fig = px.choropleth(
        df,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='State',
        color='Registered_User',
        hover_name='State',
        hover_data=['Registered_User', 'Year_Quarter', 'State'],
        animation_frame='Year_Quarter',
        title='Top User by Each Quarter for Each State',
        color_continuous_scale='Sunsetdark',
        range_color=(0, 99999999)
    )
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(width=900, height=800)
    fig.update_layout(title_font=dict(size=25), title_font_color='#801D70')
    return fig


aggregated_tab, map_tab, top_tab = st.tabs(["Aggregated", "Map", "Top"])

with aggregated_tab:
    aggregated_transaction_tab, aggregated_user_tab = st.tabs(["Aggregated Transaction", "Aggregated User"])
    with aggregated_transaction_tab:
        state_selected = state_list(cursor, 'aggregated_transaction_1')
        transaction_selected = transaction_list(cursor, 'aggregated_transaction_2')
        data = aggregated_transaction_state_and_transaction_wise(cursor, state_selected, transaction_selected)
        fig = display_aggregated_transaction_data(data)
        st.plotly_chart(fig)
    with aggregated_user_tab:
        state_selected = state_list(cursor, 'aggregated_user_1')
        brand_selected = brand_list(cursor, 'aggregated_user_2')
        data = aggregated_transaction_state_and_user_wise(cursor, state_selected, brand_selected)
        fig = display_aggregated_user_data(data)
        st.plotly_chart(fig)
with map_tab:
    map_transaction_tab, map_user_tab = st.tabs(["Map Transaction", "Map User"])
    with map_transaction_tab:
        state_selected = state_list(cursor, 'map_transaction_1')
        district_selected = district_list(cursor, state_selected, 'map_transaction_2')
        data = map_transaction_state_and_transaction_wise(cursor, state_selected, district_selected)
        fig = display_map_transaction_data(data)
        st.plotly_chart(fig)
    with map_user_tab:
        state_selected = state_list(cursor, 'map_transaction_3')
        district_selected = district_list(cursor, state_selected, 'map_transaction_4')
        data = map_transaction_state_and_user_wise(cursor, state_selected, district_selected)
        fig = display_map_user_data(data)
        st.plotly_chart(fig)
with top_tab:
    top_transaction_tab, top_user_tab = st.tabs(["Top Transaction", "Top User"])
    with top_transaction_tab:
        state_selected = state_list(cursor, 'top_transaction_1')
        district_selected = district_list(cursor, state_selected, 'top_transaction_2')
        data = top_transaction_state_and_transaction_wise(cursor, state_selected, district_selected)
        fig = display_top_transaction_data(data)
        st.plotly_chart(fig)
    with top_user_tab:
        state_selected = state_list(cursor, 'top_transaction_3')
        district_selected = district_list(cursor, state_selected, 'top_transaction_4')
        data = top_transaction_state_and_user_wise(cursor, state_selected, district_selected)
        fig = display_top_user_data(data)
