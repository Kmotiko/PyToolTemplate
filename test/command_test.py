#!/usr/bin/env python
import logging
import os
import pytest
from subprocess import Popen, PIPE
import shutil
import subprocess
import unittest
home = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
libdir = os.path.join(home, 'src')

import sys
sys.path[0:0] = [
  libdir,
  ]
import tool_main


class CommandTest(unittest.TestCase):
    def setUp(self):
        return

    def test_all_commands(self):
        """
        """
        sys.argv=['tool', 'sample', 'sample_argument']
        assert tool_main.main() == True

        return

if __name__ == '__main__':
    pytest.main()
