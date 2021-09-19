#!/usr/bin/env python

import db
import re

categs=db.query('select * from CATEGORY')
logs=db.query('select * from LOG where CATEGORY is null')

for log in logs:
    match=False
    for cat in categs:
        r='.*%s.*' % cat[1]
        if re.match(r,log[1]):
            db.query("update LOG set `CATEGORY`='%s' where `ID`=%d" % (cat[2], log[0]))
            match=True
        if not match:
            print(log)


