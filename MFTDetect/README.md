# MFT Detect

Scripts and templates that can be leveraged to automatically create detection
rules for common incident response and detection tools.

usage: Template2Detect [-h] -f FILE -c CSV [-o OUTPUT]

If no output file is specified, content will appear in stdout

Template2 Detect: the following arguments are required: -f/--file, -c/--csv

python template2detect.py -f cmd_post_exploit.yml -c cornerstonemft.csv -o
cornerstone_cmd_postexploit.yml
