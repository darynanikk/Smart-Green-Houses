import time
from influxdb_client import Point
from influxdb_client.client.write_api import SYNCHRONOUS

from db_setup import DBSetup


client = DBSetup().get_client()


def write_example():
    bucket = "home"

    write_api = client.write_api(write_options=SYNCHRONOUS)

    for value in range(5):
        point = (
            Point("measurement1")
            .tag("tagname1", "tagvalue1")
            .field("field1", value)
        )
        write_api.write(bucket=bucket, org="docs", record=point)
        time.sleep(1)  # separate points by 1 second


def read_example():
    query_api = client.query_api()

    query = """from(bucket: "home")
      |> range(start: -10m)
      |> filter(fn: (r) => r._measurement == "measurement1")
      |> mean()"""
    tables = query_api.query(query, org="docs")

    for table in tables:
        for record in table.records:
            print(record)


if __name__ == '__main__':
    #write_example()
    read_example()
