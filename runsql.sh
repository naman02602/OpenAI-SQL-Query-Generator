#!/bin/bash
echo Run SnowSQL commands

echo Teardown
snowsql -c dev -f modules/teardown.sql

echo Setup Snowflake Account
snowsql -c dev -f modules/setup_snow.sql