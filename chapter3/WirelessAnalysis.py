from _winreg import *
import mechanize, urllib, re, urlparse



def wiglePrint(username, password, netid):
    '''
    creating instance of mechanize broweser
    :param username string:
    :param password string:
    :param netid :
    :return:
    '''
    browser = mechanize.Browser()
    browser.open('http://wigle.net')
    reqData = urllib.urlencode({'credintial_0': username, 'credintail_1': password})
    browser.open('https://wigle.net/gps/gps/main/login', reqData)



def hexToMacAddr(val):
    '''

    :param val to be converted
    :description the function converts the hex bytes (e.g) \x40\x05\x85 to mac address representation (e.g) 40:05:85
    :return the converted value :
    '''

    addr = ''
    for ch in val:
        addr += ("%02x " % ord(ch))
    addr = addr.strip(" ").replace(" ", ":")[0:17]
    return addr


def printNets():

    net = "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\NetworkList\\Signatures\\Unmanaged"
    key = OpenKey(HKEY_LOCAL_MACHINE, net) # this opens the register in the above dict
    print "[+] the networks I Joined"
    for i in range(100):
        try:
            guid = EnumKey(key, i)
            netKey = OpenKey(key, str(guid))
            (n, addr, t) = EnumValue(netKey, 5)
            (n, name, t) = EnumValue(netKey, 1)
            macAddress = hexToMacAddr(addr)
            netName = str(name)
            print '[+] name is: ' + netName + '\n' + '[+] mac is: ' + macAddress
            CloseKey(netKey)

        except Exception as e:
            print e
            continue


def main():
    printNets()



if __name__ == '__main__':

    main()