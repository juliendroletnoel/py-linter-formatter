def format_linter_error(error: dict) -> dict:
    formatted_dict = {}
    formatted_dict["line"] = error["line_number"]
    formatted_dict["column"] = error["column_number"]
    formatted_dict["message"] = error["text"]
    formatted_dict["name"] = error["code"]
    formatted_dict["source"] = "flake8"
    return formatted_dict

def format_single_linter_file(file_path: str, errors: list) -> dict:
    formatted_dict = []
    formatted_dict["errors"] = [format_linter_error(error) for error in errors]
    formatted_dict["path"] = file_path
    formatted_dict["status"] = "failed"
    return formatted_dict

def format_linter_report(linter_report: dict) -> list:
    formatted_list = []
    return formatted_list
