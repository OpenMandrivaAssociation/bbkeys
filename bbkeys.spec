%define name	bbkeys
%define version 0.8.6
%define release %mkrel 6

Summary:	Bbkeys, a configurable key-grabber for blackbox
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Graphical desktop/Other
Source0:	%name-%version.tar.bz2
Source1:	%{name}-16x16.png
Source2:	%{name}-32x32.png
Source3:	%{name}-48x48.png
URL:		http://bbkeys.sourceforge.net/
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires:	X11-devel

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
%configure
make

%install
rm -fr $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%_prefix

%makeinstall

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
install -d $RPM_BUILD_ROOT/%{_iconsdir}
install -d $RPM_BUILD_ROOT/%{_liconsdir}
install -d $RPM_BUILD_ROOT/%{_miconsdir}
install %{SOURCE1}  $RPM_BUILD_ROOT/%{_miconsdir}/%{name}.png
install %{SOURCE2}  $RPM_BUILD_ROOT/%{_iconsdir}/%{name}.png
install %{SOURCE3}  $RPM_BUILD_ROOT/%{_liconsdir}/%{name}.png

rm -fr $RPM_BUILD_ROOT%_prefix/doc

%post
%{update_menus}

%postun
%{clean_menus}

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_DIR/%{name}-%{version}

%files -n %{name}
%defattr(-,root,root)
%doc README ChangeLog AUTHORS TODO COPYING INSTALL
%attr(755,root,root) 
%{_bindir}/*
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_datadir}/bbtools/*
%{_mandir}/man1/*
%{_mandir}/man5/*
%_datadir/applications/*
