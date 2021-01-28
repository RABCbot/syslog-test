# syslog-test

Install Vector https://vector.dev/guides/getting-started

Edit vector.toml file
'''
data_dir = "/var/lib/vector"

[sources.in]
  type = "stdin"

[sources.syslog]
  type = "syslog"
  address = "0.0.0.0:5514"
  mode = "udp"

[sinks.out]
  inputs   = ["in", "syslog"]
  type     = "console"
  encoding = "text"
'''
Run Vector
vector --config ./vector.toml

Run python sample file
python3 syslog.py

You should see the message on the Vector stdout console
