"""
Documentation site format rules
"""
import os
from doc_extract.parse import LibraryStructure


def read_file(path):
    """
    Reads a file
    """
    with open(path) as file_pointer:
        return file_pointer.read()

def create_home_page():
    """
    Creates the documentation home page
    """
    readme_path = f"{os.path.dirname(CURRENT_DIR)}/README.md"
    readme = read_file(readme_path)

    with open(f"{CURRENT_DIR}/index.md", "w") as file_pointer:
        file_pointer.write(readme)

def create_module_markdown_files():
    """
    Creates a markdown file for each
    of the modules in the library
    """
    structure = LibraryStructure("django_auto_model")
    serialized = structure.serialize()

    for module in serialized["modules"]:
        module_name = module["module"]["name"]
        if module_name.startswith("django_auto_model.tests"):
            print(f"- Skipping module {module_name} (Test module)")
            continue

        if not module["classes"] and not module["functions"]:
            print(f"- Skipping module {module_name} (No classes, no functions)")
            continue

        filename = (
            f"{CURRENT_DIR}/modules/{module_name}"
            .replace("django_auto_model.", "")
            .replace(".", "_") + ".md"
        )

        with open(filename, "w") as file_pointer:
            file_pointer.write(format_module(module))
            print(f"+ Generated {filename}")

def format_module(serialized_module):
    """
    Formats a module
    """
    formatted_classes = "\n".join(format_class(kls) for kls in serialized_module["classes"])
    formatted_functions = "\n".join(format_function(func) for func in serialized_module["functions"])
    return MODULE_TEMPLATE.format(
        name=serialized_module["module"]["name"],
        docstring=serialized_module["module"]["docstring"],
        classes=formatted_classes,
        functions=formatted_functions,
    )

def format_class(serialized_class):
    """
    Formats a class
    """
    formatted_functions = "\n".join(format_function(func) for func in serialized_class["methods"])
    return CLASS_TEMPLATE.format(
        name=serialized_class["name"],
        docstring=serialized_class["docstring"],
        functions=formatted_functions,
    )

def format_function(serialized_function):
    """
    Formats a function
    """
    return FUNCTION_TEMPLATE.format(
        name=serialized_function["name"],
        docstring=serialized_function["docstring"],
    )

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
MODULE_TEMPLATE = read_file(f"{CURRENT_DIR}/templates/module_template.md")
CLASS_TEMPLATE = read_file(f"{CURRENT_DIR}/templates/class_template.md")
FUNCTION_TEMPLATE = read_file(f"{CURRENT_DIR}/templates/function_template.md")
