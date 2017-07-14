import elasticsearch
import argparse

__author__ = "Christo Goosen"

'''
Script to check extra mappings on Elasticsearch mapping
Example of this occurance: This could happen if you are using Logstash
and forget to disable manage_template => false or document_type is wrong.

'''

parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument(
    '--host', dest='host',
    default=None,
    help='Input URL or IPv4 for elasticsearch'
)

args = parser.parse_args()
print("Host provided:", args.host)

print("Running on elasticsearch-py version:", elasticsearch.__versionstr__)

if args.host:
    host = str(args.host)
    try:
        inputES = elasticsearch.Elasticsearch(host)
        print("Elasticsearch server details:", inputES.info())
        input_mappings = inputES.indices.get_mapping()
        count = 0
        for k, v in input_mappings.items():
            if len(v['mappings'].keys()) > 1:
                count += 1
                print("Index: ", k)
                print("Mappings", list(v['mappings'].keys()))
                print("\n")

        print("\nMutlitple Mapping Indices Count:", count)
    except elasticsearch.ConnectionError as e:
        print(e)
