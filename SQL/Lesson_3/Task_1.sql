-- Написать крипт, добавляющий в БД vk, которую создали на занятии, 3 новые таблицы (с перечнем полей, указанием индексов и внешних ключей)

DROP TABLE IF EXISTS city_location;
CREATE TABLE city_location(
	id SERIAL PRIMARY KEY,
    city VARCHAR(255),
    INDEX users_cityname_idx(city)
);

DROP TABLE IF EXISTS region_location;
CREATE TABLE region_location(
	id SERIAL PRIMARY KEY,
    region VARCHAR(255),
    INDEX users_region_idx(region)
);

DROP TABLE IF EXISTS location;
CREATE TABLE location(
	id SERIAL PRIMARY KEY,
    city_id BIGINT unsigned NOT NULL,
    region_id BIGINT unsigned NOT NULL,
    user_id BIGINT UNSIGNED NOT NULL,
    created_at DATETIME DEFAULT NOW(),
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (city_id) REFERENCES city_location(id),
    FOREIGN KEY (region_id) REFERENCES region_location(id)
	
);
