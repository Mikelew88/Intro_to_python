import os, sys

up_python_packages = os.path.abspath(os.getenv("HOME")+'/ibottalytics/python_packages')
sys.path.insert(0, up_python_packages)

from analytics import redshift_connection_tools as rs_tools

df = rs_tools.sql_to_df('select id, total from receipts limit 100')
