#!/usr/bin/env python3
"""Module for testing utils.access_nested_map."""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock



class TestAccessNestedMap(unittest.TestCase):
    """Test case for access_nested_map function"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map function."""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b"),
    ])
    def test_access_nested_map_exception(self, nested_map, path, key_error_msg):
        """Test access_nested_map function raises KeyError"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        self.assertEqual(context.exception.args[0], key_error_msg)

class TestGetJson(unittest.TestCase):
    """Test case for get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test get_json function"""
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        """configure the mock get method"""
        mock_get.return_value = mock_response
        result = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)

class TestMemoize(unittest.TestCase):
    """Test case for memoize decorator"""

    def test_memoize(self):
        """Test memoize decorator"""
        class TestClass:
            def a_metho(self):
                return 42
            
            @memoize
            def a_property(self):
                return self.a_method()
            
        test_instance = self.TestClass()

        with patch.object(self.TestClass, 'a_method') as mock_method:
            result1 = test_instance.a_property()
            result2 = test_instance.a_property()

            """Asser that a mothod was only called once"""
            mock_method.assert_called_once()
            """Assert that the result are correct"""
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)