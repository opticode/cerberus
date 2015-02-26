"""
This module contains the error messages issued by the Cerberus Validator.
The test suite uses this module as well.
"""
ERROR_SCHEMA_MISSING = "validation schema missing"
ERROR_SCHEMA_FORMAT = "'%s' is not a schema, must be a dict"
ERROR_DOCUMENT_MISSING = "document is missing"
ERROR_DOCUMENT_FORMAT = "'%s' is not a document, must be a dict"
ERROR_UNKNOWN_RULE = "unknown rule '%s' for field '%s'"
ERROR_DEFINITION_FORMAT = "schema definition for field '%s' must be a dict"
ERROR_UNKNOWN_FIELD = "unknown field"
ERROR_REQUIRED_FIELD = "required field"
ERROR_UNKNOWN_TYPE = "unrecognized data-type '%s'"
ERROR_BAD_TYPE = "must be of %s type"
ERROR_MIN_LENGTH = "min length is %d"
ERROR_MAX_LENGTH = "max length is %d"
ERROR_UNALLOWED_VALUES = "unallowed values %s"
ERROR_UNALLOWED_VALUE = "unallowed value %s"
ERROR_ITEMS_LIST = "length of list should be %d"
ERROR_READONLY_FIELD = "field is read-only"
ERROR_MAX_VALUE = "max value is %d"
ERROR_MIN_VALUE = "min value is %d"
ERROR_EMPTY_NOT_ALLOWED = "empty values not allowed"
ERROR_NOT_NULLABLE = "null value not allowed"
ERROR_REGEX = "value does not match regex '%s'"
ERROR_DEPENDENCIES_FIELD = "field '%s' is required"
ERROR_DEPENDENCIES_FIELD_VALUE = "field '%s' is required with values: %s"
