import re
from django.http import HttpRequest
from django.shortcuts import resolve_url
from django.template.loader import render_to_string
from django.test import TestCase
from django.urls import reverse, resolve
from django.utils.html import escape

from lists.views import home_page
from lists.models import Item, List

# Create your tests here.


class NewListTest(TestCase):
    def test_saving_a_POST_request(self):
        self.client.post(reverse('lists:new_list'), data={
            'item_text': '신규 작업 아이템',
        })
        self.assertEqual(Item.objects.all().count(), 1)

        new_item = Item.objects.first()
        self.assertEqual(new_item.text, '신규 작업 아이템')

    def test_redirects_after_POST(self):
        response = self.client.post(reverse('lists:new_list'), data={
            'item_text': '신규 작업 아이템',
        })
        list_ = List.objects.first()
        # self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'],
                         reverse('lists:view_list', kwargs={'pk': list_.id}))

    def test_validation_errors_are_sent_back_to_home_page_template(self):
        response = self.client.post(
            reverse('lists:new_list'), data={
                'item_text': ''
            })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lists/home.html')
        expected_error = escape("You can't have an empty list item")
        self.assertContains(response, expected_error)

    def test_invalid_list_items_arent_saved(self):
        self.client.post(
            reverse('lists:new_list'), data={
                'item_text': ''
            })
        self.assertEqual(List.objects.count(), 0)
        self.assertEqual(Item.objects.count(), 0)


class ListViewTest(TestCase):

    def test_can_save_a_POST_request_to_an_existing_list(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()

        self.client.post(resolve_url('lists:view_list', correct_list.pk), data={
            'item_text': '기존 목록에 신규 아이템'
        })
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, '기존 목록에 신규 아이템')
        self.assertEqual(new_item.list, correct_list)

    def test_redirects_to_live_view(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()

        response = self.client.post(resolve_url('lists:view_list', correct_list.pk), data={
            'item_text': '기존 목록에 신규 아이템'
        })

        self.assertRedirects(response, resolve_url(
            'lists:view_list', correct_list.pk))

    def test_uses_list_template(self):
        list_ = List.objects.create()
        response = self.client.get(
            reverse('lists:view_list', kwargs={'pk': list_.id}))
        self.assertTemplateUsed(response, 'lists/list.html')

    def test_displays_all_items_for_that_list(self):
        correct_list = List.objects.create()
        Item.objects.create(text='양양이는 졸고있군요.', list=correct_list)
        Item.objects.create(text='링고는 양양이 자리를 뺏고, 자고 있어요.', list=correct_list)

        other_list = List.objects.create()
        Item.objects.create(text='양양이222는 졸고있군요.', list=other_list)
        Item.objects.create(
            text='링고222는 양양이222 자리를 뺏고, 자고 있어요.', list=other_list)

        response = self.client.get(
            reverse('lists:view_list', kwargs={'pk': correct_list.pk}))

        self.assertContains(response, '양양이는 졸고있군요.')
        self.assertContains(response, '링고는 양양이 자리를 뺏고, 자고 있어요.')

        self.assertNotContains(response, '양양이222는 졸고있군요.')
        self.assertNotContains(response, '링고222는 양양이222 자리를 뺏고, 자고 있어요.')

    def test_passes_correct_list_to_template(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()

        response = self.client.get(
            reverse('lists:view_list', kwargs={'pk': correct_list.pk}))

        self.assertEqual(response.context['list'], correct_list)


class HomePageTest(TestCase):
    # csrf_token 값 제외
    def remove_csrf(self, origin):
        csrf_regex = r'<input[^>]+csrfmiddlewaretoken[^>]+>'
        return re.sub(csrf_regex, '', origin)

    def test_root_url_resolve_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = self.remove_csrf(render_to_string('lists/home.html', {
        }))
        response_decode = self.remove_csrf(response.content.decode())
        self.assertEqual(response_decode, expected_html)
