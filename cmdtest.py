import os
score=0
homepath=os.environ['HOME']
#os.path.expanduser('$HOME')
os.chdir(homepath)
if os.path.exists("testdir"):
    os.chdir("testdir")
    score=score+1
if os.path.exists("mydir"):
    score=score+1
if os.path.isfile("passwd"):
    score=score+1
print score
