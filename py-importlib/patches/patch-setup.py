$NetBSD$

Fix setup

--- setup.py.orig	2014-01-06 15:03:54.000000000 +0000
+++ setup.py
@@ -1,4 +1,7 @@
-from distutils.core import setup
+try:
+    from distutils.core import setup
+except ImportError:
+    from distutils.core import setup
 import sys
 
 
