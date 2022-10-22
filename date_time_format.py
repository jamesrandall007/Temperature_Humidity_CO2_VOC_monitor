from datetime import datetime

from icecream import ic

print(datetime.now())



dt_now = datetime.now()
format_dt_now = "%Y/%m/%d %H:%M:%S"

ic(dt_now.strftime(format_dt_now))