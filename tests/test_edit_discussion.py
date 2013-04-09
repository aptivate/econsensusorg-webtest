import pytest

class TestEditDiscussion:

    @pytest.mark.nondestructive
    def test_edit_discussion(self, mozwebqa):
    
        driver = mozwebqa.selenium
        admin = mozwebqa.credentials['admin']

        # Go to base_url defined in mozwebqa.cfg
        driver.get(mozwebqa.base_url)

        # Enter the credentials
        usernameinput = driver.find_element_by_name("username")
        passwordinput = driver.find_element_by_name("password")

        usernameinput.send_keys(admin['name'])
        passwordinput.send_keys(admin['password'])

        # This is an example of not robust - as soon as another button gets added the wrong one could get clicked
        loginbutton = driver.find_element_by_class_name("button") 
        loginbutton.click()

        driver.find_element_by_partial_link_text('Logout') # Helps the test wait until user is actually logged in  
        assert 'Organization List' in driver.title
       
        smurforg = driver.find_element_by_partial_link_text("Smurfs")
        org_slug = smurforg.get_attribute("href").split('/')[3]
        discussion_tab_url = "/".join([mozwebqa.base_url, org_slug, 'item/list/discussion/'])
        # Go to discussion tab
        driver.get(discussion_tab_url)
        # Click on a specific discussion 
        discussionlink = driver.find_elements_by_class_name("id")
        # 1th to ignore header .id
        discussionlink[1].find_element_by_xpath("./a").click()
        assert driver.find_element_by_css_selector(".page_title.discussion")
        # Edit it
        edit_link = driver.find_element_by_css_selector(".controls>.edit")
        edit_link.click()
        assert driver.find_element_by_id("id_description").tag_name == 'textarea'

