import matplotlib.font_manager as fm
import os

font_dirs = ['{}/fonts/'.format(os.environ['HOME']), ]
font_files = fm.findSystemFonts(fontpaths=font_dirs)
font_list = fm.createFontList(font_files)
fm.fontManager.ttflist.extend(font_list)
