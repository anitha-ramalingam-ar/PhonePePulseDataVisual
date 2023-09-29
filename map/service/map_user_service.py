from database.create_district_table_sql import get_district_id
from map.model.map_user_model import process_map_user_files


def map_user_data_conversion(cursor):
    # Step 1: Read each state aggregated transaction json and convert as Object class
    map_user_data = process_map_user_files(
        'extracted_file/data/map/user/hover/country/india/state')

    # Step 2: Convert JSON to Object and insert each state with quarter record into table
    for data in map_user_data:
        for district_name, hover_data_obj in data.data.hoverData.items():
            district_id = get_district_id(cursor, district_name)
            if district_id is None:
                print(f"Error: District {district_name} not found in the database.")
                continue

            registered_user = hover_data_obj.registeredUsers
            app_opens = hover_data_obj.appOpens
            year_with_quarter = data.year_with_quarter
            query = """
                INSERT INTO MapUserDetails 
                (district_id, registered_user, app_opens, year_with_quarter) 
                VALUES (%s, %s, %s, %s);
                """

            cursor.execute(query, (district_id, registered_user, app_opens, year_with_quarter))
