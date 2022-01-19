import sys

class Checkbu:
        
    def validate_business_unit(self, bu):
        accepted_bu = ['assist', 'aiva', 'ai-tools', 'messaging', 'tie', 'dataplatform', 'cloudops', 'central']
        if not bu in accepted_bu:
            print ("[ERROR]: business unit must be one of:\n" + " ".join(map(str, accepted_bu)), file=sys.stderr)
            sys.exit(2)
