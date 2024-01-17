#!/usr/bin/python3
""" Fabric script that generates a .tgz archive
  from the contents of the web_static folder """

from datetime import datetime
from fabric.api import local


def do_pack():
    """Generates a .tgz archive from the contents
    of the web_static folder of this repository.
    """

    d = datetime.now()
    now = d.strftime('%Y%m%d%H%M%S')

    local("mkdir -p versions")
    archive_path = "versions/web_static_{}.tgz".format(now)
    result = local("tar -czvf {} web_static".format(archive_path))

    if result.succeeded:
        return archive_path
    else:
        return None
