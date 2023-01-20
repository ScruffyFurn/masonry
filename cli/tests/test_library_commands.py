
from click.testing import CliRunner
from masonry import library
import unittest
import shutil
import os


class new_library_project_tests(unittest.TestCase):

    @classmethod
    def setup_class(self):
        if (os.path.exists('test')):
            shutil.rmtree('test', ignore_errors=False)

    @classmethod
    def teardown_class(self):
        os.chdir('..')
        if (os.path.exists('test')):
            shutil.rmtree('test', ignore_errors=False)

    def test_create_new_library(self):
        runner = CliRunner()
        result = runner.invoke(library.create, ['--author', 'test', '--name',
                                                'test', '--dir', './',
                                                '--desc', 'test'])
        self.assertEqual(result.exit_code, 0)
        shutil.rmtree('test', ignore_errors=False)

    def test_create_new_library_auto(self):
        runner = CliRunner()
        result = runner.invoke(library.create)
        self.assertEqual(result.exit_code, 0)
        shutil.rmtree('databricks_library', ignore_errors=False)

    def test_create_new_library_fail(self):
        runner = CliRunner()
        result = runner.invoke(library.create, ['-h'])
        self.assertEqual(result.exit_code, 2)

    def test_build_new_library(self):
        runner = CliRunner()
        result = runner.invoke(library.create, ['--author', 'test', '--name',
                                                'test', '--dir', './',
                                                '--desc', 'test'])
        self.assertEqual(result.exit_code, 0)
        os.chdir('test')
        result = runner.invoke(library.build)
        self.assertEqual(result.exit_code, 0)
        os.chdir('..')
        shutil.rmtree('test', ignore_errors=False)

    def test_lint_new_library(self):
        runner = CliRunner()
        result = runner.invoke(library.create, ['--author', 'test', '--name',
                                                'test', '--dir', './',
                                                '--desc', 'test'])
        self.assertEqual(result.exit_code, 0)
        os.chdir('test')
        result = runner.invoke(library.lint)
        self.assertEqual(result.exit_code, 0)
        os.chdir('..')
        shutil.rmtree('test', ignore_errors=False)

    def test_test_new_library(self):
        runner = CliRunner()
        result = runner.invoke(library.create, ['--author', 'test', '--name',
                                                'test', '--dir', './',
                                                '--desc', 'test'])
        self.assertEqual(result.exit_code, 0)
        os.chdir('test')
        result = runner.invoke(library.test)
        self.assertEqual(result.exit_code, 1)
        os.chdir('..')
        shutil.rmtree('test', ignore_errors=False)
