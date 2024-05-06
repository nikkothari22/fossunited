import frappe

from fossunited.fossunited.doctype.foss_community_project.foss_community_project import (
    get_github_stars,
)


def update_community_project_stars():
    """
    Update the stars for all community projects
    """
    projects = frappe.get_all(
        "FOSS Community Project",
        filters={"url": ["like", "https://github.com%"]},
        fields=["name", "url"],
    )
    for project in projects:
        stars = get_github_stars(project.url)
        frappe.db.set_value(
            "FOSS Community Project",
            project.name,
            "github_stars",
            stars,
        )
