from PIL import Image
import os, re

APPDATA = "C:\\Users\\rickt\\AppData\\Local\\Packages\\"
FOCUS = "Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets\\"
BING_PAPER = "C:\\Users\\rickt\AppData\\Local\Microsoft\\BingWallpaperApp\\WPImages\\"
OWN_PATH = "C:\\Users\\rickt\\Pictures\\winFocus\\"

PICTRUE_ENDS = "^.+(\.jpg|\.png)$"
WIN_FOCUS = APPDATA + FOCUS
RES_SCREEN = (1920, 1080)

''' Test Data'''
# ERR_1 = "7e413cbbf8166eb970680de91211421f49fbd0d8cd5e21d962162a00238590ff"
# ERR_2 = "89189acc894a85d033e6e7993a898144139adb1e1415f101cb6ba2ce5d890bf9"
# RIGHT = "2cbcd23888378cc82bd4c4d8dfcd850dc256c4862127f697ced9f53a648054ab"

def fileCopy(path, toPath):
    tmps = os.listdir(path)
    i = 0

    for tmp in tmps:
        src = path + tmp
        try:
            oo = Image.open(src)
        except Exception as e:
            print(e)
            break

        filename = tmp if re.match(PICTRUE_ENDS, tmp) else tmp + ".jpg"
        print(oo.size == RES_SCREEN, filename)
        
        if oo.size >= RES_SCREEN:
            if not filename in os.listdir(toPath):
                cmd = "copy " + src + " " + toPath + filename
                print(cmd)
                result = os.system(cmd)
                i += 1
                print(("Success:" if result == 0 else "Failed:") + filename)
    print("Copy %d files from %s to %s" %(i, path, toPath))

fileCopy(WIN_FOCUS, OWN_PATH)
fileCopy(BING_PAPER, OWN_PATH)
