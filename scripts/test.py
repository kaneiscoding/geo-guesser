#import sysconfig; print(sysconfig.get_paths()["purelib"])
import sys
for path in sys.path:
    print(path)
