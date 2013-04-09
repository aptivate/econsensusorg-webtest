from pages.base import Login, Organizations
from pages.decision_detail import DecisionDetail
from pages.decision_list import DiscussionList


def test_edit_discussion(driver, server_credentials):
    # Login
    login = Login(driver, server_credentials)
    login.login_with_credentials()

    # Get Organization
    orgslug = Organizations(driver).get_all_organizations_slugs()[0]

    # Get DiscussionList
    discussionlist = DiscussionList(driver, orgslug)

    # TODO Make robust if there are no items in page
    id_links = discussionlist.get_item_links_in_page()

    # Click the first link to get to a detail page
    id_links[0].click()

    # Edit it
    discussion_page = DecisionDetail(driver)
    discussion_page.edit_description()

    # TODO Re-factor using context manager
    expected = driver.find_element_by_id("id_description").tag_name == 'textarea'

    assert expected
    if expected:
        driver.passed = True
