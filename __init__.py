import sys
import os
import json
from cudatext import *
from . import format_proc
from .node_proc import *

format_proc.INI = 'cuda_css_autoprefixer.py'
format_proc.MSG = '[CSS AutoPrefixer] '

tool_js = os.path.join(os.path.dirname(__file__), 'autoprefixer.js')


def do_format(text):
    fn = format_proc.ini_filename()
    opt = eval(open(fn).read())
    opt = json.dumps(opt)
    return run_node(text, [tool_js, opt])


class Command:
    def config_global(self):
        format_proc.config_global()

    def config_local(self):
        format_proc.config_local()

    def run(self):
        try:
            format_proc.run(do_format)
        except Exception as e:
            msg_box('Error while running Node.js \n'+str(e), MB_OK+MB_ICONERROR)
