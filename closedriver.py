# -*- encoding:UTF-8 -*-
import os
import psutil
import signal

class CloseDriver(object):
    ROBOT_LIBRARY_SCOPE = 'SUITE'
    __version__ = '0.1'
    def __init__(self):
        pass

    def getAllPidByName(self, process_name):
        pid_dict = {}
        pids = psutil.pids()
        for pid in pids:
            p = psutil.Process(pid)
            _pro_name = p.name()
            lower_processName = process_name.lower()
            if _pro_name.lower().find(lower_processName) != -1:
                pid_dict[pid] = p.name()
            print("pid-%d,pname-%s" % (pid, p.name()))
        return pid_dict

    def close_process(self, process_name):
        process_dict = self.getAllPidByName(process_name)
        for key in process_dict:
            try:
                os.kill(key, signal.SIGABRT)
                print('已杀死pid为%s的进程' % key)
            except Exception as e:
                print('没有如此进程!!!')


if __name__ == '__main__':
    cd = CloseDriver()
    cd.close_process("chromedriver")

