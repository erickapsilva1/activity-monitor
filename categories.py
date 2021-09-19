#!/usr/bin/env python

import db

print(db.query("insert into CATEGORY (`REGEXP`,`CATEGORY`) values ('.*Visual Studio Code', 'coding')"))
print(db.query('select * from CATEGORY'))
