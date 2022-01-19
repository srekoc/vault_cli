#!/usr/bin/python3
import sys, getopt

class Cmdline:

    def validate_cmd_line_parms(self, argv):
       namespace = ''
       businessunit = ''
       gitpath = ''
       secretpath = ''
       help = """ 
options:
    -h, --help     
    -n, --namespace required (sv2/dev|sv1/prod|va1/staging)
    -b, --businessunit required (assist|ai-tools|messaging|tie|dataplatform|cloudops)
    -g, --gitpath (<git_org>/<git_repo>) 
    -s, --secretpath (any name, preferably secrets)    
    -a, --action (read|create|update)    
    -f, (only relevant for replace|delete)    
    
    Ex: vcli -n sv1/prod -b cloudops -g devops/devstore  -s secrets -a read # for reading secrets
        """
       namespace, businessunit, gitpath, secretpath, action, force = "","","","","",""
       try:
          opts, args = getopt.getopt(argv,"hn:b:g:s:a:f",["--help", "namespace=","businessunit=", "gitpath=", "secretpath=", "action="])
       except getopt.GetoptError:
          print (help, file=sys.stderr)
          sys.exit(2)
       for opt, arg in opts:
          if opt == '-h':
            print (help, file=sys.stderr)
            sys.exit()
          elif opt in ("-n", "--namespace"):
             namespace = arg
          elif opt in ("-b", "--businessunit"):
             businessunit = arg
          elif opt in ("-g", "--gitpath"):
             gitpath = arg
          elif opt in ("-s", "--secretpath"):
             secretpath = arg
          elif opt in ("-a", "--action"):
             action = arg
          elif opt == '-f':
             force = 1
          else:
            print ("unknown option", file=sys.stderr)
            sys.exit(2)
       return (f'{namespace}', f'{businessunit}', f'{gitpath}', f'{secretpath}', f'{action}', f'{force}')
