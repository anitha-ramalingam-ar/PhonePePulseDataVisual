def create_top_district_transaction_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS TopDistrictTransactionDetails (
        id INT AUTO_INCREMENT PRIMARY KEY,
        district_id INT NOT NULL,
        state_id INT NOT NULL,
        count BIGINT NOT NULL,
        amount DECIMAL(30,10) NOT NULL, 
        year_with_quarter VARCHAR(255) NOT NULL,
        FOREIGN KEY (district_id) REFERENCES Districts(id),
        FOREIGN KEY (state_id) REFERENCES States(id));
    """)


def create_top_pincode_transaction_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS TopPincodeTransactionDetails (
        id INT AUTO_INCREMENT PRIMARY KEY,
        pincode INT NOT NULL,
        state_id INT NOT NULL,
        count BIGINT NOT NULL,
        amount DECIMAL(30,10) NOT NULL, 
        year_with_quarter VARCHAR(255) NOT NULL,
        FOREIGN KEY (state_id) REFERENCES States(id));
    """)
