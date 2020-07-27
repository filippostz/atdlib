import atdlib
import time
import json

TIMER = 10

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

data = json.loads(report)

name = data['Summary']['Subject']['Name']
verdict = data['Summary']['Verdict']['Description']
print("File: {0} result is {1}".format(name,verdict))

# close Session
atd.close()
