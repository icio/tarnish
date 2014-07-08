from argparse import ArgumentParser


def cant_handle_my_tarn():
    print """
00OkkxxxxkkOOO0XWWWWW0o0MMMMMMMMMMMMMMMMMMMMMMMN0000000000000000000OOOOO00OO000KKKKXXNNNWWWWWd,cKMMMMMMMMMMMMMMMMMMMMMMMMM
K0OOkkxxxkkOOO0XNWWWWx',lllccklcccccccclc,clc:cc::::;lOc;::,,::;;;:::;,;;:;',::,;::::::l:cccc;.,:ccllXMMMMMMMMMMMMMMMMMMMM
K00OkkkxxkkOOO0KNWWW0'oXXxXNd. dWNWX'.OWO.oW0;x0WWXOc,d.kWX;oWX' cWNWO. :NX;:WN';XWK0XO, dWX,..0WN0x'0MMMMMMMMMMMMMMMMMMMM
KK0OkkxxxkkOOOOKNWWWk,NMx OMN'.0W0NMc.OMMkOMK. ,WMx .lo.OMWlkMN' dM0KN; :WMXkMN';NMdcMMo xMN, .KMK. ,XMMMMMMMMMMMMMMMMMMMM
KK0OOkkxxkkOOOOKNWWWx,NMx ';; ;NXlKMd.OMMMWMK..,WMx .'..OMMMMMN'.OWlxMd :WMMWMN';NMdcMMd xMN, .KMWKd,KMMMMMMMMMMMMMMMMMMMM
KKK0OkkxxkkOOOO0XWWWk,NMx cxd.dMXdXM0'OM0KMMK. 'WMx     OMWokMN';NWk0MX.:WOxWMN';NMdcMMd xMN, .KMX;.;XMMMMMMMMMMMMMMMMMMMM
XKK0OkkxxxkkOOO0XNWWO'OM0cXM0;XMKl0MN:OMl;NMK. 'WMx     OMN;dMN;dMWxkMM::Wx.OMN';NM00MMl xMWO:.KMNkd'OMMMMMMMMMMMMMMMMMMMM
XKK0OkkkxxkkOOO0XNWWNc'cxkxl'.oo; ,oo':o' ;oc  .oo;     :ol.,ol.:oc..oo,'o; ,oo..looooc. ;ooo;.coooo'0MMMMMMMMMMMMMMMMMMMM
XKK00kkxxxkkOOO0KNWWWNKl;odx0Okxo,.                               ....';ccloollodooddkOK0kxxxx;',oxk0WMMMMMMMMMMMMMMMMMMMM
XXKK0OkkxdxkkOOOKNWWWWW0xNMMMWWk,.                                ....';ldkOOOO000KXNWWMMMMMMNd:lKMMMMMMMMMMMMMMMMMMMMMMMM
XXKK0OkkxdxkkOOOKXNWWWWKdXMMWkc.                            .     ....''';okOOOO00KXNWWMMMMMMWx:c0MMMMMMMMMMMMMMMMMMMMMMMM
XKKK0OkkxdxkkOOO0XNWWWWXd0WWXl.                  .    ..............''''''cxkOOO00KXNWWMMMMMMWk:c0MMMMMMMMMMMMMMMMMMMMMMMM
oooooooooooddxxxkOKXXXNXxONNx.            ..........................''',;,cxkOOOO0KXNWWMMMMMMMOccOMMMMMMMMMMMMMMMMMMMMMMMM
'''''''''',,,,,,;;;;:::::c:'.      ........',:ccc:::c:;,,''.........'',;cccdkkkOO0KXNWWMMMMMMM0c:kMMMMMMMMMMMMMMMMMMMMMMMM
....................''.....      ........,;clodddddooodolcccc::;;;,,;::codolxkkkO00KNNWMMMMMMMXc:xMMMMMMMMMMMMMMMMMMMMMMMM
..........................      ...'....,;cloddxxxxkkxkxdddddooooolccddooxo:dkkkOO0KXNWWMMMMMMXl:dWMMMMMMMMMMMMMMMWMMMMMMM
..........................      ..,::;,;:loddddxxxxkkxxxxxkkkkkkkkkOx0XX0OocdkkkkO0KXNWWMMMMMMNo;oNMMMMMMMMMMMMMMMMMMMMMMM
.........................       ..;cllloodddddxxxxxxxxkkkkkkOOOO00KXXNWMMKxodxxxkO0KXNWWMMMMMMWo;lXMMMMMMMMMMMMMMMMMMMMMMM
..........................      .';clooddddddddxxxxkkkkkkOOO000KKXNNWWWMMXxddddxxkOKXNWWMMMMMMWd;cXMMMMMMMMMMMMMMMMMMMMMMM
 .........................     ..':cloooddddddddxxkkkkkOOOO000KKKXNNNWWMMXkdooddxkO0XNWWMMMMMMWx;cKMMMMMMMMMMMMMMMMMMMMMMM
 ..  .....................    ..':oxxxkkkkkxxxxxxxxxxxxxkkkOOOOkO00KXNNNWN0OkxxkkkO0KNWWMMMMMMMk;cKMMMMMMMMMMMMMMMMMMMMMMM
      .....................  .;cox0KKKOd::;...'',,;:ldkOOOO0000Okdlc:coxxkkOOKNWWKk0KNWWMMMMMMMk;c0MMMMMMMMMMMMMMMMMMMMMMM
         .................''.,ll;,;d0k'..'.. ....... .'oKKXXNXk;.....,:coollll0NXOkOKNWWMMMMMMMO;:0MMMMMMMMMMMMMMMMMMMMMMM
         ................::clcl,  .,ko   ....''.     ..:K0kk0K:.......',::;;:ckXxdxOKNNWMMMMMMM0;:OMMMMMMMMMMMMMMMMMMMMMMM
            ............,::lllc'.,::xo. ........   ....c0xxO0Kl......',;:c:;:cOOooxOKNNWMMMMMMWK::OMMMMMMMMMMMMMMMMMMMMMMM
           .............::cool;.':lodx'.........  .....dxdxOKKO;.....',:clc:coKdloxk0XNWWMMMMMMXc;kMMMMMMMMMMMMMMMMMMMMMMM
            ............;:col:::;:lodkl..... ........'oxddxkKK0o'.'..',:lolccxxlloxk0XNWWMMMMMMXl;kMMMMMMMMMMMMMMMMMMMMMMM
             ...........'cllccllc:clodxl..      ....;lllddxk0XKkd:'''';:llclddllloxk0XNWWMMMMMMNo;xWMMMMMMMMMMMMMMMMMMMMMM
            .............;llllllcccloddxdl:,'.'',:colclodxkO0XNOdxdollodxOKKdllllodk0XNWWMMMMMWWx:dNMMMMMMMMMMMMMMMMMMMMMM
         .. ..............;llodoccccldddddxxxxxxxdolldddoodxkKKX0OO0KNNWWWW0ollllodk0XNWWMMMMMWWk:oNMMMMMMMMMMMMMMMMMMMMMM
             ..............;looolccclodddxxxxkxxxxddoolllloxOkx0KKKXNNWWWWNklllllodk0XNWWMMMMMWWO:oXMMMMMMMMMMMMMMMMMMMMMM
            ................':c:;:cclooddxxxxkkkxxxdddoodxxk000KXNNXXNWWN0dllllllldxOKNNWMMMMMMW0:lXMMMMMMMMMMMMMMMMMMMMMM
                 ................':cloooddxxxxxxddddddoodkkk0XXKKXNNNNWWOccclllllodxOKXNWMMMMMWWKclKMMMMMMMMMMMMMMMMMMMMMM
                   .. .   ........,cloooddddxxxddddooooooddxk0XXKKNNNWWXo:cccllllldxOKXNWWMMMMWWXlc0MMMMMMMMMMMMMMMMMMMMMM
                   .  ..   ........;cloooddddxxdolccclllc:::ldOK0OKNNWWk:::ccllllldxOKXNWWMMMMWWNlc0WMMMMMMMMMMMMMMMMMMMMM
                       .. ..........,cloodooddddooolllldxxddxkO0KXXXNNOl::::cllllloxOKXNWWMMMMMWNo:OWMMMMMMMMMMMMMMMMMMMMM
                         ...........,;:clooooooooooooolloooooxkk0XXXNkc:::::cclllloxkKXNWWMMMMMWWd:OWMMMMMMMMMMMMMMMMMMMMM
                         ........  .,;;:cllooooooooooddxxxxkOOO0KXNNOc:::::::clllloxkKXNWWMMMMMWWd:kWMMMMMMMMMMMMMMMMMMMMM
                                   .;:c::::cllooooodddxxkkO0KXKXNNkcoxc::::::cccclodk0XNWWMMMMMWWx;xNMMMMMMMMMMMMMMMMMMMMM
                                ...':cllcc:::cccllooooddxxkkO0KXXX;.;KOc:::;:cccclldk0XNWWMMMMWWWx;dNMMMMMMMMMMMMMMMMMMMMM
                             .......,cllollc:::::cccclllooodxOKXN0, 'kXdccloooolccldx0XNWWMMMMWWWk;oNMMMMMMMMMMMMMMMMMMMMM
                ...         .',......;clooooolc:::::::::cloxOKXX0d.'cd0Kl,;;:;'';codx0KNWWMMMMWWWk;oXMMMMMMMMMMMMMMMMMMMMM
          ..'',;::....     ..,:'......';clooddddoolllllodkO0K0Oxl;:xkkONNk;,'.....cxOO0KXNNWWWWWWO;lXMMMMMMMMMMMMMMMMMMMMM
      ...';::::;,'......   .,;:,........,;:clooodddxxkkkOOOkxdl:';k0OkkXWNl.......,:odxk0K0O0KXNWO;lXMMMMMMMMMMMMMMMMMMMMM
........,::;;,'...,;;;;'.   ,;::'.......,,;;:clllloodddddddol:;,,ck0OOOKNXk;'..,;',:looldxkkkxxk0O:cKMMMMMMMMMMMMMMMMMMMMM
...',codxc;;;;::::cllllc.   .,,,,.......',,'.....';ldddooolc:;,';::::xk0K0Oxl:::c:ldk0K0OkxxxxxxkxxdKWMMMMMMMMMMMMMMMMMMMM
:dxkOKK0kc::::::::cllooo;....,,,;;.......'..      .,colllcc::;,;c'...ckOK0OOkdlcddldk0KKXKOOO0K000OxOXNWMMMMMMMMMMMMMMMMMM
xkxxO000d;;:::::::ccccccc;,'';::::,....'............,ccllcc:;::c,....'oOXXK0XX0OOOooxO0KKKOkOO0OO0XXKKKKOOXWWWMMMMMMMMMMMM
cooooooo;.........''''',,;,''cllol:'.,;;..,;:;......';clllcccol:,'....;d0NXKXXK000c,;cldxkkxxddollokO0Oko:lx0XWMMMMMMMMMMM
looooodo;..........'''',,,'..:ooolc,''','.',,,......'';clccc:;'.........;o0KKKOkkx:',:clllllc:::::llloollloxxlkNWMMMMMMMMM
looddxxx;.........''''',;;.  ':,'...'''''.............';c:::,'''',,,,'.....,cdocccc,,,,:clllc:;;:col::::cldxocoONWMMMMMMMM
ldxxkkOk:''.......,,;;;::c;.......''''',,'...........',ccc:,.'',,;:::;,,,'...cocccdoc;',:lllc:;:cooc;;;:ccdxoodkKWMMMMMMMM
oddxxkOk:'''''''',;:::::ccc,.....'''',,,,,''''...'...coolc:'',,,;:ccc:;;;,''':occlx0d:,,;cdxoccclxdcc;;::;cld0KXNN00XNWWMM
lddxxkOx;'''''''',;:::cccclc,...',,,;;;:::;,,,,'..''cdddooc;,;:;:cllllccc:;;,:dolokXO:,',;ldxlccokl;::::;,;cd0KKXNOc:cldxO
:dddxxko,'''''''',:::ccccclc:,''',;;;;;:::;;;,;,'..cdoooooc;;;::::llollcc:;;;;ddodkXKl;''';lxollokl,,::;'';cd0KKKXNXOxol::
;dodoll:.........,;;;;:::;;;;;,,,,;;;;;::::;;,,,'.'lo::cloc;;;:;;:cloolc::;;;;ldddkKKl;,'.',cdlcldc,,;;,'';cdO00000KXNWNXK
'clllll:.........,;;;;;;;;,'';;;,,;;;;;:::c;,,'''.'ll;;cooc;:;;;;;:clllc::;;;,cdddx0Xo,'....':cccl,.',,c:,:lc;cdxxxxkKWWWW
.:llolc:'........;;;;;;;,,,.',;,'',,,,,;;::;'......clc:ccc;''',,,,;:ccc:,,,''.'cook0Xd,'.....,::cl,..'':;::;..'lddxddx0NWW
.'lol:;::'......';::;;;;,,'..',;'''',,,,:c:;'.....'ccllcc:,..',;;;;:ccc:,,'....:ookKXx,''....';::c'.'.,:;,....,coodddddONW
..:ol:::lc.....',::::;;;;,'..',;,',,,,,;:cc;'......:ccllcc;...,;;;;:ccc:;,''...;odk0Xk;,'....',;:c'.''ld:'...,;:cloddxxk0N
..'llcclod:..'',:llllccc::;'',;::;;;,,;:clc;'......:cccccc;'...,,,;:cllc;,'....;dxOKX0l;,'''.';:cl;'':oc::'.',;;:ldxkkkOOK
 ..,lc:codo,.'',:llllcccc:;'',;:ccllcccldddc;,,'...coooollc;,',;;;::lodol:;,,'':xk0KXKd:;;,,',::clc,,;;;c:,,;;;;;:odxxxxxk
 ...,l::lodc'.'':llllccc::,',,,;:clolclodxdl::;,'..;loddollc;,,;::;;:lddlc:;;,';dk0KXKd:;;,,,,:::cc,'',:do;:;;;;;:ldxxxxxx
.....:c::ldo,..':llllccc::,'',,,;:loollddxdl::;;;'.'looddolc;,,:::;;;:oooc:;;,,,oO0KXXx:;;;;,,:::cc,.,cdxxo:::::cccoxkkkkk
;;;'..::;:lo'...;ccccccc:;,'''',,;:looodddolc:::;'..cooddool:,,;:;;;::colc::;,'':x0KXXk:;,,,,,:cccc,.:oxxxxd:,;;:::ccloddd
;::;'..,',c:....,;;;;;;;,'.......',;:clollll:;;;;'..;ccooollc,,,;;,,;;;cc:;;,'...lO0K0x;'......;::;,':lodoooo;,'.....,;coo
,,,'...,,:;,....;;;;;;::;,'''','',,::::::::::,,,'...,::ccc::;'..''''''',;'.'''..';k00Okxxdl,..',;,;;...,;;:ccllc.......':l
.......';;,;;'..,;;;;::::,,,,;;;,;;:c:::;::c:,,,'...,:::::::;'..'''''''',..'''''';xO00OkOkx;.'''.';,.  ,cclloool,.......';
........:c;;;....',,;;::;,',,,;,,,;:c:::;;:::;,,''..':;,,,;;;'..'''''''','...'.'';xO000OOkd'';,,,::'   ,looddddd:.......';
........dOl;;'......',,,,.....''''',:;;;;;;:;,,,,'..':;,,;;;;'...'''''''''......',xOOOkkkd:';'..,:;.  .,dxxxxxxko,.'''''',
........:ko,.......''',,'..........,;;,;cllllc:c:;'.;lllccccc:;,,;;;;cc:,'''...',,xOOOkkxo;.,'.,:;,.  .'oxkxxxxkk;'''','',
........'lxl'....'''''','..........,;,;cxkkkxxddxdl;lkxkkkkxxxdooooolodl;;,;,,,;;:k00OOkkx;..'',:;,....'cdxxxxkkOc''''''''
...''''..'od;;;;;:;;;;;;;,,,,,,;;;;:::cokkkOkxxxddl:cxxkkkxkxxdooollooolllclllloddONNXXKKKd::::clc'  ...,loooodddc........
...',,''..cd;,;;ccllclloollccllloodddoddkkkOOkkkxdl:;dxxkxxkxxdoollloddoloclooooodOXXXXXXXdcccccc:.  ....:lllooodc........
....',''...,.',;:lllclloollllllllloddodoxxkkOkkxxdoc;dxxkkkkxxddolclodxoloclcllood0XXX00Kkcc:::;,.   ....coooddddl........
.....''..........,;;;:::::::::::cccolllcllllolllllc:,cooddooooc::;;;;:c:;;,''''',;dOxdodl'.....'..   ....:ddxxkkkx;',,'',,
..''''..';;,. .........'...........',,,',,,,,'.''''..':::::::;,.....',;,',........lOkoo:.......... ...',;dKKKKKKKKo:c::::c
cc::;'. ';;;.   ...................''''',,,,,........':;::;::;,.....',;,','.......:kkxd,... .....  ..',;;lkkOOOOkkdodddxxk
lcc:;'. 'c::;.    .................'''''',,,,........':;;;;;;;,.....',;,','.......,dOxx;..   ....     .,cloddxxkkkkkkOOOOO
lc::;'. .cccc;.....................''''',,,,,'........;;;;;;;;,.....',;,','.......'okkkc.........      .:lodxxkkkkkOOOOOOO
cc:;,.  .;ccc;......',,',,'........''''',,,,,'........,,;;;;,;'....'',;;,;,''...'.,dOOkd,....'...       .:lodxxkkkkOOOOOOO
cc:;,.  'cllc:......'''.'''........''''',;;;;'''',,'.',',,,,,,,....'',,,,,,'......,odxdxc.......         'codxxkkkkOOOOOOO
c:;,'.  'ccll:.......,lllll; .lllllc..lll:. ;lll..,..clllllllll. .:llllll.'..llllllll:';'.lll' .;llc.     'coddxxxkkkkkkOk
:;;,.   .;::cc...... dMMMMMK.oMMMMMX'.KMMN'.KMMk..'..KMMMMMMMMN' 'NMMMMMW;..,WMMMWWMMWo. :MMMO..OMMX'      ':odddxxkkkkkkk
:;,'.   '::cc,. .... dMMMMMW,xMMMMMX' :NMMllWMW:.''..,,lWMMMx,;. ;WMMWMMMo .,WMMMxcWMMN' :MMMWd.OMMX'       .coddxxxxkkkkk
;,,'.   '::::.     . dMMMMMMd0MWMMMX'  xMM00MMk..''..;.,WMMMl.;. oMMWOMMMk..'WMMMd,WMMN' :MMMMWoOMMX'      ..'clodxxxxkkkk
;,'.    .';;;.     . dMMWOXMNWMKWMMX'. ,NMWWM0. ... .;.,WMMMl.;. xMMXlWMMX. 'WMMMNXMW0:. :MMMMMNXMMX'      ....;cloddxxxxx
;,..    ..;::'..   . dMMWlkMMMWxWMMX'.. xMMMMc ...  .,.,WMMMl.;.'KMMO'KMMW; 'WMMM0xMMNx. :MMMNMMMMMX'       ....';cloddddx
,'.      .;ccc:,.... dMMW:oMMMXlWMMX'.' lMMMN' ...  .,.,WMMMl.,.:WMMXONMMMl 'WMMMd'NMMN' :MMMkXMMMMX'         ....,;cloodd
,'.     .';ccclc.... dMMW::MMMx;WMMX'.. lMMMN' ...  .,.,WMMMl.'.xMMMWXWMMMx 'WMMMd'NMMN' :MMM::NMMMX'           ...',;:clo
'.     .;::ccc:'.... dMMW:.XMN:'WMMX'.'.lMMMN' ...  .'.,WMMMl..'XMMMx lWMMK''WMMMd'NMMN' :MMM: xMMMX'               ..',;:
..    .,;;:::,...... 'ccc. ,c:..ccc:....'ccc:...... .'..cccc'...cccc' .:cc:..cccc'.cccc...ccc. .ccc:.                  ..'
..    .',;;;'. ......................''''''''.''.....,,,,,,,,,;....................,ccc,....''...
..    ..',,.      ...'''''..........',,,,,,,,'.......,,,;;;;,,,....'',,,,,:c::;::::cxolc;clool,;,..'.. .,,,....'  ....'.c.
'.     ..'.      ...................',,,,,,,'........,,,;,,,,,'...',,,,,;;::;;;::;,;c;:c:lxdlc,'...'.. .'.......  . ..'.'.
,'.    ....      ..................',,,,,,,'.........,,,,,,,,;'..',,,;;;;;;;,'''''.',,,,,:olc,..
"""


def main():
    prog = ArgumentParser()
    prog.add_argument('--version', action='version',
                      version='%(prog)s 0.1 [New skool edition]')
    prog.parse_args()
    cant_handle_my_tarn()


if __name__ == "__main__":
    main()
