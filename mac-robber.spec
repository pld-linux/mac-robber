#
# TODO	- pl desc
#	- make not simple
#
Summary:	mac-robber is a digital investigation tool that collects data from a mounted file system.
Summary(pl):	mac-robber jest narzêdziem zbieraj±cym dane z zamontowanego systemu plików.
Name:		mac-robber
Version:	1.00
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://puzzle.dl.sourceforge.net/sourceforge/mac-robber/%{name}-%{version}.tar.gz
# Source0-md5:	902afd8e6121e153bbc8cb93013667fd
URL:		http://www.sleuthkit.org/mac-robber
Requires:	sleuthkit
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mac-robber is a Forensics & Incident Response tool used to collect
the Modified, Access, and Change (MAC) times from allocated files.
It recursively reads MAC times of files and directories and prints
them in 'time machine' format to STDOUT.  This format is the same
that the mactime tool from The Sleuth Kit.

Note that this tool will not show deleted files, unallocated files,
or files that have been hidden by rootkits.  To view information
about those file types, the specialized tools from The Sleuth Kit
must be used.

mac-robber is useful when dealing with a file system that is not 
supported by The Sleuth Kit or other file system analysis tools.

%prep
%setup -q

%build
%{__make} simple

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install mac-robber $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%post

%preun

%postun

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
