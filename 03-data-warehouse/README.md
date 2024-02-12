
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
   SELECT * FROM ...
```