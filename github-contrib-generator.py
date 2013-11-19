#!/usr/bin/python3
import os
import sys
import time
import datetime
from datetime import timedelta

def stringdate(days):
  d = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-8)))
  dlt = timedelta(days=days)
  ntajm = (d-dlt)
  return time.asctime(ntajm.timetuple()), datetime.datetime.isoweekday(ntajm)

if __name__ == "__main__":
  if len(sys.argv) < 3:
    print("usage: {} FILE REPO".format(sys.argv[0]))
    exit(2)

  fname = sys.argv[1]
  repo  = sys.argv[2]
  with open(fname) as fin:
    data = fin.readlines()

  seen_sunday = False
  j = 0
  for i in range(365, 0, -1):
    dejt, dej = stringdate(i)

    if not seen_sunday and dej != 7:
      continue
    seen_sunday = True

    cnt = int(data[j % 7][j // 7])
#    print(cnt, i, j % 7, j // 7, dej, dejt)
    sys.stdout.write("{}%    \r".format(int(100*(365-i)/364.0)))
    for a in range(cnt):
      with open(os.path.join(repo, 'lulz'), "a") as fout:
        fout.write("{} {}\n".format(dejt, a))
      os.system("pushd \"{}\" > /dev/null ; git add lulz ;\
         git commit --date \"{} -0800\" -mlol > /dev/null ; popd > /dev/null"
          .format(repo, dejt)) # ^^^^ - Timezone offset

    j += 1

  print("done")
