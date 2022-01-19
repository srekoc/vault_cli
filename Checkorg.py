import sys

class Checkorg:
        
    def validate_git_org(self, gitpath):
        list_of_git_repos = ['CE', 'DBE', 'GCP-Infra', 'big-data', 'cicd-devops', 'cloud-infra', 'devops', 'devops-tools', 'platform', 'oe-solutions', 'Central', 'chef-platform']
        gitorg, gitrepo = gitpath.split("/", 1)
        if gitorg in list_of_git_repos:
            return 1
        else:
            print ("------", file=sys.stderr)
            print ("[ERROR]: not an accepted git org..should be one among these", file=sys.stderr)
            print (list_of_git_repos, file=sys.stderr)
            print ("------", file=sys.stderr)
            sys.exit(2)
            
