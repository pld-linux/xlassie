Summary:	Mail notification tool for X11, POP3 support, counts messages
Summary(pl.UTF-8):   Narzędzie powiadamiające o poczcie dla X11 z obsługą POP3
Name:		xlassie
Version:	1.8
Release:	2
License:	GPL
Group:		X11/Applications
Vendor:		Trent Piepho <xyzzy@speakeasy.org>
Source0:	http://www.speakeasy.org/~xyzzy/download/%{name}-%{version}.tar.gz
# Source0-md5:	d3422a80b6352da4f790da70a7156a94
Patch0:		%{name}-bufferoverflow.patch
Patch1:		%{name}-Makefile.patch
URL:		http://www.speakeasy.org/~xyzzy/xlassie/
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XLassie is an enhanced version of XBiff. Support for POP3 mailservers,
ability to run a command when clicked on, written in straight xlib so
memory usage is less, and it doesn't just tell you _if_ you have new
mail, but how many new messages you have. Extra support to operate as
a KDE or WindowMaker dock applet, in addition to plain old X11 mode.

%description -l pl.UTF-8
XLassie jest rozszerzoną wersją XBiff. Obsługuje serwery pocztowe
POP3, może wykonywać polecenia po kliknięciu na nim. Jest napisany
bezpośrednio w xlib więc zużywa mało pamięci i nie informuje _czy_
jest nowa poczta, ale ile jest nowych wiadomości. Dodatkowa obsługa
pozwala na działanie jako applet KDE czy WindowMakera.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install xlassie $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README xlassie.lsm todo
%attr(755,root,root) %{_bindir}/*
