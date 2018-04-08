import os
import modtest
import stat
import pwd
import grp
score=0
f=open('/etc/passwd','r')
while True:
    line=f.readline()
    if len(line)==0:
        f.close()
        break
    if line.find("root",0,4)!=-1:
        score=score+1
    if line.find("ubuntu",0,6)!=-1:
        score=score+1
f=open('/etc/group','r')
while True:
    line=f.readline()
    if len(line)==0:
        f.close()
        break
    if line.find("project")!=-1 and line.find("arod")!=-1:
        score=score+1
group="project"
grp_info=grp.getgrnam(group)
#print grp_info
path="/shared"
user="arod"
if os.path.exists(path) and modtest.checkuser(user):
    if modtest.is_readable(path,user) and modtest.is_writable(path,user) and modtest.is_executable(path,user):
        score=score+1
user="alex"
if os.path.exists(path) and modtest.checkuser(user):
    if modtest.is_readable(path,user) and modtest.is_writable(path,user) and modtest.is_executable(path,user):
        score=score+1
st=os.stat(path)
mode=st.st_mode
if mode&stat.S_ISGID!=0:
	score=score+1
print score

