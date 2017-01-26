# $NetBSD$

GITHUB_PROJECT=	shinken
DISTNAME=	2.4.3
PKGNAME=	${GITHUB_PROJECT}-${DISTNAME}
CATEGORIES=	net
MASTER_SITES=	${MASTER_SITE_GITHUB:=naparuba/}
DIST_SUBDIR=	${GITHUB_PROJECT}

MAINTAINER=	nils@NetBSD.org
HOMEPAGE=	http://www.shinken-monitoring.org/
COMMENT=	Nagios-compatible monitoring solution written in Python
LICENSE=	gnu-agpl-v3

DEPENDS+=	${PYPKGPREFIX}-cherrypy-[0-9]*:../../www/py-cherrypy
DEPENDS+=	${PYPKGPREFIX}-curl-[0-9]*:../../www/py-curl
DEPENDS+=	${PYPKGPREFIX}-pbr-[0-9]*:../../devel/py-pbr
DEPENDS+=	${PYPKGPREFIX}-html-[0-9]*:../../wip/py-html
PYTHON_VERSIONS_INCOMPATIBLE=	33 34 35 # no support yet

WRKSRC=		${WRKDIR}/shinken-2.4.3
USE_LANGUAGES=	# none

.include "../../mk/bsd.prefs.mk"
BUILD_DEFS+=	VARBASE

SHINKEN_USER?=	shinken
SHINKEN_GROUP?=	shinken

PKG_GROUPS=	${SHINKEN_GROUP}
PKG_USERS=	${SHINKEN_USER}:${SHINKEN_GROUP}
PKG_GECOS.${SHINKEN_USER}=	SHINKEN user
#PKG_HOME.${SHINKEN_USER}=	${SHINKEN_DATADIR}
PKG_SHELL.${SHINKEN_USER}=	${NOLOGIN}

PKG_SYSCONFSUBDIR=		shinken

.include "../../lang/python/egg.mk"
.include "../../mk/bsd.pkg.mk"
