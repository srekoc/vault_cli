import sys
import time
import json
import hvac
import signal
from Sread import Sread

class Screate:

    def create_secrets(self, client, namespace, businessunit, gitpath, secretpath, action):
        path = f'{businessunit}/{gitpath}/'
        try:
            dict = json.load( sys.stdin )
        except ValueError:
            print ("Decoding JSON failed, please fix it", file=sys.stderr)
            sys.exit(2)
            
        if bool(dict):

            try:
                client.sys.enable_secrets_engine(
                    backend_type='kv',
                    path=f'{path}',
                    options={"version":2}
                )
            except hvac.exceptions.InvalidRequest:
                print (f'[ERROR] : Cannot create, for path [{path}] ...already in use..', file=sys.stderr)
                sys.exit(2)
            except hvac.exceptions.Forbidden:
                print (f'[ERROR]: Permission denied for the namespace/path..', file=sys.stderr)
                sys.exit(2)
            
            print ("Creating secrets, please wait ...", file=sys.stderr)
            time.sleep(2)
            try:
                client.secrets.kv.v2.create_or_update_secret(
                    mount_point=f'{path}',
                    path=f'{secretpath}',
                    secret=dict,
                )
                print ("Successfully created!", file=sys.stderr)
                sread = Sread()
                secret_version_response = sread.read_secrets(client, namespace, businessunit, gitpath, secretpath)
                version = secret_version_response['data']['metadata']['version']    
                
            except hvac.exceptions.InvalidRequest:
                print (f'[ERROR] : Invalid request for path [{mount_path}] ...exiting', file=sys.stderr)
                sys.exit(2)
                
        else:
            print ("expecting json input", file=sys.stderr)
            help_str = """
echo '{ "key1": "value 1", "key2": "value 2" }' |  python vcli.py --namespace=sv2/dev --businessunit=cloudops --gitpath='devops/test-devstore-02' --secretpath='secrets' --action create
            """
            sys.exit(2)
            
