from streamtex import *
from custom.styles import Styles as s

class BlockStyles:
    pos = s.container.positions
bs = BlockStyles

def build():
    
    st_write(toc_lvl="1", label="_AIAI")
    st_image(uri = "cameleon_aiai_01.png")

    with st_overlay() as o:
        st_image(uri = "cameleon_aiai_01.png")
        with o.layer(bottom=16, left=16):
            st_write(s.big+s.bold+s.text.colors.yellow, "AIAI")
    
    st_write(s.large,"Go to bravo label", link="#bravo")