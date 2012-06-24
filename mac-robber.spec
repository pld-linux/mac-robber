#
# TODO	- make not simple
# noarch or optflags missing?
#
Summary:	mac-robber - digital investigation tool collecting data from a mounted file system
Summary(pl):	mac-robber - narz�dzie zbieraj�ce dane z zamontowanego systemu plik�w
Name:		mac-robber
Version:	1.00
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/mac-robber/%{name}-%{version}.tar.gz
# Source0-md5:	902afd8e6121e153bbc8cb93013667fd
URL:		http://www.sleuthkit.org/mac-robber/
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

%description -l pl
mac-robber to narz�dzie do analizy i reagowania na zdarzenia s�u��ce
do zbierania czas�w modyfikacji, dost�pu i zmiany (MAC - Modified,
Access, Change) z przydzielonych plik�w. Rekurencyjnie odczytuje czasy
MAC z plik�w oraz katalog�w i wypisuje je na standardowe wyj�cie w
formacie czytelnym dla maszyny. Format ten jest taki sam, jak
narz�dzia mactool z pakietu The Sleuth Kit.

Nale�y zauwa�y�, �e to narz�dzie nie poka�e plik�w usuni�tych,
nieprzydzielonych czy ukrytych przez rootkity. Aby uzyska� informacje
o tych rodzajach plik�w, nale�y u�y� specjalizowanych narz�dzi z
pakietu The Sleuth Kit.

mac-robber jest przydatny w przypadku system�w plik�w nie
obs�ugiwanych przez The Sleuth Kit czy inne narz�dzia do analizy
system�w plik�w.

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

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
