# 声明角色
define haruhi = Character("春日", color="#c8ffc8")
define mikuru = Character("朝比奈", color="#c6aac6")
define yuki = Character("长门", color="#b6b6b6")
define kyon = Character("阿虚", color="#ababab")
define itsuki = Character("古泉", color="#cdcdcd")
define g =Character("？？？", color="FFFFFF")
default q1 = False
default q2 = False
default q3 = False
default q4.1 = False
default q4.2 = False

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
menu:
    "【会】":
        jump part1.q1.1
    "【不会】":
        jump part1.q1.2
    if q1:
        g "……"
        g "真是令人困扰呢，只是一个小小的提问，在下的反应就这么重要吗？"
        g "好奇心旺盛未尝不是件好事，然而，至少现在，这是禁止事项。"
label part1.q1.1:
    $ q1 = True
    g "就是吧！真是豁达呢！"
    g "哎呀，当友人大聊特聊你听不懂的话题时，处境相当尴尬对吧？他那幅难以言表的高涨兴致，自己却完全无法理解，完全就如同局外人一样。"
    g "努力了解的话，就能畅聊相同话题，拉进彼此关系。"
    g "看到为了同自己交流而特意了解新事物的你，友人定会感动不已。"
    jump part1.q2
label part1.q1.2:
    $ q1 = True
    g "就算不去了解，想必友人也不是小肚鸡肠的人吧。"
    g "收敛自己的兴奋，缓解你的尴尬，你也能清楚友人如此豁达的心胸。"
    g "虽然之后完全不会提及这类话题，但说来如此友情，真是令人羡慕！"
    jump part1.q2
label part1.q2:
    g "那接下来是第二问题，依旧如上哦："
    g "“友人做了某种相当不可理喻的事，你会包容理解他吗？”"
menu:
    "【会】":
        jump part1.q2.1
    "【不会】":
        jump part1.q2.2
    g "自然如此！"
label part1.q2.1:
    $ q2 = True
    g "哪怕真的不可理喻，但友人终归是友人，脑海里回想他平常的样子就能理解，友人肯定是特殊状况下才为之的吧！"
    jump part1.q3
label part1.q2.2:
    $ q2 = True
    g "哎呀，毕竟人总是保守的，作为拥有智慧的高级动物，保全自己无论何时都是驻扎在脑海里的第一要素，因此无论发生何时，只要不是无可挽回，人类都会做出保守规避的选择。"
    jump part1.q3
label part1.q3
    g "人总是分为表面与内在的！那位名为弗洛什么的老师也曾提出过各种“我”的理论。所以，哪怕是多么不可理喻的事情，友人干得出来都肯定有其原因，只不过，这个原因你根本就不知道而已，换句话说，和你接触的应该就是表面哦。"
    g "选择包容的话，或许能更加了解友人的本质吧。虽然之前完全都是表面，但没关系，深入了解总需要契机的不是吗？"
    g "无法包容也有其理由，要问硬币的表里那面是“正确的”，恐怕根本无法作答。以此契机了解友人性格的另一面，并在心中提醒自己，不要触及友人的另一种性格，也无偿不是合理的相处。"
    g "哎呀，真是无可奈何呢？"
    if q2:
        g "……"
        g "您是在犹豫不决吗？诚然，任谁面对这样的问题都要拷问一遍自己的心灵。"
        g "或者两遍。 "
    g "然后，第三问题："
    g "“一个不认识的家伙突然走进你朋友的圈子，你会同他和睦相处吗？”"
menu:
    "【会】":
        jump part1.q3.1
    "【不会】":
        jump part1.q3.2
label part1.q3.1:
    $ q3 = True
    g "呀，非我族类，其心必异。排除异己也永远是人类固有的脾性吧。"
    g "说来，人就是希望能循规蹈矩地度过每天的生物。人类的适应力无比强大，但适应后不愿改变的心理也同样强大。"
    jump part1.q4
label part1.q3.2:
    $ q3 = True
    g "哪怕是再小的集团，建立后也会定死关系，一旦打破这种规矩，后果不堪设想。更加可怕的反在于作恶者完全无法意识到是何等严重的事，诸如推理小说中比比皆是的校园暴力，想必也不用咱过多赘述了吧？"
    g "这么一想，不包容倒成了正确选项。"
    g "毕竟如果包容的话，说不定自己也会被一同扫地出门……"
    if q3:
        g "……"
        g "没办法，至少在我看来，“友”就是这样悲观的字眼。 "
    jump part1.q4
label part1.q4:
    g "第四问题"
menu:
    "不对！":
        jump part1.q4.self1
label part1.q4.self1:
    g "……"
    g "怎么了？"
    g "问题太过笼统片面？ 好问题。"
    g "诚然如上解答颇有引导性质，但就算义正言辞地反驳，论倒的也仅仅是我个人的提问。"
    g "答案无法反驳，你能做到的只有逃避，装作没心没肺的样子不去在意这些东西，背过身去就看不见了，真乃唯心主义集大成者。"
    g "哎呀哎呀。"
    g "真是。"
    g "无可奈何呢。 "
    g "那么，第四，也是最后一个问题。"
    g "不必担心，这次不会出现之前那些有的没的。"
    g "十分单纯的问题而已。"
    g "被人拯救和拯救他人，你更喜欢那种呢？"
menu:
    "【前者】":
        jump part1.q4.1
    "【后者】":
        jump part1.q4.2
label part1.q4.1:
    if q4.1 == False and q4.2 == False
        g "原来如此。 "
    elif q4.1 == False and q4.2 == True
        g "哦，跟我猜的不太一样呢。"
    elif q4.1 == True and q4.2 == False
        g "果然呢！"
    g "那还请多多期待。"
    g "这是属于“他们”的故事。"
    g "当然，也是属于你的故事。 "
    jump part1_1
label part1.q4.2:
    if q4.1 == False and q4.2 == False
        g "原来如此。 "
    elif q4.1 == False and q4.2 == True
        g "哦，跟我猜的不太一样呢。"
    elif q4.1 == True and q4.2 == False
        g "果然呢！"
    g "那还请多多期待。"
    g "这是属于“他们”的故事。"
    g "当然，也是属于你的故事。 "
    jump part1_2
