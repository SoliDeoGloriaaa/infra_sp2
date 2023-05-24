import os
import sys

from django.conf import settings

sys.path.insert(0, "/d/python/infra_sp2/")

class TestRequirements:

    def test_requirements(self):
        try:
            with open(f'{os.path.join(settings.BASE_DIR, "requirements.txt")}', 'r') as f:
                requirements = f.read()
        except FileNotFoundError:
            assert False, 'Проверьте, что добавили файл requirements.txt'

        assert 'gunicorn' in requirements, 'Проверьте, что добавили gunicorn в файл requirements.txt'
        assert 'django' in requirements, 'Проверьте, что добавили django в файл requirements.txt'
        assert 'pytest-django' in requirements, 'Проверьте, что добавили pytest-django в файл requirements.txt'
