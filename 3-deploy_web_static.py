#/usr/bin/python3
from fabric.api import *
from datetime import datetime
import os

env.hosts = ['104.196.66.195', '35.237.47.86']
env.key_filename = "~/.ssh/holberton"
env.user = "ubuntu"

def do_pack():
    "packs a tar archive"
    fn = "web_static_{}.tgz".format(datetime.now().strftime("%Y%m%d%H%M%S"))
    local("mkdir -p versions")
    local("tar -cvzf versions/{} web_static".format(fn))
    if os.path.exists("versions/{}".format(fn)):
        return "versions/{}".format(fn)
    else:
        return None

def do_deploy(archive_path):
    "deploys new version of  codes"
    ap = archive_path.split("/")[1]
    apsans = ap.split(".")[0]
    try:
        put(archive_path, "/tmp/{}".format(ap))
        run("mkdir -p /data/web_static/releases/{}".format(apsans))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(ap, apsans))
        run("rm /tmp/{}".format(ap))
        run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(apsans, apsans))
        run("rm -rf /data/web_static/releases/{}/web_static".format(apsans))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(apsans))
        return True
    except:
        return False
        
def deploy():
    "calls do_pack and do_deploy"
    p = do_pack()
    if p is None:
        return False
    a = do_deploy(p)
    return a
