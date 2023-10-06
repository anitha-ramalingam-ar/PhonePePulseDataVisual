def create_top_district_user_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS TopDistrictUserDetails (
        id INT AUTO_INCREMENT PRIMARY KEY,
        district_id INT NOT NULL,
        state_id INT NOT NULL,
        registered_user BIGINT,
        year_with_quarter VARCHAR(255) NOT NULL,
        FOREIGN KEY (district_id) REFERENCES Districts(id),
        FOREIGN KEY (state_id) REFERENCES States(id));
    """)


def create_top_pincode_user_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS TopPincodeUserDetails (
        id INT AUTO_INCREMENT PRIMARY KEY,
        pincode INT NOT NULL,
        state_id INT NOT NULL,
        registered_user BIGINT,
        year_with_quarter VARCHAR(255) NOT NULL,
        FOREIGN KEY (state_id) REFERENCES States(id));
    """)
