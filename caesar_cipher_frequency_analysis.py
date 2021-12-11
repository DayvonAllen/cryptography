import string
import matplotlib.pylab as plt

ALPHABET = string.ascii_uppercase + " " + "," + "?" + "'"


def frequency_analysis(text):
    text = text.upper()

    letter_frequencies = {}
    for letter in ALPHABET:
        letter_frequencies[letter] = 0

    for letter in text:
        if letter in ALPHABET:
            letter_frequencies[letter] += 1

    return letter_frequencies


def plot_distribution(frequencies):
    plt.bar(frequencies.keys(), frequencies.values())
    plt.show()


def caesar_crack(text):
    freq = frequency_analysis(text)
    # x[0] means sort based on keys, x[1] means sort based on the value
    # reverse makes it sort in Descending order, instead of Ascending order
    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    # find the most frequent character index and subtract it from "E" to get the potential key
    # I'm getting the second most frequent character because white space is number but we want to get an actual letter
    print("The possible key value: %s" % (ALPHABET.find(freq[1][0]) - ALPHABET.find("E")))


cipher_text = "EHK,FTBILNFTBLTLBFIERT NFFRTM,QMTH?TMA,TIKBGMBG'TXG TMRI,L,MMBG'TBG NLMKRWTEHK,FTBILNFTAXLTY,,GTMA," \
              "TBG NLMKRWLTLMXG XK T NFFRTM,QMT,O,KTLBGZ,TMA,TWWWWLUTPA,GTXGTNGDGHPGTIKBGM,KTMHHDTXT'XEE,RTH?TMRI," \
              "TXG TLZKXFYE, TBMTMHTFXD,TXTMRI,TLI,ZBF,GTYHHDWTBMTAXLTLNKOBO, TGHMTHGERT?BO,TZ,GMNKB,LUTYNMTXELHTMA," \
              "TE,XITBGMHT,E,ZMKHGBZTMRI,L,MMBG'UTK,FXBGBG'T,LL,GMBXEERTNGZAXG', WTBMTPXLTIHINEXKBL, TBGTMA," \
              "TWWWWLTPBMATMA,TK,E,XL,TH?TE,MKXL,MTLA,,MLTZHGMXBGBG'TEHK,FTBILNFTIXLLX',LUTXG TFHK,TK,Z,GMERTPBMAT ," \
              "LDMHITINYEBLABG'TLH?MPXK,TEBD,TXE NLTIX',FXD,KTBGZEN BG'TO,KLBHGLTH?TEHK,FTBILNFWT "

# data = frequency_analysis(cipher_text)

# plot_distribution(data)

caesar_crack(cipher_text)
