from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Leonardo Perrella', cpf='12345678901',
                    email='leo.perrella85@gmail.com', phone='31-999464438')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):

        expect = 'Confirmação de Inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):

        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):

        expect = ['contato@eventex.com.br', 'leo.perrella85@gmail.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = ['Leonardo Perrella',
                    '12345678901',
                    'leo.perrella85@gmail',
                    '31-999464438']
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
