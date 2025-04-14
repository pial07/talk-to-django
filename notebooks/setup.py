import os
import sys
import pathlib


NBS_DIR = pathlib.Path(__file__).resolve().parent if '__file__' in globals() else pathlib.Path().cwd()
sys.path.append(str(NBS_DIR))

# NBS_DIR=pathlib.Path(__file__).resolve().parent
BASE_DIR = NBS_DIR.parent



def init_django(project_name='pialhome', django_root='src'):
    PROJECT_ROOT = BASE_DIR / django_root
    os.chdir(PROJECT_ROOT)
    sys.path.insert(0, str(PROJECT_ROOT))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"{project_name}.settings")
    os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
    import django

    django.setup()

if __name__ == "__main__":
    init_django()
