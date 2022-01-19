#!/usr/bin/python3
import sys, getopt
from Cmdline import Cmdline
from Checkenv import Checkenv
from Checkns import Checkns
from Checkbu import Checkbu
from Checkorg import Checkorg
from Sread import Sread
from Screate import Screate
from Sreplace import Sreplace

def main(argv):
    # Configuration
    vault_url = 'https://test-vault.infra.srekoc.net/'
    
    checkenv = Checkenv()
    cmdline = Cmdline()
    checkns = Checkns()
    checkbu = Checkbu()
    checkorg = Checkorg()
    sread = Sread()
    screate = Screate()
    sreplace = Sreplace()
    
    (namespace, businessunit, gitpath, secretpath, action, force) = cmdline.validate_cmd_line_parms(argv)
    vault_token = checkenv.validate_env()
    client = checkns.validate_namespace(vault_url, vault_token, namespace)
    status = checkbu.validate_business_unit(businessunit)
    status = checkorg.validate_git_org(gitpath)
    if(action == "read"):
        secret_version_response = sread.read_secrets(client, namespace, businessunit, gitpath, secretpath)
    elif(action == "create"):
        screate.create_secrets (client, namespace, businessunit, gitpath, secretpath, action)
    elif(action == "replace"):
        sreplace.replace_secrets (client, namespace, businessunit, gitpath, secretpath, action, force)
    else:
        print ("unrecognized action...should be create|read|update|delete", file=sys.stderr)
    
if __name__ == "__main__":
   main(sys.argv[1:])
