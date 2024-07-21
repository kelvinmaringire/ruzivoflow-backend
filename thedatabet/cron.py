from django_cron import CronJobBase, Schedule
from thedatabet.forebet import main as forebet
from thedatabet.stats import main as stats
from thedatabet.betway import main as betway


class ForebetData(CronJobBase):
    RUN_AT_TIMES = ['08:00']

    schedule = Schedule(run_at_times=RUN_AT_TIMES)
    code = 'thedatabet.forebet'    # a unique code

    def do(self):
        forebet()


class StatsData(CronJobBase):
    RUN_AT_TIMES = ['09:00']

    schedule = Schedule(run_at_times=RUN_AT_TIMES)
    code = 'thedatabet.stats'    # a unique code

    def do(self):
        stats()


class BetwayData(CronJobBase):
    RUN_AT_TIMES = ['05:00']

    schedule = Schedule(run_at_times=RUN_AT_TIMES)
    code = 'thedatabet.betway'    # a unique code

    def do(self):
        betway()