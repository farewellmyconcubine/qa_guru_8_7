import os
from zipfile import ZipFile

import pytest

@pytest.fixture(scope='session', autouse=True)
def create_move_delete_zip():
    with ZipFile('testzip.zip', 'w') as ZipObj:
        ZipObj.write(os.path.abspath('resources/bar_menu.pdf'), os.path.basename('resources/bar_menu.pdf'))
        ZipObj.write(os.path.abspath('resources/Company_staff.xls'), os.path.basename('resources/Company_staff.xls'))
        ZipObj.write(os.path.abspath('resources/Office_characters.xlsx'), os.path.basename('resources/Office_characters.xlsx'))
        ZipObj.write(os.path.abspath('resources/Random_note.txt'), os.path.basename('resources/Random_note.txt'))

    if not os.path.exists('tmp'):
            os.mkdir('tmp')

    os.rename('testzip.zip', 'tmp/testzip.zip')

    yield

