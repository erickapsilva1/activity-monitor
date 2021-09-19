#!/usr/bin/env python

import db
import re
import sys

if '--reset' in sys.argv:
    db.query('update LOG set `CATEGORY`=null')
    sys.exit(0)

categs=db.query('select * from CATEGORY order by `PRIORITY`, `ID`')
logs=db.query('select * from LOG where CATEGORY is null')

for log in logs:
    match=False
    for cat in categs:
        r='.*%s.*' % cat[1]
        if re.match(r,log[1]):
            db.query("update LOG set `CATEGORY`='%s' where `ID`=%d" % (cat[2], log[0]))
            match=True
            break
        if not match:
            print(log)


