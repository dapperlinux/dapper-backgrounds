WP_NAME=dapperlinux
WP_BIGNAME=DapperLinux
WP_DIR=$(DESTDIR)/usr/share/backgrounds/$(WP_NAME)
GNOME_BG_DIR=$(DESTDIR)/usr/share/gnome-background-properties
KDE_BG_DIR=$(DESTDIR)/usr/share/wallpapers/
MATE_BG_DIR=$(DESTDIR)/usr/share/mate-background-properties
XFCE_BG_DIR=$(DESTDIR)/usr/share/xfce4/backdrops
MKDIR=/bin/mkdir -p
INSTALL=/usr/bin/install -p -m644 -D
LN_S=/bin/ln -s

install:
	$(MKDIR) $(WP_DIR)/default/ultrahd
	$(MKDIR) $(WP_DIR)/default/tv-wide
	$(MKDIR) $(WP_DIR)/default/standard
	$(MKDIR) $(WP_DIR)/default/normalish
	$(MKDIR) $(GNOME_BG_DIR)
	
	for size in normalish standard ultrahd tv-wide; do \
		$(INSTALL) $${size}/$(WP_NAME).png $(WP_DIR)/default/$${size}/$(WP_NAME).png \
		# Loop \
	done;
	
	$(INSTALL) $(WP_NAME).xml $(WP_DIR)/default/$(WP_NAME).xml
	$(INSTALL) desktop-backgrounds-$(WP_NAME).xml $(GNOME_BG_DIR)/$(WP_NAME).xml
	
	$(MKDIR) $(KDE_BG_DIR)/$(WP_BIGNAME)/contents/images
	$(INSTALL) $(WP_NAME)-metadata.desktop $(KDE_BG_DIR)/$(WP_BIGNAME)/metadata.desktop
	for res in 640x480 800x600 1024x768 1152x864 1200x900 1280x960 1440x1080 1600x1200 1600x1280 1920x1440 2048x1536; do \
		$(LN_S) ../../../../backgrounds/$(WP_NAME)/default/standard/$(WP_NAME).png \
		$(KDE_BG_DIR)/$(WP_BIGNAME)/contents/images/$${res}.png ; \
	done;
	for res in 1280x1024 ; do \
	    $(LN_S) ../../../../backgrounds/$(WP_NAME)/default/normalish/$(WP_NAME).png \
		$(KDE_BG_DIR)/$(WP_BIGNAME)/contents/images/$${res}.png ; \
	done;
	for res in 800x480 1152x720 1280x768 1280x800 1440x900 1680x1050 1920x1200 2560x1440 ; do \
		$(LN_S) ../../../../backgrounds/$(WP_NAME)/default/ultrahd/$(WP_NAME).png \
		$(KDE_BG_DIR)/$(WP_BIGNAME)/contents/images/$${res}.png ; \
	done;
	for res in 1024x600 1280x720 1366x768 1920x1080 ; do \
	    $(LN_S) ../../../../backgrounds/$(WP_NAME)/default/tv-wide/$(WP_NAME).png \
		$(KDE_BG_DIR)/$(WP_BIGNAME)/contents/images/$${res}.png ; \
	done;
	
	$(MKDIR) $(MATE_BG_DIR)
	$(INSTALL) mate-backgrounds-$(WP_NAME).xml $(MATE_BG_DIR)/$(WP_NAME).xml
	
	$(MKDIR) $(XFCE_BG_DIR)
	$(LN_S) ../../backgrounds/$(WP_NAME)/default/ultrahd/$(WP_NAME).png \
		$(XFCE_BG_DIR)/$(WP_NAME).png
