def create_map_transaction_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS MapTransactionDetails (
        id INT AUTO_INCREMENT PRIMARY KEY,
        district_id INT NOT NULL,
        count BIGINT NOT NULL,
        amount DECIMAL(30,10) NOT NULL, 
        year_with_quarter VARCHAR(255) NOT NULL,
        FOREIGN KEY (district_id) REFERENCES Districts(id));
    """)
