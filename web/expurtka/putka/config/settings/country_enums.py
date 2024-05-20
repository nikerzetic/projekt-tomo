from typing import Type

from django.db.models.enums import TextChoices


class COUNTRIES_(TextChoices):
	ad = 'ad', 'Andorra'
	ae = 'ae', 'United Arab Emirates'
	af = 'af', 'Afghanistan'
	ag = 'ag', 'Antigua and Barbuda'
	ai = 'ai', 'Anguilla'
	al = 'al', 'Albania'
	am = 'am', 'Armenia'
	ao = 'ao', 'Angola'
	aq = 'aq', 'Antarctica'
	ar = 'ar', 'Argentina'
	as_ = 'as', 'American Samoa'
	at = 'at', 'Austria'
	au = 'au', 'Australia'
	aw = 'aw', 'Aruba'
	ax = 'ax', 'Åland Islands'
	az = 'az', 'Azerbaijan'
	ba = 'ba', 'Bosnia and Herzegovina'
	bb = 'bb', 'Barbados'
	bd = 'bd', 'Bangladesh'
	be = 'be', 'Belgium'
	bf = 'bf', 'Burkina Faso'
	bg = 'bg', 'Bulgaria'
	bh = 'bh', 'Bahrain'
	bi = 'bi', 'Burundi'
	bj = 'bj', 'Benin'
	bl = 'bl', 'Saint Barthélemy'
	bm = 'bm', 'Bermuda'
	bn = 'bn', 'Brunei Darussalam'
	bo = 'bo', 'Bolivia (Plurinational State of)'
	bq = 'bq', 'Bonaire, Sint Eustatius and Saba'
	br = 'br', 'Brazil'
	bs = 'bs', 'Bahamas'
	bt = 'bt', 'Bhutan'
	bv = 'bv', 'Bouvet Island'
	bw = 'bw', 'Botswana'
	by = 'by', 'Belarus'
	bz = 'bz', 'Belize'
	ca = 'ca', 'Canada'
	cc = 'cc', 'Cocos (Keeling) Islands'
	cd = 'cd', 'Congo, Democratic Republic of the'
	cf = 'cf', 'Central African Republic'
	cg = 'cg', 'Congo'
	ch = 'ch', 'Switzerland'
	ci = 'ci', 'Côte d\'Ivoire'
	ck = 'ck', 'Cook Islands'
	cl = 'cl', 'Chile'
	cm = 'cm', 'Cameroon'
	cn = 'cn', 'China'
	co = 'co', 'Colombia'
	cr = 'cr', 'Costa Rica'
	cu = 'cu', 'Cuba'
	cv = 'cv', 'Cabo Verde'
	cw = 'cw', 'Curaçao'
	cx = 'cx', 'Christmas Island'
	cy = 'cy', 'Cyprus'
	cz = 'cz', 'Czechia'
	de = 'de', 'Germany'
	dj = 'dj', 'Djibouti'
	dk = 'dk', 'Denmark'
	dm = 'dm', 'Dominica'
	do = 'do', 'Dominican Republic'
	dz = 'dz', 'Algeria'
	ec = 'ec', 'Ecuador'
	ee = 'ee', 'Estonia'
	eg = 'eg', 'Egypt'
	eh = 'eh', 'Western Sahara'
	er = 'er', 'Eritrea'
	es = 'es', 'Spain'
	et = 'et', 'Ethiopia'
	fi = 'fi', 'Finland'
	fj = 'fj', 'Fiji'
	fk = 'fk', 'Falkland Islands (Malvinas)'
	fm = 'fm', 'Micronesia (Federated States of)'
	fo = 'fo', 'Faroe Islands'
	fr = 'fr', 'France'
	ga = 'ga', 'Gabon'
	gb = 'gb', 'United Kingdom of Great Britain and Northern Ireland'
	gd = 'gd', 'Grenada'
	ge = 'ge', 'Georgia'
	gf = 'gf', 'French Guiana'
	gg = 'gg', 'Guernsey'
	gh = 'gh', 'Ghana'
	gi = 'gi', 'Gibraltar'
	gl = 'gl', 'Greenland'
	gm = 'gm', 'Gambia'
	gn = 'gn', 'Guinea'
	gp = 'gp', 'Guadeloupe'
	gq = 'gq', 'Equatorial Guinea'
	gr = 'gr', 'Greece'
	gs = 'gs', 'South Georgia and the South Sandwich Islands'
	gt = 'gt', 'Guatemala'
	gu = 'gu', 'Guam'
	gw = 'gw', 'Guinea-Bissau'
	gy = 'gy', 'Guyana'
	hk = 'hk', 'Hong Kong'
	hm = 'hm', 'Heard Island and McDonald Islands'
	hn = 'hn', 'Honduras'
	hr = 'hr', 'Croatia'
	ht = 'ht', 'Haiti'
	hu = 'hu', 'Hungary'
	id = 'id', 'Indonesia'
	ie = 'ie', 'Ireland'
	il = 'il', 'Israel'
	im = 'im', 'Isle of Man'
	in_ = 'in', 'India'
	io = 'io', 'British Indian Ocean Territory'
	iq = 'iq', 'Iraq'
	ir = 'ir', 'Iran (Islamic Republic of)'
	is_ = 'is', 'Iceland'
	it = 'it', 'Italy'
	je = 'je', 'Jersey'
	jm = 'jm', 'Jamaica'
	jo = 'jo', 'Jordan'
	jp = 'jp', 'Japan'
	ke = 'ke', 'Kenya'
	kg = 'kg', 'Kyrgyzstan'
	kh = 'kh', 'Cambodia'
	ki = 'ki', 'Kiribati'
	km = 'km', 'Comoros'
	kn = 'kn', 'Saint Kitts and Nevis'
	kp = 'kp', 'Korea (Democratic People\'s Republic of)'
	kr = 'kr', 'Korea, Republic of'
	kw = 'kw', 'Kuwait'
	ky = 'ky', 'Cayman Islands'
	kz = 'kz', 'Kazakhstan'
	la = 'la', 'Lao People\'s Democratic Republic'
	lb = 'lb', 'Lebanon'
	lc = 'lc', 'Saint Lucia'
	li = 'li', 'Liechtenstein'
	lk = 'lk', 'Sri Lanka'
	lr = 'lr', 'Liberia'
	ls = 'ls', 'Lesotho'
	lt = 'lt', 'Lithuania'
	lu = 'lu', 'Luxembourg'
	lv = 'lv', 'Latvia'
	ly = 'ly', 'Libya'
	ma = 'ma', 'Morocco'
	mc = 'mc', 'Monaco'
	md = 'md', 'Moldova, Republic of'
	me = 'me', 'Montenegro'
	mf = 'mf', 'Saint Martin (French part)'
	mg = 'mg', 'Madagascar'
	mh = 'mh', 'Marshall Islands'
	mk = 'mk', 'North Macedonia'
	ml = 'ml', 'Mali'
	mm = 'mm', 'Myanmar'
	mn = 'mn', 'Mongolia'
	mo = 'mo', 'Macao'
	mp = 'mp', 'Northern Mariana Islands'
	mq = 'mq', 'Martinique'
	mr = 'mr', 'Mauritania'
	ms = 'ms', 'Montserrat'
	mt = 'mt', 'Malta'
	mu = 'mu', 'Mauritius'
	mv = 'mv', 'Maldives'
	mw = 'mw', 'Malawi'
	mx = 'mx', 'Mexico'
	my = 'my', 'Malaysia'
	mz = 'mz', 'Mozambique'
	na = 'na', 'Namibia'
	nc = 'nc', 'New Caledonia'
	ne = 'ne', 'Niger'
	nf = 'nf', 'Norfolk Island'
	ng = 'ng', 'Nigeria'
	ni = 'ni', 'Nicaragua'
	nl = 'nl', 'Netherlands'
	no = 'no', 'Norway'
	np = 'np', 'Nepal'
	nr = 'nr', 'Nauru'
	nu = 'nu', 'Niue'
	nz = 'nz', 'New Zealand'
	om = 'om', 'Oman'
	pa = 'pa', 'Panama'
	pe = 'pe', 'Peru'
	pf = 'pf', 'French Polynesia'
	pg = 'pg', 'Papua New Guinea'
	ph = 'ph', 'Philippines'
	pk = 'pk', 'Pakistan'
	pl = 'pl', 'Poland'
	pm = 'pm', 'Saint Pierre and Miquelon'
	pn = 'pn', 'Pitcairn'
	pr = 'pr', 'Puerto Rico'
	ps = 'ps', 'Palestine, State of'
	pt = 'pt', 'Portugal'
	pw = 'pw', 'Palau'
	py = 'py', 'Paraguay'
	qa = 'qa', 'Qatar'
	re = 're', 'Réunion'
	ro = 'ro', 'Romania'
	rs = 'rs', 'Serbia'
	ru = 'ru', 'Russian Federation'
	rw = 'rw', 'Rwanda'
	sa = 'sa', 'Saudi Arabia'
	sb = 'sb', 'Solomon Islands'
	sc = 'sc', 'Seychelles'
	sd = 'sd', 'Sudan'
	se = 'se', 'Sweden'
	sg = 'sg', 'Singapore'
	sh = 'sh', 'Saint Helena, Ascension and Tristan da Cunha'
	si = 'si', 'Slovenia'
	sj = 'sj', 'Svalbard and Jan Mayen'
	sk = 'sk', 'Slovakia'
	sl = 'sl', 'Sierra Leone'
	sm = 'sm', 'San Marino'
	sn = 'sn', 'Senegal'
	so = 'so', 'Somalia'
	sr = 'sr', 'Suriname'
	ss = 'ss', 'South Sudan'
	st = 'st', 'Sao Tome and Principe'
	sv = 'sv', 'El Salvador'
	sx = 'sx', 'Sint Maarten (Dutch part)'
	sy = 'sy', 'Syrian Arab Republic'
	sz = 'sz', 'Eswatini'
	tc = 'tc', 'Turks and Caicos Islands'
	td = 'td', 'Chad'
	tf = 'tf', 'French Southern Territories'
	tg = 'tg', 'Togo'
	th = 'th', 'Thailand'
	tj = 'tj', 'Tajikistan'
	tk = 'tk', 'Tokelau'
	tl = 'tl', 'Timor-Leste'
	tm = 'tm', 'Turkmenistan'
	tn = 'tn', 'Tunisia'
	to = 'to', 'Tonga'
	tr = 'tr', 'Turkey'
	tt = 'tt', 'Trinidad and Tobago'
	tv = 'tv', 'Tuvalu'
	tw = 'tw', 'Taiwan, Province of China'
	tz = 'tz', 'Tanzania, United Republic of'
	ua = 'ua', 'Ukraine'
	ug = 'ug', 'Uganda'
	um = 'um', 'United States Minor Outlying Islands'
	us = 'us', 'United States of America'
	uy = 'uy', 'Uruguay'
	uz = 'uz', 'Uzbekistan'
	va = 'va', 'Holy See'
	vc = 'vc', 'Saint Vincent and the Grenadines'
	ve = 've', 'Venezuela (Bolivarian Republic of)'
	vg = 'vg', 'Virgin Islands (British)'
	vi = 'vi', 'Virgin Islands (U.S.)'
	vn = 'vn', 'Viet Nam'
	vu = 'vu', 'Vanuatu'
	wf = 'wf', 'Wallis and Futuna'
	ws = 'ws', 'Samoa'
	ye = 'ye', 'Yemen'
	yt = 'yt', 'Mayotte'
	za = 'za', 'South Africa'
	zm = 'zm', 'Zambia'
	zw = 'zw', 'Zimbabwe'
COUNTRIES: Type[COUNTRIES_] = COUNTRIES_

FLAGS = {
	'ad': '&#127462;&#127465;',
	'ae': '&#127462;&#127466;',
	'af': '&#127462;&#127467;',
	'ag': '&#127462;&#127468;',
	'ai': '&#127462;&#127470;',
	'al': '&#127462;&#127473;',
	'am': '&#127462;&#127474;',
	'ao': '&#127462;&#127476;',
	'aq': '&#127462;&#127478;',
	'ar': '&#127462;&#127479;',
	'as': '&#127462;&#127480;',
	'at': '&#127462;&#127481;',
	'au': '&#127462;&#127482;',
	'aw': '&#127462;&#127484;',
	'ax': '&#127462;&#127485;',
	'az': '&#127462;&#127487;',
	'ba': '&#127463;&#127462;',
	'bb': '&#127463;&#127463;',
	'bd': '&#127463;&#127465;',
	'be': '&#127463;&#127466;',
	'bf': '&#127463;&#127467;',
	'bg': '&#127463;&#127468;',
	'bh': '&#127463;&#127469;',
	'bi': '&#127463;&#127470;',
	'bj': '&#127463;&#127471;',
	'bl': '&#127463;&#127473;',
	'bm': '&#127463;&#127474;',
	'bn': '&#127463;&#127475;',
	'bo': '&#127463;&#127476;',
	'bq': '&#127463;&#127478;',
	'br': '&#127463;&#127479;',
	'bs': '&#127463;&#127480;',
	'bt': '&#127463;&#127481;',
	'bv': '&#127463;&#127483;',
	'bw': '&#127463;&#127484;',
	'by': '&#127463;&#127486;',
	'bz': '&#127463;&#127487;',
	'ca': '&#127464;&#127462;',
	'cc': '&#127464;&#127464;',
	'cd': '&#127464;&#127465;',
	'cf': '&#127464;&#127467;',
	'cg': '&#127464;&#127468;',
	'ch': '&#127464;&#127469;',
	'ci': '&#127464;&#127470;',
	'ck': '&#127464;&#127472;',
	'cl': '&#127464;&#127473;',
	'cm': '&#127464;&#127474;',
	'cn': '&#127464;&#127475;',
	'co': '&#127464;&#127476;',
	'cr': '&#127464;&#127479;',
	'cu': '&#127464;&#127482;',
	'cv': '&#127464;&#127483;',
	'cw': '&#127464;&#127484;',
	'cx': '&#127464;&#127485;',
	'cy': '&#127464;&#127486;',
	'cz': '&#127464;&#127487;',
	'de': '&#127465;&#127466;',
	'dj': '&#127465;&#127471;',
	'dk': '&#127465;&#127472;',
	'dm': '&#127465;&#127474;',
	'do': '&#127465;&#127476;',
	'dz': '&#127465;&#127487;',
	'ec': '&#127466;&#127464;',
	'ee': '&#127466;&#127466;',
	'eg': '&#127466;&#127468;',
	'eh': '&#127466;&#127469;',
	'er': '&#127466;&#127479;',
	'es': '&#127466;&#127480;',
	'et': '&#127466;&#127481;',
	'fi': '&#127467;&#127470;',
	'fj': '&#127467;&#127471;',
	'fk': '&#127467;&#127472;',
	'fm': '&#127467;&#127474;',
	'fo': '&#127467;&#127476;',
	'fr': '&#127467;&#127479;',
	'ga': '&#127468;&#127462;',
	'gb': '&#127468;&#127463;',
	'gd': '&#127468;&#127465;',
	'ge': '&#127468;&#127466;',
	'gf': '&#127468;&#127467;',
	'gg': '&#127468;&#127468;',
	'gh': '&#127468;&#127469;',
	'gi': '&#127468;&#127470;',
	'gl': '&#127468;&#127473;',
	'gm': '&#127468;&#127474;',
	'gn': '&#127468;&#127475;',
	'gp': '&#127468;&#127477;',
	'gq': '&#127468;&#127478;',
	'gr': '&#127468;&#127479;',
	'gs': '&#127468;&#127480;',
	'gt': '&#127468;&#127481;',
	'gu': '&#127468;&#127482;',
	'gw': '&#127468;&#127484;',
	'gy': '&#127468;&#127486;',
	'hk': '&#127469;&#127472;',
	'hm': '&#127469;&#127474;',
	'hn': '&#127469;&#127475;',
	'hr': '&#127469;&#127479;',
	'ht': '&#127469;&#127481;',
	'hu': '&#127469;&#127482;',
	'id': '&#127470;&#127465;',
	'ie': '&#127470;&#127466;',
	'il': '&#127470;&#127473;',
	'im': '&#127470;&#127474;',
	'in': '&#127470;&#127475;',
	'io': '&#127470;&#127476;',
	'iq': '&#127470;&#127478;',
	'ir': '&#127470;&#127479;',
	'is': '&#127470;&#127480;',
	'it': '&#127470;&#127481;',
	'je': '&#127471;&#127466;',
	'jm': '&#127471;&#127474;',
	'jo': '&#127471;&#127476;',
	'jp': '&#127471;&#127477;',
	'ke': '&#127472;&#127466;',
	'kg': '&#127472;&#127468;',
	'kh': '&#127472;&#127469;',
	'ki': '&#127472;&#127470;',
	'km': '&#127472;&#127474;',
	'kn': '&#127472;&#127475;',
	'kp': '&#127472;&#127477;',
	'kr': '&#127472;&#127479;',
	'kw': '&#127472;&#127484;',
	'ky': '&#127472;&#127486;',
	'kz': '&#127472;&#127487;',
	'la': '&#127473;&#127462;',
	'lb': '&#127473;&#127463;',
	'lc': '&#127473;&#127464;',
	'li': '&#127473;&#127470;',
	'lk': '&#127473;&#127472;',
	'lr': '&#127473;&#127479;',
	'ls': '&#127473;&#127480;',
	'lt': '&#127473;&#127481;',
	'lu': '&#127473;&#127482;',
	'lv': '&#127473;&#127483;',
	'ly': '&#127473;&#127486;',
	'ma': '&#127474;&#127462;',
	'mc': '&#127474;&#127464;',
	'md': '&#127474;&#127465;',
	'me': '&#127474;&#127466;',
	'mf': '&#127474;&#127467;',
	'mg': '&#127474;&#127468;',
	'mh': '&#127474;&#127469;',
	'mk': '&#127474;&#127472;',
	'ml': '&#127474;&#127473;',
	'mm': '&#127474;&#127474;',
	'mn': '&#127474;&#127475;',
	'mo': '&#127474;&#127476;',
	'mp': '&#127474;&#127477;',
	'mq': '&#127474;&#127478;',
	'mr': '&#127474;&#127479;',
	'ms': '&#127474;&#127480;',
	'mt': '&#127474;&#127481;',
	'mu': '&#127474;&#127482;',
	'mv': '&#127474;&#127483;',
	'mw': '&#127474;&#127484;',
	'mx': '&#127474;&#127485;',
	'my': '&#127474;&#127486;',
	'mz': '&#127474;&#127487;',
	'na': '&#127475;&#127462;',
	'nc': '&#127475;&#127464;',
	'ne': '&#127475;&#127466;',
	'nf': '&#127475;&#127467;',
	'ng': '&#127475;&#127468;',
	'ni': '&#127475;&#127470;',
	'nl': '&#127475;&#127473;',
	'no': '&#127475;&#127476;',
	'np': '&#127475;&#127477;',
	'nr': '&#127475;&#127479;',
	'nu': '&#127475;&#127482;',
	'nz': '&#127475;&#127487;',
	'om': '&#127476;&#127474;',
	'pa': '&#127477;&#127462;',
	'pe': '&#127477;&#127466;',
	'pf': '&#127477;&#127467;',
	'pg': '&#127477;&#127468;',
	'ph': '&#127477;&#127469;',
	'pk': '&#127477;&#127472;',
	'pl': '&#127477;&#127473;',
	'pm': '&#127477;&#127474;',
	'pn': '&#127477;&#127475;',
	'pr': '&#127477;&#127479;',
	'ps': '&#127477;&#127480;',
	'pt': '&#127477;&#127481;',
	'pw': '&#127477;&#127484;',
	'py': '&#127477;&#127486;',
	'qa': '&#127478;&#127462;',
	're': '&#127479;&#127466;',
	'ro': '&#127479;&#127476;',
	'rs': '&#127479;&#127480;',
	'ru': '&#127479;&#127482;',
	'rw': '&#127479;&#127484;',
	'sa': '&#127480;&#127462;',
	'sb': '&#127480;&#127463;',
	'sc': '&#127480;&#127464;',
	'sd': '&#127480;&#127465;',
	'se': '&#127480;&#127466;',
	'sg': '&#127480;&#127468;',
	'sh': '&#127480;&#127469;',
	'si': '&#127480;&#127470;',
	'sj': '&#127480;&#127471;',
	'sk': '&#127480;&#127472;',
	'sl': '&#127480;&#127473;',
	'sm': '&#127480;&#127474;',
	'sn': '&#127480;&#127475;',
	'so': '&#127480;&#127476;',
	'sr': '&#127480;&#127479;',
	'ss': '&#127480;&#127480;',
	'st': '&#127480;&#127481;',
	'sv': '&#127480;&#127483;',
	'sx': '&#127480;&#127485;',
	'sy': '&#127480;&#127486;',
	'sz': '&#127480;&#127487;',
	'tc': '&#127481;&#127464;',
	'td': '&#127481;&#127465;',
	'tf': '&#127481;&#127467;',
	'tg': '&#127481;&#127468;',
	'th': '&#127481;&#127469;',
	'tj': '&#127481;&#127471;',
	'tk': '&#127481;&#127472;',
	'tl': '&#127481;&#127473;',
	'tm': '&#127481;&#127474;',
	'tn': '&#127481;&#127475;',
	'to': '&#127481;&#127476;',
	'tr': '&#127481;&#127479;',
	'tt': '&#127481;&#127481;',
	'tv': '&#127481;&#127483;',
	'tw': '&#127481;&#127484;',
	'tz': '&#127481;&#127487;',
	'ua': '&#127482;&#127462;',
	'ug': '&#127482;&#127468;',
	'um': '&#127482;&#127474;',
	'us': '&#127482;&#127480;',
	'uy': '&#127482;&#127486;',
	'uz': '&#127482;&#127487;',
	'va': '&#127483;&#127462;',
	'vc': '&#127483;&#127464;',
	've': '&#127483;&#127466;',
	'vg': '&#127483;&#127468;',
	'vi': '&#127483;&#127470;',
	'vn': '&#127483;&#127475;',
	'vu': '&#127483;&#127482;',
	'wf': '&#127484;&#127467;',
	'ws': '&#127484;&#127480;',
	'ye': '&#127486;&#127466;',
	'yt': '&#127486;&#127481;',
	'za': '&#127487;&#127462;',
	'zm': '&#127487;&#127474;',
	'zw': '&#127487;&#127484;',
}
assert set(x for x in COUNTRIES) == set(FLAGS), set(COUNTRIES) ^ set(FLAGS)

