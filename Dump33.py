import os, platform

try:

    import requests

except:

    os.system('pip install requests')

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    from dump64 import main

    main()

elif bit == '32bit':

    from dump32 import main

    main()
