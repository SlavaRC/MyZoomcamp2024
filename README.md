# MyZoomcamp2024


NY Taxi data source, csv:
https://github.com/DataTalksClub/nyc-tlc-data


wget --no-check-certificate https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2019-09.csv.gz

CREATE TABLE "yellow_taxi_data" (
"VendorID" INTEGER,
  "tpep_pickup_datetime" TIMESTAMP,
  "tpep_dropoff_datetime" TIMESTAMP,
  "passenger_count" INTEGER,
  "trip_distance" REAL,
  "RatecodeID" INTEGER,
  "store_and_fwd_flag" TEXT,
  "PULocationID" INTEGER,
  "DOLocationID" INTEGER,
  "payment_type" INTEGER,
  "fare_amount" REAL,
  "extra" REAL,
  "mta_tax" REAL,
  "tip_amount" REAL,
  "tolls_amount" REAL,
  "improvement_surcharge" REAL,
  "total_amount" REAL,
  "congestion_surcharge" REAL
)

