import unittest
from selenium import webdriver


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

        # 브라우저의 타이틀이 'To-Do'인지 확인
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the Test!!!')


# '공작깃털 사기'라고 텍스트 상자에 입력

# 엔터키를 치면 페이지가 갱신되고 작업목록에 "1: 공작깃털 사기" 추가

# 추가 아이템을 입력할수 있는 텍스트 상자 존재

# '공작깃털을 이용해서 그물 만들기'라고 텍스트 상자에 입력

# 페이지 갱신, 두개의 목록

# 입력한 목록이 저장 됐는지 확인

# 특정 URL 생성

# URL에 대한 설명도 추가

# 작업목록이 그대로 있는지 확인


if __name__ == '__main__':
    unittest.main()
