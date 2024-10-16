import unittest

from src.pyTask.task import Task


class TestTask(unittest.TestCase):
    def test_task_execution(self):
        def sample_function(x, y):
            return x + y

        task = Task(sample_function, 1, 2)
        task.start()
        result = task.wait()
        self.assertEqual(result, 3)

    def test_task_with_callback(self):
        def sample_function(x, y):
            return x + y

        def callback(result):
            self.assertEqual(result, 3)

        task = Task(sample_function, 1, 2, callback=callback)
        task.start()
        task.wait()

if __name__ == '__main__':
    unittest.main()
