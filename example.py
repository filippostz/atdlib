import atdlib

atd = atdlib.atdsession()

# open new session to the ATD
atd.open('192.168.224.100', 'user', 'password')

# upload a file for analysis and get jobId
atd.fileup('sample.exe')

# jobId is xxxx

# Get a list of job tasks
#atd.jobtasks(xxxx)
# job initiated one task with id 14326

# getting task status
#atd.taskstatus(yyy)
