#!/usr/bin/python3
import os
import sys
import hvac
import warnings
warnings.filterwarnings("ignore")


class Checkns:
        
    def validate_namespace(self, vault_url, vault_token, ns):
        client = hvac.Client(url=vault_url, verify=0, namespace=ns, token=vault_token)
        var = client.is_authenticated()
        if(not var):
            print (f"You are not authorized to access {ns} namespace. Please create a JIRA ticket/write to vault-admins@srekoc.net", file=sys.stderr)
            print ("\n", file=sys.stderr)
            sys.exit()
        return client
