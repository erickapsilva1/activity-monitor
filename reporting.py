#!/usr/bin/env python

import sys
import db

dates=False
if len(sys.argv)>2:
    dates=sys.argv[1:3]

where='`CATEGORY` is not null'

if dates:
    where+=" and `WHEN` between '%s' and '%s'" % tuple(dates)

logs=db.query(
    'select count(`ID`) as SPENT, `CATEGORY` from LOG where %s group by `CATEGORY` order by SPENT desc' % where
)

for l in logs:
    print(l[0],l[1])



