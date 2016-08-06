# $NetBSD$

DISTNAME=	scaleway-cli-${GITHUB_TAG:S/v//}
PKGNAME=	go-${GITHUB_PROJECT}
CATEGORIES=	net
MASTER_SITES=	${MASTER_SITE_GITHUB:=scaleway/}
GITHUB_PROJECT=	scaleway-cli
GITHUB_TAG=	v1.9.0
EXTRACT_SUFX=	.zip

MAINTAINER=	nils@NetBSD.org
HOMEPAGE=	${MASTER_SITE_GITHUB:=scaleway/scaleway-cli/}
COMMENT=	Manage Scaleway BareMetal Servers from Command Line
LICENSE=	mit

#NO_CONFIGURE=	yes
#GO_SRCPATH=	github.com/scaleway/scaleway-cli
#GO_DIST_BASE=	${DISTNAME}
GO_SRCPATH=	${DISTNAME}

#BUILD_DEPENDS+=	go>=1.5:../../lang/go

.include "../../lang/go/go-package.mk"
.include "../../mk/bsd.pkg.mk"
