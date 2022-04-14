a ='<b>Золушка и тайна волшебного камня</b>                <td align="center" class="Cinema_new_box_2_BoxText"><table cellpadding="1"   ><td align="left" class="main"><!--  banner  --><table cellpadding="1"   ><td align="center" class="main"><a href="http://kinoteatr.megamag.by/redirect.php?action=banner&amp;goto=164" target="_blank"><img src="images/banners/2022-04-08_vostok.jpg"  alt="Ночь кино Восток Ночь кино Восток "><!--  banner  eof -->           <img src="images/pixel_trans.gif"  alt=""  >     ">Год: 2021'
import re
a=re.sub(r'</b>.*Год', '</b>\nГод', a)
print(a)