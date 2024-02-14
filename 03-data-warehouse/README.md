
## Step #1 
Rename `dev.env` to simply `.env`— this will _ensure_ the file is not committed to Git by accident, since it _will_ contain credentials in the future.
```bash
cp dev.env .env
```

Now, let's build the container

```bash
docker compose build
```
and start containers
```bash
docker compose up
```
Go to http://localhost:6789 in your browser.

## HomeWork:
https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2024/03-data-warehouse/homework.md

## HOMEWORK:
SQL: 
```sql
-- Create external table refering to GCS
CREATE OR REPLACE EXTERNAL TABLE `my-zoomcamp-project-1.03_homework_dataset_1.green_taxi_trip_record`
OPTIONS (
format = 'PARQUET',
uris = ['gs://my-zoomcamp-bucket-1/03_homework.parquet']
);

-- Check data
SELECT PULocationID FROM `my-zoomcamp-project-1.03_homework_dataset_1.green_taxi_trip_record`; 

-- Task #3: How many records have a fare_amount of 0?
SELECT * FROM `my-zoomcamp-project-1.03_homework_dataset_1.green_taxi_trip_record` WHERE `fare_amount` = 0; 


-- Create a non partitioned table from external table
CREATE OR REPLACE TABLE `my-zoomcamp-project-1.03_homework_dataset_1.green_taxi_trip_record__non_partitoned` AS
SELECT * FROM `my-zoomcamp-project-1.03_homework_dataset_1.green_taxi_trip_record`;

-- Create Table with "cleaned_dropoff_datetime" column of timestamp type. Workaround to do Task #5
CREATE OR REPLACE TABLE `my-zoomcamp-project-1.03_homework_dataset_1.green_taxi_trip_record_timestamp` AS 
SELECT *, TIMESTAMP_MICROS(CAST(lpep_pickup_datetime / 1000 AS INT64)) AS cleaned_pickup_datetime, TIMESTAMP_MICROS(CAST(lpep_dropoff_datetime / 1000 AS INT64)) AS cleaned_dropoff_datetime FROM `my-zoomcamp-project-1.03_homework_dataset_1.green_taxi_trip_record`;

--create a partition and cluster
CREATE OR REPLACE TABLE `my-zoomcamp-project-1.03_homework_dataset_1.green_taxi_trip_record__partitoned`
  PARTITION BY DATE(cleaned_pickup_datetime)
  CLUSTER BY PUlocationID AS
SELECT *, FROM `my-zoomcamp-project-1.03_homework_dataset_1.green_taxi_trip_record_timestamp`;

-- Write a query to retrieve the distinct PULocationID between lpep_pickup_datetime 06/01/2022 and 06/30/2022 (inclusive)
-- Use the materialized table you created earlier in your from clause and note the estimated bytes. 
-- Now change the table in the from clause to the partitioned table you created for question 4 and note the estimated bytes processed. -- What are these values?
SELECT count(DISTINCT PULocationID) FROM `my-zoomcamp-project-1.03_homework_dataset_1.green_taxi_trip_record__partitoned` 
WHERE cleaned_pickup_datetime BETWEEN "2022-06-01" and "2022-06-30"; --1,12MB
SELECT count(DISTINCT PULocationID) FROM `my-zoomcamp-project-1.03_homework_dataset_1.green_taxi_trip_record_timestamp` 
WHERE cleaned_pickup_datetime BETWEEN "2022-06-01" and "2022-06-30"; --12,82MB

```