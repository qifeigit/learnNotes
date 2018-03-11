```python
import os
import shutil
#www.iplaypython.com
 
def CleanDir( Dir ):
    if os.path.isdir( Dir ):
        paths = os.listdir( Dir )
        for path in paths:
            filePath = os.path.join( Dir, path )
            if os.path.isfile( filePath ):
                try:
                    os.remove( filePath )
                except os.error:
                    continue#引入logging
            elif os.path.isdir( filePath ):
                shutil.rmtree(filePath,True)
    return True
 
Dir = "C:\\Users\Administrator\AppData\Local\Temp"
CleanDir(Dir)

```