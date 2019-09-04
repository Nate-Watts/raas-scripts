from sseapiclient.tornado import SyncClient
import pprint
import sys

sys.stdout = open('output.txt','wt')

raas = 'http://localhost:8080'
client = SyncClient.connect(raas, 'root', 'salt', rpc_api_version='2', force_restfull=False)
response = client.api.job.get_jobs(page=1).ret

discover = client.api.api.discover().ret
pprint.pprint(discover)
