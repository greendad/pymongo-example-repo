from marshmallow import Schema
from marshmallow.fields import Str

from base_document import BaseDocument
from database import Database

class SampleSchema(Schema):
    field_name = Str(required=True)
    value = Str(required=True)

class SampleModel(BaseDocument):
    db = Database().get_db()
    meta = {
        "collection": "sample_model",
        "schema": SampleSchema,
    }