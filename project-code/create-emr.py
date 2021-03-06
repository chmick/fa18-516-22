import subprocess
import json

def create_emr():
   c_id = subprocess.run("aws emr create-cluster --name='E516-JupyterHub-Cluster' --release-label emr-5.19.0 --applications Name=JupyterHub --log-uri s3://e516-jupyterhub-backup/JupyterClusterLogs --use-default-roles --ec2-attributes SubnetIds=subnet-d0169eaa,KeyName=dlec2-key,AdditionalMasterSecurityGroups=['sg-01c1d97ca12d1f2e7'] --instance-count 2 --instance-type m4.large --configurations file://E516-Jupyter-Config.json --output text", shell=True, stdout=subprocess.PIPE)
   cid = c_id.stdout.decode('utf-8')
   cid = cid.rstrip()
   time.sleep(2)

   client = boto3.client('emr')
   pdns = client.describe_cluster(ClusterId=cid)

   response = client.list_clusters(ClusterStates=['STARTING', 'BOOTSTRAPPING', 'RUNNING', 'WAITING'])

   rtn_dict =   {
     #"ClusterId": cid,
     #"CheckClusterStatus": ("http://ec2-18-191-50-79.us-east-2.compute.amazonaws.com:8081/emr/get/?" + cid),
     #"JupyterHub": ("https://" + response + ":9443"),
     "JupyterUN": "jovyan",
     "JupyterPW": "jupyter"
   }
   return pdns

print(create_emr())
