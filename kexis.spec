Name:			kexis
Version:		0.2.2
Release:		%mkrel 1
Summary:		A lossless WAV file compressor
License:		GPLv2
Group:			Sound
URL:			http://sourceforge.net/projects/kexis/
Source:			http://etree.org/shnutils/shntool/support/formats/kxs/win32/%{version}/%{name}-%{version}-shntool.tar.gz
BuildRoot:		%{_tmppath}/%{name}-%{version}-build

%description
Kexis is a lossless WAV file compressor. It encodes and decodes files in
kxs file format.

Kexis' main goal is to develop prediction and encoding schemes to minimize
compressed file size. Kexis strives to be the premier lossless sound encoder.

This version is patched with shntool patch.

%prep
%setup -q -n %{name}-%{version}-shntool

%build
%make
mv GPL.txt COPYING
mv docs/README.txt README

%install
%__rm -rf %{buildroot}
%__install -dm 755  %{buildroot}%{_bindir}
%__install -m 755 %{name} %{buildroot}%{_bindir}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc COPYING README
%{_bindir}/*

