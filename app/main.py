def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: [dict]) -> dict:
    formatted_dict = []
    formatted_dict["errors"] = [format_linter_error(error) for error in errors]
    formatted_dict["path"] = file_path

    status = "failed"
    if len(formatted_dict["errors"]) == 0:
        status = "success"
    formatted_dict["status"] = status

    return formatted_dict


def format_linter_report(linter_report: dict) -> list:
    new_format = {
        "error": [],
        "path": linter_report["path"],
        "status": linter_report["status"]
    }

    if new_format["status"] == "failed":
        new_format["error"] = [error for error in linter_report["errors"]]

    return new_format
