 
#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import sys
import os

"""
Admin Finder - C0d3d by Th3_M4D_Ch3M!5T.
Usage:
$ python Molecular.py http://www.domain.com
"""

c_red	= 	"\033[01;31m"
c_green = 	"\033[01;32m"
c_def	=	"\033[0m"
pages	=	['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','usuarios/','usuario/','administrator/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/','memberadmin/','administratorlogin/','adm/','admin/account.php','admin/index.php','admin/login.php','admin/admin.php','admin/account.php','admin_area/admin.php','admin_area/login.php','siteadmin/login.php','siteadmin/index.php','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html','admin_area/index.php','bb-admin/index.php','bb-admin/login.php','bb-admin/admin.php','admin/home.php','admin_area/login.html','admin_area/index.html','admin/controlpanel.php','admin.php','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html','webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html','admin/cp.php','cp.php','administrator/index.php','administrator/login.php','nsw/admin/login.php','webadmin/login.php','admin/admin_login.php','admin_login.php','administrator/account.php','administrator.php','admin_area/admin.html','pages/admin/admin-login.php','admin/admin-login.php','admin-login.php','bb-admin/index.html','bb-admin/login.html','acceso.php','bb-admin/admin.html','admin/home.html','login.php','modelsearch/login.php','moderator.php','moderator/login.php','moderator/admin.php','account.php','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.php','admincontrol.php','admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.php','adminarea/index.html','adminarea/admin.html','webadmin.php','webadmin/index.php','webadmin/admin.php','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.php','moderator.html','administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html','moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html','admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.php','account.html','controlpanel.html','admincontrol.html','panel-administracion/login.php','wp-login.php','adminLogin.php','admin/adminLogin.php','home.php','admin.php','adminarea/index.php','adminarea/admin.php','adminarea/login.php','panel-administracion/index.php','panel-administracion/admin.php','modelsearch/index.php','modelsearch/admin.php','admincontrol/login.php','adm/admloginuser.php','admloginuser.php','admin2.php','admin2/login.php','admin2/index.php','usuarios/login.php','adm/index.php','adm.php','affiliate.php','adm_auth.php','memberadmin.php','administratorlogin.php']
link 	=	sys.argv[1]

def welcome():
	os.system("clear")
	print """\033[1m

 __________________________________________________________________________
Periodic Table of Elements
  __________________________________________________________________________

   1A   2A                                         3A  4A  5A  6A  7A  8A
  -----                                                               -----
1 | H |                                                               |He |
  |---+----                                       --------------------+---|
2 |Li |Be |                                       | B | C | N | O | F |Ne |
  |---+---|                                       |---+---+---+---+---+---|
3 |Na |Mg |3B  4B  5B  6B  7B |    8B     |1B  2B |Al |Si | P | S |Cl |Ar |
  |---+---+---------------------------------------+---+---+---+---+---+---|
4 | K |Ca |Sc |Ti | V |Cr |Mn |Fe |Co |Ni |Cu |Zn |Ga |Ge |As |Se |Br |Kr |
  |---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|
5 |Rb |Sr | Y |Zr |Nb |Mo |Tc |Ru |Rh |Pd |Ag |Cd |In |Sn |Sb |Te | I |Xe |
  |---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|
6 |Cs |Ba |LAN|Hf |Ta | W |Re |Os |Ir |Pt |Au |Hg |Tl |Pb |Bi |Po |At |Rn |
  |---+---+---+------------------------------------------------------------
7 |Fr |Ra |ACT|
  ===--------------------------------------------------------------------===
   Lanthanide |La |Ce |Pr |Nd |Pm |Sm |Eu |Gd |Tb |Dy |Ho |Er |Tm |Yb |Lu |
              |---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|
   Actinide   |Ac |Th |Pa | U |Np |Pu |Am |Cm |Bk |Cf |Es |Fm |Md |No |Lw |
              -------------------------------------------------------------
  __________________________________________________________________________
Helix
  __________________________________________________________________________


"""
def usage():
	print 'Usage: Molecular.py (url)'
	print 'For Skript Kiddies: Molecular.py http://target.com/'
	print "\a"
print \
"""

  ___________________________________________________________________
                  .::Th3 M3nT4l H0sP1T4l::.
			.::Th3 M4d Sc13nT15t & Th3 Ch3m15t::.
          .::We Arent As Crazy As They Say We Are::.
  ___________________________________________________________________

"""

if len(sys.argv) > 2 or len(sys.argv) < 2:
	print "\n\033[1mCorrect usage:\n$\033[0m %s %s\n" % (sys.argv[0], sys.argv[1])
elif "http" in link:
	welcome()
	for page in pages:
		get_url	=	requests.get("%s/%s" % (link, page))
		if get_url.status_code != 200:
			print "%s  Failed	[%s]	:	%s/%s%s" % (c_red, get_url.status_code, link, page, c_def)
		else:
			print "%s  Success	[%s]	:	%s/%s%s" % (c_green, get_url.status_code, link, page, c_def)
else:
	print "\nUsage: python Molecular.py \033[1mhttp://www.Target.com\033[0m\n"

# Welcome To The Mental Hospital, A Doctor Will See You Shortly
# Your Now Under The Care Of The M4dSc13nT15t & Th3 M4dCh3m15t
# We Arent Crazy, We Know Three Can Keep A Secret As Long As The Other Two Are Dead
