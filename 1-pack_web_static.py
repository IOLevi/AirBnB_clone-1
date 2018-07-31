# Fabfile to:
#    - create a TAR from web_static

# Import Fabric's API module
from fabric.api import *
from datetime import datetime
import os

#env.user='ubuntu'
env.hosts = ['104.196.66.195', '35.237.47.86']
def do_pack():
    "packs a tar archive"
    fn = "web_static_{}.tgz".format(datetime.now().strftime("%Y%m%d%H%M%S"))
    local("mkdir -p versions")
    local("tar -cvzf versions/{} web_static".format(fn))
    if os.path.exists("versions/{}".format(fn)):
        return(os.path.abspath("versions/{}".format(fn)))
    else:
        return None

def do_deploy(archive_path):
    "deploys new version of  codes"

    if not os.path.exists(archive_path):
        return False

    with cd("/"):
        put("versions/*.tgz", "tmp")
    with cd("/tmp"):
        run("tar -xf *.tgz -C /data/web_static/releases/")
        run("rm *.tgz")
    run("rm -f /data/web_static/current")
    a = run("ln -s /data/web_static/releases/web_static* /data/web_static/current")
    return a.succeeded
    
def deploy():
    "calls do_pack and do_deploy"
    p = do_pack()
    if p is None:
        return False
    a = do_deploy(p)
    return a
