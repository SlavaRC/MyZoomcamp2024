FROM python:3.9
RUN pip install pandas
WORKDIR ./
COPY pipeline.py pipeline.py
#ENTRYPOINT [ "python", "pypeline.py" ]
ENTRYPOINT ["tail", "-f", "/dev/null"]
