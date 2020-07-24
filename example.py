import atdlib
import time
import json

TIMER = 1

atd = atdlib.atdsession()

# open new session to the ATD
atd.open('192.168.224.100', 'user', 'password')

# upload a file for analysis and get jobId
jobId = atd.fileup('sample.exe')

TaskId = atd.jobtasks(jobId)[0]

# Get a list of job tasks
print('File uploaded with job task id:%d' % (TaskId))

# getting task status
status=0
while status != 1 :
    status = atd.taskstatus(TaskId)
    time.sleep(TIMER)

print('done!')

# getting report
report = atd.taskreport(TaskId, 'json')

# Decode UTF-8 bytes to Unicode, and convert single quotes to double quotes
report_json = report.decode('utf8').replace("'", '"')

data = json.loads(report_json)

print(data['Summary']['Verdict']['Description'])

# close Session
atd.close()
