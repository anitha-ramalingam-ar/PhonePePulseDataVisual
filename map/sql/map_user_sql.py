def create_map_user_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS MapUserDetails (
        id INT AUTO_INCREMENT PRIMARY KEY,
        district_id INT NOT NULL,
        state_id INT NOT NULL,
        registered_user BIGINT,
        app_opens BIGINT, 
        year_with_quarter VARCHAR(255) NOT NULL,
        FOREIGN KEY (district_id) REFERENCES Districts(id),
        FOREIGN KEY (state_id) REFERENCES States(id));
    """)
