import math 
from decimal import *
import matplotlib.pyplot as plt
 

def main():

    getcontext().prec = 1024
    value = Decimal("22.45915771836104547342715220454373502758931513399669224920300255406692604039911791231851975272714303153145007314889637271665416272720003684124587848382578019739992751627091118523867135294083489216233769249673053675166259960166872554777588806087374292011817166116137224619720904489633131459927327914091484057676488975378488534410200649259349035759476346916528629400784739540775529801982902613122402951137999068865244293114633593928571607332954149153253013772276755518306879304362284231908828679757829796726471816400070435718105836426064145802122396906974474988516161331840510621636455956108413309428992831263755783615874304692916424601833531934233642003612726382452362470354957183504907341963002354534256412909792119430311690800129252277049440369885261286191183951596873159169810191151307022170454764661795922522468451098320875962159442148399874744726417593402569366826503558047664237423706170850564466432445749673888419368868311592520055560264570505932011700936276055359582664120199812004276137019217486203191051990550681657142587081134052885380862997527608561446092631424976182336168686940651526668596241322910679647920979245456135940032831621587235354873644961319789865130702306293570353708284636059842315748494523814652293484193965122093403276663122121683983729903762647354642892365898201888714226305189224463728698968895262993222108217032849956464658688409840085447792463662398034166260937990690259689009279169940650311836387920021797492486031935412045899979701066929539121323351667259121832488806207689146376234529825352535140489832997133743651735000396188312544968495420328300544201223205230771698066847094597987090785177844585660648329084848086182075875591960903905030582791327871687918919145226691195035545586977677019822697431662195802271787265372661216715454831517329298580386810499540504352644945803817140337769746187392849169111228132424539765180202066313278888131515183199299965426191715953583002852747469981289285483357407972177287439912044116766300523260600964521366496695570276358760706523070473137646754901849053973122536579685087037357294598757095899176106189387069043178530605142194872932801916963708645106699560019021763851495626537301585400319441579955151665130128466439646148806575843182999893239082385927503043722752956299169909207638249420644803050830289783185114863316847473926352742175684330255063952634362789386662543919787432662998372674479102256552945508312020680123774358922378246553297889863237851488456780766673303589368713821944893474987909978698672753811112549375537284531591241370263009667126664637364979794228684210214213639585778344615681152831375552379122929110224953777276423543356762971888286517108913093616160590828778423366459653341591695283042453414491618419861181407414413292896447509868738017389793829671125473210055592762836273787083078146305187121449851473205377619054452414229590589002234437736668676038814806619944846038988271868604732944628651850204375089052861183233793762517478520907093959045020848237657229690137654946925163570672650282860215351228299029626296940576442437368696025638095830104066684217054869015557286191187197913763512655225398923518084105855699702246130438075916403404867137503707029876849968921652764450889786083227458025159601672538236344924362880810541550946874258872282811893655886419373455013962912715905421638315266694197665684479916875272651313448730169261537805785568820505003710726924909895332473097707951454448343670651459510299705032611627167843829521862446181946039008646590230065438313958805996523918978769581266132027510612550133359765302621651722058638006724210957071135592605162028743714664220327372911623017446847498120234886053474443008129677494635444371313226487641326810437562900553113368434657092229250338622769403047304753745630794161290052532711470131985317764825214271586552163231113507380560011412140098938536011586625923380111368911847173458838296429847114862895380098841794797126421757738137514270689305369293869767287750041313138850217512722865263311411887719394824430196973029642887786952978739354082716648042415822411388745822123779042682486610325798153451992185497975630014591940569642374535475461771964583309098542808542466588835341123167477853304244209003034460485862003706695497013759002752050092809910854375176432653046522200706891942198216400384574553634107357478942623195768387524458025595448105046966471947786327353177337109372142358642463306567227974695852926481924739739893653071155292111005963770967047194303048687217897483906269358994666709660748038757305856110994917242613698794386034829862731419830750358312177650765199409045975507524709061484366852077079456206435526887754669673080735545324859579898703743365876689055487272716242577050321282196230342496988911013379612684487801969149307808755019098756257280629681037025814751984813898570296867326500021041923814457552403784216952937717820893612068325050849123913734746485520704636410013737858692787524271918368537067129964042792520910415921997004162450455145002734030274512469965940841148671070655284745397755983337246643654733535213211601546884355807718377285448642286404923490977330990804883505020213687333012018722723653513370385815937628444366350240595909100703938233732929140310268472533747690638499946594826503529992032584286158598836632023244876748933037964189790932211023612028103495377642836510834576211098521751382994236909985450715430846288164048271010882722751529253512087448754251704384946155874258844380090156050347080689973297149040315851425652982698706442770309090904906431318033884444083090538435217649015188372675615193062172939591028973170968779992901918670899286537539838110035259293261446462798879460151027673357549480062206515795064555789015264125300698032717489120941342713247255175215283893588656206414436906907680545307383369990764824778201212620185163385068707211426259075717306185031849889759458952588084127265867865656725292332794968681728729881909810925619456473160419900506089833454314632033264202221620400275539974250514143953024173702159002044847338042660117252389048420217594700543446379682305316128879284520306762251183303249560608760220046913660430366111256686904250333624311697794435915712455204272737217997956206401227532539033283914172517832265750421957694460216632448721661839310363657710990948086967345190048987108126004476110304288358941185535590515324606479473793289935613834289105738225890808022088755479574014442739948232641865789876748143222753188024596511123357227678634688581514528363382374205330946366643731564535141147769967451297852230930446590430235888575660102914305061059042068220724608228945232012310635957130686491750324433222320451152540627860112412465956932874116818121589099123795078810101544444145477484178230189941156354619960892340143286427425602164798970983609689308647962200396554055824552171038071829494880927986868112918919478129065891378148248494387234054524090217958031750499584570659992944702504404494774201780673501227626313154768973843458067882578671588138598415554803773550110385789910785097364836550316740363391450518438882324457833944696079800537893809653233706069974736352805730867625690936623935004644250173017236910897268333315229014899630072482110339477046168294842046312808817832223723714546970359482788481955926435397840498821102806911061671268147166068367063259157910161348274241230877249395630859716268214876306393488698946382663993915520443594864925169335462706172691915916167037263080966977206406518949203719374182450957197850410651574613806000370088248246008403669915728004772678448135808116471153995528253869322877497025081575254295101185808017137313420959675292917669270158990281702741064084944295005604190951893231780562299906972351947493162169141045530000514316466553889008119984374448564689451493706402414821913586191345304199617951239984585072895609594024589353604682027289917534894133396424131848246204292475330724767729521390262866566874762125740235381912460692257039929777796086552638387060523321806734040022790765616717429465759334350376943942687112396723067827516697151666352318345695655575703685476502434506793882189717094212156359489132073603935307220308587736140847578927828658270601324688922262716096528211257950527984059071793217024116851595646738878798817031203189172672842407583696710774028647675296935777739814325160459475192969583992187490125958383461800647864052431973452200494126832374283036064069164926287110767669167419304372585337542356615443962616288280412276973845641384426111474960694358247372280630497904807352412381932762402580724941335841974385514274882972700044911785650637035583394482161094367402404379969370744320364249255132679409821024548946107849030741492213268068615340371578377234389997025965886322271382310607184309547698344120152186770549880543775058415555359170639921296232344470722567223896369133081577428650780184971403663194265622637183989758523346682324761249027957668310332827555867671483051224490767230221720986960110270026738971961834882420503952642952319721750550501170532383676615265863711003730189843581403651071611765707537772329877910565539668332736119860066521238481253563765127645479478016911445239596227655068922568536111875761149081724500028363987057072415408247287607191932279015259650197917345724067781017131856320386285223808642359032140294901957564525767673002841409153230616290597536616604995734202088669381703441372084524744436532642199366343715864624896898795242044467996963861449984214995911810288277613991516213522793488798217248138248721980432856383830466791829415745935851087152141612408224006972607752031201749883214285462417581013770199009590646567298437452616507030919604211248538098467160412768846289776361694276788722355582359216711315545740558042051156967659774485725428327931660125527835138888113702353704876874114403958692472334589387902341334506869500670667355089396074024530798902776112362525468194778445431711874830578836410021434146682341208599482337706933941433943180061146672478406885204995134920567198508021165215245890865692453480147668468409691524299843574763683362574749183974857149377980588746988154529231940037440359294041730101960507651886126638355404041246577");
    print value
    bList = [] # Stores the b values for the continued fraction
    for n in range(0,1000):
        bList.append(math.floor(value))
        value = 1/(value - Decimal(value).quantize(Decimal('1.'), rounding=ROUND_DOWN))
    print(bList)
    f= open("Pi^eConstantStandardCF.txt","w+")
    for i in range(0, 1000):
        f.write(str(bList[i]))
        f.write("\r\n")
    f.close() 
    
    plt.plot(bList)
    plt.xlabel('term in the Standard Continued Fraction')
    plt.ylabel('Value')
    plt.title('Pi^E Constant Standard CF')
    plt.show()

	
#call to main
main()