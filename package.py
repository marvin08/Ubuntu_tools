# A python script to install basic tools on a freshly installed UBUNTU desktop.


import subprocess

subprocess.call(['sudo','apt-get','install','git'])                                        # Installs git(verion control system)


subprocess.call(['sudo','apt-get','install','unity-tweak-tool'])                           # Installs Unity Tweak Tools


subprocess.call(['sudo','add-apt-repository','ppa:mc3man/trusty-media'])                   # Installs VLC Media Player
subprocess.call(['sudo','apt-get','update'])
subprocess.call(['sudo','apt-get','install','vlc','vlc-plugin-*'])


subprocess.call(['sudo','add-apt-repository','ppa:otto-kesselgulasch/gimp'])               # Installs GIMP Image Editor
subprocess.call(['sudo','apt-get','update'])
subprocess.call(['sudo','apt-get','install','gimp'])


subprocess.call(['sudo','add-apt-repository','ppa:haraldhv/shotcut'])                      # Installs Shotcut Video Editor
subprocess.call(['sudo','apt-get','update'])
subprocess.call(['sudo','apt-get','install','shotcut'])


subprocess.call(['sudo','apt-get','update'])                                          	   # Installs Synaptic Package Manager
subprocess.call(['sudo','apt-get','upgrade'])
subprocess.call(['sudo','apt-get','install','synaptic'])


subprocess.call(['sudo','add-apt-repository','-y','ppa:webupd8team/sublime-text-3'])       # Installs Sublime-Text Editor
subprocess.call(['sudo','apt-get','update'])
subprocess.call(['sudo','apt-get','install','-y','sublime-text-installer'])


subprocess.call(['sudo','apt-get','install','nautilus-dropbox'])                           # Installs Dropbox
