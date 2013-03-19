#!/usr/bin/env python

import os, sys

sys.path.append(os.path.join(os.path.dirname(__file__), os.path.pardir))
os.environ.setdefault("MLASK_CONFIG_MODULE", "example.config")

from mlask import management

if __name__ == "__main__":
	management.execute()
