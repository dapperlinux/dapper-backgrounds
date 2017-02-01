# dapper-backgrounds

##About
The Dapper Backgrounds package contains the artwork used in the desktop wallpaper for the Dapper Linux distribution. 

##Files
main.xcf - a GIMP file of the main artwork
main.png - an output of the xcf file, used for all derivative wallpaper sizes found in the dapper-backgrounds/default directory

##Building
To build this package, first install an RPM development chain:

```bash
$ sudo dnf install fedora-packager fedora-review

```

Next, setup rpmbuild directories with

```bash
$ rpmdev-setuptree
```
And place the file dapper-backgrounds.spec in the SPECS directory, and rename the dapper-backgrounds directory to dapper-backgrounds-25.0 and compress it:
```bash
$ mv dapper-backgrounds.spec ~/rpmbuild/SPECS/
$ mv dapper-backgrounds dapper-backgrounds-25.0
$ tar -czvf dapper-backgrounds-25.0.tar.gz dapper-backgrounds-25.0
$ mv dapper-backgrounds-25.0.tar.gz ~/rpmbuild/SOURCES/
```

and finally, you can build RPMs and SRPMs with:
```bash
$ cd ~/rpmbuild/SPECS
$ rpmbuild -ba dapper-backgrounds.spec
```


