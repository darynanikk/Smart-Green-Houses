import configparser

from influxdb_client import InfluxDBClient

config = configparser.ConfigParser()

config.read('config.ini')


class DBSetup:
    def __init__(self):
        self._token = config.get("APP", "INFLUXDB_TOKEN")
        self._org = config.get("APP", "INFLUXDB_ORG")
        self._url = config.get("APP", "INFLUX_URL")

    def get_client(self):
        return InfluxDBClient(url=self._url, token=self._token, org=self._org)