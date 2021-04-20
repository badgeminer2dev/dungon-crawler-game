##my game's loader tool
def inv2text(inv_dat, dat):
    return inv_dat[ dat ]
def text2inv(text_dat, key):
    return text_dat[key]
def disp_inv(inv, inv_data):
    length = len(inv) - 1
    i = 0
    while i <= length :
        if inv[i] != 0:
            print(inv2text(inv_data, i) + ' ' + str(inv[i]))
        i = i +1
    return '1'
def inv_stash(inv_, text_dat, cmd, stash):
    item = input('drop>>>')
    print('droping ' + str(inv_[text_dat[item]]) + ' ' +item)
    stash[text_dat[item]] =  inv_[text_dat[item]]
    inv_[text_dat[item]] = 0
    return inv_, stash
    
