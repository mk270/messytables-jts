
import messytables
from messytables.types import *
import jsontableschema

__classes = {
    StringType: "string",
    IntegerType: "integer",
    FloatType: "number",
    DecimalType: "number",
    DateType: "date",
    DateUtilType: "date"
}

def celltype_as_string(celltype):
    return __classes[celltype.__class__]

def rowset_as_schema(rowset):
    _, headers = messytables.headers_guess(rowset.sample)
    types = map(celltype_as_string, messytables.type_guess(rowset.sample))

    j = jsontableschema.JSONTableSchema()

    for field_id, field_type in zip(headers, types):
        j.add_field(field_id=field_id, 
                    label=field_id,
                    field_type=field_type)

    return j
