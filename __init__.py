# -*- encoding:UTF-8 -*-
import sys

sys.path.append('C:/Python/Python37/Lib/site-packages')
from CloseProcessLib.closedriver import CloseDriver


class CloseProcessLib(CloseDriver):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
