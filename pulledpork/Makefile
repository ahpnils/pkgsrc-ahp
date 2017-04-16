# $NetBSD$

DISTNAME=	pulledpork-0.7.2
CATEGORIES=	net
MASTER_SITES=	${MASTER_SITE_GITHUB:=shirkdog/}

MAINTAINER=	nils@NetBSD.org
HOMEPAGE=	https://github.com/shirkdog/pulledpork/
COMMENT=	Script for Snort and Suricata rule management
LICENSE=	gnu-gpl-v2

GITHUB_TAG=	v${PKGVERSION_NOREV}
NO_BUILD=	yes
USE_TOOLS+=	perl:run
REPLACE_PERL+=	pulledpork.pl
REPLACE_PERL+=	contrib/oink-conv.pl
WRKSRC=		${WRKDIR}/pulledpork-${PKGVERSION_NOREV}

# File/Find.pm is a part of lang/perl5
# File/Basename.pm is a part of lang/perl5
# File/Copy.pm is a part of lang/perl5
DEPENDS+=	p5-Crypt-SSLeay-[0-9]*:../../security/p5-Crypt-SSLeay
DEPENDS+=	p5-Sys-Syslog-[0-9]*:../../sysutils/p5-Sys-Syslog
DEPENDS+=	p5-Digest-MD5-[0-9]*:../../security/p5-Digest-MD5
DEPENDS+=	p5-File-Path-[0-9]*:../../devel/p5-File-Path
DEPENDS+=	p5-Getopt-Long-[0-9]*:../../devel/p5-Getopt-Long
DEPENDS+=	p5-Archive-Tar-[0-9]*:../../archivers/p5-Archive-Tar
DEPENDS+=	p5-PathTools-[0-9]*:../../devel/p5-PathTools
DEPENDS+=	p5-Data-Dumper-[0-9]*:../../devel/p5-Data-Dumper
DEPENDS+=	p5-libwww-[0-9]*:../../www/p5-libwww
# LWP/Useragent.pm is part of www/p5-libwww
DEPENDS+=	p5-HTTP-Message-[0-9]*:../../www/p5-HTTP-Message
# Request/Common.pm is part of www/p5-HTTP-Message
# Status.pm is part of www/p5-HTTP-Message
DEPENDS+=	p5-Carp-[0-9]*:../../wip/p5-Carp

EGDIR=			${PREFIX}/share/examples/pulledpork
PKG_SYSCONFSUBDIR=	pulledpork
DOCDIR=			share/doc/pulledpork
INSTALLATION_DIRS+=	${EGDIR} ${PKG_SYSCONFDIR} ${OWN_DIRS} ${DOCDIR} bin
AUTO_MKDIRS=		yes
USE_LANGUAGES=		# none

CONF_FILES=	${EGDIR}/disablesid.conf \
		${PKG_SYSCONFDIR}/disablesid.conf
CONF_FILES+=	${EGDIR}/dropsid.conf \
		${PKG_SYSCONFDIR}/dropsid.conf
CONF_FILES+=	${EGDIR}/enablesid.conf \
		${PKG_SYSCONFDIR}/enablesid.conf
CONF_FILES+=	${EGDIR}/modifysid.conf \
		${PKG_SYSCONFDIR}/modifysid.conf
CONF_FILES+=	${EGDIR}/pulledpork.conf \
		${PKG_SYSCONFDIR}/pulledpork.conf

do-install:
	${INSTALL_SCRIPT} ${WRKSRC}/pulledpork.pl ${DESTDIR}${PREFIX}/bin/pulledpork
	${INSTALL_SCRIPT} ${WRKSRC}/contrib/oink-conv.pl ${DESTDIR}${PREFIX}/bin/oink-code
	${INSTALL_DATA} ${WRKSRC}/LICENSE ${DESTDIR}${PREFIX}/share/doc/pulledpork/
	${INSTALL_DATA} ${WRKSRC}/README.md ${DESTDIR}${PREFIX}/share/doc/pulledpork/
	${INSTALL_DATA} ${WRKSRC}/doc/README.* ${DESTDIR}${PREFIX}/share/doc/pulledpork/
	${INSTALL_DATA} ${WRKSRC}/etc/*.conf ${DESTDIR}${EGDIR}

.include "../../mk/bsd.pkg.mk"
