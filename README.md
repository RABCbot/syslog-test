# syslog-test
Python Syslog client to send messages to [Vector](https://vector.dev) syslog input sync<br/>

## Installation
Install [Vector](https://vector.dev/guides/getting-started)<br/>
Edit vector.toml configuration file<br/>
```
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
  
[sinks.cloud_watch_logs]
type = "aws_cloudwatch_logs"
inputs = ["stdin"]
group_name = "/<your-log-group>"
stream_name = "<your-stream-name>"
region = "<your-region>"
encoding = "json"  
# Add your AWS access key/token to ~\.aws\credentials file
```
## Run
Launch Vector<br/>
```
vector --config ./vector.toml
```

Run python sample file<br/>
```
python3 syslog.py
```

You should see the message on the Vector stdout console
