from pathlib import Path

from androguard.misc import AnalyzeAPK

with open('out.csv', 'w') as f:
   f.write("apk, AndroidVersionCode, AndroidVersionName, MinSDK, MaxSDK, TargetSDK, EffectiveSDK \n")
   for p in Path('samplesNDS').rglob('*.apk'):
       if p.exists():
          print(p)	
          a, d, dx = AnalyzeAPK(p.absolute().as_posix())
          vc = a.get_androidversion_code() 
          vn = a.get_androidversion_name() 
          min_v = a.get_min_sdk_version() 
          max_v = a.get_max_sdk_version() 
          tv = a.get_target_sdk_version()
          etv = a.get_effective_target_sdk_version()
          f.write("%s, %s, %s, %s, %s, %s, %s\n" %(p.stem, vc, vn, min_v, max_v, tv, etv))
