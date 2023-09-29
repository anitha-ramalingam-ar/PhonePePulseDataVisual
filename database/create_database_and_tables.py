import mysql.connector

from aggregated.sql.aggregated_transaction_sql import create_aggregated_transaction_type_static_table, \
    create_aggregated_transaction_table
from aggregated.sql.aggregated_user_sql import create_device_brand_static_table, create_aggregated_user_table
from database.create_district_table_sql import create_district_table, insert_static_district_values_table
from database.create_state_table_sql import create_state_static_table
from map.sql.map_transaction_sql import create_map_transaction_table
from map.sql.map_user_sql import create_map_user_table


def mysql_connection(host, port, user, password, database):
    return mysql.connector.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database
    )


def create_all_tables(cursor):
    create_aggregated_transaction_type_static_table(cursor)
    create_state_static_table(cursor)
    create_district_table(cursor)
    insert_static_district_values_table(cursor)
    create_device_brand_static_table(cursor)
    create_aggregated_transaction_table(cursor)
    create_aggregated_user_table(cursor)
    create_map_transaction_table(cursor)
    create_map_user_table(cursor)
