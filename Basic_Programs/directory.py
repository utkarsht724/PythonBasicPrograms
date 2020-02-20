import os
print(f for f  in os.listdir('home'/'pycharmprojects')if os.path.isfile(os.path.join('home'/'pycharmprojects',f)))