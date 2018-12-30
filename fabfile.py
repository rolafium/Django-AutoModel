"""
Fabfile
"""
from fabric.operations import local
from docs.rules import create_home_page, create_module_markdown_files

def clean_docs():
    """
    Cleans the docs/modules folder of any existing .md files
    """
    local("rm -f docs/*.md")
    local("rm -f docs/modules/*.md")

def prepare_docs():
    """
    Creates the documentation files
    """
    clean_docs()
    create_home_page()
    create_module_markdown_files()

def serve_docs():
    """
    Serves the docs without creating the site folder
    """
    prepare_docs()
    local("mkdocs serve --config-file docs/mkdocs.yml --no-livereload")

def create_docs():
    """
    Creates the docs site
    """
    prepare_docs()
    local("mkdocs build --config-file docs/mkdocs.yml")
