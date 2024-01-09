from unittest import TestCase

import os

from src.services.storage_service_sqlite import SQLiteSaveService


class EmailVerificationTests(TestCase):

    def setUp(self):
        self.test_data_1 = {'email': 'test1_email@test.com', 'status': 'test1_status'}
        self.test_data_2 = {'email': 'test2_email@test.com', 'status': 'test2_status'}
        self.test_db_instance = SQLiteSaveService('test.db')
        self.test_db_instance.cursor.execute(
            'INSERT INTO email_status (email, status) VALUES (?, ?)',
            (self.test_data_1['email'], self.test_data_1['status']),
        )
        self.test_db_instance.connection.commit()

    def tearDown(self):
        self.test_db_instance.cursor.execute('DROP TABLE IF EXISTS email_status')
        self.test_db_instance.connection.commit()
        os.remove('test.db')

    def test_get_record(self):
        resp = self.test_db_instance.get_record(self.test_data_1['email'])
        self.assertEqual(type(resp), dict)
        self.assertEqual(resp['data'][1], self.test_data_1['email'])

    def test_is_current_record_exist(self):
        resp = self.test_db_instance.is_current_record_exist(self.test_data_1)
        self.assertTrue(resp, True)

    def test_add_record(self):
        resp = self.test_db_instance.add_record(self.test_data_2)
        self.assertEqual(resp['status'], 'New data added')

    def test_update_record(self):
        resp = self.test_db_instance.update_record(self.test_data_1)
        self.assertEqual(resp['status'], 'Data updated')

    def test_delete_record(self):
        resp = self.test_db_instance.delete_record(self.test_data_2['email'])
        self.assertEqual(resp['status'], 'Data deleted')
