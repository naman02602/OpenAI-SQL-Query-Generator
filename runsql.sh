#!/bin/bash
echo Run SnowSQL commands

echo Teardown
snowsql -c dev -f modules/teardown.sql

echo Setup Snowflake Account
snowsql -c dev -f modules/setup_snow.sql

echo Load Raw data
snowsql -c dev -f modules/load_raw.sql

echo Clean Raw data
snowsql -c dev -f modules/data_cleaning.sql

echo Run usecase scripts
snowsql -c dev -f modules/airport_crowd.sql
snowsql -c dev -f modules/hourly_crowd.sql
snowsql -c dev -f modules/carbon_footprint.sql

echo End of script
