# $NetBSD$

GITHUB_PROJECT=	fedmsg
DISTNAME=	0.18.2
PKGNAME=	${PYPKGPREFIX}-${GITHUB_PROJECT}-${DISTNAME}
CATEGORIES=	www python
MASTER_SITES=	${MASTER_SITE_GITHUB:=fedora-infra/}
DIST_SUBDIR=	${GITHUB_PROJECT}

MAINTAINER=	nils@NetBSD.org
HOMEPAGE=	https://github.com/fedora-infra/fedmsg/
COMMENT=	send and receive messages to and from applications
LICENSE=	gnu-lgpl-v2.1

DEPENDS+=	${PYPKGPREFIX}-zmq-[0-9]*:../../net/py-zmq
DEPENDS+=	${PYPKGPREFIX}-kitchen-[0-9]*:../../wip/py-kitchen
DEPENDS+=	${PYPKGPREFIX}-six-[0-9]*:../../lang/py-six
DEPENDS+=	${PYPKGPREFIX}-arrow-[0-9]*:../../time/py-arrow
DEPENDS+=	${PYPKGPREFIX}-cryptography-[0-9]*:../../security/py-cryptography
DEPENDS+=	${PYPKGPREFIX}-pygments-[0-9]*:../../textproc/py-pygments
DEPENDS+=	${PYPKGPREFIX}-psutil-[0-9]*:../../sysutils/py-psutil

USE_LANGUAGES=	#none
USE_TOOLS+=	bash:run

REPLACE_INTERPRETER+=	bash
REPLACE.bash.old=	/bin/bash
REPLACE.bash.new=	${TOOLS_PATH.bash}
REPLACE_FILES.bash=	extras/stress/launcher.sh
REPLACE_FILES.bash+=	fedmsg/commands/trigger.py
REPLACE_FILES.bash+=	fedmsg/tests/test_certs/rebuild-all-fedmsg-certs
REPLACE_FILES.bash+=	initsys/sysv/fedmsg-gateway.init
REPLACE_FILES.bash+=	initsys/sysv/fedmsg-hub.init
REPLACE_FILES.bash+=	initsys/sysv/fedmsg-irc.init
REPLACE_FILES.bash+=	initsys/sysv/fedmsg-relay.init

WRKSRC=			${WRKDIR}/${GITHUB_PROJECT}-${DISTNAME}
EGDIR=			${PREFIX}/share/example/fedmsg
PKG_SYSCONFSUBDIR=	fedmsg.d
DOCDIR=			${PREFIX}/share/doc/fedmsg
OWN_DIRS=		${PKG_SYSCONFDIR}
INSTALLATION_DIRS+=	${EGDIR} ${EGDIR}/fedmsg.d ${PKG_SYSCONFDIR}

AUTO_MKDIRS=		yes
PYCFGFILES=		base.py endpoints.py gateway.py ircbot.py logging.py relay.py ssl.py

.for configfile in ${PYCFGFILES}
CONF_FILES+=		${EGDIR}/fedmsg.d/${configfile} ${PKG_SYSCONFDIR}
.endfor

SUBST_CLASSES+=		paths
SUBST_STAGE.paths=	pre-configure
SUBST_MESSAGE.paths+=	Substituting paths variables.
SUBST_FILES.paths=	${WRKSRC}/setup.py
SUBST_FILES.paths=	${WRKSRC}/fedmsg/config.py
SUBST_SED.paths=	-e 's,/etc,${PREFIX}/etc,g'

pre-install:
.for configfile1 in ${PYCFGFILES}
	${INSTALL_DATA} ${WRKSRC}/fedmsg.d/${configfile1} ${DESTDIR}${EGDIR}/fedmsg.d/
.endfor

.include "../../lang/python/distutils.mk"
.include "../../mk/bsd.pkg.mk"
