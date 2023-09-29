from aggregated.model.aggregated_user_model import process_aggregated_user_files
from aggregated.sql.aggregated_user_sql import get_device_brand_id
from database.create_state_table_sql import get_state_id


def aggregated_user_state_data_conversion(cursor):
    # Step 1: Read each state aggregated transaction json and convert as Object class
    aggregated_user_data = process_aggregated_user_files(
        'extracted_file/data/aggregated/user/country/india/state')

    # Step 2: Convert JSON to Object and insert each state with quarter record into table
    for data in aggregated_user_data:
        device_brand_id = get_device_brand_id(cursor, data.data.usersByDevice[0].brand)
        state_id = get_state_id(cursor, data.state_name)
        count = data.data.usersByDevice[0].count
        percentage = data.data.usersByDevice[0].percentage
        year_with_quarter = data.year_with_quarter
        registered_user = data.data.aggregated.registeredUsers
        app_opens = data.data.aggregated.appOpens
        query = """
            INSERT INTO AggregatedUserDetails 
            (brand_names_id, state_id, count, percentage, year_with_quarter, registered_user, app_opens) 
            VALUES (%s, %s, %s, %s, %s, %s, %s);
            """

        cursor.execute(query,
                       (device_brand_id, state_id, count, percentage, year_with_quarter, registered_user, app_opens))
