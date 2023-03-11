import unittest
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_init_no_args(self):
        """
        Test initialization of BaseModel instance with no arguments.
        """
        model = BaseModel()
        self.assertTrue(hasattr(model, 'id'))
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime.datetime)
        self.assertIsInstance(model.updated_at, datetime.datetime)

    def test_init_with_kwargs(self):
        """
        Test initialization of BaseModel instance with kwargs.
        """
        kwargs = {'id': '123', 'created_at': '2022-03-09T11:30:00.000000',
                  'updated_at': '2022-03-09T11:30:00.000000',
                  'name': 'Test Model'}
        model = BaseModel(**kwargs)
        self.assertEqual(model.id, '123')
        self.assertEqual(model.name, 'Test Model')
        self.assertIsInstance(model.created_at, datetime.datetime)
        self.assertIsInstance(model.updated_at, datetime.datetime)

    def test_to_dict(self):
        """
        Test to_dict method of BaseModel instance.
        """
        kwargs = {'id': '123', 'created_at': '2022-03-09T11:30:00.000000',
                  'updated_at': '2022-03-09T11:30:00.000000',
                  'name': 'Test Model'}
        model = BaseModel(**kwargs)
        model_dict = model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], '123')
        self.assertEqual(model_dict['name'], 'Test Model')
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

    def test_save(self):
        """
        Test save method of BaseModel instance.
        """
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        new_updated_at = model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
