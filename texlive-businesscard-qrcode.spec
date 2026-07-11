%global tl_name businesscard-qrcode
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	Business cards with QR-Code
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/xetex/latex/businesscard-qrcode
License:	lgpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/businesscard-qrcode.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/businesscard-qrcode.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
What happens when you give your visiting card to someone? Either they
manually type the text into their computer or mobile phone, or it will
end up in a box and be forgotten. Nowadays data is required
electronically, not on paper. Here is the solution: A visiting card with
QR-Code that contains a full vcard so that it can be scanned with an app
on the mobile phone and thereby automatically imported into the
electronic contacts. This also works well when you are offline and
bluetooth transfer fails. So here is the highly configurable business
card or visiting card with full vcard as QR-Code, ready to send to
online printers. You can specify the exact size of the paper and the
content within the paper, including generation of crop marks. The
package depends on the following other LaTeX packages: calc, crop,
DejaVuSans, etoolbox, fontawesome, fontenc, geometry, kvoptions,
marvosym, qrcode, varwidth, and wrapfig. The package needs XeLaTeX for
working properly.

