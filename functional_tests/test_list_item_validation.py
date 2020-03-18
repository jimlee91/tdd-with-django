from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # 빈 아이템 드록
        # 입력상자 비어있는 상태에서 엔터
        # 페이지 새로고침 -> 빈 아이템을 등록할 수 없다는 에러 메시지

        # 다른 아이템 입력 정상 자처리

        # 다시 빈 아이템 등록

        # 에러표시

        # 아이템 입력 -> 정상 작동
        self.fail('write me!')
