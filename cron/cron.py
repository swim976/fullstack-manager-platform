import datetime
import sys
from io import StringIO

from cron.models import Log


class Cron:
    """
    所有定时任务的基类，主要用于记录日志到数据库
    """
    symbol = 'BASE_CRON'

    def __init__(self):
        self.db = {
            'symbol': self.symbol,      # 定时任务标识
            'successful': True,         # 执行状态
            'begin_at': datetime.datetime.today(),    # 定时任务开始时间
            'end_at': '',               # 定时任务结束时间
            'stdout': '',               # 定时任务执行过程中的输出
            'stderr': '',               # 定时任务执行过程中的错误输出
        }

        self.old_stdout = sys.stdout            # 输出重定向
        self.old_stderr = sys.stderr            # 错误重定向
        self.my_stdout = sys.stdout = StringIO()     # 输出重定向
        self.my_stderr = sys.stderr = StringIO()     # 错误重定向

    def __del__(self):
        sys.stdout = self.old_stdout
        sys.stderr = self.old_stderr

        self.db['stdout'] = self.my_stdout.getvalue()
        self.db['stderr'] = self.my_stderr.getvalue()

        self.insert_cron_log()

        self.my_stdout.close()
        self.my_stderr.close()

    def insert_cron_log(self):
        Log(
            symbol=self.db['symbol'],
            stdout=self.db['stdout'],
            stderr=self.db['stderr'],
            successful=False if self.db['stderr'] else True,
            begin_at=self.db['begin_at'],
            end_at=datetime.datetime.today()
        ).save()