# 声明角色
define haruhi = Character("春日", color="#c8ffc8")
define mikuru = Character("朝比奈", color="#c6aac6")
define yuki = Character("长门", color="#b6b6b6")
define kyon = Character("阿虚", color="#ababab")
define itsuki = Character("古泉", color="#cdcdcd")
define g =Character("？？？", color="FFFFFF")

label part1:
    with fade
    g "哎呀哎呀，若是打搅众人诸位兴致还请多多见谅。 "
    g "只是故事而已，不必当真."
    g "喜欢闹事的她，口中出现有趣的故事不少."
    g "但如此有趣又能稍微沾点正经的，却实属少数。"
    g "不用做开幕的话，尤为可惜。"
    g "那么，就切入正题吧。"
    g "接下来的两批人会砰地碰撞，究竟能擦出怎样的火花，就算咱也不得而知。"
    g "但如若恳请大家观察两次开篇，未免太过刁难。"
    g "毕竟你看，大部分故事的开篇都是平凡而枯燥的。"
    g "所以，我便在此非常善解人意地出几份题目，以便帮助大家尽快找到自身所属吧！"
    g "哎呀呀，真是温柔，真是良善，连我自己都颇有些不信呢。"
    g "那么——"
    g "第一问题，是和朋友有关的哦，劳烦诸君侧耳聆听："
    g "“你会为了与友人相处，而去刻意地了解某类兴趣爱好吗？”"
    "【会】":
        jump part1.q1.1
    "【不会】":
        jump part1.q1.2
label part1.q1.1:
    g "就是吧！真是豁达呢！"
    g "哎呀，当友人大聊特聊你听不懂的话题时，处境相当尴尬对吧？他那幅难以言表的高涨兴致，自己却完全无法理解，完全就如同局外人一样。"
    g "努力了解的话，就能畅聊相同话题，拉进彼此关系。"
    g "看到为了同自己交流而特意了解新事物的你，友人定会感动不已。"
    jump part1.q2
label part1.q1.2:
    g "就算不去了解，想必友人也不是小肚鸡肠的人吧。"
    g "收敛自己的兴奋，缓解你的尴尬，你也能清楚友人如此豁达的心胸。"
    g "虽然之后完全不会提及这类话题，但说来如此友情，真是令人羡慕！"
    jump part1.q2
label part1.q2:
    g "那接下来是第二问题，依旧如上哦："
    g "“友人做了某种相当不可理喻的事，你会包容理解他吗？”"
    "【会】":
        jump part1.q2.1
    "【不会】":
        jump part1.q2.2
    g "自然如此！"
label part1.q2.1:
    g "哪怕真的不可理喻，但友人终归是友人，脑海里回想他平常的样子就能理解，友人肯定是特殊状况下才为之的吧！"
    jump part1.q3
label part1.q2.2:
    g "哎呀，毕竟人总是保守的，作为拥有智慧的高级动物，保全自己无论何时都是驻扎在脑海里的第一要素，因此无论发生何时，只要不是无可挽回，人类都会做出保守规避的选择。"
    jump part1.q3
label part1.q3
    g "人总是分为表面与内在的！那位名为弗洛什么的老师也曾提出过各种“我”的理论。所以，哪怕是多么不可理喻的事情，友人干得出来都肯定有其原因，只不过，这个原因你根本就不知道而已，换句话说，和你接触的应该就是表面哦。"
    g "选择包容的话，或许能更加了解友人的本质吧。虽然之前完全都是表面，但没关系，深入了解总需要契机的不是吗？"
    g "无法包容也有其理由，要问硬币的表里那面是“正确的”，恐怕根本无法作答。以此契机了解友人性格的另一面，并在心中提醒自己，不要触及友人的另一种性格，也无偿不是合理的相处。"
    g "哎呀，真是无可奈何呢？"
    g "然后，第三问题："
    g "“一个不认识的家伙突然走进你朋友的圈子，你会同他和睦相处吗？”"
    "【会】":
        jump part1.q3.1
    "【不会】":
        jump part1.q3.2
label part1.q3.1:
    g "呀，非我族类，其心必异。排除异己也永远是人类固有的脾性吧。"
    g "说来，人就是希望能循规蹈矩地度过每天的生物。人类的适应力无比强大，但适应后不愿改变的心理也同样强大。"
    jump part1.q4
label part1.q3.2:
    g "哪怕是再小的集团，建立后也会定死关系，一旦打破这种规矩，后果不堪设想。更加可怕的反在于作恶者完全无法意识到是何等严重的事，诸如推理小说中比比皆是的校园暴力，想必也不用咱过多赘述了吧？"
    g "这么一想，不包容倒成了正确选项。"
    g "毕竟如果包容的话，说不定自己也会被一同扫地出门……"
    jump part1.q4
label part1.q4:
    g "第四问题"
    "【不对！】"
        jump part1.q4.self1
label part1.q4.self1:
    g "……"
    g "怎么了？"
    g "问题太过笼统片面？ 好问题。"
    g "诚然如上解答颇有引导性质，但就算义正言辞地反驳，论倒的也仅仅是我个人的提问。"
    g "哎呀哎呀。"
    g "真是。"
    g "无可奈何呢。 "
    g "那么，第四，也是最后一个问题。"
    g "不必担心，这次不会出现之前那些有的没的。"
    g "十分单纯的问题而已。"
    g "被人拯救和拯救他人，你更喜欢那种呢？"
    "【前者】"
    "【后者】"
    g ""
    g 
    g 

    haruhi "“恐怖故事才是现在的主流！仔细想想就明白了，恐惧可是人类自诞生起就抱有的情感，未知与好奇在心中相互挑战的乐趣，我们电影里缺少的就是这个啊！剧本我都想好了，这样这样……”"
    s "——于是乎，就有了方才的一幕。"
    s "但是，但是啊……"
    s "春日忘记了一个非常重要的事实："
    s "这部电影的主演——朝比奈实玖瑠，是个完全应付不来恐怖故事的可爱生物！"
    mikuru "“呜呜……”"
    s "看吧，她此时已经捂着耳朵在地上蜷作一团，把自己与世界分割开来了，完全就是一个把脑袋扎在沙子里的鸵鸟。"
    s "朝比奈学姐胆小是众所周知的事实，倒不如说……对她的第一印象就是如此。设想一下，这样可爱的女生在鬼屋里一脸凛然地说“没关系，交给我”然后毅然投身的场景，反而会很奇怪吧？"
    s "总之，现在也只能像哄小孩一样安慰她了，我这么想着，走过去请拍了拍她的肩膀，希望手部传达到的触感能让她重拾人间的温暖。"
    kyon "“朝比奈学姐，冷静点，这故事只是她脑内的异想天开，与现实没有任何关系。”"
    kyon "“来，先把那种无聊的故事忘掉，放下心来深呼吸，来……”"
    kyon "“喂，你干嘛——”"
    haruhi "“ 不行不行不行，实玖瑠！太过软弱好欺负了，虽然这也是你的卖点没错，但这样下去你该怎么对抗有希的精神魔影攻击啊？”"
    mikuru "“呜呜，对不起……”"
    s "在轻抚中放下戒备的刺猬再度武装了起来。"
    itsuki ""
    kyon "“啊啊，看看你都做了些什么啊！刚才朝比奈学姐明明都已经逐渐信任人类了，但你一脚又把她重新踢回了深渊里，你是会在恋人走到冥府入口时对它们大喊‘你们有东西丢在这儿’的那种人吗！”"
    kyon "“况且，那个，什么魔影是啥，你拥有想象力确实很棒，但可否考虑到特效与经费问题呢？距离文化祭也就只有一周多，临时加新剧情的话……”"
    haruhi "“那根本不是问题的重点，阿虚！”"
    s "面对我为了拯救朝比奈学姐而抛出的大义凛然型攻势，春日毫不犹豫地采取了暴呵一招反驳，面对这种无赖式的反击，我完全没有应对手段。"
    haruhi "“举个例子，你打过游戏对吧？”"
    kyon "“这是当然。”"
    haruhi "“RPG游戏里，如果攻略一个资料完全被公开的boss，肯定要换上相对克制的装备，为了效率，也为了安全。”"
    haruhi "“战斗时因为克制的关系，己方完全占据优势，随随便便就击败了。剧情里不可一世的家伙如此轻易就被干掉了，你脑子里肯定会这么想吧！”"
    kyon "“这么说……也没错。”"
    haruhi "“看吧！任谁都会这么想的！”"
    haruhi "“没错，如果实玖瑠克服不了恐惧，这部电影的评价就会沦为：BOSS因放水而输的烂片啊！”"
    s "她一脸凛然地说出来这个可笑的话题。"
    haruhi "“是我的失职，我早就该考虑到这一点了。”"
    haruhi "“如果电影里的实玖瑠还是这个样子的话，最终决战时肯定会被有希攻其弱点一口气拿下……”"
    haruhi "“我早就该想到这点的，不好不好，这样下去肯定会被吹毛求疵的观众评为烂作……”"
    kyon "“先等等，会出现这种问题的原因完全在于你的异想天开吧？若不是你突然要加些恐怖元素，我们的工作都已经可以收尾了啊！”"
    haruhi "“我知道，我当然知道，但是——”"
    haruhi "“我不能容许这样的漏洞存在！”"
    haruhi "“明明面对一群没有魔法抗性的勇者，却一味用物理攻击的BOSS，只能活在红白机里。”"
    haruhi "“还是说，你觉得有希和那种红白机一样蠢？”"
    kyon "“当然不了，就算把地球最强的电脑拿出来和有希比拼，后者都不会落败。”"
    kyon "不，倒不如说，如果有希真的是BOSS，人类早就毁灭了吧。”"
    haruhi "“看吧，你也知道有希设定中的实力。”"
    s "虽然我说的并不只是设定而已……"
    haruhi "“按照剧情来说，有希这样等级的人不可能没调查过实玖瑠就跑去袭击，明知对手的弱点却无视掉这种桥段……”"
    haruhi "“出现在我的电影里就太过愚蠢了！”"
    haruhi "“所以，实玖瑠，加紧训练，我们要追加一段你经历折磨后成长的戏份，这可是毫无疑问的主角待遇哦，欢呼雀跃吧！”"
    haruhi "“地址我早就选好了，全员带好必要的设备跟我走！”"
    mikuru "“咿呀啊啊——”"
    haruhi "“没错，再大点声实玖瑠！这就是你获得奥斯卡奖迈出的第一步！”"
    s "抱着朝比奈学姐的春日兴奋地嚷着，当然，在场真正兴奋的只有她一人而已。"
    s "朝比奈学姐发出的声音，是怎么听都不像欢呼的呐喊……"
    s "之后的事情便很简单了，春日带着我们在后山转了三圈，就在我即将为这次强行军而举起反抗之旗时，春日终于停下了脚步。"
    haruhi "“到达！看，这就是作为故事素材用的隧道！”"
    itsuki "“果……不其然，和故事中一样的阴森呢。”"
    s "气喘吁吁的样子就不要去拍马屁了啊……虽然我像这么吐槽，但我实在没有力气闹腾了，毕竟扛着大包道具的我和只拿遮光板的某人不一样。"
    s "面前的隧道正如春日所言，是个看上去相当诡异阴森的场所。"
    kyon "若是拍的尽兴之时突然驶来一辆电车，这部电影就会作为一部用生命来呼吁高中生不要作死的名作——”"
    haruhi "“那还用说，我当然调查过了，看，地图上大概是在这里……”"
    haruhi "“本来是绕山铁路的一部分，但近来建了许多地铁，在新兴交通工具面前，这类老式的电车也就逐渐被淘汰荒废了。看周围铁轨的痕迹就知道了，不可能有电车会在这种半脱轨的铁路上通车吧。所以，这次活动在安全性上有着绝对的保证。”"
    s "说起来也对，若不是有这个现实中的隧道铺垫，她也不可能讲出那么惟妙惟肖的故事……这女人只有行动力足矣称赞，估计她已经实地考察过许多次了。"
    s "拿出手机，我姑且把这个地区拍了下来，"
    s "别的不说，作为电影的取材地确实相当良好。"
    haruhi "“好，大家一起进去吧，打好手电筒哦，接下来要迎接的可是直通深渊的桥梁……”"
    kyon "“那么，具体要在隧道的那里拍摄呢，你早就选好了吧？”"
    s "既然没法阻止，至少也要把对朝比奈学姐可能造成的伤害减到最小。"
    haruhi "“诶？说什么胡话呢阿虚，隧道里面不进去怎么知道？”"
    kyon "“你没进去过吗？！”"
    haruhi "“当然了！"
    haruhi "“个中存有很复杂的原因，那个，你想啊……”"
    s "她想说些什么？是想保持第一次进入的新鲜感吗？是作为导演有什么特殊的追求吗？"
    s "但不论她找些什么借口，我都已经找好了反驳回去的方式。"
    s "来吧，春日，让我看看你能说些什么。"
    haruhi "“那个，这个……嗯。”"
    haruhi "“果然，一个人进去很可怕的吧！”"
    s "——"
    s "大脑停止了转动。"
    s "对于她能用这种态度说出这话，我确实没能预测到。"
    s "其他人也都是如此，朝比奈学姐疯狂地点头回应，长门一动不动，古泉还是那份苦笑。"
    kyon "“啊啊……”"
    kyon "“你连自己的恐惧心都没克服还要求朝比奈学姐吗……”"
    haruhi "“虽然我很想反驳，但你说的确实很有道理，这或许就是我和实玖瑠需要共同攻克的心魔。”"
    haruhi "“我之前真的想过自己先进去看看的，但没想到的是——”"
    haruhi "“刚找到这地方时，就从里面传来了某种咕噜咕噜的，相当诡异的声音。”"
    haruhi "“完全不像是人类发出的声音……我刚听到时相当兴奋，但随着自己离隧道越来越近，那种声音也愈发明显，到入口时，那声音仿佛就在耳边鸣响。”"
    haruhi "“隧道里面漆黑一片，手机灯的光完全被吞噬，根本不清楚究竟是何种东西。但脑内却本能地想着，声音的来源不是人类，也不是动物……”"
    haruhi "“越往里走，奇妙的感觉就越是涌现，然后，在隧道的转角处……”"
    kyon "“转角处……”"
    haruhi "“我看到了……”"
    haruhi "“一只老鼠啊！”"
    kyon "“啊啊啊啊……啊？老鼠？”"
    haruhi "“没错，一只老鼠突然从转角处冲出，我也因此一口气跑了回来，还把手机掉在了隧道里……”"
    haruhi "“真……真的没办法啊，除了那种奇怪的声音意外里面就是一片寂静了，这种时候不是怪物而是冲出老鼠，这种被吓一跳的感觉，简直就是最低级的恐怖！”"
    haruhi "“本来如果真的遇到怪物，还指望拍下来后好好调查一番呢……”"
    s "不，综合春日描述的现象，就算如她预想般真的有什么东西，她也只会慌乱地跑回来。"
    kyon "“从刚才说的开始，你不是在讲故事的后续吧？”"
    haruhi "“是真的。”"
    haruhi "“虽然难以置信，但确实真实发生过，说起来很耻辱，当时满脑子都是赶快离开，啊，方才的故事也有一部分取材于此……不过如今这些都不重要了。”"
    haruhi "“仔细想想，也没什么可怕的对吧！只要聚集SOS团的力量，这种怪物相当轻松就能攻略了……大概。”"
    s "这家伙的语气已经出卖了她。"
    haruhi "“总之，赶紧出发就是了！带着手机的人打开灯光，组成前后左右的方阵把实玖瑠夹在中间，然后……”"
    kyon "“我拒绝。”"
    haruhi "“为什么？！”"
    kyon "“请你更多考虑一下自己团员的心理健康问题，朝比奈学姐这样子已经不可能进去了，必须要留人在外面照顾她。”"
    haruhi "“实玖瑠根本就没有那么脆弱！看，快清醒过来，拿出你的骨气，实玖瑠……”"
    s "看着春日不停摧残着半昏迷状态的朝比奈学姐，我心中涌出了许多不满。"
    s "……事后想来，这也应该是必然会出现的事件吧，毕竟无论三味线，旅鸽，还是朝比奈激光，她对世界的影响都有点做过了头。"
    s "拍电影的压力在每个人心头积累着，宛若一触即发的火药桶。"
    s "我也暗自发誓，如果她对朝比奈学姐作出什么过分的事，绝对会出手阻止她。"
    s "但出人意料的是，当我提出把朝比奈丢进河里的电影情节有些过分时，她没怎么反驳就接受了我的意见。"
    s "本以为她真的从本质上改变了，但没想到隔天她就又搞了这么一出戏。"
    s "深吸了一口气，我冲到春日的身边，像是提猫一样揪着她衣服的后领，把她和实玖瑠身边拖开。"
    kyon "“你给我冷静一下。”"
    kyon "“就因为你的一时兴起而把朝比奈学姐搞到不能上课，你是喜欢这个下场吗？”"
    kyon "“而且说到底，除了拍电影的要素外，你的另一个目的绝对是把手机找回来。”"
    kyon "“从你动机不纯的这一点开始，我们就不可能陪你进去瞎胡闹了！而且拍摄恐怖场景的话，只需要贴个图就成了，之后在把人用后期加上去，电影都是这么拍的。”"
    haruhi "“……”"
    haruhi "“你自顾自地胡说些什么呢？我确实想把手机找回来，但我也同样想把电影拍好！如果我真的想找手机直说就行了，何必还想出那么复杂的故事！”"
    haruhi "“真是的，那我自己一个人去好了，你们在这里给我等着！”"
    haruhi "“还有，拍到怪物的话功劳是我一个人的，你们可别到时候再后悔，在我接受各大媒体采访时不甘心地咬着手指看着吧！”"
    itsuki "“这可真是……”"
    s "暂且不提已经昏厥过去口吐白沫的朝比奈学姐和在自己身上绑手电筒跃跃欲试的春日，话说到这里时，古泉朝我使了一个眼色。"
    itsuki "我这里有备用的。"
    kyon "“唔啊啊啊！你突然贴这么近干什么，方才的气氛还没散干净呢，还有你的脸，那种难以形容的表情，要不是我的话肯定当场就又会昏过去一个人！”"
    haruhi "“古泉，你脸很痛吗？”"
    itsuki "“不，我没关系，只是在对剧本上恐惧的表情做一些试演而已。”"
    s "他在说谎这方面真的很有一套，再加上这张脸，天知道他曾经骗过多少无知纯洁的少女……不过，再让他把鬼脸做下去，说不定春日就要搞怪脸合集之类的东西了，我不得已只好眨了几下眼，意思是我听懂了他的潜台词。"
    s "趁着春日还在努力把粘在长门身上的实玖瑠撕开，我特意把古泉拉到了春日听不见对话的角落。"
    kyon "“于是，你到底是什么意思？”"
    itsuki "“诶呀诶呀，虽然事出突然，但看凉宫同学那样子，估计还要过上很久才能鼓起勇气冲进去吧。”"
    itsuki "“时间相对还来得及，我就用比较容易理解的方式来说明了。你对日本的妖怪传说是怎么看的呢？”"
    kyon "“妖怪传说……是指金太郎一类的吗？”"
    itsuki "“不是那种童话，打比方来说的话，类似百鬼夜行之类，你对那些了解的多吗？”"
    kyon "“这是不甚精通，但你总不会觉得这些和那家伙说的有关系吧？”"
    kyon "“隧道里的奇异声响？那只是钢筋类的东西因为松动而发出的声音而已，根本就没有什么鬼怪，要说的话，全部都只是人类的臆想……”"
    itsuki "“说的没错，虽然我们周围存在许多超自然的东西，但无论朝比奈同学，长门同学，亦或我自己，都从未见到过鬼怪这类事物。在我们科学的现实里，或许它们根本就不存在。”"
    itsuki "“恐惧源于人心，古时之所以有那么多的妖魔传说，很大一部分都源于人们对未知的恐惧吧，毕竟黑夜里出现什么东西都有可能，渐渐地，类似的故事便流传了起来。”"
    itsuki "“很有趣吧，明明是什么都没有的地方，人却能凭借自身的想象创造出恐怖的家伙。这或许也是作家或导演必不可缺的一份才能吧，在心里塑造出一个连自己都可以蒙骗的怪物，并让其在电影中登场……”"
    s "对对，所以说历来的恐怖电影都是那么的……"
    s "——等一下。"
    s "我倒吸了一口凉气，不为别的，单纯是我听懂了古泉话内蕴藏的意思。"
    s "作家凭借自己的想象结合现实创造怪物，并为了情节的必要而投放至笔下的世界。虽然听起来有些儿戏，但作家之于作品就是这样的地位，拥有宛若神明般创造一切的权能。"
    s "很是不巧，就在我们身边，也有一位这样的家伙。"
    s "凉宫春日。"
    s "她就是这样的家伙，不知原因为何，世界总会不由自主地朝着她所想的方向行驶。所幸她从本质上来说还是个普通人，拥有常识的她不会做出明天世界就毁灭掉之类的想象。"
    s "但这也代表她和常人一样，拥有无尽对未知的想象力"
    itsuki "“你能明白这点就很简单了，毕竟这是直接说出来就完全没有说服力的东西。”"
    s "说的也是，毕竟本来不存在的东西，就算再有想象力的人也无法做到无中生有。举个例子来说，某日新闻突然播报地球上发现了第八大洲，任谁都会觉得这是个假新闻，毕竟地球都探索过这么长时间了，人们对它早就有了足够科学的认识，常识告诉这我们，这是不可能的东西。"
    s "可讽刺的是，科学常识也有作用不了的地方。"
    s "假如你深夜独自走在空无一人的墓地里，世上没有鬼怪的思想就那么的坚强吗？"
    s "鬼怪或许并不存在与现实，但绝对驻扎在每个人的心中。"
    itsuki "没错，凉宫同学上次来探索的时候，说不定隧道里真的因她而衍生了某种东西。”"
    itsuki "“真的要感谢那只老鼠呢，否则对我们来说极有可能就是无可挽回的大灾难了。”"
    itsuki "“恐惧尤其会在独自一人时不断滋生，如果再让凉宫同学独自身处那种地方，若是她坚信到一定程度——”"
    itsuki "“不过，这也都和恐惧的感情一样，是我个人的预测罢了。”"
    itsuki "“凉宫同学拥有常识，虽然喜欢恐怖悬疑等非自然的事件，但她的常识也告诉她那些东西仅存于故事中的世界，现实是不可能发生的。换句话说，只要能说服凉宫同学，那也就只是个普通的废弃隧道，会有蝙蝠老鼠居住也在正常不过了。”"
    itsuki "“所以你明白了吧，千万不要让凉宫同学独自进入隧道。”"
    itsuki "“而且，即使有陪同也要甄别人选，如果是朝比奈同学和凉宫同学一起的话，恐怕根本起不到任何作用，甚至会有反效果，长门同学也是一样。归根结底来说，能给她心理上的安全和依赖感的，果然还是男性……”"
    kyon "“……”"
    itsuki "“‘为什么不自己去’你的脸上写满了这些字啊。”"
    itsuki "“如果你无论如何都不愿意的话，我也可以承担护卫的工作。但……这份依赖感很可能不止会在隧道中起效，吊桥效应这个词，你应该比我更加熟悉。如果你实在不愿意的话，我便会自告奋勇地承担吧，倒不如说，我很荣幸……”"
    itsuki "“哦呀，你这是有答案了吗？”"
    s "那还用说吗……"
menu:
    "给我打消这个念头，古泉":
        jump part1_1
    "是啊，我去，我去总行了吧。":
        jump part1_1
