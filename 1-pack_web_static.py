#!/usr/bin/python3
""" Creates .tgz archive from the contents of the web_static dir """
from fabric.api import local, settings
import datetime


def do_pack():
    """ Creates .tgz archive from the contents of the web_static dir """
    dtime_stamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    pre_path = 'versions'
    archive_path = '{}/web_static_{}.tgz'.format(pre_path, dtime_stamp)

    with settings(warn_only=True):
        local('mkdir -p {}'.format(pre_path))
        result = local('tar -cvzf {} web_static'.format(archive_path))
        if result.failed:
            return None
    return archive_path
