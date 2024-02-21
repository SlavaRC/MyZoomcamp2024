FROM python:3.9
RUN pip install --upgrade pip
RUN pip install pandas
RUN pip install dlt
WORKDIR ./
COPY pipeline.py pipeline.py
#ENTRYPOINT [ "python", "pipeline.py" ]
ENTRYPOINT ["tail", "-f", "/dev/null"]

#docker build -t test:python .
#docker run -it -d --network=pg-network --name=python3 test:python
#docker exec -it python3 /bin/bash