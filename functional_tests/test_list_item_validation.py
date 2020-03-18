from .base import FunctionalTest
from selenium import webdriver


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # 빈 아이템 입력상자 비어있는 상태에서 엔터
        self.browser.get(self.server_url)
        inputbox = self.browser.find_element_by_id(
            'id_new_item').send_keys('\n')

        # 페이지 새로고침 -> 빈 아이템을 등록할 수 없다는 에러 메시지
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.self, "빈 아이템을 등록할 수 없습니다.")

        # 다른 아이템 입력 정상 자처리
        self.browser.find_element_by_id('id_new_item').send_keys('우유 사기\n')
        self.check_for_row_in_list_table('1: 우유 사기')

        # 다시 빈 아이템 등록
        inputbox = self.browser.find_element_by_id(
            'id_new_item').send_keys('\n')

        # 기존에 작성한 목록이 있는지 체크
        self.check_for_row_in_list_table('1: 우유 사기')

        # 에러표시
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.self, "빈 아이템을 등록할 수 없습니다.")

        # 아이템 입력 -> 정상 작동
        inputbox = self.browser.find_element_by_id(
            'id_new_item').send_keys('tea 만들기\n')
        self.check_for_row_in_list_table('1: 우유 사기')
        self.check_for_row_in_list_table('2: tea 만들기')

        self.fail('write me!')
