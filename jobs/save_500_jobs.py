from sseapiclient.tornado import SyncClient
import json

raas = 'http://localhost:8080'
client = SyncClient.connect(raas, 'root', 'salt', rpc_api_version='2', force_restfull=False)

with open('jobdata.json', 'r') as f:
    array = json.load(f)
for i in range(0, 500):
  job = client.api.job.save_job(fun=array['job1']['fun'], name=array['job1']['name'], cmd=array['job1']['cmd'])
print(job)
