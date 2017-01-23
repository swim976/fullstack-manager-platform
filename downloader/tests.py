from django.test import TestCase

# Create your tests here.

import sys
from you_get import *
from you_get.extractors import *
from you_get.common import script_main
from you_get.__main__ import main as m


def main():
    # sys.argv = ['/Library/Frameworks/Python.framework/Versions/3.6/bin/you-get',
    #             'http://v.youku.com/v_show/id_XNzA0NTQ2NTEy.html?spm=a2hww.20023042.ykRecommend.5~5~5~1!2~3~A']
    # m()
    youku.download('http://v.youku.com/v_show/id_XMjE4Nzg2NzM3Ng==.html', info_only=False, output_dir='.', merge=True)

if __name__ == '__main__':
    main()