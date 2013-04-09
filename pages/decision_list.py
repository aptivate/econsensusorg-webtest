class DecisionList:
    """
    Base Class for Decision List pages
    """

    def get_item_links_in_page(self):
        """
        Get the links for all the items in the page. Note this may not be all
        the items as pagination may be limiting the result.
        """
        css_selector = "td.id > a"
        id_links = self.driver.find_elements_by_css_selector(css_selector)
        return id_links


class DiscussionList(DecisionList):

    def __init__(self, driver, orgslug):
        self.driver = driver
        baseurl = self.driver.baseurl
        discussion_url = "/".join([baseurl, orgslug, 'item/list/discussion'])
        self.driver.get(discussion_url)


class ProposalList(DecisionList):

    def __init__(self, driver, orgslug):
        self.driver = driver
        baseurl = self.driver.baseurl
        proposal_url = "/".join([baseurl, orgslug, 'item/list/proposal'])
        self.driver.get(proposal_url)
