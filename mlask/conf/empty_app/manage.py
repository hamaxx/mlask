
#!/usr/bin/env python

import os, sys

sys.path.append(os.path.join(os.path.dirname(__file__), os.path.pardir))
os.environ.setdefault("RLIBS_SETTINGS_MODULE", "{{ empty_app }}.settings")

from mlask import manager

if __name__ == "__main__":
	manager.execute()
