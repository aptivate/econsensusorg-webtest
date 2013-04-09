#!/usr/bin/env python
import optparse
import sys
import unittest 
from selenium import webdriver

class TestEditDiscussion(unittest.TestCase):

    def setUp(self):
        print opts
        self.username = opts.username
        self.password = opts.password
        self.remote_url = opts.remoteurl
        self.base_url = opts.baseurl

        if self.remote_url: 
            caps = webdriver.DesiredCapabilities.FIREFOX
            caps['platform'] = "Linux"
            caps['version'] = "19"
            caps['name'] = 'Testing Econsensus Edit Discussions'
            self.driver = webdriver.Remote(
                desired_capabilities = caps,
                command_executor = self.remote_url
            )
        else:
            self.driver = webdriver.Firefox()

        self.driver.implicitly_wait(30)


    def test_edit_discussion(self):
    
        driver = self.driver

        driver.get(self.base_url)

        # Enter the credentials
        usernameinput = driver.find_element_by_name("username")
        passwordinput = driver.find_element_by_name("password")

        usernameinput.send_keys(self.username)
        passwordinput.send_keys(self.password)

        # This is an example of not robust - as soon as another button gets added the wrong one could get clicked
        loginbutton = driver.find_element_by_class_name("button") 
        loginbutton.click()

        driver.find_element_by_partial_link_text('Logout') # Helps the test wait until user is actually logged in  
        assert 'Organization List' in driver.title
       
        smurforg = driver.find_element_by_partial_link_text("Smurfs")
        org_slug = smurforg.get_attribute("href").split('/')[3]
        discussion_tab_url = "/".join([self.base_url, org_slug, 'item/list/discussion/'])
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

    def tearDown(self):
        if self.remote_url:
            print("Link to your job: https://saucelabs.com/jobs/%s" % self.driver.session_id)
        self.driver.quit()

if __name__ == "__main__":
    parser = optparse.OptionParser()
    parser.add_option('--username')
    parser.add_option('--password')
    parser.add_option('--baseurl')
    parser.add_option('--remoteurl', help='Supply remote url to run on saucelabs')
    (opts, args) = parser.parse_args()
    print opts
    sys.argv[1:] = args
    unittest.main()

