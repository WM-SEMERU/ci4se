def str2url(str):
    try:
        str = str.encode('utf-8')
    except:
        pass
    mfrom = 'ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝßàáâãäåæçèéêëìíîï'
    to = 'AAAAAAECEEEEIIIIDNOOOOOOUUUUYSaaaaaaaceeeeiiii'
    mfrom += 'ñòóôõöøùúûüýÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģ'
    to += 'noooooouuuuyyaaaaaaccccccccddddeeeeeeeeeegggggggg'
    mfrom += 'ĤĥĦħĨĩĪīĬĭĮįİıĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŉŊŋŌōŎŏŐőŒœŔŕŖŗŘř'
    to += 'hhhhiiiiiiiiiijjkkkllllllllllnnnnnnnnnoooooooorrrrrr'
    mfrom += 'ŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽžſƀƂƃƄƅƇƈƉƊƐƑƒƓƔ'
    to += 'ssssssssttttttuuuuuuuuuuuuwwyyyzzzzzzfbbbbbccddeffgv'
    mfrom += 'ƖƗƘƙƚƝƞƟƠƤƦƫƬƭƮƯưƱƲƳƴƵƶǍǎǏǐǑǒǓǔǕǖǗǘǙǚǛǜǝǞǟǠǡǢǣǤǥǦǧǨǩ'
    to += 'likklnnoopettttuuuuyyzzaaiioouuuuuuuuuueaaaaeeggggkk'
    mfrom += 'ǪǫǬǭǰǴǵǷǸǹǺǻǼǽǾǿȀȁȂȃȄȅȆȇȈȉȊȋȌȍȎȏȐȑȒȓȔȕȖȗȘșȚțȞȟȤȥȦȧȨȩ'
    to += 'oooojggpnnaaeeooaaaaeeeeiiiioooorrrruuuusstthhzzaaee'
    mfrom += 'ȪȫȬȭȮȯȰȱȲȳḀḁḂḃḄḅḆḇḈḉḊḋḌḍḎḏḐḑḒḓḔḕḖḗḘḙḚḛḜḝḞḟḠḡḢḣḤḥḦḧḨḩḪḫ'
    to += 'ooooooooyyaabbbbbbccddddddddddeeeeeeeeeeffgghhhhhhhhhh'
    mfrom += 'ḬḭḮḯḰḱḲḳḴḵḶḷḸḹḺḻḼḽḾḿṀṁṂṃṄṅṆṇṈṉṊṋṌṍṎṏṐṑṒṓṔṕṖṗṘṙṚṛṜṝṞṟ'
    to += 'iiiikkkkkkllllllllmmmmmmnnnnnnnnoooooooopppprrrrrrrr'
    mfrom += 'ṠṡṢṣṤṥṦṧṨṩṪṫṬṭṮṯṰṱṲṳṴṵṶṷṸṹṺṻṼṽṾṿẀẁẂẃẄẅẆẇẈẉẊẋẌẍẎẏẐẑẒẓẔẕ'
    to += 'ssssssssssttttttttuuuuuuuuuuvvvvwwwwwwwwwwxxxxxyzzzzzz'
    mfrom += 'ẖẗẘẙẚẛẠạẢảẤấẦầẨẩẪẫẬậẮắẰằẲẳẴẵẶặẸẹẺẻẼẽẾếỀềỂểỄễỆệỈỉỊị'
    to += 'htwyafaaaaaaaaaaaaaaaaaaaaaaaaeeeeeeeeeeeeeeeeiiii'
    mfrom += 'ỌọỎỏỐốỒồỔổỖỗỘộỚớỜờỞởỠỡỢợỤụỦủỨứỪừỬửỮữỰựỲỳỴỵỶỷỸỹ'
    to += 'oooooooooooooooooooooooouuuuuuuuuuuuuuyyyyyyyy'
    for i in zip(mfrom, to):
        str = str.replace(*i)
    return str