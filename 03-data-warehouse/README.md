
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
SELECT * FROM `my-zoomcamp-project-1.03_homework_dataset_1.green_taxi_trip_record`
```