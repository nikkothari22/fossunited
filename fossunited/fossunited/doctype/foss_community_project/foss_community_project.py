# Copyright (c) 2024, Frappe x FOSSUnited and contributors
# For license information, please see license.txt


import requests

# import frappe
from frappe.website.website_generator import WebsiteGenerator


class FOSSCommunityProject(WebsiteGenerator):
    # begin: auto-generated types
    # This code is auto-generated. Do not modify anything in this block.

    from typing import TYPE_CHECKING

    if TYPE_CHECKING:
        from frappe.types import DF

        from fossunited.fossunited.doctype.foss_community_project_links.foss_community_project_links import (
            FOSSCommunityProjectLinks,
        )

        description: DF.TextEditor | None
        github_stars: DF.Int
        header_badges: DF.HTMLEditor | None
        headline: DF.SmallText | None
        is_foss_hack_winner: DF.Check
        is_foss_united_grant_recipient: DF.Check
        is_published: DF.Check
        links: DF.Table[FOSSCommunityProjectLinks]
        logo: DF.AttachImage | None
        organisation: DF.Data | None
        project_name: DF.Data
        route: DF.Data | None
        url: DF.Data
    # end: auto-generated types

    pass

    def before_insert(self):
        self.route = f"/projects/{self.scrub(self.project_name)}"

        # Get Github stars
        if self.url.startswith("https://github.com"):
            self.github_stars = get_github_stars(url=self.url)


def get_github_stars(url):
    """
    Get the number of stars for a project on Github
    """
    url = (
        f"https://api.github.com/repos/{url.split('github.com/')[1]}"
    )
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("stargazers_count")
    return 0
