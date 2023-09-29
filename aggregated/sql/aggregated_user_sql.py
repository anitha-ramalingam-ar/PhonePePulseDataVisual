def create_device_brand_static_table(cursor):
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS DeviceBrands (id INT AUTO_INCREMENT PRIMARY KEY,brand_name VARCHAR(255) UNIQUE NOT NULL);")
    device_brands = {
        'Xiaomi', 'Samsung', 'Vivo', 'Oppo', 'OnePlus', 'Realme', 'Apple', 'Motorola', 'Lenovo', 'Huawei', 'Others'
    }

    for device_brand in device_brands:
        cursor.execute("INSERT IGNORE INTO DeviceBrands (brand_name) VALUES (%s);", (device_brand,))


def create_aggregated_user_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS AggregatedUserDetails (
        id INT AUTO_INCREMENT PRIMARY KEY,
        brand_names_id INT NOT NULL,
        state_id INT NOT NULL,
        count BIGINT NOT NULL,
        percentage DECIMAL(30,10) NOT NULL, 
        year_with_quarter VARCHAR(255) NOT NULL,
        registered_user BIGINT,
        app_opens BIGINT,
        FOREIGN KEY (brand_names_id) REFERENCES DeviceBrands(id),
        FOREIGN KEY (state_id) REFERENCES States(id));
    """)


def get_device_brand_id(cursor, device_brand):
    query = "SELECT id FROM DeviceBrands WHERE brand_name = %s;"
    cursor.execute(query, (device_brand,))
    result = cursor.fetchone()
    return result[0] if result else None
