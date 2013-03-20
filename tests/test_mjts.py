#!/usr/bin/env python
import messytables_jts
import messytables
from StringIO import StringIO as sio
ts = messytables.CSVTableSet.from_fileobj(sio('''name,dob\nmk,2012-01-02\n'''))
rs = ts.tables[0]
print messytables_jts.rowset_as_schema(rs).as_json()
