from elasticsearch import Elasticsearch, helpers
import psycopg
import requests
import json
import yaml
from datetime import datetime, timezone


def es_search(index=None, query=None):

    client = Elasticsearch("https://localhost:9200/", verify_certs=False, ssl_show_warn=False, api_key="T2dEZnJKSUJtT2RjdnlGQllreF86MXJfVE5ucVlTN09kT1pzb3ZGd1YyUQ==")
    
    resp = client.search(index=index, body=query)

    return resp._body['hits']['hits']

def psql_ingest(es_resp):
    # conn = psycopg.connect(database = "postgres",
    #                     user = "postgres",
    #                     password = "pwd",
    #                     host = "127.0.0.1",
    #                     port = "5432")

    # cur = conn.cursor()

    # Connect to an existing database
    with psycopg.connect("host=localhost port=5432 dbname=testdb user=postgres password=pwd") as conn:

        # Open a cursor to perform database operations
        with conn.cursor() as cur:

            for doc in es_resp:
                id = doc.get('_source').get('game').get('id')
                print(id)

                # Pass data to fill a query placeholders and let Psycopg perform
                # the correct conversion (no SQL injections!)
                cur.execute(
                    f"INSERT INTO test (id) VALUES ('{id}')"
                )

                # Make the changes to the database persistent
                conn.commit()


    # for i in range(0 ,len(df)):
    #     values = (df['date'][i], df['open'][i], df['high'][i], df['low'][i], df['close'][i])
    #     cur.execute("INSERT INTO stock_market_forecasting_new (date, open, high, low, close) VALUES (%s, %s, %s, %s, %s)",
    #                 values)

    # conn.commit()
    # print("Records created successfully")
    # conn.close()

if __name__ == '__main__':

    es_resp = es_search(index="allgames_latest", query='{"size": 10}')

    for doc in es_resp:
        print(doc)
        break

    psql_ingest(es_resp)