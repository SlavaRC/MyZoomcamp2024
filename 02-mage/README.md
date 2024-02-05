## Step #0
```bash
git clone https://github.com/SlavaRC/MyZoomcamp2024.git
cd ./02-mage
```


## Step #1 
Rename `dev.env` to simply `.env`— this will _ensure_ the file is not committed to Git by accident, since it _will_ contain credentials in the future.
```bash
cp dev.env .env
```



Now, let's build the container

```bash
docker compose build
```

## Step #2
```bash
git clone https://github.com/mage-ai/mage-zoomcamp.git mage-zoomcamp
```


## ISSUE: 

SSL: CERTIFICATE_VERIFY_FAILED
https://jonathansoma.com/everything/python/ignoring-ssl-issues/ 