import ConfigParser
import io
import sys
import yaml
import subprocess

if len(sys.argv) == 1:
    print("You need to specify at least one environment.\n")
    print("Examples:\n")
    print("    python get-credentials.py dev")
    print("    python get-credentials.py dev qa epic")
    sys.exit(0)

COMMAND = 'okta-awscli --profile default'
PREFIX = '/home/vagrant/'

# Read new AWS credentials
with open(PREFIX + '.aws/credentials') as f:
    sample_config = f.read()

config = ConfigParser.RawConfigParser(allow_no_value=True)
config.readfp(io.BytesIO(sample_config))

key = config.get('default','aws_access_key_id')
secret = config.get('default','aws_secret_access_key')
token = config.get('default','aws_session_token')

# Read current ec2-config.yml file
with open(PREFIX + 'billing/.ec2-config.yml', 'r') as ymlfile:
    cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

for env in sys.argv[1:]:
    if env in cfg:
        print("Updating '%s' section..." % env)
        # Update env section
        cfg[env]['access_key_id'] = key
        cfg[env]['secret_access_key'] = secret
        cfg[env]['session_token'] = token
    else:
        print("Skipping '%s' section, not found!" % env)

# Save new content
stream = file(PREFIX + 'billing/.ec2-config.yml', 'w')
yaml.dump(cfg, stream)
