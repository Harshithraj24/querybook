import json
from const.query_execution import QueryExecutionErrorType
from lib.query_executor.exc import QueryExecutorException


def merge_str(str1: str, str2: str, separator: str = "\n") -> str:
    """Join two strings together if by the separator. If either is empty
       then separator will not be used

    Arguments:
        str1 {str} -- Joined on left
        str2 {str} -- Joined on right

    Keyword Arguments:
        separator {str} -- Middle string if both input are non-empty
                           (default: {'\n'})

    Returns:
        str -- The joined str
    """
    if len(str1) and len(str2):
        return str1 + separator + str2
    return str1 or str2


def parse_exception(e):
    error_type = QueryExecutionErrorType.INTERNAL.value
    error_str = str(e)
    error_extracted = None

    return error_type, error_str, error_extracted


def format_if_internal_error_with_stack_trace(
    exc: Exception,
    error_type: QueryExecutionErrorType,
    error_str: str,
    stack_trace: str,
):
    """If the error is internal (which means its either unknown or caused by Querybook).
       Then include the stack trace for better debugging.
       Note if the error is instance of QueryExecutorException, then we know where
       and why it is thrown. So it is ignored even tho it is internal.

    Args:
        error_type (QueryExecutionErrorType): The type of Querybook runtime error
        error_str (str): The stringified exception that was thrown
        stack_trace (str): The stack trace generated by traceback

    Returns:
        str: The combined error trace string
    """
    if error_type == QueryExecutionErrorType.INTERNAL.value and not isinstance(
        exc, QueryExecutorException
    ):
        return (error_str or "") + "\nStack trace:\n" + stack_trace
    return error_str


def get_parsed_syntax_error(
    message: str,
    line_num: int = None,
    char_num: int = None,
):
    error_type = QueryExecutionErrorType.SYNTAX.value
    error_str = json.dumps(
        {
            "line": line_num,
            "char": char_num,
            "message": message,
        }
    )
    return error_type, error_str, None


def format_error_message(code: int, message: str):
    return f"Error #{code}: {message}"
