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
    # return fig.show()
    return fig


def state_list(cursor):
    query = "SELECT * FROM States"
    cursor.execute(query)
    result = cursor.fetchall()
    state_names = [state[2] for state in result]
    option = st.selectbox('Select the state', state_names)
    return option


def transaction_list(cursor):
    query = "SELECT * FROM TransactionTypes"
    cursor.execute(query)
    result = cursor.fetchall()
    transaction_names = [transaction[1] for transaction in result]
    option = st.selectbox('Select the Transaction', transaction_names)
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
    fig = px.choropleth(df,
                        geojson="https://raw.githubusercontent.com/geohacker/india/master/state/india_telengana.geojson",
                        featureidkey='properties.NAME_1',
                        locations='State',
                        color='Amount',  # You can also change this to 'Count' if you wish
                        hover_name='State',
                        hover_data=['Transaction_Types', 'Count', 'Amount', 'Year_Quarter'],
                        animation_frame='Year_Quarter',
                        color_continuous_scale='Reds',
                        title="Amount by Year_Quarter for Each State")

    fig.update_geos(fitbounds="locations", visible=False, scope='asia')
    return fig


aggregated_tab, map_tab, top_tab = st.tabs(["Aggregated", "Map", "Top"])

with aggregated_tab:
    aggregated_transaction_tab, aggregated_user_tab = st.tabs(["Aggregated Transaction", "Aggregated User"])
    with aggregated_transaction_tab:
        st.text("Aggregated Transaction")
        state_selected = state_list(cursor)
        transaction_selected = transaction_list(cursor)
        data = aggregated_transaction_state_and_transaction_wise(cursor, state_selected, transaction_selected)
        fig = display_aggregated_transaction_data(data)
        st.plotly_chart(fig)
    with aggregated_user_tab:
        st.text("Aggregated User")
with map_tab:
    map_transaction_tab, map_user_tab = st.tabs(["Map Transaction", "Map User"])
    with map_transaction_tab:
        st.text("Map Transaction")
    with map_user_tab:
        st.text("Map User")
with top_tab:
    top_transaction_tab, top_user_tab = st.tabs(["Top Transaction", "Top User"])
    with top_transaction_tab:
        st.text("Top Transaction")
    with top_user_tab:
        st.text("Top User")
