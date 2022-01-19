#!/usr/bin/python3
import sys
import os

class Checkenv:
    def validate_env(self):
            vault_token = os.environ.get("VAULT_TOKEN")
            if not vault_token:
                print ("\n".join(map(str.strip, """\
                    [ERROR]: set VAULT_TOKEN environment variable
                    Ex: export VAULT_TOKEN=s.Abc11Def0gHiJKLMnoPQrstU\
                """.split("\n"))), file=sys.stderr)
                sys.exit()
            return vault_token