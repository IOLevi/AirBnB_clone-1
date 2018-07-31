#!/usr/bin/python3
# Fabfile to:
#    - create a TAR from web_static

# Import Fabric's API module
from fabric.api import *
from datetime import datetime
import os


def do_pack():
    "packs a tar archive"
    fn = "web_static_{}.tgz".format(datetime.now().strftime("%Y%m%d%H%M%S"))
    local("mkdir -p versions")
    local("tar -cvzf versions/{} web_static".format(fn))
    if os.path.exists("versions/{}".format(fn)):
        return(os.path.abspath("versions/{}".format(fn)))
    else:
        return None
