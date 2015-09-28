import os
from tool.lib import common


class SampleSubcommand():
    def __init__(self, opts):
        self.logger=common.get_logger()
        self.home = os.getenv('TOOL_HOME')
        self.options = opts

    def run(self):
        """
        run command
        """
        ########################################
        # add your own processing
        #
        return True
