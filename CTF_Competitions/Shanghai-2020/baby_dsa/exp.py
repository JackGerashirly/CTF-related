from hashlib import sha512,md5
from Crypto.Util.number import long_to_bytes
import gmpy2

def hash(message):
	return int(sha512(message).hexdigest(), 16) # sha512

# data
p = 3297226463037324458008837284498963372649038889390685051849680175016505646001761220109858921624266044035133134135402561235635833428206886888308027772353030767400921078346868377298401213812053250316002033941692272192644613252296579884516731560436501073253924457646558698855484781747029397755111633297587215976579633451933658235385386539518006570069653575146060016811911140614606471930327341368582979836042585406811352236326065292636484550807213756482153084427714549694264685695977531537425682212155553568848666088576932888234659355213664909753781753917401161977762663658097504411914908081677033980915039079517766159760522261279115347385813009437510156898969769563687869495721977265444799585634019880951532080217960456901788918439265788169910062822889580199366417455186595489973000351770200485095008494228829300145039695936946379585625051402553034971207474762463147744467360158847593356030745194143276254949463650698210515569533
q = 82302835442112137125891403368151249910268706824854786126600390413622302196443
g = 1156233264299340971106498371495495695225880592354374034142195518472540521911699506391311324676590685365234887170345722135060009885002334748836477169806166169806180231794918961214520698361874839110454610266388341977984902756569838594616255112661600466818870137432772800368859461445854700956291885576855069405183771903076277144927769029433730710613058788277691211698675287829143272152835171859480781061918556840079857761203012054552142555673071865310355331986288606422711525790877591376770834180618492794265362178603111236615495225612101250344421932588038244804199229449738675082560512062564365473035097263889257937140778993389305893378514344032352806521972367991027459721160744835688761657797398841523104074451793557924512992305640697344011520550723893828185707635141404445213445935586965289450282024222064488965878769991566367115153619761583843561579531705057955933288008556165952066173304891391375100346312776539530448611005
y = 290999623787731812697719691852061290246619413463636312382146969900546384514710782843153962704851916091601679028830866176332331519515156301401537173069908181509028464322647352256632424684809349121024262597006913707483811117644197481959053785475083406472583099140506505071300193356002443007750220524932219191932969202270343323955035291396808472686684787610559114702054784699365490860392737061056233160308943296478540798353134878937088336672928162894332961762277559345860479916248086821117811990391025187125193074059001086441305977133252774698996653122297123447837449168657347308016270030881395674066421144002959751936839166935726200833785132736328859710351871352567511516142170956091885352178579302299634322254818383978585773136692588922976043617337904545396146755609284163743476297772686548475170197605412847689587171522453229055932712714154869989454808561458852031769119489235598402066924082778376081494632258448434048562053

message1 = b'0234e7971889def7e60348f77db94b7a'
message2 = b'16c5ac270b72f70319657b4410d985d4'
r1 = 10859236269959765735236393779936305217305574331839234502190226708929991582386
s1 = 13707557323895695260471053137828523837745895683218331343360027380310980108819
r2 = 41960642246379067640524709416001536058292817319109764317369777224426218746518
s2 = 74676725322515593502346275468843411563746982149373670021082686341369076719088
h1 = hash(message1)
h2 = hash(message2)

'''
for i in range(1,512):
    for j in range(1,512):
        C = (gmpy2.invert(i,q) * j) % q
        t = gmpy2.invert((r2 * s1 - r1 * s2 * C),q)
        possi_k1 = ((r2*h1 - r1 * h2) * t) % q
        check = pow(g, possi_k1, p) % q
        if check == r1:
            print("----- Fund! -----")
            print(possi_k1)
'''       
k1 = 77848834446550608347531937137939661582784844474315975183877393841202843491327
x = ((k1 * s1 - h1) * gmpy2.invert(r1,q)) % q
flag = 'flag{'+md5(long_to_bytes(x)).hexdigest()+'}'
print(flag)