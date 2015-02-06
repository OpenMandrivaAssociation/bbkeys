Summary:	A configurable key-grabber for blackbox
Name:		bbkeys
Version:	0.9.1
Release:	6
License:	MIT
Group:		Graphical desktop/Other
Source0:	http://heanet.dl.sourceforge.net/sourceforge/bbkeys/%name-%version.tar.gz
Source1:	%{name}-16x16.png
Source2:	%{name}-32x32.png
Source3:	%{name}-48x48.png
URL:		http://bbkeys.sourceforge.net/
BuildRequires:	pkgconfig(x11) blackbox-devel

%description
Bbkeys is a configurable key-grabber designed for the blackbox window 
manager which is written by Brad Hughes.  
It is based on the bbtools object code created by John Kennis
and re-uses some of the blackbox window manager classesas well.  
Bbkeys is easily configurable via directly hand-editing ~/.bbkeysrc 
file, or by using the gui configuration tool bbconf.  

%prep 

%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=Bbkeys, a configurable key-grabber for blackbox
Exec=%{name} -c
Icon=%{name}
Terminal=false
Type=Application
Categories=Settings;DesktopSettings;
EOF
  
#icon
install -d %{buildroot}/%{_iconsdir}
install -d %{buildroot}/%{_liconsdir}
install -d %{buildroot}/%{_miconsdir}
install %{SOURCE1}  %{buildroot}/%{_miconsdir}/%{name}.png
install %{SOURCE2}  %{buildroot}/%{_iconsdir}/%{name}.png
install %{SOURCE3}  %{buildroot}/%{_liconsdir}/%{name}.png

rm -fr %{buildroot}%{_prefix}/doc

%clean

%files -n %{name}
%doc README ChangeLog AUTHORS TODO INSTALL
%attr(755,root,root) 
%{_bindir}/*
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_datadir}/%{name}
%{_mandir}/man1/*
%{_mandir}/man5/*
%_datadir/applications/*


%changelog
* Wed Feb 02 2011 Funda Wang <fwang@mandriva.org> 0.9.1-3mdv2011.0
+ Revision: 635004
- rebuild
- tighten BR

* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.1-2mdv2011.0
+ Revision: 616735
- the mass rebuild of 2010.0 packages

* Wed Jun 10 2009 Jérôme Brenier <incubusss@mandriva.org> 0.9.1-1mdv2010.0
+ Revision: 384643
- update to new version 0.9.1
- fix license

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 0.9.0-1mdv2008.1
+ Revision: 135828
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Sep 05 2007 Funda Wang <fwang@mandriva.org> 0.9.0-1mdv2008.0
+ Revision: 79752
- fix file list
- BR blackbox
- New version 0.9.0

* Fri Aug 31 2007 Funda Wang <fwang@mandriva.org> 0.8.6-6mdv2008.0
+ Revision: 76707
- bunzip2 the images
- fix menu entries


* Mon Jul 31 2006 Lenny Cartier <lenny@mandriva.com> 0.8.6-5mdv2007.0
- rebuild

* Fri Jun 18 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.8.6-4mdk
- rebuild

* Mon Feb 23 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.8.6-3mdk
- rebuild

