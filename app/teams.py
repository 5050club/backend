from elasticsearch import Elasticsearch, helpers
#import json
import yaml
#from datetime import datetime, timezone


def es_ingest(data):

    # TODO: put creds in k8s secrets
    #un = "j10s"
    #api_key = "T2dEZnJKSUJtT2RjdnlGQllreF86MXJfVE5ucVlTN09kT1pzb3ZGd1YyUQ=="

    client = Elasticsearch("https://localhost:9200/", verify_certs=False, api_key="T2dEZnJKSUJtT2RjdnlGQllreF86MXJfVE5ucVlTN09kT1pzb3ZGd1YyUQ==")

    #https://elasticsearch-py.readthedocs.io/en/v8.15.1/quickstart.html#indexing-documents
    helpers.bulk(client, generate_docs(data))

    client.indices.refresh(index="teams")

def generate_docs(data):
    for d in data.items():
        yield {
            "_index": "teams",
            "team": {
                "id": d[0],
                "name": d[0],
                "address": d[1].get("address"),
                "stadium": d[1].get("stadium"),
                "field": d[1].get("field"),
                "location": {
                    "lat": d[1].get("lat"),
                    "lon": d[1].get("lon"),
                }
            }
        }

if __name__ == '__main__':

    teams = open('/Users/j10s/apps/5050club/backend/data/teams.yaml', "r")
    data=yaml.load(teams, Loader=yaml.SafeLoader)

    es_ingest(data)

#es_ingest(results)