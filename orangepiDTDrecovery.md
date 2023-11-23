Orange pi 5 plus flash memory MTD0 recovery

To recover a flash memory where the firmware are recorded is easy, does not get desperade 
if you accidentaly overwritten it like me, because it continue booting by sdcard, and you
just need to reflash the /dev/mtdblock0.

First thing you must to do is download armbian for orange pi 5 plus, in 2023-11 I downloaded from: https://redirect.armbian.com/region/NA/orangepi5/Bookworm_legacy_gnome

I wrote this image to a sdcard of 32GB, you can use balena ecther.

Boot the armbian, and run armbian-config, you may do that by command line or clicking on the app this is on your own.

Now the sequence of images to help you to do the right thing.

Click on System and security settings:

![img001](https://github.com/ppsilv/ScriptsUtils/assets/15231809/59025d7e-3c97-4e8f-9c41-a3778c6256f2)


Click on Update all packages and firmware:

![img002](https://github.com/ppsilv/ScriptsUtils/assets/15231809/8c4a7e1f-92d9-44a7-8cef-2273d7ca1151)


Click on Yes - After loading and installation it asks for reboot, please reboot system!:

![img003](https://github.com/ppsilv/ScriptsUtils/assets/15231809/d822d571-d735-470d-acc2-a4ba59f2dd15)


Click on Install to/update boot loader:

![img004](https://github.com/ppsilv/ScriptsUtils/assets/15231809/2c923ea5-1656-4ddd-814f-e965b8359362)


Click on option 7: Install/Update the bootloader on MTD Flash:

![img005](https://github.com/ppsilv/ScriptsUtils/assets/15231809/d07a3363-a5d6-41a6-8893-c70aec16260d)


Take off the sdcard from orange pi board and reboot the machine, and now it will boot from NVME.

