# $NetBSD$

GITHUB_PROJECT=	scaleway-cli
DISTNAME=	go-scw-1.5.0
PKGNAME=	${GITHUB_PROJECT}
CATEGORIES=	wip
MASTER_SITES=	${MASTER_SITE_GITHUB:=scaleway/}
EXTRACT_SUFX=	.zip
DIST_SUBDIR=	${GITHUB_PROJECT}

GITHUB_TAG=	v${PKGVERSION_NOREV}
MAINTAINER=	nils@NetBSD.org
HOMEPAGE=	${MASTER_SITE_GITHUB:=scaleway/scaleway-cli/}
COMMENT=	Manage Scaleway BareMetal Servers from Command Line
LICENSE=	mit

#WRKSRC=		${WRKDIR}/src/scaleway-cli-1.5.0
USE_LANGUAGES=	# go
NO_CONFIGURE=	yes

BUILD_DEPENDS+=	go-[0-9]*:../../lang/go

GO_SRCPATH=	${GITHUB_PROJECT}-1.5.0

.include "../../lang/go/go-package.mk"
.include "../../mk/bsd.pkg.mk"
