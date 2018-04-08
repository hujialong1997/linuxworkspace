import os
import pwd
import stat
  
def checkuser(user):
  name=os.popen("grep ^user: /etc/passwd|awk -F: '{print $1}'|head -1")
  if name.read().strip():
    return True
  else:
    return False

def checkgrp(grp):
  name=os.popen("grep ^grp: /etc/group|awk -F: '{print $1}'|head -1")
  if name.read().strip():
    return True
  else:
    return False

def is_readable(path, user):
  user_info = pwd.getpwnam(user)
  uid = user_info.pw_uid
  gid = user_info.pw_gid
  s = os.stat(path)
  mode = s[stat.ST_MODE]
  return (
    ((s[stat.ST_UID] == uid) and (mode & stat.S_IRUSR > 0)) or
    ((s[stat.ST_GID] == gid) and (mode & stat.S_IRGRP > 0)) or
    (mode & stat.S_IROTH > 0)
 
    )
def is_writable(path, user):
  user_info = pwd.getpwnam(user)
  uid = user_info.pw_uid
  gid = user_info.pw_gid
  s = os.stat(path)
  mode = s[stat.ST_MODE]
  return (
    ((s[stat.ST_UID] == uid) and (mode & stat.S_IWUSR > 0)) or
    ((s[stat.ST_GID] == gid) and (mode & stat.S_IWGRP > 0)) or
    (mode & stat.S_IWOTH > 0)
 
    )
 
 
def is_executable(path, user):
  user_info = pwd.getpwnam(user)
  uid = user_info.pw_uid
  gid = user_info.pw_gid
  s = os.stat(path)
  mode = s[stat.ST_MODE]
  return (
    ((s[stat.ST_UID] == uid) and (mode & stat.S_IXUSR > 0)) or
    ((s[stat.ST_GID] == gid) and (mode & stat.S_IXGRP > 0)) or
    (mode & stat.S_IXOTH > 0)
 
    )

