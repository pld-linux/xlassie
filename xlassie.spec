Summary:	Mail notification tool for X11, POP3 support, counts messages
Summary(pl):	Narzêdzie powiadamiaj±ce o poczcie dla X11 z obs³ug± POP3
Name:		xlassie
Version:	1.8
Release:	1
License:	GPL
Group:		X11/Applications
Vendor:		Trent Piepho <xyzzy@speakeasy.org>
Source0:	http://www.speakeasy.org/~xyzzy/download/%{name}-%{version}.tar.gz
# Source0-md5:	d3422a80b6352da4f790da70a7156a94
URL:		http://www.speakeasy.org/~xyzzy/xlassie/
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XLassie is an enhanced version of XBiff. Support for POP3 mailservers,
ability to run a command when clicked on, written in straight xlib so
memory usage is less, and it doesn't just tell you _if_ you have new
mail, but how many new messages you have. Extra support to operate as
a KDE or WindowMaker dock applet, in addition to plain old X11 mode.

%description -l pl
XLassie jest rozszerzon± wersj± XBiff. Obs³uguje serwery pocztowe
POP3, mo¿e wykonywaæ polecenia po klikniêciu na nim. Jest napisany
bezpo¶rednio w xlib wiêc zu¿ywa ma³o pamiêci i nie informuje _czy_
jest nowa poczta, ale ile jest nowych wiadomo¶ci. Dodatkowa obs³uga
pozwala na dzia³anie jako applet KDE czy WindowMakera.

%prep
%setup -q

%build
# TODO: %%{pmcflags}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install xlassie $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README xlassie.lsm
%attr(755,root,root) %{_bindir}/*
