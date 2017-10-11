#-*- coding:utf8 -*-

thounds_data = '''
select ss.id, ss.lyric_temp, cm.mv_name, ccm.comment
from test500.stadmin_songscover ss
left join test500.stadmin_covermaterial cm 
on ss.covermaterial_id = cm.id
left join test500.stadmin_covercomment ccm
on ccm.song_cover_id = ss.id
where ss.status != 998 and ss.status != 999
limit 500
'''