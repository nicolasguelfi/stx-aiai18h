from streamtex import *
from custom.styles import Styles as s
from streamtex.enums import Tags as t

def build():

    st_write(s.text.alignments.center_align + s.project.titles.title_green_01,
            "Content", tag=t.div,
            toc_lvl='2')