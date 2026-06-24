#region ASCII art
falcon=r"""
                               /T /I
                              / |/ | .-~/
                          T\ Y  I  |/  /  _
         /T               | \I  |  I  Y.-~/
        I l   /I       T\ |  |  l  |  T  /
 __  | \l   \l  \I l __l  l   \   `  _. |
 \ ~-l  `\   `\  \  \\ ~\  \   `. .-~   |
  \   ~-. "-.  `  \  ^._ ^. "-.  /  \   |
.--~-._  ~-  `  _  ~-_.-"-." ._ /._ ." ./
 >--.  ~-.   ._  ~>-"    "\\   7   7   ]
^.___~"--._    ~-{  .-~ .  `\ Y . /    |
 <__ ~"-.  ~       /_/   \   \I  Y   : |
   ^-.__           ~(_/   \   >._:   | l______
       ^--.,___.-~"  /_/   !  `-.~"--l_ /     ~"-.
              (_/ .  ~(   /'     "~"--,Y   -=b-. _)
               (_/ .  \  :           / l      c"~o \
                \ /    `.    .     .^   \_.-~"~--.  )
                 (_/ .   `  /     /       !       )/
                  / / _.   '.   .':      /        '
                  ~(_/ .   /    _  `  .-<_      -Row
                    /_/ . ' .-~" `.  / \  \          ,z=.
                    ~( /   '  :   | K   "-.~-.______//
                      "-,.    l   I/ \_    __{--->._(==.
                       //(     \  <    ~"~"     //
                      /' /\     \  \     ,v=.  ((
                    .^. / /\     "  }__ //===-  `
                   / / ' '  "-.,__ {---(==-
                 .^ '       :  T  ~"   ll
                / .  .  . : | :!        \\
               (_/  /   | | j-"          ~^
                 ~-<_(_.^-~"
"""
scared="""

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣶⣶⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣈⠉⠻⣿⣿⣿⣿⣿⠿⠿⠿⢿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⢷⡀⠛⢿⣿⣿⣧⣴⣶⣶⣤⣬⡅⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠨⠧⠀⠁⣴⣾⣄⠈⡟⠉⠀⢤⡈⢻⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣂⠍⢁⠤⢿⣿⣿⣿⡻⡀⠡⣤⣜⡓⠀⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣻⢇⣴⠀⡀⠈⣿⠁⠀⠹⢱⡘⡖⣶⣷⣜⣏⢹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⠇⡴⢀⣶⣿⠶⢖⣠⣿⣿⣾⣿⣿⣿⣿⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠚⡿⠿⠏⠀⢡⣾⣿⡿⢛⡛⢛⣛⠛⢿⣿⣿⣿⣿⣿⠀⠀⠐⠀⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⠀⠀⠀⠀⣤⣶⡶⢉⣅⢙⠿⠿⢟⣶⣄⠙⢿⣿⣿⡿⠀⠀⡀⢠⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⢱⡇⠀⠀⠀⠉⠁⠀⣭⡿⠀⣭⣴⠀⡢⣄⣑⠀⢹⣿⡇⠀⠀⠁⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣴⣾⣿⣿⣷⢿⡵⡄⠀⠀⠀⠱⡀⠀⠀⠀⣰⣶⡆⠀⠚⣣⣹⣧⣃⠸⢿⣷⠀⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣇⣳⡷⠀⠀⠀⢀⣶⠀⠀⠸⠿⠙⠀⠀⠻⣿⣿⣟⣿⡀⢲⣦⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⡟⢽⡿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⣿⠀⠀⢠⡄⠂⠀⣶⠆⣃⣠⣾⣿⠛⠀⢀⠐⣄⠀⠀⠀⠀⠀⠞⣠⢊⣽⣿⣿⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣷⠈⣇⢹⣿⣿⣿⣿⣿⡄⠀⠀⠀⡏⠀⠀⣿⡀⠠⠀⠠⣼⣿⡿⠛⢁⣤⣶⡟⠁⡀⠀⠀⠀⠀⠀⡈⣷⣿⣿⣭⣽⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⣾⣿⣿⣿⣿⣿⣧⠀⠀⠀⠎⠀⣸⣏⠖⠀⢠⣀⠘⠉⠀⣴⡿⠟⢋⣤⠆⠘⣀⣤⣤⠀⣬⣧⠘⣿⡟⢻⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⣿⠋⠀⣀⡘⠁⣀⣴⡤⠄⠀⣴⠟⢡⣴⣾⣿⣿⣿⣷⣝⣿⡇⢹⣷⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡘⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠉⠀⢴⣿⣛⣉⣸⠋⢁⣤⡆⢁⣴⣿⣿⣿⣿⣿⣿⣿⠄⣿⣿⡀⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠈⠿⢿⡿⢏⣤⣏⡁⢠⣿⣿⣿⣿⣿⣿⣿⡿⣅⣄⠘⢻⡇⠈⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡑⠪⣿⣿⣿⣿⣿⣿⣿⣿⠿⠂⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠿⠇⢹⣿⣿⠟⠻⢟⠩⢐⣨⡶⠋⣨⣷⣷⠀⠸⢿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣶⣿⣿⣿⣿⣿⣿⠇⣸⢠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠈⢁⣰⣶⣾⡿⠋⠀⠙⢿⣿⡇⠀⠂⠈⣿⣿⣿⣿⣿⣿⠂⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⢿⣦⠳⣄⠀⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢴⣿⣿⣿⠏⠀⠐⠀⠁⢠⣿⣌⠢⣴⣾⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠈⠻⣷⣙⣷⣄⠙⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠿⠟⡁⠀⠀⠀⢀⠙⢿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⡿⢻⠀⠀⠙⢳⣿⣟⡛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠋⠀⡄⠐⣴⠁⢳⣤⢙⢃⠎⠉⠻⣿⣿⣿⣿⣿⣷⣾⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣃⣿⣦⡙⣇⣀⡀⠀⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⢀⣤⣷⣄⣠⣾⣿⣷⣌⣀⡎⣾⣴⡙⣰⣬⢻⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⣧⠓⣻⣿⣿⣏⠀⠉⠁⠀⠀⠀⣷⣦⢬⠟⠀⡔⡰⠃⣌⡂⣻⣿⡿⢋⣘⠻⣿⣿⣿⣿⣧⣼⠁⢙⣿⡻⠿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀
"""
yellow="""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡿⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡶⠶⢖⠦⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣷⡀⠀⠀⠀⠀⠀⠐⠋⠉⠉⠛⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠟⠀⠀⠀⠀⠀⠈⢳⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⠋⠀⠀⠀⢀⣀⣠⠤⠤⠤⠤⠤⠤⠤⢌⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⠀⠀⠀⠀⠀⠀⠀⢸⠇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠁⣠⠤⠒⣋⡭⠤⠒⠒⠉⠉⡩⢟⣣⣤⣀⡢⣬⣉⠒⠤⣄⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⡞⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠖⣉⠴⠒⠉⠀⠀⠀⠀⠀⢀⣞⣴⠟⠋⠉⠛⢿⣾⣎⠑⢤⡀⠙⠢⣄⠀⠀⠀⠀⠀⠸⡄⠀⠀⠀⠀⠀⠀⣸⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⢋⡤⢊⣁⡀⠀⠀⠀⠀⠀⠀⠀⣞⣾⠃⠀⠀⠀⠀⠀⠹⣿⡄⠀⠱⡄⠀⠀⠑⣄⠀⠀⢀⣠⣽⠶⠶⠶⠒⠒⠒⠛⢤⣄⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠋⡴⢋⢔⣭⣴⣿⣷⣤⠀⠀⠀⠀⠰⣽⠃⠀⠀⠀⠀⠀⠀⠀⢹⣇⠀⠀⠘⡄⠀⠀⠈⢳⣶⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠯⠻⣦⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡜⢡⠎⢠⢯⣿⠋⠁⠀⠈⠻⣷⠀⠀⠀⠀⡏⠀⠀⠀⠐⢷⢶⣄⠀⠀⣿⠀⠀⠐⠁⠀⠀⢰⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠪⠙⣆⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⢠⠃⠀⣮⡿⠁⠀⠀⠀⠀⠀⠻⣇⠀⠀⠀⡇⠀⠀⢀⠀⣸⣷⣻⡄⠀⣿⠀⠀⠀⠀⠀⣏⠓⠒⢀⣀⣀⣀⣀⣀⣀⣀⣀⠀⢠⠂⠀⠀⠀⠘⡄
⠀⠀⣀⣠⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⢀⠇⠀⢰⣿⠇⠀⠀⠀⠀⠶⣶⡄⢹⠀⠀⠀⡇⠀⠀⣾⢹⣿⣿⣏⡇⠀⣿⠀⠀⣀⣤⡤⠤⣼⣶⠿⠛⠉⠀⠀⠀⠀⠀⠀⠉⠙⡇⠀⠀⠀⠀⠀⡇
⣠⠾⠋⠀⠀⠈⠻⡷⡀⠀⠀⠀⠀⠀⠀⢰⠁⠸⠀⠀⠸⣿⠀⠀⠀⠀⣄⣀⣷⣽⣸⠀⠀⠀⣇⠀⠀⠸⣞⣿⣅⣽⠁⢀⣇⣴⠞⠋⠁⠀⣼⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠇⠀⠀⠀⠀⠀⢸
⡇⠀⠀⠀⠀⠀⠀⠀⠘⡆⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⢰⣿⠀⠀⠀⠀⣇⣿⣿⣿⣿⠀⠀⠀⠀⡄⠀⠀⠙⠧⠽⠃⠀⡼⠋⠀⠀⠀⠀⠀⣯⠦⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢳⡀⠀⠀⠀⠀⠀⠀⢀⣹⣤⣤⣤⣤⣄⡇⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⢻⡽⠿⣾⢹⠀⠀⠀⠀⠻⡄⠀⠀⠀⠀⢠⠞⠁⠀⣀⣀⡀⠀⠀⠘⢧⡀⣠⣤⡶⠖⠛⠛⠛⠒⠒⡞⠀⠀⠀⠀⠀⠀⢀⠀
⠀⠉⠳⣄⠀⢀⡤⡺⠛⠉⠀⠀⠀⠀⠈⣻⢦⠀⠀⠀⠀⢻⡆⠀⠀⠀⠈⠻⠟⢁⡎⠀⠀⠀⠀⠀⠙⠦⣄⣀⣤⠟⠀⠀⠉⣀⣀⣀⡉⠂⠀⠀⣽⣏⠁⠀⠀⠀⠀⠀⠀⠀⢇⠀⠀⠀⠀⠀⢠⡞⠀
⠀⠀⠀⢈⣷⠋⠀⠁⠀⠀⠀⠀⠀⢀⣠⣤⣼⣧⣤⡀⠀⠀⠻⡄⠀⠀⠀⠀⢀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠀⠀⣈⣭⠵⠒⠋⠉⠂⠀⠀⠹⡌⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀
⠀⠀⠀⣾⠋⠀⠀⠀⠀⠀⢀⡤⠞⠉⠉⠀⠀⠀⠈⣻⡆⠀⣀⣙⡦⠤⣀⣤⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠴⠋⣡⡏⠀⠀⠀⠀⠀⠀⠀⠀⠙⠲⣄⡀⠀⠀⠀⠀⠀⠀⣀⣠⠴⠋⠁⠀⠀⠀
⠀⠀⢸⠇⠀⠀⠀⠀⢀⡶⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⡧⠋⠉⠁⠀⠀⠀⠘⠀⠀⠀⠀⠀⠀⠀⢀⣠⠴⠚⠉⠀⢀⣴⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠁⠈⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⠀⠀⠀⠉⠑⢏⠀⠀⠀⠀⠀⠀⣀⣤⠶⠶⠾⣧⡀⠀⠀⠀⠀⠀⣤⣤⣤⣤⡤⠒⠒⠉⠁⠀⠀⣀⣤⣶⠿⢿⡿⠀⠀⠀⠀⠀⠀⠀⠀⢀⡶⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⡆⠀⠀⠀⠀⠈⠇⠀⠀⢀⡤⠚⠉⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣶⣶⣶⣶⣾⠿⣿⡟⠁⠀⣼⠃⠀⠀⠀⠀⠀⣠⠞⣠⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠹⡄⠀⠀⠀⠀⠀⠀⠉⠻⡄⠀⠀⠀⠀⠀⠀⣰⠁⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⠃⣠⠏⠀⠀⣰⠏⠀⠀⠀⠀⠠⠞⢁⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠙⣄⠀⠀⠀⠀⠀⠀⠀⠊⠀⠀⠀⠀⢀⡴⠋⠳⢄⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⠁⠊⠀⠀⢀⡰⠋⠀⠀⠀⠀⠀⣠⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠑⠦⣀⡀⠀⠀⠀⠀⠀⣀⡠⠖⠋⠀⠀⠀⠀⠙⠢⢄⡀⠀⠀⠀⠀⠈⠛⢿⣇⣀⣀⣠⠴⠋⠀⠀⠀⢀⣀⠤⠚⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠒⠒⠚⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠒⠤⢤⣀⣀⣀⣀⣀⣀⣀⣀⡠⠤⠖⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
steve="""
⠀⠀⠀⠀⠀⣾⠛⡟⠻⢶⣤⣼⣿⡶⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣧⣾⠇⠀⠀⢸⠛⡿⣄⠀⠉⠻⢶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢀⡀⢤⣀⣂⣤⣤⣷⣶⣷⠈⠻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⣿⡿⢠⣆⠀⡟⠲⠇⠀⠙⠲⢄⡀⠉⠛⠷⣦⡀⠀⢠⣾⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠈⠙⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣴⣿⡟⢻⠧⣼⠁⠉⠀⠀⠀⢰⠦⣀⠀⠈⠓⠦⣄⣼⡇⠀⣿⣿⣿⣿⣿⣿⣿⡿⠿⠟⠛⠋⠉⢹⣿⣿⡀⠀⠀⠀⠀⠉⢻⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⣿⣿⠀⡏⠀⠀⠀⣤⣄⣿⠱⣿⣄⡈⠙⠲⢄⡀⢨⠋⢻⣾⣿⣿⡏⠉⠉⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⣇⠀⠀⠀⠀⠀⠈⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣼⣿⠇⢸⠁⢀⡷⣶⣇⡼⠉⠙⠻⣿⣿⣶⣤⣀⠈⣿⣦⣾⣿⡿⠛⠃⠀⠀⣀⠀⠀⠀⢠⣶⡎⠉⢨⠀⢠⣿⠳⣤⠀⠀⠀⠰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣿⡿⠀⡏⠀⣸⠁⣿⣿⠟⠲⠂⢤⣿⡀⠉⠛⠋⠙⠛⠉⠁⣿⡄⢰⠋⠉⣿⣿⡀⣠⠤⡜⠛⠙⠋⠉⠀⡇⠉⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣼⣿⠇⢸⠁⢀⡏⢸⣿⣿⣷⣦⣀⣀⠉⣿⡄⠀⠀⠀⠀⠀⠀⢿⡇⠈⠐⠉⢁⣀⡠⠤⠶⢣⣶⡆⠀⠀⠀⡇⠀⠀⢸⣀⠀⠀⠀⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢿⣿⣦⡏⠀⣸⢁⡟⢸⣿⣿⣇⣸⠉⢙⠿⣧⡀⠀⠀⠀⠀⠀⢸⡇⠀⠀⢰⣿⣿⣀⣤⣤⣾⣿⡇⠀⠀⢀⣇⠀⠀⠀⠉⣷⡀⢀⣷⣴⡶⠶⠦⢶⡄⠀⠀⠀⠀⠀⠀⠀
⠀⣿⣿⡟⢳⣿⣼⠃⠀⠈⣿⣿⡟⢲⡾⣤⣼⠇⠀⠀⠀⠀⠀⣸⡇⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣿⠿⡶⢤⣠⠞⠉⠉⠀⠀⠀⠀⠀⠈⣿⡄⠀⠀⠀⠀⠀⠀
⠀⠙⠛⠛⠛⠉⠀⠀⠀⠘⠻⣿⣷⣾⣀⣰⠋⠙⢄⣠⣤⣴⠶⠿⠷⣶⣶⣿⣿⣿⡿⠿⠟⠛⠋⠉⣉⣿⣀⣠⠴⠷⠀⡜⠀⠀⠀⠀⠀⠀⢠⠀⠀⠘⢾⡄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣯⣸⠏⠛⣿⡛⠭⠄⠒⠒⢲⠁⠹⡏⠁⠀⢸⣶⣦⡤⠴⠖⣿⠉⠉⠀⠀⠀⢠⢰⠁⠀⠀⠀⠀⢀⣀⣧⠀⠀⠀⠈⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣿⣿⣿⣶⠼⠛⡁⠤⠊⠁⠀⠈⣇⢠⡷⠒⠋⠉⠁⠘⠒⠒⠛⠉⠀⠀⠀⠀⠀⠀⢫⠐⠒⠒⠈⠉⠀⠀⠈⢧⠀⠀⢰⠉⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⣴⠾⠛⢉⣛⣉⡭⣤⠒⠉⠀⠀⠀⠀⠀⠀⢸⣸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⡀⠀⠀⠀⠀⠀⠀⠀⢣⠀⡎⠀⠈⢻⣆⠀⠀
⠀⠀⠀⠀⠀⠀⠘⣿⠒⠋⠉⠁⠀⠀⠀⠸⡄⠀⠀⠀⠀⠀⠀⠀⣸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⠹⣄⠀⠀⣀⣀⣀⠤⠤⢿⡀⠀⠀⠀⠻⣆⠀
⠀⠀⠀⠀⠀⠀⠀⢻⡇⠀⠀⠀⠀⠀⠀⠀⢳⠀⠀⠀⠀⠀⠀⢀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡆⢸⡍⠉⠁⠀⠀⠀⠀⠀⢳⡀⠀⠀⠀⢙⣆
⠀⠀⠀⠀⠀⠀⠀⠸⣿⡀⠀⠀⠀⠀⠀⠀⠈⡆⠀⠀⢀⣠⣶⡟⠋⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢸⣿⣄⠀⠀⠀⠀⠀⠀⠀⠱⡀⠀⠀⠀⢻
⠀⠀⠀⠀⠀⠀⠀⠀⢿⡇⠀⠀⠀⠀⠀⠀⢀⣹⣠⣶⠻⣿⠏⠀⠀⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡟⢿⣆⠀⠀⠀⠀⠀⠀⠀⠱⡀⠀⠀⡈
⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣶⣶⡶⠾⠟⠛⠛⢿    ⠀⠀⠀⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⢻⣦⠀⠀⠀⠀⠀⠀⠀⠙⡄⢀⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠻⣧⡀⠀⠀⠀⠀⠀⣀⣈⣨⡎
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡀⡗⢦⣀⡇⠀⠀⠀⠙⠷⠶⠶⠾⠟⠛⠛⠋⠉⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡝⠃⠀⢈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⢀⣀⣀⣠⣤⣴⠆⠀⠀⠀⠀⠀⠀⠀⣼⠁⠹⣦⣸⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⣰⠃⠀⠀⠹⣿⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⣰⠃⠀⠀⠀⢠⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢻⣿⠏⠀⠀⠀⠀⠀⠀⠀⢠⠏⠀⠀⠀⢀⣿⣏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠏⠀⠀⠀⠀⠀⠀⠀⢀⡟⠀⠀⠀⠀⣾⣿⠘⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠇⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣶⣤⣤⣾⢿⡇⣸⠉⠻⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠏⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣯⣾⠀⢹⡄⠀⣼⡗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠏⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣷⣄⡼⠀⢠⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠃⠀      ⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣋⣉⣉⣳⣄⣾⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠏⠀⠀⠀⠀⠀⠀⠀⠀⣰⠏⢻⣿⣿⣿⣿⡿⠓⠛⠛⠒⠒⠚⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠏⠀⠀⢀⣀⣀⣀⣀⣠⣴⠏⠀⠀⠋⠘⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⣽⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⣰⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⢠⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⠿⠿⠿⠿⠛⠛⠛⠛⠛⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
earth=r"""
        _____
    ,-:` \;',`'-, 
  .'-;_,;  ':-;_,'.
 /;   '/    ,  _`.-\
| '`. (`     /` ` \`|
|:.  `\`-.   \_   / |
|     (   `,  .`\ ;'|
 \     | .'     `-'/
  `.   ;/        .'
    `'-._____. '
"""
rabbit=fr"""
             ,
            /|      __
           / |   ,-~ /
          Y :|  //  /
          | jj /( .^
          >-"~"-v"
         /       Y
        jo  o    |
       ( ~T~     j
        >._-' _./
       /   "~"  |
      /     _,  |
     /| ;-"~ _  l
    / l/ ,-"~    \
    \//\/      .- \
     Y        /    \    
     l       I     !
     ]\      _\    /"\
    (" ~----( ~   Y.  )
~~~~~~~~~~~~~~~~~~~~~~~~~
"""
cards=fr"""
 _____________   _____________   _____________   _____________ 
/             \ /             \ /             \ /             \
│A    ___     │ │A     ^      │ │A  __   __   │ │A     ^      │
│    /   \    │ │     / \     │ │  /  \ /  \  │ │     / \     │
│  __\   /__  │ │    /   \    │ │  \   V   /  │ │    /   \    │
│ /         \ │ │   /     \   │ │   \     /   │ │   (     )   │
│ \___/ \___/ │ │  /       \  │ │    \   /    │ │    \   /    │
│     │_│     │ │  \__/^\__/  │ │     \ /     │ │     \ /     │
│            A│ │     /_\    A│ │      V     A│ │      V     A│
\_____________/ \_____________/ \_____________/ \_____________/
"""
heart=fr"""
  |  \ \ | |/ /            
  |  |\ `' ' /             
  |  ;'      \      / ,    
  | ;    _,   |    / / ,   
  | |   (  `-.;_,-' '-' ,  
  | `,   `-._       _,-'_  
  |,-`.    `.)    ,<_,-'_, 
 ,'    `.   /   ,'  `;-' _,
;        `./   /`,    \-'  
|         /   |  ;\   |\   
|        ;_,._|_,  `, ' \  
|        \    \ `       `; 
`      __ ;    \         ;;
 \   ,'  `      \,       ;;
  \_(            ;,      ;;
  |  \           `;,     ;;
  |  |`.          `;;,   ;'
  |  |  `-.        ;;;;,;' 
  |  |    |`-.._  ,;;;;;'  
  |  |    |   | ``';;;'   
"""
ps2=fr"""
      _=====_                               _=====_
     / _____ \                             / _____ \
   +.-'_____'-.---------------------------.-'_____'-.+
  /   |     |  '.        S O N Y        .'  |  _  |   \
 / ___| /|\ |___ \                     / ___| /_\ |___ \
/ |      |      | ;  __           _   ; | _         _ | ;
| | <---   ---> | | |__|         |_:> | ||_|       (_)| |
| |___   |   ___| ;                   ; |___       ___| ;
|\    | \|/ |    /  _     ___      _   \    | (X) |    /|
| \   |_____|  .','" "', |___|  ,'" "', '.  |_____|  .' |
|  '-.______.-' /       \      /       \  '-._____.-'   |
|               |       |------|       |                |
|              /\       /      \       /\               |
|             /  '.___.'        '.___.'  \              |
|            /                            \             |
 \          /                              \           /
  \________/                                \_________/                   
"""
sonic=fr"""
                             ...,?77??!~~~~!???77?<~.... 
                        ..?7`                           `7!.. 
                    .,=`          ..~7^`   I                  ?1. 
       ........  ..^            ?`  ..?7!1 .               ...??7 
      .        .7`        .,777.. .I.    . .!          .,7! 
      ..     .?         .^      .l   ?i. . .`       .,^ 
       b    .!        .= .?7???7~.     .>r .      .= 
       .,.?4         , .^         1        `     4... 
        J   ^         ,            5       `         ?<. 
       .%.7;         .`     .,     .;                   .=. 
       .+^ .,       .%      MML     F       .,             ?, 
        P   ,,      J      .MMN     F        6               4. 
        l    d,    ,       .MMM!   .t        ..               ,, 
        ,    JMa..`         MMM`   .         .!                .; 
         r   .M#            .M#   .%  .      .~                 ., 
       dMMMNJ..!                 .P7!  .>    .         .         ,, 
       .WMMMMMm  ?^..       ..,?! ..    ..   ,  Z7`        `?^..  ,, 
          ?THB3       ?77?!        .Yr  .   .!   ?,              ?^C 
            ?,                   .,^.` .%  .^      5. 
              7,          .....?7     .^  ,`        ?. 
                `<.                 .= .`'           1 
                ....dn... ... ...,7..J=!7,           ., 
             ..=     G.,7  ..,o..  .?    J.           F 
           .J.  .^ ,,,t  ,^        ?^.  .^  `?~.      F 
          r %J. $    5r J             ,r.1      .=.  .% 
          r .77=?4.    ``,     l ., 1  .. <.       4., 
          .$..    .X..   .n..  ., J. r .`  J.       `' 
        .?`  .5        `` .%   .% .' L.'    t 
        ,. ..1JL          .,   J .$.?`      . 
                1.          .=` ` .J7??7<.. .; 
                 JS..    ..^      L        7.: 
                   `> ..       J.  4. 
                    +   r `t   r ~=..G. 
                    =   $  ,.  J 
                    2   r   t  .; 
              .,7!  r   t`7~..  j.. 
              j   7~L...$=.?7r   r ;?1. 
               8.      .=    j ..,^   .. 
              r        G              . 
            .,7,        j,           .>=. 
         .J??,  `T....... %             .. 
      ..^     <.  ~.    ,.             .D 
    .?`        1   L     .7.........?Ti..l 
   ,`           L  .    .%    .`!       `j, 
 .^             .  ..   .`   .^  .?7!?7+. 1 
.`              .  .`..`7.  .^  ,`      .i.; 
.7<..........~<<3?7!`    4. r  `          G% 
                          J.` .!           % 
                            JiJ           .` 
                              .1.         J 
                                 ?1.     .'         
                                     7<..%
"""
#endregion
#atempts
atempts=0
#valid answers
valid=['a','b','c']
yes_no=['yes','no']
#setting loop to play quiz
play=True

#introduction and instructions
print()
print("Welcome to my 10 question general knowledge quiz")
print("For the best experience make the terminal as big as possible")
print("When a question gives options a, b or c please use either a,b or c to answer")
print("If you want to exit the program, answer the question with 'quit'")
print("Good luck!")
print()

#quiz loop
while play==True:

    #scoring
    score= 0

    #question 1 
    print("1) What is the fastest animal?\na: cheetah\nb: swordfish\nc: peregrine falcon")
    #user answer
    question_1= input("Your answer:").strip().lower()
    answer_1= "c"
    #while loop for invalid answer
    while not question_1 in valid:
        #if user wants to quit program
        if question_1=="quit":
            break
        #if user gave invalid answer
        question_1=input("ERROR please answer using a, b or c\nYour answer: ").strip().lower()
    #check answer
    if question_1==answer_1:
        print(f"Correct! Peregrine falcons are the fastest animal in the world{falcon}")
        score +=1
    #if user wants to quit program
    elif question_1=="quit":
        break
    else:
        print("Whoops that's incorrect, the correct answer was peregrine falcon (c)")
    print()

    #question 2
    print("2) What is acrophobia a fear of?\na: Spiders\nb: Hieghts\nc: Water")
    #user answer
    question_2=input("your answer:").strip().lower()
    answer_2="b"
    #while loop for invalid answer
    while not question_2 in valid:
        #if user wants to quit program
        if question_2=="quit":
            break
        question_2=input("ERROR please answer using a, b or c\nYour answer: ").strip().lower()
    #check answer
    if question_2==answer_2:
        print(f"Correct! Acrophbia is the fear of hieghts{scared}")
        score +=1
    #if user wants to quit program
    elif question_2=="quit":
        break
    else:
        print("whoops that's incorrect, the correct answer was hieghts (b)")
    print()


    #question 3
    print("3) What color is aureolin a shade of?\na: blue\nb: green\nc: yellow")
    question_3=input("your answer:").strip().lower()
    answer_3="c"
    #while loop for invalid answer
    while not question_3 in valid:
        #if user wants to exit program
        if question_3=="quit":
            break
        question_3=input("ERROR please answer using a, b or c\nYour answer: ")
    #check answer
    if question_3==answer_3:
        print(f"That's correct!{yellow}")
        score +=1
    #if user wants to quit program
    elif question_3=="quit":
        break        
    else:
        print("whoops that's incorrect, the correct answer was yellow (c)")
    print()


    #question 4
    question_4= input("4) What year was the video game 'Minecraft' officially released?\nyour answer:").strip().lower()
    answer_4= "2011"
    #check answer is valid
    try:
        question_4=int(question_4)
        question_4=str(question_4)
    except:
        #if user wants to quit program
        if question_4=="quit":
            break
        print("please answer using numbers")
        question_4=input("your answer: ").strip()
    #check answer
    if question_4==answer_4:
        print(f"That's correct!{steve}")
        score +=1
    #if user wants to quit program
    elif question_4=="quit":
        break
    else:
        print("Whoops That's incorrect, the correct answer was 2011")
    print()

    #question 5
    question_5= input("5) how many time zones are there in the world?\nyour answer:").strip()
    answer_5= "24"
    try:
        question_5=int(question_5)
        question_5=str(question_5)
    except:
        #if user wants to quit program
        if question_5=="quit":
            break
        print("please answer using numbers and no spaces")
        question_5=input("your answer: ").strip()
    #check answer
    if question_5==answer_5:
        print(f"That's correct!{earth}")
        score +=1
    elif question_5=="quit":
        break
    else:
        print("Whoops that's incorrect, the correct answer was 24")
    print()

    #question 6
    print("6) In the series 'The Amazing World Of Gumball' what kind of animal is Anais?\na: Mouse\nb: Hamster\nc: Rabbit")
    question_6= input("Your answer: ").strip().lower()
    answer_6= "c"
    #while loop for invalid answer
    while not question_6 in valid:
        #if user wants to quit program
        if question_6=="quit":
            break
        question_6=input("ERROR please answer using a, b or c\nYour answer: ").strip().lower()
    #check answer
    if question_6==answer_6 :
        print(f"Correct!{rabbit}")
        score +=1
    #if user wants to quit program
    elif question_6=="quit":
        break
    else:
        print("Whoops that's incorrect, the correct answer was rabbit (c)")
    print()

    #question 7
    question_7=input("7) How many cards are in a standard playing deck?\nyour answer: ").strip().lower()
    answer_7= "52"
    try:
        question_7=int(question_7)
        question_7=str(question_7)
    except:
        #if user wants to quit program
        if question_7=="quit":
            break
        print("please answer using numbers and no spaces")
        question_7=input("your answer: ").strip()
    #check answer
    if question_7==answer_7:
        print(f"That's correct!{cards}")
        score +=1
    #if user wants to quit program
    elif question_7=="quit":
        break
    else:
        print("Whoops that's incorrect, the correct answer was 52")
    print()

    #question 8
    print("8) How many hearts does an octopus have?\na: 3\nb: 1\nc: 8")
    question_8=input("Your answer: ").strip().lower()
    answer_8="a"
    #while loop for invalid answer
    while not question_8 in valid:
        #if user wants to quit program
        if question_8=="quit":
            break
        question_8=input("ERROR please answer using a, b or c\nYour answer: ").strip().lower()
    #check answer
    if question_8==answer_8:
        print(f"That's correct!{heart}")
        score+=1
    #if user wants to quit program
    elif question_8=="quit":
        break
    else:
        print("Whoops that's incorrect, the correct answer was 3 (a)")
    print()

    #question 9
    print("9) Which of the following gaming consoles were released first\na: original xbox\nb: PS2\nc: nintendo DS")
    question_9=input("Your answer: ").strip().lower()
    answer_9="b"
    #while loop for invalid answer
    while not question_9 in valid:
        #if user wants to quit program
        if question_9=="quit":
            break
        question_9=input("ERROR please answer using a, b or c\nYour answer: ").strip().lower()
    #check answer
    if question_9==answer_9:
        print(f"that's correct! the PS2 was released in 2000, the original Xbox in 2001 and the Nintendo DS in 2004{ps2}")
        score+=1
    #if user wants to quit program
    elif question_9=="quit":
        break
    else:
        print("whoops that's incorrect, the correct answer was PS2 (b)")
    print()

    #question10
    print("10) What year did the Sonic franchise start\na: 1991\nb: 2000\nc: 1989")
    question_10=input("Your answer: ").strip().lower()
    answer_10="a"
    #while loop for invalid answer
    while not question_10 in valid:
        #if user wants to quit program
        if question_10=="quit":
            break
        question_10=input("ERROR please answer using a, b or c\nYour answer: ").strip().lower()
    #check answer
    #answer correct
    if question_10==answer_10:
        print(f"That's correct! The first sonic game was released in 1991{sonic}")
        score+=1
    #if user wants to quit program
    elif question_10=="quit":
        break
    #answer incorrect
    else:
        print("Whoops that's incorrect, the correct answer was 1991 (a)")
    print()

    #final score
    print(f"You got {score} out of 10 questions correct")
    #score feedback
    if score==10:
        print("Congradulations, you got all of them correct!")
    elif score>5:
        print(f"Great work! you got more than half right, you were only {10-score} away from a perfect score")
    elif score==5:
        print("You got exactly half of them correct")
    elif score==0:
        print("Oh no! You didn't get any correct, better luck next time")
    elif score<5:
        print("That's less than half, better luck next time")

    #play again
    play_again=input("would you like to play again (Y/N): ").strip().lower()
    while not play_again in yes_no:
        print("please answer using yes or no")
        play_again=input("would you like to play again (Y/N): ").strip().lower()
    if play_again=="yes":
        print("restarting...\n")
        continue
    else:
        play=False
        print()
print("Thanks for playing! Ending program")