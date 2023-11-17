echo Load Raw data
snowsql -c dev -f modules/load_raw.sql

echo Clean Raw data
snowsql -c dev -f modules/data_cleaning.sql

echo Run usecase scripts
snowsql -c dev -f modules/airport_crowd.sql
snowsql -c dev -f modules/hourly_crowd.sql
snowsql -c dev -f modules/carbon_footprint.sql
snowsql -c dev -f modules/seat_occupancy.sql

echo End of script