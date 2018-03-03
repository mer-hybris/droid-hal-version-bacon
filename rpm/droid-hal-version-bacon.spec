# rpm_device is the name of the ported device
%define rpm_device bacon
# rpm_vendor is used in the rpm space
%define rpm_vendor oneplus
# Manufacturer and device name to be shown in UI
%define vendor_pretty OnePlus
%define device_pretty One

# See ../droid-hal-version/droid-hal-device.inc for similar macros:
# define have_vibrator 1
# define have_ffmemless 1
%define have_vibrator_native 1
%define have_led 1

%include droid-hal-version/droid-hal-version.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

