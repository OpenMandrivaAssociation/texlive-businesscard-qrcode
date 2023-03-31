Name:		texlive-businesscard-qrcode
Version:	61719
Release:	2
Summary:	Business cards with QR-Code
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/businesscard-qrcode
License:	lgpl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/businesscard-qrcode.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/businesscard-qrcode.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
What happens when you give your visiting card to someone?
Either they manually type the text into their computer or
mobile phone, or it will end up in a box and be forgotten.
Nowadays data is required electronically, not on paper. Here is
the solution: A visiting card with QR-Code that contains a full
vcard so that it can be scanned with an app on the mobile phone
and thereby automatically imported into the electronic
contacts. This also works well when you are offline and
bluetooth transfer fails. So here is the highly configurable
business card or visiting card with full vcard as QR-Code,
ready to send to online printers. You can specify the exact
size of the paper and the content within the paper, inluding
generation of crop marks. The package depends on the following
other LaTeX packages: calc, crop, DejaVuSans, etoolbox,
fontawesome, fontenc, geometry, kvoptions, marvosym, qrcode,
varwidth, and wrapfig. The package needs XeLaTeX for working
properly.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/xelatex/businesscard-qrcode
%doc %{_texmfdistdir}/doc/xelatex/businesscard-qrcode

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
