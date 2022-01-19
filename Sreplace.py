import sys
import time
import json
import signal
from Sread import Sread

class Sreplace:

    def replace_secrets(self, client, namespace, businessunit, gitpath, secretpath, action, force):
        sread = Sread()
        path = f'{businessunit}/{gitpath}/'
        secret_version_response = sread.read_secrets(client, namespace, businessunit, gitpath, secretpath)
        version = secret_version_response['data']['metadata']['version']    
        replace_secrets_in_vault(self, client, namespace, businessunit, gitpath, secretpath, version, path, force)
                
def replace_secrets_in_vault (self, client, namespace, businessunit, gitpath, secretpath, version, path, force):
    # repetition. can leverage code from Screate module, no time for this now. 
    try:
        dict = json.load( sys.stdin )
    except ValueError:
        print ("Decoding JSON failed, please fix it")
        sys.exit(2)
    if force:
        if bool(dict):
            time.sleep(2)
            try:
                client.secrets.kv.v2.create_or_update_secret(
                    mount_point=f'{path}',
                    cas=f'{version}',
                    path=f'{secretpath}',
                    secret=dict,
                )
            except hvac.exceptions.InvalidRequest:
                print (f'[ERROR] : Invalid request for path [{mount_path}] provided...exiting', file=sys.stderr)
                sys.exit(2)
            print (f'Successfully replaced secrets to new version...', file=sys.stderr)
            sread = Sread()
            secret_version_response = sread.read_secrets(client, namespace, businessunit, gitpath, secretpath)
            version = secret_version_response['data']['metadata']['version']    
            
        else:
            print ("Expecting json input", file=sys.stderr)
            help_str = """
    echo '{ "key1": "value 1", "key2": "value 2" }' |  python vcli.py --namespace=sv2/dev --businessunit=cloudops --gitpath='devops/test-devstore-02' --secretpath='secrets' --action update
            """
            sys.exit(2)
    else:    
        print ("Replace option would need explicit -f option", file=sys.stderr)
        print ("Exiting ...", file=sys.stderr)
        sys.exit(2)
