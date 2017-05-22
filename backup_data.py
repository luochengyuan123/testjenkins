# -*- coding: utf-8 -*-
#!/usr/bin/python


import os

def backup_data():
	shell_str = 'find /data/django/blogdev -name "db.sqlite3" | xargs -I {} scp {} /data/yuan/'
	os.system(shell_str)


if __name__ == '__main__':
	backup_data()
