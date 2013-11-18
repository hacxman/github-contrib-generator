#!/usr/bin/python3
import os
import sys
import time
from datetime import datetime
from datetime import timedelta

def stringdate(days):
  d = datetime.today()
  dlt = timedelta(days=days)
  ntajm = (d-dlt)
  return time.asctime(ntajm.timetuple()), datetime.isoweekday(ntajm)

if __name__ == "__main__":
  if len(sys.argv) < 3:
    print("usage: {} FILE REPO".format(sys.argv[0]))
    exit(2)

  fname = sys.argv[1]
  repo  = sys.argv[2]
  with open(fname) as fin:
    data = fin.readlines()
  print(data)

  seen_sunday = False
  for i in range(365, 0, -1):
    dejt, dej = stringdate(i)

    if not seen_sunday and dej != 7:
      continue
    seen_sunday = True

    cnt = int(data[(365-i) % 7][(365-i) // 7])
    print(cnt, i, (365-i) % 7, (365-i) // 7, dej, dejt)
    for a in range(cnt):
      with open(os.path.join(repo, 'lulz'), "a") as fout:
        fout.write("{} {}\n".format(dejt, a))
      os.system("pushd \"{}\" > /dev/null ; git add lulz ;\
         git commit --date \"{}\" -mlol > /dev/null ; popd > /dev/null"
          .format(repo, dejt))
