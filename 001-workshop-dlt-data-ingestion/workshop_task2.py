import dlt
import duckdb



def people_1():
    for i in range(1, 6):
        yield {"ID": i, "Name": f"Person_{i}", "Age": 25 + i, "City": "City_A"}

def people_2():
    for i in range(3, 9):
        yield {"ID": i, "Name": f"Person_{i}", "Age": 30 + i, "City": "City_B", "Occupation": f"Job_{i}"}


# Above you have 2 generators. You will be tasked to load them to duckdb and answer some questions from the data
# 1. Load the first generator and calculate the sum of ages of all people. Make sure to only load it once.
# 2. Append the second generator to the same table as the first.
# 3. After correctly appending the data, calculate the sum of all ages of people.
if __name__ == "__main__":

    generators_pipeline = dlt.pipeline(destination='duckdb', dataset_name='pep_1')

    # we can load any generator to a table at the pipeline destnation as follows:
    info = generators_pipeline.run(people_1(),
                                   table_name="people_1_result",
                                   write_disposition="replace")
    # the outcome metadata is returned by the load and we can inspect it by printing it.
    print(info)

    conn = duckdb.connect(f"{generators_pipeline.pipeline_name}.duckdb")
    print(conn.sql("show tables"))
    #
    # print(generators_pipeline)

    # peoples_1 = conn.sql("SELECT * FROM people_1_result").df()
    # print(peoples_1)
    #
    # print(generators_pipeline)

    # for person in people_1():
    #     print(person)
    #
    # for person in people_2():
    #     print(person)