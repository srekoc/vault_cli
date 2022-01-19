import sys
import json
import hvac

class Sread:

    def read_secrets(self, client, namespace, businessunit, gitpath, secretpath):
        mount_path = f'{businessunit}/{gitpath}/'
        try:
            secret_version_response = client.secrets.kv.v2.read_secret_version(
                mount_point=mount_path,
                path=secretpath,
            )

        except hvac.exceptions.InvalidPath:
            print (f'[ERROR] : Invalid path [{mount_path}] provided...exiting')
            sys.exit(2)
        #print (secret_version_response['data']['data'])
        version = secret_version_response['data']['metadata']['version']    
        print (f'Reading secrets for [{mount_path}], version [{version}]...', file=sys.stderr)
        json_data = secret_version_response['data']['data']
        print (json.dumps(json_data, indent=4, sort_keys=True), file=sys.stderr)
        return secret_version_response