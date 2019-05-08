from selenium import webdriver
import unittest


class ScoreGatherTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_input_fyid_and_get_a_list_of_team_members_in_group(self):
        # Xiao Wang Needs to give his team members a score
        # The score is 100 marks split among himself and the members of his group

        # This score is used to calculate a 'PAF' and a 'SAPA'
        # PAF stands for Peer Assessment Factor
        # SAPA stands for Self Assessment over Peer Assessment.
        # SAPA gives an indication of how realistically students judge their individual contribution to a group project

        # The calculation and interpretation of PAF and SAPA is explained here:
        # https://elearning.uq.edu.au/guides/group-peer-assessment/paf-formula-and-moderation-overview

        # Eventually Xiao Wang will access the page to give his team mates via an iframe
        # but for now he goes to localhost
        self.browser.get('http://localhost:8000')

        # To establish which members are in his team, he needs to supply his fyid

        self.fail('Finish the test!')

    if __name__ == '__main__':
        unittest.main(warnings='ignore')

