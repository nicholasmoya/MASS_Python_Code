# ~/.profile: executed by the command interpreter for login shells.
# This file is not read by bash(1), if ~/.bash_profile or ~/.bash_login
# exists.
# see /usr/share/doc/bash/examples/startup-files for examples.
# the files are located in the bash-doc package.

# the default umask is set in /etc/profile; for setting the umask
# for ssh logins, install and configure the libpam-umask package.
#umask 022

# if running bash
if [ -n "$BASH_VERSION" ]; then
    # include .bashrc if it exists
    if [ -f "$HOME/.bashrc" ]; then
	. "$HOME/.bashrc"
    fi
fi

# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/bin" ] ; then
    PATH="$HOME/bin:$PATH"
fi

# export SLOTS=/sys/devices/bone_capemgr.9/slots
# export PINS=/sys/kernel/debug/pinctrl/44e10800.pinmux/pins

# sudo sh -c "echo BB-ADC > $SLOTS"

# sudo sh -c "echo am33xx_pwm > $SLOTS"
# sudo sh -c "echo bone_pwm_P9_42 > $SLOTS"
# sudo sh -c "echo am33xx_pwm > $SLOTS"
# sudo sh -c "echo bone_pwm_P9_22 > $SLOTS"

# sudo sh -c "echo 116 > /sys/class/gpio/export"
# sudo sh -c "echo out > /sys/class/gpio/gpio116/direction"

# /sbin/route add default gw 192.168.7.1
# /usr/sbin/ntpdate -b -s -u www.pool.ntp.org

# sudo python ~/pylemo/obstacle_avoidance/ovtest.py
