import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        # 웹 브라우저 접속
        self.browser = webdriver.Chrome(
            '/Users/ieonsang/study/tdd/chromedriver')
        self.browser.implicitly_wait(3)

    def tearDown(self):
        # exit
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')

        # 브라우저의 타이틀과 헤더가 'To-Do'인지 확인
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'), '작업 아이템 입력'
        )

        # '공작깃털 사기'라고 텍스트 상자에 입력
        inputbox.send_keys('공작깃털 사기')

        # 엔터키를 치면 페이지가 갱신되고
        inputbox.send_keys(Keys.ENTER)

        # 작업목록에 "1: 공작깃털 사기" 추가
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: 공작깃털 사기' for row in rows),
            "신규 추가작업이 테이블에 표시되지 않는다. -- 해당 텍스트: \n%s" % (table.text, )
        )

        # 추가 아이템을 입력할수 있는 텍스트 상자 존재
        inputbox = self.browser.find_element_by_id('id_new_item')

        # '공작깃털을 이용해서 그물 만들기'라고 텍스트 상자에 입력
        inputbox.send_keys('공작깃털을 이용해서 그물 만들기')
        inputbox.send_keys(Keys.ENTER)

        # 페이지 갱신, 두개의 목록
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: 공작깃털 사기', [row.text for row in rows])
        self.assertIn('2: 공작깃털을 이용해서 그물 만들기', [
            row.text for row in rows
        ])
        # 입력한 목록이 저장 됐는지 확인

        # 특정 URL 생성

        # URL에 대한 설명도 추가

        # 작업목록이 그대로 있는지 확인

        self.fail('Finish the Test!!!')


if __name__ == '__main__':
    unittest.main()
