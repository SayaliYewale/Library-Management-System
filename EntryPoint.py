import db
import sys
import os
py=sys.executable


# Entry point for application
if __name__ == '__main__':
    if not db.checkSetup():
        db.setup()
        os.system('%s %s' % (py, 'Add_Student.py'))
    else:
        os.system('%s %s' % (py, 'options.py'))