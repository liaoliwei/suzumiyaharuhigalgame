# 声明游戏中要用到的图像。
image bg lecturehall = "lecturehall.jpg"
image bg uni = "uni.jpg"
image bg meadow = "meadow.jpg"
image bg club = "club.jpg"

image sylvie normal = "sylvie_normal.png"
image sylvie giggle = "sylvie_giggle.png"
image sylvie smile = "sylvie_smile.png"
image sylvie surprised = "sylvie_surprised.png"

image sylvie2 normal = "sylvie2_normal.png"
image sylvie2 giggle = "sylvie2_giggle.png"
image sylvie2 smile = "sylvie2_smile.png"
image sylvie2 surprised = "sylvie2_surprised.png"

# 声明角色
define narrator = Character(None, kind=nvl)
define s = Character(None, kind=adv)
define haruhi = Character("春日", color="#c8ffc8")
define mikuru = Character("朝比奈", color="#c6aac6")
define yuki = Character("长门", color="#b6b6b6")
define kyon = Character("阿虚", color="#ababab")
define itsuki = Character("古泉", color="#cdcdcd")

# NVL 配置
init python:
    #menu = nvl_menu

    # 没有得到焦点时的分支选项颜色。
    style.nvl_menu_choice.idle_color = "#ccccccff"

    # 得到焦点时的分支选项颜色。
    style.nvl_menu_choice.hover_color = "#ffffffff"

    # 没有得到焦点时的分支选项背景颜色。
    style.nvl_menu_choice_button.idle_background = "#00000000"

    # 得到焦点时的分支选项背景颜色。
    style.nvl_menu_choice_button.hover_background = "#ff000044"

    # 距离左侧分支选项应该缩进多少。
    style.nvl_menu_choice_button.left_margin = 20


    style.nvl_window.background = "nvl_window.png"
    style.nvl_window.xpadding = 55
    style.nvl_window.ypadding = 55

    config.empty_window = nvl_show_core
    config.window_hide_transition = dissolve
    config.window_show_transition = dissolve

    preferences.text_cps = 20
    gui.nvl_height = None


# 从这里开始
label start:
    scene 2_bai_tian
    with fade
    window show
    "注意到这个问题是在十年前。"
    "那是他除了太阳为什么会升起外，有意识地去疑惑的第一个问题。"
    #window hide
    #nvl clear
    play music "audio/lianggongbgm/1.mp3" fadeout 1.0 fadein 1.0
    #with fade
    #window show
    "他住在偏远的城郊。"
    "人口稀少，设施不齐，几乎没有商业活动，只有一条老旧的水泥路勉强可供往来交通，而且遇到暴雨或积雪便会瘫痪。"
    "说是城郊，实际上甚至不如普通的村落。"
    "晚上遥望隔壁X市的灯火，是这里仅有的娱乐。"
    #window hide
    nvl clear
    #with fade
    #window show
    "虽然地势偏僻，但好歹和市区相连，如果能完成建设，按照当时的地价，投资商必然会牟得暴利吧。"
    "但工程进行到一半之时，因为各种突发事故不得不叫停，投资商也因此破产。"
    "没有人愿意接手，就连政府都懒得管理，留下一座座徒有四壁的空屋。"
    "他的家，便是其中之一。"
    window hide
    nvl clear
    scene 1
    #with fade
    window show
    "选择这里的原因自然是低廉的价格。"
    "因为父母的工作，搬家转学已然成了他的家常便饭，而这周围最便宜的房子，非这里莫属。"
    "简单修缮就能入住，而且算上这些费用，也要比市区的房子便宜上三倍不止。"
    "当然，居住条件相当差劲就是了。"
    "一旦下雨便会变成龙宫，室内的光线也暗得难以想象。"
    "哪怕不提这些，光是房间里弥漫着的石灰粉，就足够令人望而却步。"
    "更何况，是仅有八岁的他呢？"
    #window hide
    nvl clear
    #with fade
    #window show
    "因此，打扫房间便占用了他几乎所有的空余时间。"
    "至于如何与人相处，孩子间流行的游戏的玩法……这些从来都与他无关。"
    window hide
    nvl clear
    play music "audio/lianggongbgm/2.mp3" fadeout 1.0 fadein 1.0
    scene 2_bai_tian
    with dissolve
    window show
    "那是某个秋日的早晨。"
    "艳阳高照，清风拂面，是开窗通风和晒被子的好天气。"
    "换作往常，想到屋子里的积霾能一扫而空，就足以令他欢呼雀跃。"
    "但这一整天，他的脸上都笼罩着闷闷不乐的表情。"
    "不为别的，仅仅是要去办理转学的手续而已。"
    #window hide
    nvl clear
    #with fade
    #window show
    "“没关系的。那里的学校，老师和小朋友都很友善，你一定能交到很多新朋友……”"
    "一路上，母亲不停地安慰着他。"
    "“嗯，我会努力的。”"
    "他微笑着回应母亲，母亲也安心地摸了摸他的头。"
    #window hide
    nvl clear
    #with fade
    #window show
    play music "audio/2.mp3"
    "“他的性格有些内向，还希望老师能多多关心……”"
    "母亲握着老师的手不停嘱咐着，老师频频点头，虽然不清楚他究竟能听进去多少。"
    "“不用担心，小孩子嘛，很快就能建立友谊的。”"
    "老师说完后，便转头看向了他这边，他则下意识地避开了视线。"
    window hide
    nvl clear
    scene 1
    with fade
    window show
    "一直以来，他在家里受到的教育就是“不能说谎”。"
    "但是，定下规矩的是父母，触犯最多的也是父母。"
    "像“忙完工作就来陪你”“乖乖听话就给你买玩具”之类的话，他们不知道说了多少次。。"
    "大人的世界相当繁忙，一句话就能打发走小孩子，何乐而不为呢？"
    #window hide
    nvl clear
    #with fade
    #window show
    "从结果来看，这确实是谎言，但他们并没有说谎的意思。"
    nvl clear
    "毕竟，他们始终相信自己奉行着“诚实守信”的教育方针。如果真的屡屡说谎，提到这个方针时的父母肯定会羞愧地低下头吧。"
    "他说过谎，自然明白那种罪恶感。"
    window hide
    nvl clear
    scene 3_bai_tian
    with fade
    window show
    "母亲的背影愈来愈远，学校的操场上只留下他和老师二人。"
    "一块乌云遮住了太阳。"
    "难以想象秋天也会有如此善变的天气。"
    window hide
    nvl clear
    play music "audio/lianggongbgm/2.mp3" fadeout 1.0 fadein 1.0
    scene 4_bai_tian
    with fade
    window show
    "“你叫B吧，欢迎你来到这里……”"
    "说着，老师挽起了他的手，一边朝班级走去，一边向他介绍这所小学。"
    "“大家好，我是刚刚转学来的B……”"
    "简单地介绍了自己后，他朝着座位走去。"
    "要说转学的流程，没人比他更清楚了。所以，他早就知道该如何表现。"
    "比如，那份怎么看都不像一个内敛的孩子能露出的笑容。"
    #window hide
    nvl clear
    #with fade
    #window show
    "第一天的课间，他与主动和他接触的同学们相处得非常好。"
    "一点也看不出来内向嘛，明明完全融入孩子圈里了……老师得出了这个结论后，心满意足地结束了对他的重点关照。"
    "没错， 他并不像父母口中说的那样，是个“内向”的孩子。"
    "性格腼腆，寡言少语？"
    "面对完全陌生的环境，谁都会表露出这样的性格。"
    window hide
    nvl clear
    play audio "audio/lianggongbgm/4.mp3"
    stop music
    scene xue_xiao_wai_bu_huang_hun
    with fade
    window show
    "这副热闹的景象只持续了不到半周。"
    "在转学生的新鲜感逐渐淡化后，孩子们就不再找他玩了。"
    "毕竟，他们早就建立起了各自的交友圈子，此时突然加进来一个人的话，总会觉得不适应。孩子们是可怕的。"
    "一无所知的年龄，几乎完全遵循生物本能的行为。"
    "正因如此，恶意也会在无意识中流露。"
    "之前几次转学的时候，他早就体验过那种生活了。"
    "所以，他也很识相地不主动去找别的孩子。"
    window hide
    nvl clear
    scene xue_xiao_wai_bu_ye_wan
    with fade
    window show
    "无需过多言语，无需过多接触，他奉行着这样的原则。"
    "反正过不了半年又会离开，倒不如这样就好。"
    "彼此间仅仅停留在普通交流的程度，即便一方突然消失也不会有什么特别的感觉。"
    "因而，他往往会选择自娱自乐，而不加入集体活动。"
    window hide
    nvl clear
    stop audio
    play music "<from 10>audio/lianggongbgm/2.mp3"
    scene 1
    with fade
    window show
    "“看吧，大家都很友善吧……”"
    "某天回去的路上，母亲微笑着说道。"
    "但除了这一句外，其他的话他根本就没听进去。"
    "因为他在思考。"
    #window hide
    nvl clear
    #with fade
    #window show
    $ renpy.music.set_pause(True, channel='music')
    "思考迎接自己的老师。"
    "思考鼓掌欢迎的同学。"
    "思考微笑着的母亲。“小孩子嘛，很快就能建立友谊的。”"
    "——为何说谎也不会感到任何的羞耻。"
    window hide
    nvl clear
    $ renpy.music.set_pause(False, channel='music')
    scene 4_bai_tian
    with fade
    window show
    "但无论怎样，这个话题对孩子来说都太深奥了。"
    "他最后也没得到明确的答案。"
    #window hide
    nvl clear
    #with fade
    #window show
    "日子一天天度过，不知不觉间便过了一个月。"
    "他也彻底地“融入”了班级。"
    window hide
    nvl clear
    scene 4_ye_wan
    with fade
    window show
    "说起来，这个班级，不光只有他一个不合群的孩子。"
    "只要留心就能注意到，教室角落里也有一个孤零零的女孩。"
    #window hide
    nvl clear
    #with fade
    #window show
    "她身材矮小，留着黑色的短发，眼睛不自然地垂着，看上去就很好欺负的样子。"
    "除了在教室，"
    with fade
    scene gong_yuan_bai_tian
    "她最常出现的地方就是操场的沙坑了。"
    "单单坐着，什么也不做。"
    "大概单纯是因为沙坑没人愿意去吧。"
    "文弱的少女安静地坐在沙坑边上，就算不想在意，这副光景也吸引着他。"
    #window hide
    nvl clear
    #with fade
    #window show
    "“为什么她不和别人一起玩呢？”"
    "据说，孩子们试着邀请过她无数次。"
    "也无数次被她拒绝。"
    "现在，孩子们即使看到她在旁边，也不去理会她了。"
    "他打听到的就是这样。"
    window hide
    nvl clear
    play music "audio/lianggongbgm/1.mp3" fadeout 1.0 fadein 1.0
    scene gong_yuan_huang_hun
    with fade
    window show
    "最开始只是好奇，但随着对少女的观察，他产生了另一种感情。"
    "……并非青涩的恋情，那对他而言为时尚早。"
    "对于少女，他总是不自觉地感到一种难以言说的焦虑。"
    "用比喻来说的话，就仿佛是磁铁间的引力一样。"
    "其他同学是正极，偏偏她是负极。"
    "简单形容的话，就是这种感觉。"
    #window hide
    nvl clear
    #with fade
    #window show
    "不过……说到底，这都是孩童的直觉。"
    "没有任何依据，由于奉行的原则使然，他也不会主动去找少女聊天的。"
    "在他们之间，需要一个契机，故事才能开始。"
    "于是，如同命定一般，那个契机降临了。"
    #window hide
    nvl clear
    with fade
    #window show
    "“我的发带掉在沙坑里了……”"
    "一天，同班女生楚楚可怜地跑过来拜托他。"
    "他一言不发地走进了沙坑，坐在一旁的少女似乎不自觉的颤抖了一下。"
    "由于不知道该说些什么，他便选择了这种相当率直的方式。"
    "“你好……xx的发带掉在这里了。”"
    "他说完后，少女很明显地松了一口气，但她并没有回应，只是把手伸了过去。"
    #window hide
    nvl clear
    #with fade
    #window show
    "她手里拿着的，正是那个同学的发带。"
    "他接过了少女手中的发带，坦率地说了声“谢谢”。"
    "少女似乎又颤抖了几下，很费力地从嘴里吐出了几个字。"
    "“不、不……用谢……”"
    #window hide
    nvl clear
    #with fade
    #window show
    "说话时要尽量看着对方才礼貌，老师曾经这样教过他们。"
    "也多亏这点，他才能和少女对上视线。"
    "原来如此，只是性格别扭而已嘛。"
    "这就是他们成为朋友的契机。"
    #window hide
    nvl clear
    #with fade
    #window show
    "与少女相处多了之后，他发现她的性格也并非如传闻般扭曲。"
    "少女对他人有着不由自主的恐惧，之所以会选择沙坑，只是因为在那里相当安心。"
    "人在感觉到危险时就会本能地逃离，而对她（他）来说，最安全的地方就是沙坑了。"
    "确实，被阳光晒暖的沙子很令人安心。"
    "他很能理解少女的想法，但他并未多说什么。"
    window hide
    nvl clear
    stop music
    with fade
    window show
    "倒不如说,是他来不及多说什么。"
    window hide
    nvl clear
    play music "audio/wuyubgm/1.mp3" fadeout 1.0 fadein 1.0
    window show
    "某天放学后，他受邀请去少女家里玩。"
    "在校门口和老师简单说了两句，他没等母亲到来就匆匆离开。"
    "说起来，这是他第一次去朋友家。"
    window hide
    nvl clear
    scene shao_nv_jia_fu_jing
    with fade
    window show
    "他被少女带到附近的住宅区。"
    "对于少女回家的路上没有家长陪同这一点，他稍微有些奇怪，但这个想法很快就被他抛到脑后了。一路上，各式各样的建筑映入眼帘，他小小的头脑有些应接不暇。"
    "对住在废弃城郊的他来说，钢筋水泥的丛林是完全崭新的世界，而就在他即将分不清方向时，少女停下了脚步。"
    "“到了，这里就是。”"
    "少女指着自己眼前的建筑说道。"
    "“……”"
    play sound "audio/duan_pei_yue_5.mp3"
    "他看着面前的建筑，一种说不上来的违和感迎上心头。"
    #window hide
    nvl clear
    #with fade
    #window show
    "当然，他并没有见过这里的建筑，这仅仅是扎根于脑内的本能。"
    "他之前一次都没来过这里，但根据各种照片和人们口中的形容，他对城市有着浅薄的理解，这份理解也在之前的路上得到了证实。"
    "但就在这片密集的住宅区内，少女的家显得那么奇怪。"
    play music "audio/1.mp3" fadeout 1.0 fadein 1.0
    "宛如平缓乐曲中迸出的不和谐音符一般，这栋平房突兀地立在这里。"
    #window hide
    nvl clear
    with fade
    #window show
    "那是间相当老旧的和式房屋。"
    "“年久失修”这个词恐怕形容的就是这种状况，看上去就很难给人安全感，与他自己的家十分类似，不过总归还是能住人的程度。"
    "他没想太多，便和少女一起踏入了玄关。"
    scene 6_yin_sen
    with fade
    "玄关处散乱地放着三双鞋子。漫长的走廊两旁，有许多房间，，里面隐隐地传出激烈的谈话声，却没有人出来迎接。"
    play sound "audio/pao_bu_2.mp3"
    "少女在玄关驻足了一会儿，快步拉着他朝里面走去。"
    #window hide
    nvl clear
    with fade
    #window show
    "“我的父母脾气不是很好，还是快进来吧……”"
    "这样不打招呼很没礼貌，但他还没来得及说，就被少女拉进了房间。"
    with fade
    scene 7_zhen_chang
    "踮脚锁上了门，少女才安心地舒了一口气，但眼神里并没有笑意。"
    "“我……很讨厌这个家。”"
    "……"
    window hide
    nvl clear
    play music "audio/4.mp3" fadeout 1.0 fadein 1.0
    #with fade
    window show
    "在这之前，他还以为只有故事中才会出现这类家庭。"
    "她的母亲因为怀了她的缘故无奈离家出走，但生下她仅仅一年，她父亲的公司便倒闭了。父亲再就业时不是嫌工资低就是嫌工作差，偶尔的借酒消愁也逐渐变成了日常。母亲无力管束父亲，更无力拯救自己，于是全家的怨气几乎都发泄在了少女的身上。"
    "经济拮据时，债主上门催债时，或者只是心情不好时，少女都会受到责骂。"
    "{color=#f00}“都是你的错……”{/color}这是少女从父母那里听到最多的一句话。"
    "到最后，把自己封闭在房里已然是少女唯一的选择。"
    "“里面的家伙也是催债的吧，不用搭理他们，过个半小时应该就走了，到时候如果你想见我父母，就直接去打招呼好了。”"
    #window hide
    nvl clear
    with fade
    #window show
    "“不……”"
    "“怎么可能会想见他们啊，那种混账，不值得去打招呼！可恶，可恶！他们不是还欠着债吗，赶紧被警察抓起来好了……”"
    "发泄着的时候，少女轻捂住了他的嘴巴。"
    "“谢谢你。”"
    "……要说此时的他心中没有某种青涩的感情，就实在太虚假了。"
    #window hide
    nvl clear
    with fade
    #window show
    "“不过……他们不会突然冲过来什么的吗，要是知道你带同学回来的话……”"
    "“没关系，我今天也试着大胆了一回，这个房间的钥匙我已经藏起来了，现在只剩我手上的一把。”"
    "少女亮了亮自己手中的钥匙，收进了口袋里。"
    stop music
    "“接下来，该做点什么呢……”"
    #window hide
    nvl clear
    play music "audio/lianggongbgm/3.mp3" fadeout 1.0 fadein 1.0
    with fade
    #window show
    "那真的是非常快乐的时光。"
    "似乎终于吐出了心中的不快，少女很快就一改在学校里的性格。"
    "语气变得开朗，笑容也多了不少，时不时还会更换各种腔调——这方面她真的很有天赋，声音即便是面对面的他也难以分辨，要是外面的人听起来，肯定会觉得这屋子里至少有四五个人吧。"
    "他也被这种气氛感染，放下了自己的拘谨，把平时攒下来的话一口气全说了出来。"
    #window hide
    nvl clear
    with fade
    #window show
    "虽然家庭环境并不相同，但他完全能理解少女的痛苦，所以，他从那一刻起便默默发誓，{size=+10}{b}{color=#f00}无论外面发生什么，都绝对不会打开房门。{/color}{/b}{/size}"
    "因此，无论是外面愈演愈烈的争吵，摔坏茶具的碎裂声，不知何物倒下的巨响，都和这两个孩子没有关系。"
    "在两个孩子的欢笑声中，外面的吵闹归于寂静。"
    "中途似乎有人转过几下门把，但在两人无声的抵抗下，转动声很快就停止了。"
    #window hide
    nvl clear
    with fade
    #window show
    stop music fadeout 1.0
    "不过，说来奇怪。"
    "他刚好坐在靠门的一侧，门外只要有什么动静，他就能通过地板感知到。"
    play sound "audio/zou_lu_1.mp3"
    "那个转动门把的家伙走过来时，也是他最先觉察到的。"
    "但……那个人只有来时的脚步声，没有离开时的脚步声。"
    "把耳朵紧贴在门上也什么都听不到，如果那人还在的话，至少会有呼吸的声音。"
    "——但，外面只有单纯的寂静。"
    #window hide
    nvl clear
    with fade
    #window show
    "他把这些事情告诉少女后，少女却只是摇了摇头，让他不要在意。"
    "“那个人可能只是踮着脚回去了。”"
    play sound "audio/duan_pei_yue_5.mp3"
    "不可能，就算是踮脚，踩在地板上的重量也能传达过来。"
    "渐渐浓重起来的诡异气氛，让他不自觉地把手伸向了门锁。"
    #window hide
    nvl clear
    with fade
    #window show
    "“不行，不能出去。”"
    "他才刚伸出手，少女就突然跑到了门口，把整个身子贴在门上。"
    "不是低声哀求的语气，少女的态度非常坚决。"
    "她死死地守住门口，没有一点让开的意思。"
    "这份坚决让他愈发感到恐惧。"
    #window hide
    nvl clear
    with fade
    #window show
    play music "audio/1.mp3" fadeout 1.0 fadein 1.0
    "按照少女的性格……为了挽留朋友，她或许真的会不择手段吧。"
    "但，即使知道少女没有恶意，这种行为还是令他不安。"
    "恐惧这种东西一旦产生，除非有足够说服自己的理由，否则便会如癌细胞般无限增殖。"
    "必须要看看到底发生了什么，可是房门出不去的话……他想着这点，开始打量这间屋子的四周。"
    "有了……"
    "在书桌的上方，有一处微微打开的很小的窗户，大概只有他这样的孩子才能通过吧。"
    "周围除了书桌也几乎没有能垫脚的东西，可以说是个非常险峻的地形，正常的孩子想翻出去是不可能的……大概。"
    "不过对他来说，这并非不可能。"
    #window hide
    nvl clear
    with fade
    #window show
    "“我稍微出去看看，很快就回来！”"
    "当着少女的面，他以无比矫健的身姿踩上椅子，翻上书桌，打开窗子，两手撑着窗沿，先把下半身伸出窗户，随后最大限度地拉直身体跳了下去。"
    "“等一下——”"
    "少女哀求的声音并未打动他，况且自己选择的这种路径，她也肯定追不上来。"
    "弄清楚情况之后，自己很快就会回来……"
    play sound "audio/pao_bu_1.mp3"
    "他怀着这样的念头，往少女家的门口跑去。"
    #window hide
    nvl clear
    with fade
    #window show
    play sound "audio/duan_pei_yue_4.mp3"
    "从窗户下跑到门口，对了，房门……诶？"
    window hide
    stop music
    "怎么……回事？"
    "……"
    "……"
    "……"
    "……"
    "……"
    #window hide
    nvl clear
    play music "audio/2.mp3" fadeout 1.0 fadein 1.0
    scene 1
    with fade
    window show
    "“然后呢，你做了些什么？”"
    "“不……我……”"
    "站在一旁的警察摇了摇头，小声冲着身边的记录员嘀咕了一句。“他的记忆残缺，问下去也没用……”"
    "他努力地回想着，但正如警察所说的一样，从少女家的窗户翻出去后，自己的记忆便有相当一部分是空白。"
    "在这段空白之后，他就只能回想起自己在奔跑着的碎片。"
    "在这个鱼店左转……走错了，路上没有这家电影院……自己见过这座公园……"
    "发疯般地在住宅区里奔跑，但自己为何这么做，却什么都想不起来。而当他彻底回过神来时，已经身处学校内了。"
    "手电筒的光芒把周围完全照亮，数不清的警察们嘈杂地围着小学，门口停着五辆以上的警车，老师和校长不停解释着什么，母亲只是一味地蹲在地上哭。"
    "“你还记得，从那孩子的家出来之后，都发生了什么吗？”"
    "面前是两个面如土色的警察，他的记忆从这里开始。"
    window hide
    nvl clear
    with fade
    window show
    "他能想起来的，除了和少女的谈话以外，就只有一件事了。"
    "“我……在回来的路上，似乎看到了某个隧道。”"
    window hide
    scene 12_bai_tian
    with fade
    window show
    "并没有踏足其中，只是看到而已。"
    "但不知为何，关于这个隧道的记忆却特别明晰。"
    #window hide
    nvl clear
    with fade
    #window show
    "暗无天日的隧洞，"
    "湿哒哒的、流淌着的水声，"
    "四处弥漫着的腐臭，"
    "以及，某个男人的身形……"
    #window hide
    nvl clear
    with fade
    #window show
    "“不，稍等一下。”"
    "正当他描述之时，一个警察却突然打断了他的话。"
    "“你记错了吧，那种地方哪有什么隧道？”"
    #window hide
    nvl clear
    with fade
    #window show
    "这是个不太有趣的玩笑。"
    "对还是孩童的他来说，就更是如此了。"
    "但警察和自己母亲的脸都异常认真，完全不像在说谎的样子。"
    "“别开玩笑了……”"
    #window hide
    nvl clear
    with fade
    #window show
    "然后，确实，通往住宅区的路上没有任何隧道。"
    "那里有的只不过是被树林环绕的幽暗的泥土路。"
    "他急忙用有些混乱的脑袋，试图让记忆能符合逻辑。"
    "首先最大的可能是自己看错了，像是把浓密的树枝看成了隧道的顶部什么的。"
    "但树木最茂盛的地方，也只不过是一排排杨树。"
    "就算是在孩童眼里，这里也没有能和隧道搞混的路。"
    "那么是在做梦吗？"
    "不，不可能——"
    "他曾到少女家里拜访是不争的事实，看到他们一同回家的同学也做了证。"
    scene white
    with fade
    stop music
    "“……”"
    #window hide
    nvl clear
    scene xue_xiao_wai_bu_huang_hun
    with fade
    #window show
    "说来奇怪，在那之后，少女就再没来过学校，他自然也再没去过少女家里。"
    "就算自己提起这件事，周围的人也都会编出一些借口带过话题，他也很快被迫搬家，从这所小学转走。"
    "在告别会上，老师和同学们意味深长地看着他。"
    "仿佛是在看什么奇怪的东西一样，那种实现让人很不舒服。"
    scene white
    with fade
    "这就是他有关这件事的最后的记忆。"
    #window hide
    nvl clear
    with fade
    #window show
    play music "audio/3.mp3" fadeout 1.0 fadein 1.0
    "时光流转，他已经长成了一名俊朗的青年。"
    "高中毕业后便直接步入社会，托工作地方的前辈的关系，他很快就搬离了父母身边，在市区周围租下了一间房子。工资虽然不甚丰厚，但对于一个人生活、很少去社交的他来说，已经是绰绰有余了。"
    "不过……说来奇怪。"
    stop music
    scene shao_nian_fang_jian
    "在那之后，直到现在，他一直有种被什么人监视着的感觉。"
    "时不时总听到些奇怪的脚步声，回过头去却什么都看不到；"
    "深夜躺在床上的时候，突然感觉窗外有透骨的视线盯着自己。"
    "和父母住在一起时还好，等到他长大搬离老家之后，这种感觉就愈发频繁了。"
    #window hide
    nvl clear
    with fade
    #window show
    "因此，青年在公寓门口的隐秘处安装了摄像头。"
    "数据都被保存在硬盘里，这样只要第二天检查一遍，就能知道究竟发生了什么。"
    #window hide
    nvl clear
    with fade
    #window show
    "摄像头什么都没有照到。"
    "除了下班回家路过的邻居，不确信它在工作而盯着摄像头的自己以外，什么都没照到。"
    "不过，自从安了这个摄像头之后，被人监视的感觉确实消失了。"
    "是犯人发现了摄像头呢，还是自己的心理安慰呢？青年并未考虑那么多。"
    "至少能正常地生活了，他由衷地感叹道。"
    #window hide
    nvl clear
    with fade
    #window show
    "距离他安装摄像头已经过去了两个月，这座城市悄然步入了秋天。"
    "在那之后，被跟踪的感觉几乎彻底消失了。"
    "即使偶尔出现，青年也权当是着凉了打冷战，没什么大不了的。"
    stop music
    "到头来，果然还是心理作用嘛。"
    #window hide
    nvl clear
    scene 9_ye_wan
    play music "audio/3.mp3" fadeout 1.0 fadein 1.0
    with fade
    #window show
    "“那你还真是神经质啊，这点小事儿就困扰了你这么长时间。”"
    "几杯酒下肚后，青年便把一直以来的故事都告诉了少女。"
    "说巧不巧，明明两人从那之后就再没见过面，这天却在乘坐的电车上一下就认出了彼此。"
    "“现在想来，确实是一段奇妙的回忆呢。”"
    "青年把杯中的酒一饮而尽后，对着少女说道。"
    #window hide
    nvl clear
    with fade
    #window show
    "青年是单纯外出谈业务，少女则似乎久违地从外国跑了回来。出手阔绰的少女当即签下"
    "“当然，这也是有代价的——”"
    "因此，青年便被少女拽到了酒馆里。"
    #window hide
    nvl clear
    with fade
    #window show
    "“呀，说起来真是巧呢，居然能一眼认出小学同学之类的，简直是言情剧一样的展开。”"
    "“要是在大街上，我肯定认不出来。但这趟环山电车整条线路都暴露在太阳下面，光照得人想睡也睡不着，就只能盯着其余乘客的脸看，仔细一瞧，自然就想起你的脸了。”"
    "少女抱怨的这一点，青年也深有同感。"
    stop music
    "这趟电车的采光太过良好，反而成为了乘客们的噩梦。"
    play music "audio/3.mp3" fadeout 1.0 fadein 1.0
    #window hide
    nvl clear
    with fade
    #window show
    "不过，因为青年住的地方远离城市，平日里坐这趟列车的人不是很多，很容易找到座位，也算不幸中的万幸了。"
    #window hide
    nvl clear
    with fade
    #window show
    "酒吧放着时下流行的音乐，再加上少女大大咧咧的玩笑，气氛一直都很高涨。"
    "“不过你变化真大，完全不像以前那样乖巧认真。”"
    "“你记错了吧，我的性格可一直都是这样，从来没变过哟。”"
    "少女断然否定了这点，看来出国真的会给人足够的改变，青年也就没多问什么。"
    "两人开心地回忆着各种事情——"
    "虽然只有少数残留的记忆，但也一直聊到了深夜时分。"
    #window hide
    nvl clear
    with fade
    #window show
    "“说起来，你说的当时看见的隧道我也有印象，但现在想来，估计只是工程通道吧。你想，那种把集装箱拼在一起的临时建筑，当时还是小孩子的你的脑袋就会把它当成隧道了，正所谓杯弓蛇影嘛。”"
    "少女如此安慰着青年，虽然感觉像是在刻意扯上些引经据典的东西，但仍相当有说服力。"
    "“说的对啊……”"
    "或许正是如此，青年才会放下警惕吧。"
    #window hide
    nvl clear
    stop music
    with fade
    #window show
    "——现在想来，那真的是个十分愚蠢的念头。"
    window hide
    nvl clear
    play music "audio/lianggongbgm/4.mp3" fadeout 1.0 fadein 1.0
    scene 1
    with fade
    window show
    "夜色渐浓，月亮隐在云后，时针朝着数字12缓慢移动。"
    "与少女分别后，青年看了看表。"
    "这个时间，只要赶一赶还能坐上末班车。"
    window hide
    nvl clear
    scene yue_tai_ye_wan_wu_che
    with fade
    play sound "audio/pao_bu_3.mp3"
    play music "audio/2.mp3" fadeout 1.0 fadein 1.0
    window show
    "啪嗒，啪嗒，啪嗒。"
    "一口气跑到了月台，距离末班车还有三分钟时间。"
    "“呼……”"
    "长舒了一口气，还好赶上了。"
    "青年的耳边回响着自己的呼气声。"
    "“诶？”"
    "他这时才注意到，月台空无一人。"
    #window hide
    nvl clear
    with fade
    #window show
    "四周异常寂静，连呼吸声都变得刺耳起来。"
    "说起来，毕竟已经深夜了，这种偏僻的小站，没什么人也是常事。"
    "不过话虽如此，青年乘坐这样的末班车还是第一次。"
    "不用怕，怀着平常心就好，都只是心理作用而已。"
    "电车驶进了月台。"
    "自动门缓缓打开，车厢内空无一人，自然也就没人下车。"
    "青年犹豫了一下，还是登上了电车。"
    window hide
    nvl clear
    scene 11_ye_wan_wu_xue
    with fade
    window show
    "随便找了个座位坐下，青年紧盯着车门。"
    "哪怕再有一个人上车也好，就能消除这诡异的气氛。"
    "但直到自动门关闭，都没有任何声音传来。"
    "电车微微摇晃着，离开了月台。"
    #window hide
    nvl clear
    with fade
    #window show
    "车内的灯光相当昏暗，老式灯泡的亮度甚至不及外面的路灯。"
    "看着车窗外越来越熟悉的风景，青年的眼皮有些沉重。"
    "车厢里只有青年一人，无聊的时间还要持续半小时以上。"
    "这种情况对时常应酬的上班族是常事，青年自然也不只经历过一次两次了。"
    #window hide
    nvl clear
    with fade
    #window show
    "还好家是终点站，就算真的睡着也不必担心……青年残存的理性这样想着。"
    "酒精终于开始发挥作用，意识昏昏沉沉，看着暗黄的老式灯泡，他逐渐……"
    window hide
    nvl clear
    scene
    with fade
    window show
    "——"
    "——"
    "——"
    "不。"
    "青年还没睡着。"
    "他轻掐了几下脸颊，传来一阵痛感，这并不是梦。"
    "但不是梦的话，再怎么说也太奇怪了，四周一片伸手不见五指的漆黑，简直就像——"
    stop music
    "驶进了某座隧道一般。"
    scene 12_ye_wan
    scene 11_ye_wan_wu_xue
    window hide
    nvl clear
    play music "audio/lianggongbgm/4.mp3" fadeout 1.0 fadein 1.0
    with fade
    window show
    "被酒精麻痹的神经顿时清醒，青年捂着嘴轻轻地呼吸。"
    "是因为恐慌的缘故吗，直到青年的眼睛完全适应黑暗之后，他才敢大口喘气。"
    "车厢内漆黑一片，但并非彻底的黑暗，只是今晚刚好没有月亮，车灯和路灯也都在一瞬间熄灭了而已。"
    "不知是不是地震之类的缘故，让发电厂暂时瘫痪了。"
    "不对啊……再怎么说，电车上的灯也不会受到影响吧。"
    "最令青年诧异的是，电车也好像失去了动力，停在了半路上。"
    "车厢之间的连接门不说；车门的开关是由系统控制的，断电后的车门就和卡住的电梯一样，无论他怎么尝试都纹丝不动。"
    "这算什么，被困在这里了啊……"
    "青年这样想着，内心的不安逐渐加剧。"
    "他不停地来回踱步，但狭小车厢内脚步的回音，却让他倍感恐惧。"
    "……等一下。"
    "青年停下了脚步，但脑内回荡着的脚步声却并未停止。"
    window hide
    nvl clear
    with fade
    window show
    "“我是本列电车的乘务员，电车目前因为不明原因发生故障，不过请您放心，很快就能排查出问题来。对了，请您配合出示一下相关证件。BB……诶，你之前是住在X市周围吗？”"
    "“是……没错，不过那已经是很久之前了。”"
    "“你还记……不，忘了才是正常的吧，毕竟当时你只是个孩子。看你的样子，现在事业小有所成了吧，能从那样的案件中存活下来，果然你很幸运呢。”"
    "“案件？你是指什么……”"
    "“诶？就是指那次你逃出来的，X市的入室杀人案啊。”"
    "乘务员相当平静地说出了不得了的话。"
    window hide
    nvl clear
    scene 6_xue_xin
    with fade
    stop music
    window show
    "“大概已经是十年之前了吧，那件事现在说起来还令人毛骨悚然，住在里面的夫妻俩和女儿无一幸免。据说杀人魔一早就潜进了房子里，丈夫被钝器敲破脑袋，妻子被划破喉咙之后挣扎着爬到玄关附近，血都已经流干了。但那个小女孩的尸体却更为惊悚……”"
    play music "audio/1.mp3" fadeout 1.0 fadein 1.0
    scene 7_xue_xin
    "“尸体被发现的房间门紧锁着，凶手似乎在行凶后就把她自己丢在了房间里。她倒在地上的血泊中，喉咙上有足以致命的伤口，从墙壁上满满的沾血的指甲印来看，她大概是想从窗户逃走吧，但那对刚上小学的女孩来说实在是太高了……”"
    "“不过，我刚才说的这些都只是我个人的见解。”"
    "乘务员咬了咬嘴唇，叹了一口气。"
    "“个人……为什么这么说？”"
    "“我是这起命案的第一发现者，但那时除了条警棍外，连对讲机都配不起，我只能跑回警局去找同事。但当我们再次赶到那栋房子时，那个女孩的尸体却不翼而飞了。”"
    "“她母亲的尸体还留在现场，但她房间里的血迹和抓痕全部都消失了，房间整洁如初，仿佛什么也没发生过一般。那家因为户口来路不正也查不到什么资料，到最后，大家都觉得那是我胡编乱造的故事。”"
    "“毕竟那个年代，杀人案多到难以估计，这只不过是其中一起而已……案子最终被归为单纯的杀人案，我后来也因此被调职。现在想来，还是很可恨的事情啊……”"
    window hide
    nvl clear
    scene
    with fade
    window show
    "乘务员仍在抱怨，但对青年来说，这些已经足够了——"
    window hide
    nvl clear
    with fade
    window show
    "不需要过多的描述和解释，只需要把事件点明，对他来说就足够了。"
    "少女毫无疑问是真实存在的，不然他不可能会跑到不认识的人的家里。记忆中残留的断片如潮水般回涌，那个正体不明的隧道也开始清晰起来。"
    "没错，隧道不是别的，正是少女家幽深的走廊。"
    "当时他跳出窗户、跑到正门时，映入眼帘的便是乘务口中的惨案。"
    "杀人魔大概是在他们进入房间后才动手的吧，就是他们听到剧烈响声的前后。"
    "他不禁在脑海里想象，少女的母亲被划开喉咙，跌跌撞撞地跑到少女门前，拼命地拧着门把手、敲着房门求救的样子。"
    "门内毫无回应。"
    window hide
    nvl clear
    with fade
    window show
    "说起来，少女当时明显转变的态度，或许就是因为注意到了这一点。"
    "但母亲死前的举动不仅让她意识到了外面的危险，也让杀人魔知道了这个房间里还有人。"
    "但对当时的她来说，已经没法逃去别的地方了，而且可能就她的想法而言，比起逃走，躲在房间里更为安全，就像学校的沙坑一样。"
    "只要躲在房间里就是安全的，少女如此坚信着。"
    "无论是刻意把嗓门加大，还是改变腔调模仿其他人，都是为了让对方起疑心而不敢贸然闯入。"
    "但自己却完全没有意识到这一点，反而自顾自地从窗户逃走了。"
    "没错，那种情况之下，自己本能地逃走了。"
    "房间里的少女会怎么想。"
    window hide
    nvl clear
    #with fade
    window show
    $ renpy.music.set_pause(True, channel='music')
    "那家伙，逃走了。"
    $ renpy.music.set_pause(False, channel='music')
    "逃走了逃走了……"
    $ renpy.music.set_pause(True, channel='music')
    "逃走了逃走了逃走了逃走了逃走了逃走了逃走了逃走了"
    $ renpy.music.set_pause(False, channel='music')
    "逃走了逃走了逃走了逃走了逃走了逃走了逃走了逃走了"
    $ renpy.music.set_pause(True, channel='music')
    "逃走了逃走了逃走了逃走了逃走了逃走了逃走了逃走了"
    $ renpy.music.set_pause(False, channel='music')
    window hide
    nvl clear
    #with fade
    window show
    "——"
    "在那之后，少女究竟一个人过了多久呢？"
    "对她来说，时间肯定难以想象地漫长吧。"
    "她声嘶力竭地叫喊着，到最后，嗓子已经发不出一点声音，她便转而尝试从窗户逃走，指甲被磨破，血迹留在墙上，但对少女来说，这点距离就宛如天堑难以跨越。"
    "而随着时间的流逝，犯人从杀人的冲动中冷静下来，开始寻找钥匙。"
    window hide
    nvl clear
    with fade
    window show
    "拉开书桌的抽屉，只有小刀和杂乱的明信片。"
    "翻着父亲的口袋，除了零钱之外什么都没有。"
    "……啊，从桌下的角落里找到了。"
    window hide
    nvl clear
    scene 6_xue_xin
    with fade
    window show
    "走过漫长的走廊，湿哒哒的血迹滴在地板上，正要开锁之时，却突然发现大门敞开着。"
    "说起来，外面之前好像有个小孩经过来着，还往这里看了一眼……算了，反正太阳都沉下去了，走廊也没开灯，从外面看来应该是一片漆黑。"
    "但这倒是提醒了他，赶紧跑过去把大门关上，然后跑回来，拿出钥匙，轻轻转动两下，“咔嚓”一声，房门打开了。"
    "只有一个小女孩在里面。"
    window hide
    nvl clear
    with fade
    window show
    "{size=+20}{color=#f00}到这里，结束。{/color}{/size}"
    window hide
    nvl clear
    with fade
    scene 11_bai_tian_wu_xue
    window show
    "“各位乘客非常抱歉，本次列车故障已经解决，预计到站时间为……”"
    "青年被电车的广播拽回了现实。"
    "乘务员早就离开了，车厢内又只剩下他一个人。电车再次开动，虽然灯泡依旧闪个不停，不过行驶中的电车也给了他不少安全感——还有半小时就到家了。"
    play music "audio/zou_lu_1.mp3"
    "脚步声淹没在了电车行驶的声音里，但仍在他的脑海中回荡。"
    "声音已经深入脑髓，宛若蠕虫一般啃啮着他的神经。"
    "通往旁边车厢的门上的灯变成了绿色，那是它即将打开的征兆。"
    play sound "audio/chuan_qi_1"
    "青年死死地盯着那扇门。"
    play sound "audio/chuan_qi_1"
    "随着刺耳的机械声，门缓缓张开——"
    play sound "audio/chuan_qi_1"
    "那不过是另一节空旷的车厢。"
    play sound "audio/chuan_qi_1"
    "电灯完好无损，地面一尘不染，单独拍下来作为宣传照片都毫无问题的车厢。"
    stop music
    stop sound
    "脑内的脚步声也停了下来。"
    "只是幻听而已，他闭上眼睛呼出了一口气。"
    "大脑给出的理由足够说服自己。"
    nvl clear
    with fade
    scene white
    "白天遇到的“少女”也应该只是其他的同学，从幼儿园到高中有那么多女同学，怎么可能一个个都记住，只是相似的其他人被自己误认成了她而已。"
    "明天自己就搬回去住，彻底告别这个城市……"
    "没关系，一切都会过去……"
    "青年这样想着，睁开了眼睛——"
    window hide
    nvl clear
    play music "audio/1.mp3"
    with fade
    window show
    "电灯摇曳晃动。"
    "车厢的中间，多了某些东西，青年相当熟悉的东西。"
    "永存于记忆中的那个傍晚，"
    "喉咙被割裂，指甲被折断……"
    "本该消失的少女，如今断然出现在面前。"
    "这辆列车究竟会通往何处，青年似乎有了答案。"
    "少女伸出了手，渴求般地说着……"
    window hide
    nvl clear
    with fade
    window show
    "“不要走——”"
    window hide
    nvl clear
    with fade
    s "“哇啊啊啊啊啊——”"
    s "果然啊，果然。"
    s "娇弱可爱的尖叫在耳边爆开。"
    s "身为人类的保护欲和悔意此时被放大到极致，保护欲自不必多提，悔意的由来则是我没能阻止讲述故事的那家伙。"
    haruhi "“胆子太小了啊，实玖瑠！”"
    s "是的，打从面前的家伙不顾气氛地开讲这个故事时，我就已经意识到接下来会发生什么了……"
jump part1
