"""
File created from install / settongs
Use: from Defines import BINDIR, FILEDIR

Antonio Golfari - 2018
"""
import yaml, os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
with open('defines.yaml', 'rb') as f:
        """use safe_load instead load"""
        config = yaml.safe_load(f)


MYSQLUSER = config['db']['User']  # mysql db user
MYSQLPASSWORD = config['db']['Pass']  # mysql db password
MYSQLHOST = config['db']['Server'] # mysql host name
DATABASE = config['db']['Name'] # mysql db name

BINDIR = config['dir']['bin']  # script directory
FILEDIR = config['dir']['file']  # files directory
LOGDIR = config['dir']['log']  # log files directory
RESULTDIR = config['dir']['result']  # log files directory
IMAGEDIR = config['dir']['image']  # image/icon files directory
MAPOBJDIR = config['dir']['map']  # mapobj files directory

XC_LOGIN = config['xcontest']['User']
XC_password = config['xcontest']['Pass']
